import allure
import datetime
import os
from logs.logger_path import LOGS_DIR


class Logger:
    file_name = LOGS_DIR / str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.log')

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    @allure.step('Start test')
    def add_request(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = '\n------\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'method: {method}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)
