import time, pytest
from basic import screen_is_match



class TestLoginDev:
    """
    Набор для запуска тестов на Dev окружении
    """
    def test_login_screen_state(self, device_name, device_templates, enter_dev_login_screen_without_popups, appium_driver):
        """
        1) Входим на экран логина в игру
        2) Проверяем его состояние
        """
        screen_is_match(device_templates.LoginTemplates.LOGIN_SCREEN, 0.90, appium_driver)


    def test_check_server_list_and_go_online(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        1) Входим в лобби
        2) Проверяем список серверов
        3) Переходим на первый сервер
        4) Смотрим, что оказались на сервере (низкий threshold, нужно быть внимательнее)
        """
        device_name.MainLobby.GAME_MODE.tap(appium_driver)
        time.sleep(5)
        device_name.MainLobby.SERVER_LIST.tap(appium_driver)
        time.sleep(5)
        screen_is_match(device_templates.LoginTemplates.SERVER_LIST_SCREEN, 0.40, appium_driver)
        device_name.MainLobby.FIRST_SERVER_IN_LIST.tap(appium_driver)
        time.sleep(15)
        screen_is_match(device_templates.LoginTemplates.ONLINE_GAMEPLAY_SCREEN, 0.15, appium_driver)


    def test_go_single_mode(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в одиночную игру
        3) Проверяем, что игрок появился у своей избушки
        """
        device_name.MainLobby.GAME_MODE.tap(appium_driver)
        time.sleep(2)
        device_name.MainLobby.SINGLE_MODE.tap(appium_driver)
        time.sleep(20)
        screen_is_match(device_templates.LoginTemplates.SINGLE_MODE_HOUSE, 0.50, appium_driver)


    def test_go_ftue(self, device_name, device_templates, enter_dev_login_screen_without_popups, appium_driver):
        """
        1) Входим в игру
        2) Проверяем, что оказались во FTUE
        """
        device_name.LoginScreen.GUEST_LOGIN_BUTTON.tap(appium_driver)
        time.sleep(30)
        device_name.LoginScreen.PROLOGUE_SKIP_CUTSCENE.tap(appium_driver)
        time.sleep(35)
        screen_is_match(device_templates.LoginTemplates.FTUE_START_SCREEN, 0.80, appium_driver)


class TestShopsProd:
    """
    Набор для запуска на Prod окружении
    """
    pass