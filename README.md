# TLC Batch

## Description
It is quite troublesome to test these similar and complicated tasks with the TLA+ Toolbox.
So the TLC Batch script was written to automatically check the Jupiter protocol family under different test scales.

## How to run
Simply make it.
```bash
# run refinement and output 4 latex result table files.
# will only run AbsJupiterH, AJupiterImplXJupiter, CJupiterImplAbsJupiter and XJupiterImplCJupiter.
make
make run
make WORKERS=  # using n workers. n will be set as physical cores.
make WORKERS=2  # using 2 workers.
```

## Others
Each time you run tlc, a subdirectory will be generated in the protocol directory,
such as `TypeOK (1 clients, 1 chars)`. This directory is used to store the tla file and cfg file required for running.

Any files start with `MC` may be helpful for you.

| filename                     | description                                  |
|------------------------------|----------------------------------------------|
| MC.cfg/MC.tla                | Generated by TLCWrapper.py. Required by TLC. |
| MC_out.txt                   | TLC (tool mode) log.                         |
| MC_user.txt                  | User output (using Print or PrintT).         |
| MC_states.dump/MC_states.dot | All states dump (if enabled).                |
| MC_coverage.txt              | Coverage information (if enabled.).          |

The `tlcwrapper.py` script encapsulates the running mode of tlc, which can be reused.
The first parameter of the script is the configuration file, the detailed rules of the configuration file can be found 
in `config.ini`; the second parameter is optional tlc log file (`MC_out.txt` by default).
