import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base_page import BasePage
from page_objects.common_login.login import Login
from framework.logger import Logger

logger = Logger(logger='测试流程').get_log()
project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(os.path.join(os.path.join(project_path, 'config'), 'management'), 'quota_management.json')
menu_file = os.path.join(os.path.join(project_path, 'config'), 'menu_element.json')
method_file = os.path.join(os.path.join(project_path, 'config'), 'method.json')
reminder_file = os.path.join(os.path.join(project_path, 'config'), 'reminder.json')

with open(json_file, encoding='utf-8') as file1:
    quota_management_json = json.load(file1)

with open(menu_file, encoding='utf-8') as file2:
    menu_json = json.load(file2)

with open(method_file, encoding='utf-8') as file3:
    method_json = json.load(file3)

with open(reminder_file, encoding='utf-8') as file4:
    reminder_json = json.load(file4)


class Quota_Management_Page(BasePage):
    setting_button_element = (method_json["method"][0], menu_json["setting"]["button"][0])
    group_element = (method_json["method"][0], menu_json["setting"]["group"][0])
    cd1_quota_management_element = (method_json["method"][0], menu_json["cd1_setting"]["quota_management"][0])
    staging_quota_management_element = (method_json["method"][0], menu_json["staging_setting"]["quota_management"][0])
    quota_amount = (method_json["method"][0], quota_management_json["quota_amount"][0])
    available_amount = (method_json["method"][0], quota_management_json["available_amount"][0])
    used_amount = (method_json["method"][0], quota_management_json["used_amount"][0])
    frozen_amount = (method_json["method"][0], quota_management_json["frozen_amount"][0])

    def login(self):
        login = Login(self.driver)
        login.login('invited')

    def get_quota_info(self):
        self.click(*self.setting_button_element)
        self.click(*self.group_element)
        if self.get_url() == 'http://10.1.1.80:7001/':
            self.click(*self.cd1_quota_management_element)
        elif self.get_url() == 'http://staging.test.frontend.moqi.com.cn/shell':
            self.click(*self.staging_quota_management_element)
        self.sleep(6)
        self.forced_wait(*self.frozen_amount)
        quota_amount = self.get_element(*self.quota_amount)
        available_amount = self.get_element(*self.available_amount)
        used_amount = self.get_element(*self.used_amount)
        frozen_amount = self.get_element(*self.frozen_amount)
        logger.info(quota_amount)
        logger.info(available_amount)
        logger.info(used_amount)
        logger.info(frozen_amount)
        return [quota_amount, available_amount, used_amount, frozen_amount]


