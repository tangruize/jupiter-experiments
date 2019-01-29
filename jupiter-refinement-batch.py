#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by tangruize on 19-1-29.

import sys
import os

from collections import OrderedDict
from io import StringIO
from tlcwrapper import TLCWrapper

if len(sys.argv) == 1:
    raise ValueError('Usage: python3 {} result_dir [worker num]'.format(sys.argv[0]))
elif len(sys.argv) == 3:
    workers = int(sys.argv[2])
else:
    workers = os.cpu_count()
    if workers is None:
        workers = 1

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
{constraint}
'''


class _SafeSubstitute(dict):
    def __missing__(self, key):
        if key == 'char' or key == 'client':
            return '{{' + key + '}}'
        return '{' + key + '}'


template = template.format_map(_SafeSubstitute({'worker': workers}))

config = OrderedDict()
config['AbsJupiterH'] = {'FILENAME': 'tlc-absjupiterh-table.tex',
                         'VERIFYING': r'\absjupiter{} satisfies $WLSpec$',
                         'target': 'AbsJupiterH/AbsJupiterH.tla',
                         '_model': 'WLSpec',
                         'spec': 'SpecH',
                         'invariant': 'WLSpec: WLSpec',
                         'msg': 'Cop'}
config['CJupiterImplAbsJupiter'] = {'FILENAME': 'tlc-cjupiterimplabsjupiter-table.tex',
                                    'VERIFYING': r'\cjupiter{} refines \absjupiter{}',
                                    'target': 'CJupiterImplAbsJupiter/CJupiterImplAbsJupiter.tla',
                                    '_model': 'AbsJ!Spec',
                                    'spec': 'Spec',
                                    'invariant': '[properties]\nCJupiterImplAbsJupiter: AbsJ!Spec',
                                    'msg': 'Cop'}
config['XJupiterImplCJupiter'] = {'FILENAME': 'tlc-xjupiterimplcjupiter-table.tex',
                                  'VERIFYING': r'\xjupiter{} refines \cjupiter{}',
                                  'target': 'XJupiterImplCJupiter/XJupiterImplCJupiter.tla',
                                  '_model': 'CJ!Spec',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nXJupiterImplCJupiter: CJ!Spec',
                                  'msg': 'Cop'}
config['AJupiterImplXJupiter'] = {'FILENAME': 'tlc-ajupiterimplxjupiter-table.tex',
                                  'VERIFYING': r'\ajupiter{} refines \xjupiter{}',
                                  'target': 'AJupiterImplXJupiter/AJupiterImplXJupiter.tla',
                                  '_model': 'XJ!Spec',
                                  'spec': 'SpecImpl',
                                  'invariant': '[properties]\nAJupiterImplXJupiter: XJ!Spec',
                                  'msg': 'AJMsgEx'}

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

field_len = [12, 10, 18, 18, 12]

formatter = []
for i in field_len:
    formatter.append('{{:<{}}}'.format(i))
formatter = '    {} \\\\ \\hline\n'.format(' & '.join(formatter))

chars = ['a', 'b', 'c', 'd', 'e']
clients = ['c1', 'c2', 'c3', 'c4', 'c5']

os.makedirs(sys.argv[1], exist_ok=True)

for proto, proto_config in config.items():
    latex_file = open(os.path.join(sys.argv[1], proto_config['FILENAME']), 'w')
    latex_begin = latex_template_begin.replace('FILENAME', proto_config['FILENAME'])\
        .replace('VERIFYING', proto_config['VERIFYING']).replace('LABEL', proto.lower())
    latex_file.write(latex_begin)
    for client in range(1, 6):
        config_clients = clients[:client]
        for char in range(1, 6):
            if char != 1 and client != 1 and char + client >= 6:
                proto_config['constraint'] = 'ClientConstraint: ClientConstraint'
                # continue
            else:
                proto_config['constraint'] = ''
                # continue
            config_chars = chars[:char]
            proto_config['client'] = ', '.join(config_clients)
            proto_config['char'] = ', '.join(config_chars)
            proto_config['model'] = '{} ({} clients, {} chars)'.format(proto_config['_model'], client, char)
            config_string_io = StringIO(template.format(**proto_config))
            tlc = TLCWrapper(config_string_io)
            print('starting "{}" : {} clients, {} chars'.format(proto, client, char))
            result = tlc.run()
            client_char = '({}, {})'.format(client, char)
            str_list = []
            for item in (client_char, result['diameter'], result['total states'], result['distinct states'],
                         str(result['time consuming'])):
                str_list.append('${}$'.format(item))
            latex_file.write(formatter.format(*str_list))
            latex_file.flush()
            del tlc
            print()

    latex_file.write(latex_template_end)
    latex_file.close()
