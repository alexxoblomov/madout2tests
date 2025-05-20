import time, pytest
from basic import screen_is_match
from conftest import enter_dev_lobby_without_popups, enter_dev_lobby_with_popups


def test_claim_battle_pass_reward(device_name, device_templates, appium_driver):
    """
    1. Входим в игру;
    2. Проверяем наличие точки входа в бп;
    3. Входим в бп, проверяем мету;
    4. Собираем награду за 1-ый уровень, проверяем сбор;
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_ENTRY_POINT, 0.90, appium_driver)
    device_name.MainLobby.BATTLE_PASS_ENTRY.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_MAIN_SCREEN, 0.90, appium_driver)
    device_name.BattlePass.CLAIM_REWARDS.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_1LVL_REWARD_POPUP, 0.90, appium_driver)
    time.sleep(2)
    device_name.BattlePass.CLAIM_REWARD_POPUP.tap(appium_driver)
    time.sleep(2)
    device_name.BattlePass.BUY_PREMIUM.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_MAIN_SCREEN, 0.90, appium_driver)


def test_daily_login(device_name, device_templates, appium_driver):
    """
    1. Входим в игру;
    2. Проверяем, что собрали первую награду еще в enter_dev_lobby()/enter_prod_lobby();
    3. Проверяем вкладки с каждой неделей.
    p.s. Можем смотреть в принципе каждую награду по отдельности, надо подумать нужно ли.
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    # !!! daily-логин поменял координаты !!!
    device_name.MainLobby.DAILY_LOGIN.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.DL_WEEK_1_SCREEN, 0.90, appium_driver)
    device_name.DailyLogin.WEEK_2.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.DL_WEEK_2_SCREEN, 0.90, appium_driver)
    device_name.DailyLogin.WEEK_3.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.DL_WEEK_3_SCREEN, 0.90, appium_driver)
    device_name.DailyLogin.WEEK_4.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.DL_WEEK_4_SCREEN, 0.90, appium_driver)


def test_claim_client_quest(device_name, device_templates, appium_driver):
    """
    1. Входим в лобби;
    2. Проверяем точку входа в квесты;
    3. Входим в квесты, проверяем состояние кнопки "собрать всё";
    4. Собираем всё (1 квест в духе "войти в игру" всегда будет выполнен);
    5. Проверяем наградной поп-ап;
    6. Возвращаемся в квесты, смотрим что "собрать всё" задизейблена.
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    screen_is_match(device_templates.LobbyTemplates.CLIENTS_QUESTS_ENTRY, 0.90, appium_driver)
    device_name.MainLobby.QUESTS_ENTRY.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.CLAIM_ALL_REWARDS_BUTTON, 0.90, appium_driver)
    device_name.Quests.CLAIM_ALL_REWARDS.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.QUEST_REWARD_POPUP, 0.90, appium_driver)
    device_name.Quests.CLAIM_REWARD_POPUP.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.CLAIM_ALL_REWARDS_BUTTON_DISABLED, 0.90, appium_driver)


def test_claim_grow_found_reward(device_name, device_templates, appium_driver):
    """
    1. Входим в лобби;
    2. Проверяем точку входа в гроуфонд;
    3. Входим в гроуфонд, проверяем общее состояние окна;
    4. Собираем награду за 1-й уровень;
    5. Проверяем наградной поп-ап;
    6. Возвращаемся в гроуфонд, проверяем что награда забрана.
    """
    enter_dev_lobby_with_popups(device_name, appium_driver)
    screen_is_match(device_templates.LobbyTemplates.GROW_FOUND_ENTRY_POINT, 0.90, appium_driver)
    device_name.MainLobby.GROW_FOUND_ENTRY.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.GROW_FOUND_MAIN_SCREEN, 0.90, appium_driver)
    device_name.GrowFound.CLAIM_1LVL_REWARD.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.GROW_FOUND_1LVL_REWARD_POPUP, 0.90, appium_driver)
    device_name.GrowFound.CLAIM_REWARD_POPUP.tap(appium_driver)
    time.sleep(2)
    screen_is_match(device_templates.LobbyTemplates.CLAIMED_1LVL_FREE_REWARD, 0.90, appium_driver)


def test_subscribe_to_get_rewards(device_name, appium_driver):
    """
    """
    enter_dev_lobby_without_popups(device_name, appium_driver)
    time.sleep(1)
