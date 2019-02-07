#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by anonymous on 19-1-29.

import sys
import os
import time
import re

from collections import OrderedDict, defaultdict
from io import StringIO
from shutil import copy2
from tlcwrapper import TLCWrapper

if len(sys.argv) == 1:
    raise ValueError('Usage: python3 {} result_dir [worker num]'.format(sys.argv[0]))
elif len(sys.argv) == 3:  # worker num
    workers = int(sys.argv[2])
else:
    workers = os.cpu_count()
    if workers is None:
        workers = 1

# config file template
template = '''[options]
target: {target}
model name: {model}
worker num: {worker}

[behavior]
temporal formula: {spec}

[invariants]
{invariant}

[constants]
Char: [model value]<symmetrical>{{{char}}}
Client: [model value]{{{client}}}
Server: [model value]
InitState: <<>>
Msg: {msg}

[override]
Nop: [model value]

[state constraint]
{has_sc}SC: TLCSet("exit", TLCGet("distinct") > {distinct})
'''


class _SafeSubstitute(dict):
    """to keep {}"""
    def __missing__(self, key):
        if key == 'char' or key == 'client':
            return '{{' + key + '}}'
        return '{' + key + '}'


template = template.format_map(_SafeSubstitute({'worker': workers}))

# configurations
config = OrderedDict()
config['AbsJupiter'] = {'FILENAME': 'tlc-absjupiter-table',  # filename will add a timestamp
                        'VERIFYING': r'\absjupiter{} satisfies $WLSpec$',  # latex description
                        'VERIFYING_MD': r'`absjupiter` satisfies `WLSpec`',
                        'target': 'AbsJupiterH/AbsJupiterH.tla',  # target file
                        '_model': 'WLSpec',  # model (description)
                        'spec': 'SpecH',
                        'invariant': 'WLSpec: WLSpec',
                        'msg': 'Cop',
                        'distinct': 100000000}  # state constraint
config['CJupiterImplAbsJupiter'] = {'FILENAME': 'tlc-cjupiterimplabsjupiter-table',
                                    'VERIFYING': r'\cjupiter{} refines \absjupiter{}',
                                    'VERIFYING_MD': r'`cjupiter` refines `absjupiter`',
                                    'target': 'CJupiterImplAbsJupiter/CJupiterImplAbsJupiter.tla',
                                    '_model': 'AbsJ!Spec',
                                    'spec': 'Spec',
                                    'invariant': '[properties]\nCJupiterImplAbsJupiter: AbsJ!Spec',
                                    'msg': 'Cop',
                                    'distinct': 80000000}
config['XJupiterImplCJupiter'] = {'FILENAME': 'tlc-xjupiterimplcjupiter-table',
                                  'VERIFYING': r'\xjupiter{} refines \cjupiter{}',
                                  'VERIFYING_MD': r'`xjupiter` refines `cjupiter`',
                                  'target': 'XJupiterImplCJupiter/XJupiterImplCJupiter.tla',
                                  '_model': 'CJ!Spec',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nXJupiterImplCJupiter: CJ!Spec',
                                  'msg': 'Cop',
                                  'distinct': 80000000}
config['AJupiterImplXJupiter'] = {'FILENAME': 'tlc-ajupiterimplxjupiter-table',
                                  'VERIFYING': r'\ajupiter{} refines \xjupiter{}',
                                  'VERIFYING_MD': r'`ajupiter` refines `xjupiter`',
                                  'target': 'AJupiterImplXJupiter/AJupiterImplXJupiter.tla',
                                  '_model': 'XJ!Spec',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nAJupiterImplXJupiter: XJ!Spec',
                                  'msg': 'AJMsgEx',
                                  'distinct': 80000000}

# latex output file template
latex_template_begin = r'''% file: FILENAME

% \usepackage{graphicx}
\begin{table}[t]
  \caption{Model checking results of verifying that VERIFYING.}
  \label{tbl:tlc-LABEL}
  \resizebox{\textwidth}{!}{%
    \centering
    \renewcommand*{\arraystretch}{1.1}
    \begin{tabular}{|c|c|c|c|c|}
    \hline
    \textbf{\incell{TLC Model}{$(\# Clients, \# Chars)$}} & \textbf{Diameter} & \textbf{\# States} & \textbf{\# Distinct States} 
    & \textbf{\incell{Checking Time}{$(hh:mm:ss)$}} \\ \hline
    \hline
'''
latex_template_end = r'''    \end{tabular}%
  }
\end{table}
'''

# markdown output file template
markdown_template_begin = r'''# Model checking results of verifying that VERIFYING.

'''

# using uniform start time as timestamp
start_time = time.strftime("%Y%m%d-%H%M%S")


def get_time():
    return start_time


def get_filename(proto_):
    # return '{}-{}.tex'.format(proto_['FILENAME'], get_time())
    return '{}.tex'.format(proto_['FILENAME'])


def get_latex_formatter():
    """to format result string"""
    field_len_ = [12, 10, 18, 18, 12]
    formatter_ = []
    for i in field_len_:
        formatter_.append('{{:<{}}}'.format(i))
    formatter_ = '    {} \\\\ \\hline\n'.format(' & '.join(formatter_))
    return formatter_, field_len_


def get_markdown_formatter(ignore_proto=False):
    field_len_ = [22, 14, 19, 9, 13, 8, 10, 17]
    if ignore_proto:
        field_len_ = [7, 5] + field_len_[2:]
    formatter_ = []
    for i in field_len_:
        formatter_.append('{{:<{}}}'.format(i))
    formatter_ = '| {} |\n'.format(' | '.join(formatter_))
    return formatter_, field_len_


def get_markdown_title(formatter_, field_len_, ignore_proto=False):
    """markdown table header"""
    title_ = ['Protocol', 'Property', 'Start Time', '# Workers', 'Checking Time', 'Diameter', '# States',
              '# Distinct States']
    if ignore_proto:
        title_ = ['Clients', 'Chars'] + title_[2:]
    title_ = formatter_.format(*title_)
    title2 = formatter_.format(*['-' * i for i in field_len_])
    return title_ + title2


def copy_files_from_md(proto_):
    """copy required tla files from README.md"""
    target_dir = os.path.dirname(proto_['target'])
    md_file = open(os.path.join(target_dir, 'README.md'), 'r')
    pat = re.compile(r'\[(.*tla)\]\((.*)\)')
    file_list = []
    for line in md_file:
        line = line.strip()
        if line == '# PDF Files':
            break
        m = pat.match(line)
        if m is not None:
            tla_dst = os.path.join(target_dir, m.groups()[0])
            tla_src = os.path.join(target_dir, m.groups()[1])
            file_list.append(tla_dst)
            copy2(tla_src, tla_dst)
    return file_list


# scales
chars = ['a', 'b', 'c', 'd', 'e']
clients = ['c1', 'c2', 'c3', 'c4', 'c5']
exp_size = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3),
            (4, 1), (4, 2),
            (5, 1)]
# exp_size = [(1, 1), (1, 2)]
sc_set = {(2, 4), (3, 3), (4, 2)}  # big experiment that use state constraint

formatter, _ = get_latex_formatter()
md_formatter, md_field_len = get_markdown_formatter(ignore_proto=True)
md_title = get_markdown_title(md_formatter, md_field_len, ignore_proto=True)
sys.argv[1] = os.path.join(sys.argv[1], get_time())
os.makedirs(sys.argv[1], exist_ok=True)
result_dict = defaultdict(list)


# run and output to latex result file
for proto, proto_config in config.items():
    latex_file = open(os.path.join(sys.argv[1], get_filename(proto_config)), 'w')
    latex_begin = latex_template_begin.replace('FILENAME', proto_config['FILENAME'] + '.tex')\
        .replace('VERIFYING', proto_config['VERIFYING']).replace('LABEL', proto.lower())  # replace descriptions
    latex_file.write(latex_begin)  # write template
    markdown_file = open(os.path.join(sys.argv[1], proto_config['FILENAME'] + '.md'), 'w')
    markdown_begin = markdown_template_begin.replace('VERIFYING', proto_config['VERIFYING_MD'])
    markdown_file.write(markdown_begin)
    markdown_file.write(md_title)
    tla_files = copy_files_from_md(proto_config)
    for client, char in exp_size:
        config_clients = clients[:client]
        config_chars = chars[:char]
        proto_config['client'] = ', '.join(config_clients)
        proto_config['char'] = ', '.join(config_chars)
        proto_config['model'] = '{} ({} clients, {} chars) {}'.format(proto_config['_model'], client, char, get_time())
        if (client, char) in sc_set:
            proto_config['has_sc'] = ''  # enable state constraint
        else:
            proto_config['has_sc'] = '#'  # disable state constraint

        # StringIO is a file object. no need to create temp files
        config_string_io = StringIO(template.format_map(proto_config))
        tlc = TLCWrapper(config_string_io)
        print('starting "{}" : {} clients, {} chars'.format(proto, client, char))
        try:
            result = tlc.run()  # run tlc
        except KeyboardInterrupt:  # ctrl + c to interrupt current task
            print('Interrupted: "{}" with {} clients, {} chars'.format(proto, client, char))
            del tlc
            continue
        client_char = '({}, {})'.format(client, char)
        str_list = []
        for item in (client_char, result['diameter'], result['total states'], result['distinct states'],
                     str(result['time consuming'])):
            str_list.append('${}$'.format(item))
        latex_file.write(formatter.format(*str_list))  # write result
        latex_file.flush()
        result_dict[(client, char)].append((proto, proto_config.copy(), result))  # save result for markdown file
        markdown_file.write(md_formatter.format(client, char, str(result['start time']), workers,
                                                str(result['time consuming']), result['diameter'],
                                                result['total states'], result['distinct states']))
        markdown_file.flush()
        del tlc
        print()
    for tla in tla_files:
        os.remove(tla)
    latex_file.write(latex_template_end)
    latex_file.close()
    markdown_file.close()


# markdown all result in one file
formatter, field_len = get_markdown_formatter()
title = get_markdown_title(formatter, field_len)
markdown_file = open(os.path.join(sys.argv[1], 'result-all.md'), 'w')
markdown_file.write('# Model Checking Result\n')
for client, char in exp_size:
    suffix_client = 's' if client != 1 else ''
    suffix_char = 's' if char != 1 else ''
    config_clients = clients[:client]
    config_chars = chars[:char]
    markdown_file.write('\n## {} Client{} `{{{}}}` + {} Char{} `{{{}}}`\n'.format(
        client, suffix_client, ', '.join(config_clients), char, suffix_char, ', '.join(config_chars))
    )
    markdown_file.write(title)
    result_list = result_dict[(client, char)]
    for proto, proto_config, result in result_list:
        markdown_file.write(formatter.format(proto, proto_config['_model'], str(result['start time']), workers,
                                             str(result['time consuming']), result['diameter'], result['total states'],
                                             result['distinct states']))
markdown_file.close()

# finished! awesome!
