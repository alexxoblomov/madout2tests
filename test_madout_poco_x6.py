import time
from buttons import PocoX6
from templates.templates import Templates
from basic import element_is_present
from conftest import enter_dev_lobby


def test_clans_quick_join(poco_x6_appium_driver):
    """
    allure desc place
    """
    enter_dev_lobby(PocoX6, poco_x6_appium_driver)

    element_is_present(Templates.CLAN_ENTRY, 0.90, poco_x6_appium_driver)
    PocoX6.MainLobby.CLAN_ENTRY.tap(poco_x6_appium_driver)
    time.sleep(1)

    element_is_present(Templates.QUICK_JOIN, 0.90, poco_x6_appium_driver)
    PocoX6.ClansSearch.CLAN_QUICK_JOIN.tap(poco_x6_appium_driver)