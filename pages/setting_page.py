import allure

from pages.base_page import BasePage
from utils.logger import Logger


class SettingsPage(BasePage):
    EXPANDER_THEME = 'AppThemeExpander'
    LIGHT_THEME = 'LightThemeRadioButton'
    DARK_THEME = 'DarkThemeRadioButton'
    SYSTEM_THEME = 'SystemThemeRadioButton'
    BACK_BUTTON = 'BackButton'

    def change_themes(self, type_them):
        Logger.add_method('change_themes')
        types = {"light": self.LIGHT_THEME,
                 "dark": self.DARK_THEME,
                 "system": self.SYSTEM_THEME}
        with allure.step('Click Expander.'):
            self.window_app.child_window(auto_id=self.EXPANDER_THEME).click_input()
        with allure.step(f'Select theme {type_them}.'):
            self.window_app.child_window(class_name="RadioButton", auto_id=types[type_them]).click()
        with allure.step('Check actual theme.'):
            select_state = self.window_app.child_window(class_name="RadioButton",
                                                        auto_id=types[type_them]).is_selected()
        return select_state

    @allure.step('Click back button.')
    def click_back_button(self):
        self.window_app.child_window(auto_id=self.BACK_BUTTON).click_input()
