import logging

# 简单的日志输出
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")
#
#
# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.INFO, "This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL, "This is a critical log.")


# 设置日志器级别
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

# 日志输出目标文件和日志格式
#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='my.log',
#                     level=logging.DEBUG,
#                     format=LOG_FORMAT)
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

#  配置日期/时间格式
#
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
