# coding=utf-8
import os
import unittest
from ddt import ddt, file_data
from framework.browser_engine import BrowserEngine
from framework.browser_info import Message
from page_objects.available_quota import Available_quota_Page
from framework.logger import Logger
from selenium.webdriver.common import action_chains

logger = Logger(logger='登录测试结果').get_log()
get_message = Message()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(os.path.join(project_path, 'data'), 'available_quota_data.json')


@ddt
class Test_available_quota(unittest.TestCase):
    """
    测试登录模块
    """

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.driver.close()

    @file_data(data_path)
    def test_available_quota(self, account, password):
        """
        测试登录用例
        """
        available_quota_page = Available_quota_Page(self.driver)  # 把 setup 的 driver 传下来
        available_quota_page.input_login_message_account(account)
        available_quota_page.input_login_message_password(password)  # 调用页面对象中的方法
        action_chains.ActionChains(self.driver).move_by_offset(0, 0).click().perform()  # 点击空白解除网页的非安全链接提醒
        available_quota_page.click_login_button()
        available_quota_page.click_username_button()
        available_quota_page.click_quota_button()

        # 如果找到登录的元素那么判定登录成功
        if available_quota_page.get_result() is True:
            self.assertTrue(available_quota_page.get_result(), logger.info("查看算力成功，且当前角色未加入域"))
        else:
            self.assertTrue(available_quota_page.get_result(), logger.critical('查看算力失败失败'))


if __name__ == '__main__':
    unittest.main()
