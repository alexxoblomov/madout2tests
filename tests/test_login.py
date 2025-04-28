import time, pytest
from templates.templates import Templates
from basic import element_is_present, check_element_by_xpath, element_is_not_present
from conftest import enter_dev_lobby


def test_guest_login_and_check_server_list(device_name, appium_driver):
    """
    1. Логинимся в игру гостем;
    2. Проверяем, что оказались в лобби.
    """
    enter_dev_lobby(device_name, appium_driver)
    time.sleep(5)
    element_is_present(Templates.LOBBY_SCREEN, 0.90, appium_driver)
    device_name.MainLobby.ONLINE_GAME.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.SERVER_LIST.tap(appium_driver)
    time.sleep(5)
    element_is_not_present(Templates.EMPTY_SERVER_LIST, 0.80, appium_driver)


@pytest.mark.skip
def test_google_login(device_name, appium_driver):
    """
    Реализуемо только на release-like билде, подлежит обсуждению
    """


def test_tos_and_privacy_policy(device_name, appium_driver):
    """
    1. Входим в игру;
    2. Проверяем, что поп-ап "добро пожаловать" и все его элементы совпадают с шаблоном;
    3. Переходим по кнопке "privacy policy";
    4. Проверяем, что на экране браузера есть нужный контент и мы действительно перешли;
    5. Переходим по кнопке "terms of service";
    6. Проверяем, что на экране браузера есть нужный контент и мы действительно перешли.
    """
    time.sleep(8)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.WELCOME_SCREEN, 0.90, appium_driver)

    device_name.LoginScreen.TERMS_OF_SERVICE.tap(appium_driver)
    time.sleep(2)
    check_element_by_xpath(appium_driver, device_name.LoginScreen.TOS_XPATH)

    device_name.LoginScreen.PRIVACY_POLICY.tap(appium_driver)
    time.sleep(2)
    check_element_by_xpath(appium_driver, device_name.LoginScreen.PP_XPATH)

    appium_driver.terminate_app("com.android.chrome")