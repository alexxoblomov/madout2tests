import time, pytest

from templates.templates import Templates
from basic import element_is_present
from conftest import enter_login_screen


@pytest.mark.xfail
def test_tos_and_privacy_policy(device_name, appium_driver):
    """
    1. Входим в игру;
    2. Проверяем, что поп-ап "добро пожаловать" и все его элементы совпадают с шаблоном;
    3. Переходим по кнопке "privacy policy";
    4. Проверяем, что на экране браузера есть нужный контент и мы действительно перешли;
    5. Возвращаемся к поп-апу;
    6. Переходим по кнопке "terms of service";
    7. Проверяем, что на экране браузера есть нужный контент и мы действительно перешли.
    """
    time.sleep(8)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.WELCOME_SCREEN, 0.90, appium_driver)

    device_name.LoginScreen.PRIVACY_POLICY.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.PRIVACY_POLICY, 0.90, appium_driver)
    time.sleep(2)

    device_name.DeviceKeyboard.BACK.tap(appium_driver)
    time.sleep(2)

    # не рабочая часть, нужен фикс
    device_name.LoginScreen.TERMS_OF_SERVICE.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.TERMS_OF_SERVICE, 0.90, appium_driver)
    time.sleep(2)


@pytest.mark.xfail
def test_ways_to_login(device_name, appium_driver):
    """
    1. Входим на экран логина;
    2. Проверяем, что экран логина и все его элементы совпадают с шаблоном;
    3. Переходим по кнопке "facebook";
    4. Смотрим в браузере, что нас действительно редиректит на страницу facebook;
    5. Возвращаемся к приветственному поп-апу;
    6. Переходим по кнопке "google";
    7. Смотрим, что открылся поп-ап с выбором аккаунта.
    """
    enter_login_screen(device_name, appium_driver)
    element_is_present(Templates.LOGIN_SCREEN, 0.90, appium_driver)
    time.sleep(2)

    device_name.LoginScreen.FACEBOOK_LOGIN.tap(appium_driver)
    time.sleep(5)
    element_is_present(Templates.FACEBOOK_HEADER, 0.90, appium_driver)
    time.sleep(1)

    device_name.DeviceKeyboard.BACK.tap(appium_driver)
    time.sleep(2)

    device_name.LoginScreen.GOOGLE_LOGIN.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.GOOGLE_LOGIN, 0.90, appium_driver)
