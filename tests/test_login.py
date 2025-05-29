import time, pytest
from selenium.webdriver.support.wait import WebDriverWait

from basic import screen_is_match
from conftest import enter_dev_lobby_without_popups, enter_login_screen_without_popups


def test_login_screen_state(device_name, device_templates, appium_driver):
    """
    1) Входим на экран логина в игру
    2) Проверяем его состояние
    """
    enter_login_screen_without_popups(device_name, appium_driver)
    screen_is_match(device_templates.LoginTemplates.LOGIN_SCREEN, 0.90, appium_driver)


def test_check_server_list_and_go_online(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Проверяем список серверов
    3) Переходим на первый сервер
    4) Смотрим, что оказались на сервере (низкий threshold, нужно быть внимательнее)
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    device_name.MainLobby.GAME_MODE.tap(appium_driver)
    time.sleep(5)
    device_name.MainLobby.SERVER_LIST.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.LoginTemplates.SERVER_LIST_SCREEN, 0.40, appium_driver)
    device_name.MainLobby.FIRST_SERVER_IN_LIST.tap(appium_driver)
    time.sleep(15)
    screen_is_match(device_templates.LoginTemplates.ONLINE_GAMEPLAY_SCREEN, 0.15, appium_driver)


def test_go_single_mode(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Переходим в одиночную игру
    3) Проверяем, что игрок появился у своей избушки
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    device_name.MainLobby.GAME_MODE.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.SINGLE_MODE.tap(appium_driver)
    time.sleep(20)
    screen_is_match(device_templates.LoginTemplates.SINGLE_MODE_HOUSE, 0.50, appium_driver)


def test_go_ftue(device_name, device_templates, appium_driver):
    """
    1) Входим в игру
    2) Проверяем, что оказались во FTUE
    """
    enter_login_screen_without_popups(device_name, appium_driver)
    device_name.LoginScreen.GUEST_LOGIN_BUTTON.tap(appium_driver)
    time.sleep(30)
    device_name.LoginScreen.PROLOGUE_SKIP_CUTSCENE.tap(appium_driver)
    time.sleep(35)
    screen_is_match(device_templates.LoginTemplates.FTUE_START_SCREEN, 0.80, appium_driver)