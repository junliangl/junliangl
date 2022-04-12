# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from framework.browser_info import Message

logger = Logger(logger="浏览器初始化配置").get_log()
get_message = Message()


class BrowserEngine:
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    geckodriver_driver_path = os.path.join(os.path.join(dir, 'tools'), 'geckodriver.exe')
    chrome_driver_path = os.path.join(os.path.join(dir, 'tools'), 'chromedriver.exe')
    ie_driver_path = os.path.join(os.path.join(dir, 'tools'), 'IEDriverServer.exe')

    def __init__(self, driver):
        self.driver = driver

        # 从 browser_message 里面拿到数据
    def open_browser(self, driver):
        # 获取配置文件属性
        logger.info(f"You had select {get_message.get_driver()} browser.")
        logger.info(f"The test server url is: {get_message.get_url()}")

        if get_message.get_driver() == "Firefox":
            driver = webdriver.Firefox(executable_path=self.geckodriver_driver_path)  # 给Firefox()指定驱动路径
            logger.info("Starting firefox browser.")
        elif get_message.get_driver() == "Chrome":
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path)  # 给Chrome()指定驱动路径
            logger.info("Starting Chrome browser.")
        elif get_message.get_driver() == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        driver.get(get_message.get_url())
        logger.info(f"Open url: {get_message.get_url()}.")
        driver.maximize_window()
        logger.info("Maximize the current window.")
        # WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(element))
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
