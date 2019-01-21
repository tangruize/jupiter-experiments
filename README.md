# TLC Batch v1.3

## 简介
用TLA+ Toolbox图形化界面检验这些相似而繁多的任务颇为麻烦, 所以编写了TLC Batch脚本自动检验Jupiter协议族不同测试规模下的状态数和性能.

## 运行
直接`make`将使用10个worker运行. `make WORKERS=4`将使用4个worker. `make WORKERS=`将使用系统核心数的worker数量运行.
运行终端将打印当前tlc的进展. `result.md`文件实时输出模型检验结果, 可以使用`tail -F result.md`观察输出.

## 说明
每一次运行tlc都会协议目录下会生成一个子目录, 如`TypeOK (1 clients, 1 chars)`. 该目录用于存放运行需要的tla文件和cfg文件.
并将tlc的输出实时写入`MC.out`文件中. 该目录中的`states`目录为checkpoint, 当程序非正常终止时可以通过某些选项来重新启动.

tlc工具选项较多, 只挑选了一部分进行封装. 比较有意思的选项有:
1. `-dump file` 将检验产生的状态输出到`file`文件, 这有助于某些情况下的调试.
2. `-userFile file` 将 `Print` 或 `PrintT` 函数的输出重定向到`file`文件, 也有助于调试.

`tlcwrapper.py`脚本封装了tlc的运行方式, 可以复用. 该脚本第一个参数为配置文件, 配置文件详细规则见`config.ini`; 第二个参数为可选的 tlc
输出文件, 如果不指定则输出到运行目录的`MC.out`文件中.

`tlcbatch.py`脚本为Jupiter各个协议的运行配置, 并产生`chars: 1..3`和`clients 1..3`的组合. 不会运行`chars: 3, clients:3`.
脚本第一个参数为输出模型检验结果文件, 如`result.md`; 第二个参数为可选的`worker num`, 如果不指定则根据当前系统的核心数设置.

注意`tla2tools.jar`, `tlcbatch.py` 和 `tlcwrapper.py` 要放在同一个目录下.

---
Ruize Tang

2019-01-21 14:12:12
