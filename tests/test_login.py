import time
from buttons import PocoX6
from templates.templates import Templates
from basic import element_is_present
from conftest import enter_login_screen
from utils import get_screenshot


def test_login_screen_state(appium_driver):
    """
    1. Входим на экран логина (дев-билд);
    2. Проверяем, что экран логина и все его элементы совпадают с шаблоном.
    """
    enter_login_screen(PocoX6, appium_driver)
    element_is_present(Templates.LOGIN_SCREEN, 0.90, appium_driver)

