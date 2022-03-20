- [参考教程](https://www.cnblogs.com/yyds/p/6901864.html)
---

# logging模块之简单使用模块函数

## 一、  logging模块的日志级别

|日志等级（level）|描述|
|:----|:---|
|DEBUG	|最详细的日志信息，典型应用场景是 问题诊断|
|INFO	|信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
|WARNING	|当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
|ERROR	|由于一个更严重的问题导致某些功能不能正常运行时记录的信息
|CRITICAL	|当发生严重错误，导致应用程序不能继续运行时记录的信息

> - **DEBUG < INFO < WARNING < ERROR < CRITICAL**
> - **当指定日志级别后，会记录大于等于指定级别的日志**
> - **eg:指定INFO，则日志会记录 INFO < WARNING < ERROR < CRITICAL 这些日志级别日志**
> - **如果不设置日志级别，默认是 WARNING**

## 二、  logging模块的使用方法

- **使用logging提供的模块级别的函数**
- **使用Logging日志系统的四大组件**


## 三、  使用logging提供的模块级别的函数记录日志

| 函数|	说明|
|:---|:---|
| logging.debug(msg, *args, **kwargs)|创建一条严重级别为DEBUG的日志记录
| logging.info(msg, *args, **kwargs)|创建一条严重级别为INFO的日志记录
| logging.warning(msg, *args, **kwargs)|创建一条严重级别为WARNING的日志记录
| logging.error(msg, *args, **kwargs)|创建一条严重级别为ERROR的日志记录
| logging.critical(msg, *args, **kwargs)	|创建一条严重级别为CRITICAL的日志记录
| logging.log(level, *args, **kwargs)	|创建一条严重级别为level的日志记录
| **logging.basicConfig(**kwargs)** |	对root logger进行一次性配置,指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息


- **logging.basicConfig()函数说明**

|参数名称 |	描述|
|:---|:---|
|**filename**	|指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
|filemode	|指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
|**format**	|指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序
|**datefmt** |	指定日期/时间格式。需要注意的是，**该选项要在format中包含时间字段%(asctime)s时才有效**
|level |	指定日志器的日志级别
|stream	|指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
|style	|Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
|handlers |	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。

- **logging.basicConfig()中format参数**

| 字段/属性名称 | 使用格式 | 描述 |
| --- | --- | --- |
| asctime | %(asctime)s | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
| created | %(created)f | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值 |
| relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的） |
| msecs | %(msecs)d | 日志事件发生事件的毫秒部分 |
| levelname | %(levelname)s | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
| levelno | %(levelno)s | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50） |
| name | %(name)s | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger |
| message | %(message)s | 日志记录的文本内容，通过 `msg % args`计算得到的 |
| pathname | %(pathname)s | 调用日志记录函数的源码文件的全路径 |
| filename | %(filename)s | pathname的文件名部分，包含文件后缀 |
| module | %(module)s | filename的名称部分，不包含后缀 |
| lineno | %(lineno)d | 调用日志记录函数的源代码所在的行号 |
| funcName | %(funcName)s | 调用日志记录函数的函数名 |
| process | %(process)d | 进程ID |
| processName | %(processName)s | 进程名称，Python 3.1新增 |
| thread | %(thread)d | 线程ID |
| threadName | %(thread)s | 线程名称 |

### 3.1 最简单的日志输出

```python
import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

'''
等价于
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
# 结果
WARNING:root:This is a warning log.
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log
'''
# 1.为什么前两条日志没有打印出来？
# 答: 记录函数所使用的日志器设置的日志级别默认是WARNING

# 2.打印出来的字段结果代表什么？
# 答: WARNING:root:This is a warning log. == 日志级别:日志器名称:日志内容  
```


### 3.2 配置日志器的日志级别
- `logging.basicConfig(level=logging.DEBUG)`

```python
import logging
'''
logging.DEBUG 日志级别有这么多 
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0 
'''
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

''' 
结果:所有等级的日志信息都被输出了，说明配置生效了。

DEBUG:root:This is a debug log.
INFO:root:This is a info log.
WARNING:root:This is a warning log.
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log.
'''
```


### 3.3 配置下日志输出目标文件和日志格式【重点】

```python
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', 
                    level=logging.DEBUG, 
                    format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

'''
此时会发现控制台中已经没有输出日志内容了，但是在python代码文件的相同目录下会生成一个名为'my.log'的日志文件，该文件中的内容为：
2017-05-08 14:29:53,783 - DEBUG - This is a debug log.
2017-05-08 14:29:53,784 - INFO - This is a info log.
2017-05-08 14:29:53,784 - WARNING - This is a warning log.
2017-05-08 14:29:53,784 - ERROR - This is a error log.
2017-05-08 14:29:53,784 - CRITICAL - This is a critical log.
'''
```

### 3.4 配置日期/时间格式
```python
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', 
                    level=logging.DEBUG, 
                    format=LOG_FORMAT, 
                    datefmt=DATE_FORMAT)
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
'''
05/08/2017 14:29:04 PM - DEBUG - This is a debug log.
05/08/2017 14:29:04 PM - INFO - This is a info log.
05/08/2017 14:29:04 PM - WARNING - This is a warning log.
05/08/2017 14:29:04 PM - ERROR - This is a error log.
05/08/2017 14:29:04 PM - CRITICAL - This is a critical log.
'''

```

