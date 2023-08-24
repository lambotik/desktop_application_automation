import time

from pages.setting_page import SettingsPage
from pages.standard_page import StandardPage


class TestCalc:
    def test_calc(self):
        expression = 5 + 6
        result = StandardPage.mathematical()
        assert expression == result, 'Incorrect result!'

    def test_amount_simple_numbers(self, app):
        standard_page = StandardPage(app)
        result = standard_page.amount_numbers(5, 155)
        assert result == 160, 'Incorrect result!'

    def test_change_theme(self, app):
        standard_page = StandardPage(app)
        standard_page.open_menu()
        settings_page = standard_page.open_page('settings')
        selected_state = settings_page.change_themes('light')
        settings_page.click_back_button()
        assert selected_state == 1, 'Incorrect result!'


