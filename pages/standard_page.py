import allure
from pywinauto import Application

from pages.base_page import BasePage
from utils.logger import Logger


class StandardPage(BasePage):
    ELEMENTS_FOR_ACTION_BY_NAME = ['Пять', 'Плюс', 'Шесть', 'Равно']

    @staticmethod
    def mathematical_operations(list_locators) -> int:
        """
        Performs successive clicks on the given locators and returns the result of a mathematical operation
        :param list_locators:
        :return: int
        """
        app = Application(backend='uia').start(fr'calc.exe')
        app.connect(best_match='Калькулятор', timeout=5)

        for i in list_locators:
            app.top_window().__getattribute__(i).click()
            with allure.step(f'Clicked on: {i}'):
                print(f'Clicked on: {i}')
        calc_list = app.top_window().child_window(auto_id='CalculatorResults')
        result = int(calc_list.texts()[0].split(' ')[-1])
        print(f'Result equal : {result}')
        app.kill(soft=True)
        return result

    @staticmethod
    def mathematical():
        Logger.add_method('mathematical_operations')
        result = StandardPage.mathematical_operations(StandardPage.ELEMENTS_FOR_ACTION_BY_NAME)
        return result

    def amount_numbers(self, num1: int, num2: int) -> int:
        """
        :param num1:
        :param num2:
        :return: int
        """
        Logger.add_method('amount_numbers')
        self.click_number(num1)
        self.click_plus()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()
