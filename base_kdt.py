# -*- coding:utf-8 -*-
"""
关键字驱动
"""
from time import sleep

from loguru import logger
from selenium import webdriver


def browser(type_):
    """
    浏览器driver
    :param type_:
    :return:
    """
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e, "出现异常，启动chrome浏览器")
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    return driver


class KeyWord:
    """
    kdt驱动
    """

    def __init__(self, type_):
        """
        初始化方法,传入浏览器名称
        :param type_:
        """
        self.driver = browser(type_)

    def open(self, **kwargs):
        """
        打开url
        :param kwargs:
        :return:
        """
        self.driver.get(url=kwargs['txt'])

    def locator(self, **kwargs):
        """
        定位元素方法
        :param kwargs:
        :return:
        """
        return self.driver.find_element(kwargs['ele_type'], kwargs['index'])

    def input(self, **kwargs):
        """
        输入方法
        :param kwargs:
        :return:
        """
        self.locator(**kwargs).send_keys(kwargs['txt'])

    def click(self, **kwargs):
        """
        点击方法
        :param kwargs:
        :return:
        """
        self.locator(**kwargs).click()

    def switch_to_window(self, **kwargs):
        """
        切换浏览器标签页
        :param kwargs:
        :return:
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[kwargs['txt']])

    def wait(self, **kwargs):
        """
        强制等待
        :param kwargs:
        :return:
        """
        sleep(kwargs['txt'])

    def close(self, **kwargs):
        """
        关闭浏览器页面
        :param kwargs:
        :return:
        """
        self.driver.close()

    def quit(self, **kwargs):
        """
        退出浏览器驱动
        :param kwargs:
        :return:
        """
        self.driver.quit()


logger.debug('这是一条调试消息')
logger.info('这是一条info信息')
logger.error('这是一条错误信息')
