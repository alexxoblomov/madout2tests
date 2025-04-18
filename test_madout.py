import time
from buttons import PocoX6
from templates.templates import Templates
from basic import element_is_present
from conftest import enter_dev_lobby
from utils import get_screenshot


def test_clans_quick_join(appium_driver):
    """
    1. Входим в лобби;
    2. Проверяем, что точка входа в кланы существует;
    3. Переходим в окно поиска кланов;
    4. Проверяем, что кнопка быстрого присоединения существует;
    5. Нажимаем на кнопку быстрого присоединения;
    6. Проверяем, что действительно оказались в мете клана.
    """
    enter_dev_lobby(PocoX6, appium_driver)

    element_is_present(Templates.CLAN_ENTRY, 0.90, appium_driver)
    PocoX6.MainLobby.CLAN_ENTRY.tap(appium_driver)
    time.sleep(1)

    element_is_present(Templates.QUICK_JOIN, 0.90, appium_driver)
    PocoX6.ClansSearch.CLAN_QUICK_JOIN.tap(appium_driver)
    time.sleep(5)

    element_is_present(Templates.CLAN_META, 0.90, appium_driver)
