import allure
from pywinauto import Application


class BasePage:
    NAVIGATION_BUTTON = 'TogglePaneButton'
    SETTING_ITEM = 'SettingsItem'
    STANDARD_ITEM = 'Standard'
    PLUS_BUTTON = 'plusButton'
    EQUAL_BUTTON = 'equalButton'
    RESULT = 'CalculatorResults'

    def __init__(self, app: Application):
        self.app = app
        self.window_app = app.top_window()
        self.window_app.wait('ready', timeout=5)

    @allure.step('Open menu')
    def open_menu(self):
        self.window_app.child_window(auto_id=self.NAVIGATION_BUTTON).set_focus().click()

    @allure.step('Click number')
    def click_number(self, number: int):
        self.window_app.child_window(auto_id=f'num{number}Button').set_focus().click()

    @allure.step('Click plus')
    def click_plus(self):
        self.window_app.child_window(auto_id=self.PLUS_BUTTON).click_input()

    @allure.step('Click equal')
    def click_equal(self):
        self.window_app.child_window(auto_id=self.EQUAL_BUTTON).click_input()

    @allure.step('Get result')
    def get_result(self):
        result = self.window_app.child_window(auto_id=self.RESULT).texts()
        return int(result[0].split(' ')[-1])

    @allure.step('Set numbers')
    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.RESULT).type_keys(number)

    @allure.step('Open page')
    def open_page(self, page_name: str):
        pages = {'standard': self.STANDARD_ITEM,
                 'settings': self.SETTING_ITEM}
        self.window_app.child_window(auto_id=pages[page_name]).set_focus().click_input()

        if page_name == 'standard':
            from pages.standard_page import StandardPage
            with allure.step('Open page standard'):
                return StandardPage(self.app)
        elif page_name == 'settings':
            from pages.setting_page import SettingsPage
            with allure.step('Open page settings'):
                return SettingsPage(self.app)
