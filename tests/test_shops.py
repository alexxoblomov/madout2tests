import time, pytest
from basic import screen_is_match
from conftest import enter_dev_lobby_without_popups, enter_dev_lobby_with_popups


def test_enter_shops(device_name, device_templates, appium_driver):
    """
    1. Входим в игру;
    2. Тапаем по машине на бэкграунде;
    3. Переходим в категорию машин, которые у нас есть;
    4. Проверяем, что действительно перешли по тапу по машине и попали в категорию, где по умолчанию есть Citizen;
    5. Переходим в магазин одежды, переключаемся на пресеты внешностей;
    6. Проверяем, что действительно попали на экран пресетов;
    7. Переходим в магазин оружия;
    8. Проверяем, что действительно попали на экран магазина оружия.
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    time.sleep(1)
    device_name.MainLobby.CAR_SHOP.tap(appium_driver)
    device_name.CarShop.ALREADY_HAVE.tap(appium_driver)
    time.sleep(4)
    screen_is_match(device_templates.ShopTemplates.CAR_SHOP_CITIZEN_SCREEN, 0.90, appium_driver)
    device_name.MainShop.BACK.tap(appium_driver)
    device_name.MainLobby.APPEARANCE_SHOP.tap(appium_driver)
    time.sleep(4)
    device_name.AppearanceShop.APPEARANCE_PRESETS.tap(appium_driver)
    time.sleep(4)
    screen_is_match(device_templates.ShopTemplates.APPEARANCE_PRESETS_SCREEN, 0.90, appium_driver)
    time.sleep(2)
    device_name.MainShop.BACK.tap(appium_driver)
    time.sleep(4)
    device_name.MainLobby.WEAPON_SHOP.tap(appium_driver)
    time.sleep(4)
    screen_is_match(device_templates.ShopTemplates.WEAPON_SHOP_SCREEN, 0.90, appium_driver)



def test_buy_some_stuff(device_name, device_templates, appium_driver):
    """
    1. Входим в игру;
    2. Покупаем buggy в магазине машин и проверяем наградной поп-ап;
    3. Покупаем золотую цепочку в магазине вещей и проверяем наградной поп-ап;
    4. Покупаем FNP-45 в магазине оружия и проверяем наградной поп-ап.
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    time.sleep(1)

    device_name.MainLobby.CAR_SHOP.tap(appium_driver)
    time.sleep(4)
    device_name.CarShop.SPECIAL.tap(appium_driver)
    time.sleep(1)
    device_name.CarShop.REVEAL_LIST.tap(appium_driver)
    time.sleep(1)
    device_name.CarShop.CAR_BUGGY.tap(appium_driver)
    time.sleep(1)
    device_name.CarShop.BUY.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.CAR_BUGGY_REWARD_POPUP, 0.85, appium_driver)
    time.sleep(2)
    device_name.MainLobby.CLAIM_REWARD_POPUP.tap(appium_driver)
    time.sleep(5)

    device_name.CarShop.APPEARANCE_SHOP.tap(appium_driver)
    time.sleep(2)
    device_name.AppearanceShop.ACCESSORIES.tap(appium_driver)
    time.sleep(2)
    device_name.AppearanceShop.ACCESSORIES_CHAINS.tap(appium_driver)
    time.sleep(2)
    device_name.AppearanceShop.ACCESSORIES_CHAINS_GOLD_CHAIN.tap(appium_driver)
    device_name.AppearanceShop.BUY.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.GOLD_CHAIN_REWARD_POPUP, 0.85, appium_driver)
    time.sleep(2)
    device_name.MainLobby.CLAIM_REWARD_POPUP.tap(appium_driver)
    # смотреть цену
    time.sleep(5)

    device_name.AppearanceShop.WEAPON_SHOP.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.PISTOL_CATEGORY.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.FNP_45.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.BUY_AMMO.tap(appium_driver)
    time.sleep(2)
    device_name.WeaponShop.BUY_AMMO_MIN.tap(appium_driver)
    time.sleep(5)
    screen_is_match(device_templates.ShopTemplates.FNP_45_REWARD_POPUP, 0.85, appium_driver)
    device_name.MainLobby.CLAIM_REWARD_POPUP.tap(appium_driver)
    # смотреть цену

@pytest.mark.skip(reason="Не готов, требуется доработка")
def test_attention_mark(device_name, device_templates, appium_driver):
    """
    1. Входим в игру;
    2. Входим в магазин;
    3. Смотрим, что на разделе с рекламой есть аттеншн марка;
    4. Переходим в раздел с рекламой;
    5. Смотрим, что на разделе с рекламой нет аттеншн марки.

    Важно! Стоит рассмотреть другой способ проверки аттеншн марок, этот мне кажется ненадежным.
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    time.sleep(1)
    device_name.MainLobby.MAIN_SHOP.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ShopTemplates.ATTENTION_MARK_UNSEEN, 0.90, appium_driver)
    time.sleep(1)
    device_name.MainShop.ADS.tap(appium_driver)
    time.sleep(1)
    screen_is_match(device_templates.ShopTemplates.ATTENTION_MARK, 0.90, appium_driver)

def test_install_car_upgrade(device_name, device_templates, appium_driver):
    """
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    time.sleep(1)
    device_name.MainLobby.CAR_SHOP.tap(appium_driver)
    time.sleep(2)
    device_name.CarShop.ALREADY_HAVE.tap(appium_driver)
    time.sleep(2)
    device_name.CarShop.UPGRADE.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.UPGRADE_CAR_SCREEN, 0.90, appium_driver)
    time.sleep(2)
    device_name.CarShop.BUY_UPGRADE.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.UPGRADE_BUY_CONFIRM_SCREEN, 0.90, appium_driver)
    time.sleep(2)
    device_name.CarShop.BUY_UPGRADE_CONFIRM.tap(appium_driver)
    time.sleep(7)
    screen_is_match(device_templates.ShopTemplates.UPGRADE_REWARD_POPUP, 0.90, appium_driver)
    time.sleep(2)
    device_name.CarShop.CLAIM_REWARD_POPUP.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.ShopTemplates.UPGRADED_CAR_SCREEN, 0.70, appium_driver)