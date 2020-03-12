from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.support.ui import Select

waiting_time = 1


class Application:

    def __init__(self, browser, base_ulr):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(waiting_time)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_ulr = base_ulr

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_ulr)

    def destroy(self):
        self.wd.quit()

    def set_textbox_value(self, textbox_name, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(textbox_name).click()
            wd.find_element_by_name(textbox_name).clear()
            wd.find_element_by_name(textbox_name).send_keys(value)

    def select_combobox_value(self, combobox_name, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(combobox_name).click()
            Select(wd.find_element_by_name(combobox_name)).select_by_visible_text(value)
            #wd.find_element_by_name(combobox_name).click()
            #wd.find_element_by_name(combobox_name).send_keys(value)
