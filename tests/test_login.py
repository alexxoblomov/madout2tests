import time, pytest
from templates.templates import Templates
from basic import element_is_present, check_element_by_xpath, element_is_not_present
from conftest import enter_dev_lobby, enter_login_screen, enter_dev_lobby_with_popups


def test_login_screen_state(device_name, appium_driver):
    """
    1. Входим на экран логина;
    2. Проверяем состояние окна логина.
    """
    enter_login_screen(device_name, appium_driver)
    element_is_present(Templates.LOGIN_SCREEN, 0.90, appium_driver)


def test_guest_login_and_check_server_list(device_name, appium_driver):
    """
    1. Логинимся в игру гостем;
    2. Проверяем, что оказались в лобби;
    3. Переходим к списку серверов для игры;
    4. Проверяем, что лист серверов не пустой.
    """
    enter_dev_lobby(device_name, appium_driver)
    time.sleep(5)
    element_is_present(Templates.LOBBY_SCREEN, 0.90, appium_driver)
    device_name.MainLobby.GAME_MODE.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.SERVER_LIST.tap(appium_driver)
    time.sleep(5)
    element_is_not_present(Templates.EMPTY_SERVER_LIST, 0.80, appium_driver)


def test_google_login_and_go_single_mode(device_name, appium_driver):
    """
    Надо подумать, в какой аккаунт логиниться. Если их несколько тап может улететь не туда.
    1. Входим в игру через логин гугла;
    2. Переходим в режимы игры, выбираем сингл;
    3. Проверяем, что появились у избушки игрока в сингле.
    """
    enter_login_screen(device_name, appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GOOGLE_LOGIN.tap(appium_driver)
    time.sleep(5)
    device_name.LoginScreen.GOOGLE_ACCOUNT.tap(appium_driver)
    time.sleep(35)
    device_name.LoginScreen.PROLOGUE_SKIP.tap(appium_driver)
    time.sleep(5)
    device_name.MainLobby.GAME_MODE.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.SINGLE_MODE.tap(appium_driver)
    time.sleep(20)
    element_is_present(Templates.SINGLE_MODE_HOUSE, 0.50, appium_driver)


@pytest.mark.skip
def test_facebook_login(device_name, appium_driver):
    """
    Подумать, как провернуть это через впн.
    1. Входим в игру через логин гугла;
    2. Переходим в режимы игры, выбираем сингл;
    3. Проверяем, что появились у избушки игрока в сингле.
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