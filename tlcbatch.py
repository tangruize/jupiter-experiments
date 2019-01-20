#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by tangruize on 19-1-20.
import sys

from collections import OrderedDict
from io import StringIO
from tlcwrapper import TLCWrapper

if len(sys.argv) != 2:
    raise ValueError('Usage: python3 {} result.md'.format(sys.argv[0]))

template = '''[options]
target: {target}
model name: {model}
worker num: 10

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

config = OrderedDict()
config['AbsJupiter'] = {'target': 'AbsJupiter/AbsJupiter.tla',
                        'model': 'TypeOK',
                        'spec': 'Spec',
                        'invariant': 'TypeOK: TypeOK',
                        'msg': 'Cop'}
config['AbsJupiterH'] = {'target': 'AbsJupiterH/AbsJupiterH.tla',
                         'model': 'WLSpec',
                         'spec': 'SpecH',
                         'invariant': 'WLSpec: WLSpec',
                         'msg': 'Cop'}
config['CJupiter'] = {'target': 'CJupiter/CJupiter.tla',
                      'model': 'Compactness',
                      'spec': 'Spec',
                      'invariant': 'Compactness: Compactness',
                      'msg': 'Cop'}
config['CJupiterH'] = {'target': 'CJupiterH/CJupiterH.tla',
                       'model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'Cop'}
config['CJupiterImplAbsJupiter'] = {'target': 'CJupiterImplAbsJupiter/CJupiterImplAbsJupiter.tla',
                                    'model': 'AbsJ!Spec (NO)',
                                    'spec': 'Spec',
                                    'invariant': '[properties]\nCJupiterImplAbsJupiter: AbsJ!Spec',
                                    'msg': 'Cop'}
config['XJupiter'] = {'target': 'XJupiter/XJupiter.tla',
                      'model': 'CSSync',
                      'spec': 'Spec',
                      'invariant': 'CSSync: CSSync',
                      'msg': 'Cop'}
config['XJupiterH'] = {'target': 'XJupiterH/XJupiterH.tla',
                       'model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'Cop'}
config['XJupiterExtended'] = {'target': 'XJupiterExtended/XJupiterExtended.tla',
                              'model': 'CSSync',
                              'spec': 'SpecEx',
                              'invariant': 'CSSync: CSSync',
                              'msg': 'Cop'}
config['XJupiterImplCJupiter'] = {'target': 'XJupiterImplCJupiter/XJupiterImplCJupiter.tla',
                                  'model': 'CJ!Spec (NO)',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nXJupiterImplCJupiter: CJ!Spec',
                                  'msg': 'Cop'}
config['AJupiter'] = {'target': 'AJupiter/AJupiter.tla',
                      'model': 'QC',
                      'spec': 'Spec',
                      'invariant': 'QC: QC',
                      'msg': 'AJMsg'}
config['AJupiterH'] = {'target': 'AJupiterH/AJupiterH.tla',
                       'model': 'WLSpec',
                       'spec': 'SpecH',
                       'invariant': 'WLSpec: WLSpec',
                       'msg': 'AJMsg'}
config['AJupiterExtended'] = {'target': 'AJupiterExtended/AJupiterExtended.tla',
                              'model': 'QC',
                              'spec': 'SpecEx',
                              'invariant': 'QC: QC',
                              'msg': 'AJMsgEx'}
config['AJupiterImplXJupiter'] = {'target': 'AJupiterImplXJupiter/AJupiterImplXJupiter.tla',
                                  'model': 'XJ!Spec (NO)',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nAJupiterImplXJupiter: XJ!Spec',
                                  'msg': 'AJMsgEx'}
chars = ['a', 'b', 'c', 'd']
clients = ['c1', 'c2', 'c3', 'c4']

output = open(sys.argv[1], 'w')
output.write('# Model Checking Result\n')

title = ['Protocol', 'Fairness', 'Property', 'Start Time', '# Workers', 'Checking Time', 'Diameter', '# States',
         '# Distinct States', 'Symmetry for Char', 'Symmetry for Client']
title_len = [22, 8, 14, 19, 9, 13, 8, 10, 10, 17, 19]
formatter = []
for i in title_len:
    formatter.append('{{:<{}}}'.format(i))
formatter = '| {} |\n'.format(' | '.join(formatter))
title = formatter.format(*title)
title2 = formatter.format(*['-' * i for i in title_len])

for client in range(1, 4):
    for char in range(1, 4):
        if client == 3 and char == 3:
            continue
        config_clients = clients[:client]
        config_chars = chars[:char]
        output.write('\n## {} Clients `{{{}}}` + {} Chars `{{{}}}`\n'.format(client, ', '.join(config_clients),
                                                                             char, ', '.join(config_chars)))
        output.write(title)
        output.write(title2)
        for proto in config:
            proto_config = config[proto]
            proto_config['client'] = ', '.join(config_clients)
            proto_config['char'] = ', '.join(config_chars)
            config_string_io = StringIO(template.format(**proto_config))
            tlc = TLCWrapper(config_string_io)
            print('starting "{}" : {} clients, {} chars'.format(proto, len(config_clients), len(config_chars)))
            result = tlc.run()
            output.write(formatter.format(proto, 'No', proto_config['model'], str(result['start time']), 10,
                                          str(result['time consuming']), result['diameter'], result['total states'],
                                          result['distinct states'], 'YES', 'NO'))
            output.flush()
            tlc.save_log()
            del tlc
            print()

output.close()
