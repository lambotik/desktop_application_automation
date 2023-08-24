import pytest
from pywinauto import Application


@pytest.fixture()
def app():
    app = Application(backend='uia').start('calc.exe', timeout=10)
    app.connect(best_match='Калькулятор', timeout=5)
    yield app
    app.kill(soft=True)
