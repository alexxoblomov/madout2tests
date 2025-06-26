import random
import time, pytest
from appium.webdriver.extensions.android.nativekey import AndroidKey
from basic import screen_is_match


def test_clans_quick_join(device_name, device_templates, enter_dev_lobby_without_popups, appium_driver, log_test_start_end):
    """
    1. Входим в лобби;
    2. Проверяем, что точка входа в кланы существует;
    3. Переходим в окно поиска кланов;
    4. Проверяем, что кнопка быстрого присоединения существует;
    5. Нажимаем на кнопку быстрого присоединения;
    6. Проверяем, что действительно оказались в мете клана.
    """
    device_name.MainLobby.CLANS_ENTRY_POINT.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ClansTemplates.QUICK_JOIN_BUTTON, 0.90, appium_driver)
    device_name.ClansSearch.CLAN_QUICK_JOIN_BUTTON.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ClansTemplates.CLAN_META_SCREEN, 0.50, appium_driver)


def test_clan_manually_join(device_name, device_templates, enter_dev_lobby_without_popups, appium_driver, log_test_start_end):
    """
    1. Входим в лобби;
    2. Переходим в окно поиска кланов;
    3. Ищем открытый клан по названию;
    4. Проверяем, что нашли именно его;
    5. Вступаем и смотрим, что оказались в мете клана.
    """
    device_name.MainLobby.CLANS_ENTRY_POINT.tap(appium_driver)
    time.sleep(1)
    device_name.ClansSearch.CLANS_SEARCH_STRING.tap(appium_driver)
    time.sleep(1)
    appium_driver.execute_script("mobile: type", {"text": "qatest2"})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(2)
    screen_is_match(device_templates.ClansTemplates.OPEN_CLAN_TO_JOIN_SCREEN, 0.80, appium_driver)
    device_name.ClansSearch.REQUEST_OR_JOIN_1ST_CLAN_BUTTON.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ClansTemplates.OPEN_CLAN_TO_JOIN_META_SCREEN, 0.80, appium_driver)


def test_sent_to_join_request(device_name, device_templates, enter_dev_lobby_without_popups, appium_driver, log_test_start_end):
    """
    1. Входим в лобби;
    2. Переходим в окно поиска кланов;
    3. Ищем закрытый клан по названию;
    4. Смотрим, что нашли именно его;
    5. Кидаем реквест;
    6. Переходим на таб реквестов, смотрим что кинули реквест.
    """
    device_name.MainLobby.CLANS_ENTRY_POINT.tap(appium_driver)
    time.sleep(1)
    device_name.ClansSearch.CLANS_SEARCH_STRING.tap(appium_driver)
    time.sleep(1)
    appium_driver.execute_script("mobile: type", {"text": "qatest1"})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(1)
    screen_is_match(device_templates.ClansTemplates.CLAN_TO_JOIN_SCREEN, 0.80, appium_driver)
    device_name.ClansSearch.REQUEST_OR_JOIN_1ST_CLAN_BUTTON.tap(appium_driver)
    time.sleep(1)
    device_name.ClansSearch.REQUEST_AND_INVITES_TAB.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ClansTemplates.REQUEST_AND_INVITES_SCREEN, 0.80, appium_driver)


@pytest.mark.skip
def test_clan_create_and_delete(device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
    """
    1. Входим в лобби;
    2. Проверяем точку входа в кланы;
    3. Проверяем кнопку "создать клан" на экране поиска кланов;
    4. Переходим в окно создания, проверяем его;
    5. Создаем клан;
    6. Проверяем, что оказались в мете;
    7. Переходим к удалению клана;
    8. Проверяем попап перед удалением;
    9. Удаляем клан;
    10. Проверяем попап после удаления.
    """
    screen_is_match(device_templates.ClansTemplates.CLANS_ENTRY_POINT, 0.70, appium_driver)
    device_name.MainLobby.CLANS_ENTRY_POINT.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ClansTemplates.CREATE_CLAN_BUTTON, 0.80, appium_driver)
    time.sleep(1)
    device_name.ClansSearch.CREATE_CLAN_BUTTON.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ClansTemplates.CREATE_CLAN_SCREEN, 0.80, appium_driver)
    time.sleep(1)
    device_name.CreateClan.CLAN_NAME_STRING.tap(appium_driver)
    time.sleep(2)
    appium_driver.execute_script("mobile: type", {"text": str(random.randint(1_000_000_000, 9_999_999_999))})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(2)
    device_name.CreateClan.CREATE_CLAN_BUTTON.tap(appium_driver)
    time.sleep(15)
    device_name.MainClans.CLAN_CREATE_CONFIRM_BUTTON.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ClansTemplates.CLAN_META_SCREEN, 0.80, appium_driver)
    time.sleep(5)
    device_name.MainClans.CLAN_SETTINGS_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.MainClans.CLAN_DELETE_BUTTON.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ClansTemplates.CLAN_DELETE_POPUP, 0.80, appium_driver)
    time.sleep(1)
    device_name.MainClans.CLAN_DELETE_STRING.tap(appium_driver)
    time.sleep(1)
    appium_driver.execute_script("mobile: type", {"text": "DELETE"})
    time.sleep(2)
    appium_driver.press_keycode(AndroidKey.ENTER)
    time.sleep(1)
    device_name.MainClans.CLAN_DELETE_CONFIRM_BUTTON.tap(appium_driver)
    time.sleep(10)
    screen_is_match(device_templates.ClansTemplates.CLAN_DELETED_POPUP, 0.60, appium_driver)
    time.sleep(1)