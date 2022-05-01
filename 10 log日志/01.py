import logging

# 定义日志的格式，里面有固定的参数
LOG_FMT = '%(levelname)s: %(asctime)s-%(message)s-%(name)s'
logging.basicConfig(filename='zhu xianfu.log', level=logging.DEBUG,
                    format=LOG_FMT)


a = 100
logging.debug('debug级别的调试信息')

b = a + 20
logging.info('info级别的日志')

print(b)
logging.error('error')