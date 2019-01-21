#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by tangruize on 19-1-18.
import sys
import re
import os
import subprocess

from collections import OrderedDict
from configparser import ConfigParser
from itertools import chain, zip_longest
from shutil import copy2
from datetime import datetime


class TLCConfigFile:
    """generate TLC config file"""
    model_sym_pat = re.compile(r'\[model value\]<symmetrical>{(.*)}')
    model_pat = re.compile(r'\[model value\]{(.*)}')
    tag = '\\* Generated by ' + os.path.basename(__file__)

    def __init__(self, cfg, output_cfg_fn, output_tla_fn):
        self.cfg = cfg
        self.output_cfg_fn = output_cfg_fn
        self.output_tla_fn = output_tla_fn
        self.top_module = os.path.basename(cfg.get('options', 'target')).rstrip('.tla')
        self.output_cfg = []
        self.output_tla = []
        self.parse()

    def _add_behavior(self, specifier, prefix, value):
        behavior_name = '{}_{}'.format(prefix, id(value))
        behavior_value = '{} ==\n{}'.format(behavior_name, value)
        self.output_cfg.append('{}\n{}'.format(specifier, behavior_name))
        self.output_tla.append(behavior_value)

    def _parse_behavior(self):
        """parse behavior section"""
        if 'behavior' in self.cfg:
            behavior = self.cfg['behavior']
            init_predicate = behavior.get('init')
            next_state = behavior.get('next')
            temporal_formula = behavior.get('temporal formula')
            if (init_predicate or next_state) and (not init_predicate or not next_state or temporal_formula):
                raise ValueError('[behavior] choose one or none: "init/next" **OR** "temporal formula"')
            if temporal_formula:
                self._add_behavior('SPECIFICATION', 'spec', temporal_formula)
            else:
                self._add_behavior('INIT', 'init', init_predicate)
                self._add_behavior('NEXT', 'next', next_state)

    def _add_specifications(self, keyword, specifier, prefix):
        """invariants and properties share the same parser"""
        if keyword in self.cfg:
            spec = self.cfg[keyword]
            spec_names = '\n'.join('{}_{}_{}'.format(prefix, i, id(i)) for i in spec)
            if spec_names != '':
                self.output_cfg.append('{}\n{}'.format(specifier, spec_names))
                spec_values = '\n'.join('{}_{}_{} ==\n{}'.format(prefix, i, id(i), spec[i]) for i in spec)
                self.output_tla.append(spec_values)

    def _parse_invariants(self):
        """parse invariants section"""
        self._add_specifications('invariants', 'INVARIANT', 'inv')

    def _parse_properties(self):
        """parse properties section"""
        self._add_specifications('properties', 'PROPERTY', 'prop')

    def _parse_constants(self, keyword='constants', prefix='const'):
        """parse constants section"""
        if keyword in self.cfg:
            constants = self.cfg[keyword]
            for name in constants:
                value = constants[name]
                is_model_value = False
                is_symmetrical = False
                if self.model_sym_pat.match(value):
                    is_model_value = True
                    value = self.model_sym_pat.match(value).groups()[0].replace(' ', '').split(',')
                    if len(value) <= 1:
                        print('Warning: "{}: {}": <symmetrical> ignored'.format(name, constants[name]), file=sys.stderr)
                    else:
                        is_symmetrical = True
                elif self.model_pat.match(value):
                    is_model_value = True
                    value = self.model_pat.match(value).groups()[0].replace(' ', '').split(',')
                elif value == '[model value]':
                    is_model_value = True
                    value = name
                if is_model_value:
                    if isinstance(value, list):  # set of model values
                        model_val = '\n'.join('{} = {}'.format(i, i) for i in value)
                        cfg_str = 'CONSTANTS\n{}\nCONSTANT\n{} <- const_{}_{}'.format(model_val, name, name, id(name))
                        model_val = ', '.join(i for i in value)
                        tla_str = 'CONSTANTS\n{}\nconst_{}_{} ==\n{{{}}}'.format(model_val, name, id(name), model_val)
                        if is_symmetrical:  # symmetry set
                            cfg_str = '{}\nSYMMETRY symm_{}_{}'.format(cfg_str, name, id(value))
                            tla_str = '{}\nsymm_{}_{} ==\nPermutations(const_{}_{})'.format(tla_str, name, id(value),
                                                                                            name, id(name))
                    else:  # model value
                        cfg_str = 'CONSTANT {} = {}'.format(name, value)
                        tla_str = None
                else:  # ordinary assignment
                    cfg_str = 'CONSTANT\n{} <- {}_{}_{}'.format(name, prefix, name, id(name))
                    tla_str = '{}_{}_{} == \n{}'.format(prefix, name, id(name), value)
                self.output_cfg.append(cfg_str)
                self.output_tla.append(tla_str)

    def _parse_override(self):
        """parse override section"""
        self._parse_constants(keyword='override', prefix='over')

    def _parse_const_expr(self):
        """parse const expr section"""
        if 'const expr' in self.cfg:
            const_expr = self.cfg.get('const expr', 'expr', fallback=None)
            if const_expr:
                self.output_cfg.append(None)
                val = 'const_expr_{}'.format(id(const_expr))
                self.output_tla.append('{} ==\n{}\nASSUME PrintT(<<"$!@$!@$!@$!@$!",{}>>)'.format(val, const_expr, val))

    def parse(self):
        self.output_cfg = []
        self.output_tla = []
        self._parse_behavior()
        self._parse_invariants()
        self._parse_properties()
        self._parse_constants()
        self._parse_override()
        self._parse_const_expr()

    def write(self, output_cfg_fn=None, output_tla_fn=None):
        """write parsed buf to file"""
        if output_cfg_fn is None:
            output_cfg_fn = self.output_cfg_fn
        if output_tla_fn is None:
            output_tla_fn = self.output_tla_fn
        with open(output_cfg_fn, 'w') as cfg_f:
            cfg_f.write('{} on {}\n'.format(self.tag, datetime.now()))
            cfg_f.write('\n\n'.join(filter(None, self.output_cfg)))
            cfg_f.write('\n')
        with open(output_tla_fn, 'w') as tla_f:
            module = '---- MODULE {} ----\n'.format(output_tla_fn.rstrip('.tla'))
            tla_f.write(module)
            tla_f.write('EXTENDS {}, TLC\n'.format(self.top_module))
            tla_f.write('\n----\n\n'.join(filter(None, self.output_tla)))
            tla_f.write('\n{}\n'.format('=' * len(module)))
            tla_f.write('{} on {}\n'.format(self.tag, datetime.now()))


class TLCWrapper:
    """TLC cmdline options"""
    _script_dir = os.path.dirname(os.path.realpath(__file__))
    tla2tools_jar = os.path.join(_script_dir, 'tla2tools.jar')
    tla2tools_class = 'tlc2.TLC'
    _tlc_cmd = ['java', '-cp', tla2tools_jar, tla2tools_class]

    default_config_file = 'config.ini'
    default_mc_cfg = 'MC.cfg'
    default_mc_tla = 'MC.tla'
    default_mc_log = 'MC.out'

    def __init__(self, config_file=None, log_file=True, gen_cfg_fn=None, gen_tla_fn=None):
        """create model dir, chdir, copy files and generate tlc configfile"""
        config_file = config_file if config_file is not None else self.default_config_file
        self.cfg = ConfigParser()
        self.cfg.optionxform = str  # case sensitive
        if hasattr(config_file, 'read'):
            self.cfg.read_file(config_file)
        else:
            self.cfg.read(config_file)
        self.orig_cwd = os.getcwd()

        if isinstance(log_file, str):  # if log_file specified, open it before change cwd
            self.log_file = open(log_file, 'w')

        target = self.cfg.get('options', 'target')
        model_name = self.cfg.get('options', 'model name')
        os.chdir(os.path.dirname(os.path.realpath(target)))
        os.makedirs(model_name, exist_ok=True)
        for file in os.listdir('.'):
            if file.endswith('.tla'):
                copy2(file, model_name)
        os.chdir(model_name)

        if log_file:
            if not isinstance(log_file, str):
                self.log_file = open(self.default_mc_log, 'w')
        else:
            self.log_file = None

        self.gen_cfg_fn = gen_cfg_fn if gen_cfg_fn is not None else self.default_mc_cfg
        self.gen_tla_fn = gen_tla_fn if gen_tla_fn is not None else self.default_mc_tla
        TLCConfigFile(self.cfg, self.gen_cfg_fn, self.gen_tla_fn).write()

        self.options = []
        self._parse_options()

        result_key = ['start time', 'finish time', 'time consuming',
                      'diameter', 'total states', 'distinct states', 'queued states',
                      'warnings', 'errors', 'exit state']
        self.result = OrderedDict(zip_longest(result_key, tuple()))
        self.log_lines = []

    def __del__(self):
        if hasattr(self.log_file, 'close'):
            self.log_file.close()
        os.chdir(self.orig_cwd)

    def _parse_options(self):
        """parse options section"""
        self.options = [self.gen_tla_fn, '-config', self.gen_cfg_fn]
        opt = self.cfg['options']
        options_list = [opt.get('user print file'), opt.getint('worker num'), opt.getint('checkpoint num'),
                        opt.get('dump states file'), opt.getint('dfs depth'), not opt.getboolean('check deadlock')]
        options = ['-userFile', '-workers', '-checkpoint', '-dump', '-dfid', '-deadlock']
        for i, j in zip(options, options_list):
            if j:
                self.options.append(i)
                if not isinstance(j, bool):
                    self.options.append(str(j))
        if opt.get('other TLC options') is not None:
            for field in opt.get('other TLC options').split('\n'):
                self.options.append(field)

    def get_cmd(self):
        """get tlc command line"""
        return ' '.join(i for i in chain(self._tlc_cmd, self.options))

    def raw_run(self):
        """directly call tlc program without analysing the output"""
        subprocess.call(self._tlc_cmd + self.options)

    def run(self):
        """call tlc and analyse output"""
        title_printed = False
        title_list = ['Time', 'Diameter', 'States Found', 'Distinct States', 'Queue Size']

        def print_state(time):
            nonlocal title_printed
            value_list = [str(time), self.result['diameter'], self.result['total states'],
                          self.result['distinct states'], self.result['queued states']]
            if all(i is not None for i in value_list):
                if not title_printed:
                    title_printed = True
                    print(('{:<16}' * 5).format(*title_list))
                print(('{:<16}' * 5).format(*value_list))

        progress_pat = re.compile(r'Progress\((\d+)\) at (.*): (\d+) s.*\(.*\), (\d+) d.*\(.*\), (\d+) s')
        finish_pat = re.compile(r'(\d+) states generated, (\d+) distinct states found, (\d+) states left on queue')

        self.result['warnings'] = []
        self.result['errors'] = []
        self.result['start time'] = datetime.now()

        process = subprocess.Popen(self._tlc_cmd + self.options, stdout=subprocess.PIPE, universal_newlines=True)
        for line in iter(process.stdout.readline, ''):
            self.log_lines.append(line)
            if self.log_file:
                self.log_file.write(line)
                self.log_file.flush()
            line = line.rstrip()
            if len(line) == 0:
                continue
            if line.startswith('Starting...'):
                self.result['start time'] = datetime.strptime(line, 'Starting... (%Y-%m-%d %H:%M:%S)')
            elif line.startswith('Finished in'):
                self.result['finish time'] = datetime.strptime(line.split('at')[1], ' (%Y-%m-%d %H:%M:%S)')
                # if self.result['finish time'] == self.result['start time']:
                #     self.result['finish time'] = datetime.now()
                self.result['time consuming'] = self.result['finish time'] - self.result['start time']
                print_state(self.result['time consuming'])
            elif line.startswith('Progress'):
                groups = progress_pat.match(line).groups()
                self.result['diameter'] = int(groups[0])
                self.result['total states'] = int(groups[2])
                self.result['distinct states'] = int(groups[3])
                self.result['queued states'] = int(groups[4])
                current_time = datetime.strptime(groups[1], '%Y-%m-%d %H:%M:%S')
                print_state(current_time - self.result['start time'])
            elif line.startswith('Finished computing initial states'):
                states = int(line.split(':')[1].split(' ')[1])
                self.result['diameter'] = 0
                self.result['total states'] = states
                self.result['distinct states'] = states
                self.result['queued states'] = states
                print_state(str(datetime.now() - self.result['start time']).split('.')[0])
            elif line[0].isdigit() and finish_pat.match(line) is not None:
                groups = finish_pat.match(line).groups()
                self.result['total states'] = int(groups[0])
                self.result['distinct states'] = int(groups[1])
                self.result['queued states'] = int(groups[2])
            elif line.startswith('The depth of the complete state graph search is'):
                diameter = int(line.split(' ')[9].rstrip('.'))
                self.result['diameter'] = diameter
            elif line.startswith('Warning:'):
                self.result['warnings'].append(line)
            elif line.startswith('Error:'):
                self.result['errors'].append(line)

        self.result['exit state'] = process.poll()
        if self.result['exit state'] is None:
            self.result['exit state'] = 0
        return self.result

    def get_log(self):
        return self.log_lines

    def save_log(self, filename=None):
        if filename is None:
            filename = self.default_mc_log
        with open(filename, 'w') as f:
            f.writelines(self.log_lines)


def main(config_file, log_file=True):
    tlc = TLCWrapper(config_file, log_file=log_file)
    result = tlc.run()
    for msg in chain(result['warnings'], result['errors']):
        print(msg, file=sys.stderr)
    print('errors: {}, warnings: {}, exit_state: {}'.format(len(result['errors']), len(result['warnings']),
                                                            result['exit state']), file=sys.stderr)
    del tlc


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise ValueError('Usage: python3 {} config.ini [MC.out]'.format(sys.argv[0]))
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
