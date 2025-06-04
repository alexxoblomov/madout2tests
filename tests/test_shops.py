import time, pytest
from basic import screen_is_match


class TestShopsDev:
    """
    Набор для запуска тестов на Dev окружении
    """
    def test_enter_shops(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        1) Входим в лобби
        2) Поочередно проверяем, что можем перейти в магазины через элементы лобби (машина, персонаж, оружие)
        """
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


    def test_buy_for_soft_and_hard(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в магазин оружия
        3) Покупаем броню за софт-валюту
        4) Покупаем м4а1 за хард-валюту
        """
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


    def test_install_car_upgrade(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим к апгрейду Citizen
        3) Улучшаем его, проверяем наградной поп-ап
        """
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


    def test_weapon_upgrade(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в магазин оружия
        3) Переходим к улучшению оружия
        4) Проверяем экран улучшения
        5) Пропускаем анимацию улучшения, проверяем экран
        """
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


    def test_watch_ads_marathon(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в раздел рекламы магазина
        3) Смотрим первую часть марафона
        4) Проверяем, что на экране тестовая реклама
        5) Проверяем поп-ап с наградой за рекламу
        """
        device_name.MainLobby.MAIN_SHOP_BUTTON.tap(appium_driver)
        time.sleep(1)
        device_name.MainShop.ADS_CATEGORY_BUTTON.tap(appium_driver)
        time.sleep(1)
        device_name.MainShop.MARATHON_CH1_ADS_BUTTON.tap(appium_driver)
        time.sleep(10)
        screen_is_match(device_templates.ShopTemplates.TEST_AD_SCREEN, 0.30, appium_driver)
        time.sleep(5)

        # промахиваемся по крестику, если заглушка красная, поправить координаты
        device_name.MainShop.CLOSE_TEST_AD.tap(appium_driver)

        time.sleep(8)
        screen_is_match(device_templates.ShopTemplates.AD_REWARD_POPUP, 0.90, appium_driver)


class TestShopsProd:
    """
    Набор для запуска на Prod окружении
    """
    pass