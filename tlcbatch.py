#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by tangruize on 19-1-20.
import sys

from collections import OrderedDict
from io import StringIO
from tlcwrapper import TLCWrapper

if len(sys.argv) == 1:
    raise ValueError('Usage: python3 {} result.md [worker num]'.format(sys.argv[0]))
elif len(sys.argv) == 3:
    workers = int(sys.argv[2])
else:
    workers = 10

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
'''


class _SafeSubstitute(dict):
    def __missing__(self, key):
        if key == 'char' or key == 'client':
            return '{{' + key + '}}'
        return '{' + key + '}'


template = template.format_map(_SafeSubstitute({'worker': workers}))

config = OrderedDict()
config['AbsJupiter'] = {'target': 'AbsJupiter/AbsJupiter.tla',
                        '_model': 'TypeOK',
                        'spec': 'Spec',
                        'invariant': 'TypeOK: TypeOK',
                        'msg': 'Cop'}
config['AbsJupiterH'] = {'target': 'AbsJupiterH/AbsJupiterH.tla',
                         '_model': 'WLSpec',
                         'spec': 'SpecH',
                         'invariant': 'WLSpec: WLSpec',
                         'msg': 'Cop'}
config['CJupiter'] = {'target': 'CJupiter/CJupiter.tla',
                      '_model': 'Compactness',
                      'spec': 'Spec',
                      'invariant': 'Compactness: Compactness',
                      'msg': 'Cop'}
config['CJupiterH'] = {'target': 'CJupiterH/CJupiterH.tla',
                       '_model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'Cop'}
config['CJupiterImplAbsJupiter'] = {'target': 'CJupiterImplAbsJupiter/CJupiterImplAbsJupiter.tla',
                                    '_model': 'AbsJ!Spec (NO)',
                                    'spec': 'Spec',
                                    'invariant': '[properties]\nCJupiterImplAbsJupiter: AbsJ!Spec',
                                    'msg': 'Cop'}
config['XJupiter'] = {'target': 'XJupiter/XJupiter.tla',
                      '_model': 'CSSync',
                      'spec': 'Spec',
                      'invariant': 'CSSync: CSSync',
                      'msg': 'Cop'}
config['XJupiterH'] = {'target': 'XJupiterH/XJupiterH.tla',
                       '_model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'Cop'}
config['XJupiterExtended'] = {'target': 'XJupiterExtended/XJupiterExtended.tla',
                              '_model': 'CSSync',
                              'spec': 'SpecEx',
                              'invariant': 'CSSync: CSSync',
                              'msg': 'Cop'}
config['XJupiterImplCJupiter'] = {'target': 'XJupiterImplCJupiter/XJupiterImplCJupiter.tla',
                                  '_model': 'CJ!Spec (NO)',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nXJupiterImplCJupiter: CJ!Spec',
                                  'msg': 'Cop'}
config['AJupiter'] = {'target': 'AJupiter/AJupiter.tla',
                      '_model': 'QC',
                      'spec': 'Spec',
                      'invariant': 'QC: QC',
                      'msg': 'AJMsg'}
config['AJupiterH'] = {'target': 'AJupiterH/AJupiterH.tla',
                       '_model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'AJMsg'}
config['AJupiterExtended'] = {'target': 'AJupiterExtended/AJupiterExtended.tla',
                              '_model': 'QC',
                              'spec': 'SpecEx',
                              'invariant': 'QC: QC',
                              'msg': 'AJMsgEx'}
config['AJupiterImplXJupiter'] = {'target': 'AJupiterImplXJupiter/AJupiterImplXJupiter.tla',
                                  '_model': 'XJ!Spec (NO)',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nAJupiterImplXJupiter: XJ!Spec',
                                  'msg': 'AJMsgEx'}
chars = ['a', 'b', 'c', 'd']
clients = ['c1', 'c2', 'c3', 'c4']

output = open(sys.argv[1], 'w')
output.write('# Model Checking Result\n')

title = ['Protocol', 'Fairness', 'Property', 'Start Time', '# Workers', 'Checking Time', 'Diameter', '# States',
         '# Distinct States', 'Symmetry for Char', 'Symmetry for Client']
field_len = [22, 8, 14, 19, 9, 13, 8, 10, 17, 17, 19]
formatter = []
for i in field_len:
    formatter.append('{{:<{}}}'.format(i))
formatter = '| {} |\n'.format(' | '.join(formatter))
title = formatter.format(*title)
title2 = formatter.format(*['-' * i for i in field_len])

for client in range(1, 4):
    suffix_client = 's' if client != 1 else ''
    for char in range(1, 4):
        if client == 3 and char == 3:
            continue
        config_clients = clients[:client]
        config_chars = chars[:char]
        suffix_char = 's' if char != 1 else ''
        output.write('\n## {} Client{} `{{{}}}` + {} Char{} `{{{}}}`\n'.format(
            client, suffix_client, ', '.join(config_clients), char, suffix_char, ', '.join(config_chars))
        )
        output.write(title)
        output.write(title2)
        sym_char = 'YES' if char != 1 else 'NO'
        for proto in config:
            proto_config = config[proto]
            proto_config['client'] = ', '.join(config_clients)
            proto_config['char'] = ', '.join(config_chars)
            proto_config['model'] = '{} ({} clients, {} chars)'.format(proto_config['_model'], client, char)
            config_string_io = StringIO(template.format(**proto_config))
            tlc = TLCWrapper(config_string_io)
            print('starting "{}" : {} clients, {} chars'.format(proto, len(config_clients), len(config_chars)))
            result = tlc.run()
            output.write(formatter.format(proto, 'No', proto_config['_model'], str(result['start time']), workers,
                                          str(result['time consuming']), result['diameter'], result['total states'],
                                          result['distinct states'], sym_char, 'NO'))
            output.flush()
            del tlc
            print()

output.close()
