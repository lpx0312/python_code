import logging
import sys

# # 日志级别：debug < info < warning < error < critical(严重错误)
# # logging 只支持这几个级别，
# # 不指定level的话：logging的默认级别是warning只有大于warning级别的才会显示
# # 不指定filename则logging会默认流向屏幕，终端显示，不能存储到文件。
#
# # 第一种方式：basicConfig配置，不建议使用，不能同时在终端和文件中同时显示和记录
# logging.basicConfig(level=logging.DEBUG,filename='log.txt',
#                     format="%(asctime)s:%(name)s %(message)s 行数:%(lineno)s",
#                     datefmt='%Y/%m/%d %H:%M:%S'
#                     )
#
# logging.debug('debug信息')
# logging.info('info信息')
# logging.warning('warning信息')
# logging.error('error信息')
# logging.critical('critical信息')




# 第二种方式：基于日志对象（日志流的处理）

# 构建日志对象（日志器）
logger = logging.getLogger()
# 设置logger对象的默认级别
# logger.setLevel(logging.DEBUG)  # 有级别


# 构建两个handler,日志流向的处理
# 文件流对象
fh =  logging.FileHandler("test.log",encoding='utf8')
# 输出流对象()终端显示
ch = logging.StreamHandler()

# 将fh和ch两个流向设置给logger对象(绑定日志器和流向器)
# 不添加流向，也就是不绑定，默认是终端流，如何添加了，就按照添加的来。
logger.addHandler(fh)
logger.addHandler(ch)

# 设置各个流的级别
fh.setLevel(logging.DEBUG)  # 流也有级别
ch.setLevel(logging.INFO)   # 如果流有默认级别，则会使用流的级别，如果没有则去找logger对象的级别，如果流和logger级别都没级别，则会默认使用logger对象的默认级别，warning级别


# 格式化
formatter1 = logging.Formatter(fmt="%(asctime)s %(name)s %(filename)s %(message)s",
                               datefmt="%Y/%m/%d %H:%M:%S"
                               )

formatter2 = logging.Formatter(fmt="%(asctime)s ::: %(message)s",
                               datefmt="%Y/%m/%d %H:%M:%S"
                               )
fh.setFormatter(formatter1)
ch.setFormatter(formatter2)



# 使用logger对象进行 日志记录
logger.debug('debug信息')
logger.info('info信息')
logger.warning('warning信息')
logger.error('error信息')
logger.critical('critical信息')

#
