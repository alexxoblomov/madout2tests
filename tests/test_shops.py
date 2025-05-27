import time, pytest
from basic import screen_is_match
from conftest import enter_dev_lobby_without_popups, enter_dev_lobby_with_popups


def test_enter_shops(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Поочередно проверяем, что можем перейти в магазины через элементы лобби (машина, персонаж, оружие)
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    device_name.MainLobby.CAR_SHOP_AREA.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.CAR_SHOP_MAIN_SCREEN, 0.80, appium_driver)
    device_name.MainShop.BACK_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.WEAPON_SHOP_AREA.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.WEAPON_SHOP_MAIN_SCREEN, 0.80, appium_driver)
    device_name.MainShop.BACK_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.MainLobby.APPEARANCE_SHOP_AREA.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.APPEARANCE_SHOP_MAIN_SCREEN, 0.80, appium_driver)


def test_buy_for_soft_and_hard(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Переходим в магазин оружия
    3) Покупаем броню за софт-валюту
    4) Покупаем м4а1 за хард-валюту
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    device_name.MainLobby.WEAPON_SHOP_AREA.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.ARMOR_SHOWCASE.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.BUY_AMMO_BUTTON.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.BUY_AMMO_MIN_PRICE_BUTTON.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.ARMOR_REWARD_POPUP, 0.80, appium_driver)
    device_name.WeaponShop.CLAIM_REWARD_POPUP_BUTTON.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.M4A1_SHOWCASE.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.BUY_AMMO_BUTTON.tap(appium_driver)
    time.sleep(1)
    device_name.WeaponShop.BUY_AMMO_MIN_PRICE_BUTTON.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.M4A1_REWARD_POPUP, 0.80, appium_driver)


def test_install_car_upgrade(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Переходим к апгрейду Citizen
    3) Улучшаем его, проверяем наградной поп-ап
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    device_name.MainLobby.CAR_SHOP_AREA.tap(appium_driver)
    time.sleep(2)
    device_name.CarShop.ALREADY_HAVE_PAGE.tap(appium_driver)
    time.sleep(2)
    device_name.CarShop.UPGRADE_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.CarShop.BUY_UPGRADE_BUTTON.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.UPGRADE_BUY_CONFIRM_SCREEN, 0.80, appium_driver)
    time.sleep(2)
    device_name.CarShop.BUY_UPGRADE_CONFIRM_BUTTON.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.UPGRADE_REWARD_POPUP, 0.80, appium_driver)


def test_weapon_upgrade(device_name, device_templates, appium_driver):
    """
    1) Входим в лобби
    2) Переходим в магазин оружия
    3) Переходим к улучшению оружия
    4) Проверяем экран улучшения
    5) Пропускаем анимацию улучшения, проверяем экран
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    device_name.MainLobby.WEAPON_SHOP_AREA.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.ARMOR_SHOWCASE.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.UPGRADE_WEAPON_BUTTON.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.WEAPON_UPGRADE_MAIN_SCREEN, 0.80, appium_driver)
    device_name.WeaponShop.CONFIRM_UPGRADE_WEAPON_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.SKIP_WEAPON_UPGRADE_ANIMATION_TAP.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.WEAPON_UPGRADED_SCREEN, 0.70, appium_driver)