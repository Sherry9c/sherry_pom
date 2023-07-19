import logging
from datetime import date

from common.file_handler import path_create

log_path = path_create('E:/result/log')


class Logger:
    def __init__(self):
        # 名字是以点号分割的命名方式命名的(a.b.c)。对同一个名字的多个调用logging.getLogger()
        # 方法会返回同一个logger对象。这种命名方式里面，后面的loggers是前面logger的子logger，自动继承父loggers的log信息.
        # 正因为此, 没有必要把一个应用的所有logger都配置一遍，只要把顶层的logger配置好了，然后子logger根据需要继承就行了。
        # logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        fmt = '%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
        _formatter = logging.Formatter(fmt)

        for handle in self.log.handlers:
            print('log remove:' + str(handle.get_name()))
            self.log.removeHandler(handle)

        if not self.log.handlers:
            sh = logging.StreamHandler()
            sh.setFormatter(_formatter)
            self.log.addHandler(sh)

            fh = logging.FileHandler(f'{log_path}/log-{date.today()}', encoding='utf-8')
            fh.setFormatter(_formatter)
            self.log.addHandler(fh)

    def debug(self, msg):
        self.log.debug(msg)
        return

    def info(self, msg):
        self.log.info(msg)
        return

    def error(self, msg):
        self.log.error(msg)
        return

    def log_driver_info(self, driver):
        self.log.info('环境信息：')
        # logger.info(driver.capabilities)
        self.log.info('Platform Name: ' + driver.capabilities['platformName'])
        self.log.info('Browser Name: ' + driver.capabilities['browserName'])
        self.log.info('Browser Version: ' + driver.capabilities['browserVersion'])
        self.log.info('Driver Info: ' + str(driver.capabilities[f'{driver.capabilities["browserName"]}']))
