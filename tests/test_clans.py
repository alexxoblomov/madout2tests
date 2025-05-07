import random
import time, pytest

from appium.webdriver.extensions.android.nativekey import AndroidKey
from templates.templates import Templates
from basic import element_is_present
from conftest import enter_dev_lobby


def test_clans_quick_join(device_name, appium_driver):
    """
    1. Входим в лобби;
    2. Проверяем, что точка входа в кланы существует;
    3. Переходим в окно поиска кланов;
    4. Проверяем, что кнопка быстрого присоединения существует;
    5. Нажимаем на кнопку быстрого присоединения;
    6. Проверяем, что действительно оказались в мете клана.
    """

    enter_dev_lobby(device_name, appium_driver)

    element_is_present(Templates.CLAN_ENTRY_POINT, 0.70, appium_driver)
    device_name.MainLobby.CLAN_ENTRY.tap(appium_driver)
    time.sleep(1)

    element_is_present(Templates.QUICK_JOIN, 0.90, appium_driver)
    device_name.ClansSearch.CLAN_QUICK_JOIN.tap(appium_driver)
    time.sleep(5)

    element_is_present(Templates.CLAN_META, 0.90, appium_driver)


def test_clan_create_and_delete(device_name, appium_driver):
    """
    """

    enter_dev_lobby(device_name, appium_driver)
    time.sleep(1)
    element_is_present(Templates.CLAN_ENTRY_POINT, 0.70, appium_driver)

    device_name.MainLobby.CLAN_ENTRY_POINT.tap(appium_driver)
    time.sleep(1)
    element_is_present(Templates.CREATE_CLAN_BUTTON, 0.90, appium_driver)
    time.sleep(1)
    device_name.ClansSearch.CREATE_CLAN_BUTTON.tap(appium_driver)
    time.sleep(1)

    element_is_present(Templates.CREATE_CLAN_SCREEN, 0.90, appium_driver)
    time.sleep(1)
    device_name.CreateClan.CLAN_NAME.tap(appium_driver)
    time.sleep(2)
    appium_driver.execute_script("mobile: type", {"text": str(random.randint(1_000_000_000, 9_999_999_999))})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(2)
    device_name.CreateClan.CREATE_CLAN_BUTTON.tap(appium_driver)
    time.sleep(15)
    device_name.MainClans.CLAN_CREATE_CONFIRM.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.CLAN_META_SCREEN, 0.90, appium_driver)
    time.sleep(5)

    device_name.MainClans.CLAN_SETTINGS.tap(appium_driver)
    time.sleep(2)
    device_name.MainClans.CLAN_DELETE.tap(appium_driver)
    time.sleep(2)
    element_is_present(Templates.CLAN_DELETE_POPUP, 0.90, appium_driver)
    time.sleep(1)
    device_name.MainClans.CLAN_DELETE_STRING.tap(appium_driver)
    time.sleep(1)
    appium_driver.execute_script("mobile: type", {"text": "DELETE"})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(1)

    device_name.MainClans.CLAN_DELETE_CONFIRM.tap(appium_driver)
    time.sleep(10)
    element_is_present(Templates.CLAN_DELETED_POPUP, 0.90, appium_driver)
    time.sleep(1)