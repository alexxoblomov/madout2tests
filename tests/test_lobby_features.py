import time, pytest
from appium.webdriver.extensions.android.nativekey import AndroidKey
from basic import screen_is_match


class TestLobbyFeaturesDev:
    """
    Набор для запуска на Dev окружении
    """
    def test_claim_battle_pass_reward(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в батлпасс
        3) Проверяем основной экран
        4) Забираем бесплатную награду
        5) Проверяем наградной поп-ап
        """
        time.sleep(2)
        device_name.MainLobby.BATTLE_PASS_ENTRY_POINT.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_MAIN_SCREEN, 0.50, appium_driver)
        device_name.BattlePass.CLAIM_REWARDS_BUTTON.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.BATTLE_PASS_1LVL_REWARD_POPUP, 0.80, appium_driver)


    def test_claim_client_quest(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в клиентские квесты
        3) Забираем все награды через кнопку
        4) Проверяем наградной поп-ап
        5) Проверяем, что кнопка сбора задизейблена
        """
        device_name.MainLobby.QUESTS_ENTRY_POINT.tap(appium_driver)
        time.sleep(2)
        device_name.Quests.CLAIM_ALL_REWARDS_BUTTON.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.QUEST_REWARD_POPUP, 0.90, appium_driver)
        time.sleep(2)
        device_name.Quests.CLAIM_REWARD_POPUP_BUTTON.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.CLAIM_ALL_REWARDS_BUTTON_DISABLED, 0.90, appium_driver)


    def test_claim_grow_found_reward(self, device_name, device_templates, enter_dev_lobby_with_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в гроуфонд
        3) Проверяем экран гроуфонда
        4) Забираем бесплатную награду
        5) Проверяем наградной поп-ап
        """
        device_name.MainLobby.GROW_FOUND_ENTRY_POINT.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.GROW_FOUND_MAIN_SCREEN, 0.80, appium_driver)
        device_name.GrowFound.CLAIM_1LVL_REWARD_BUTTON.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.GROW_FOUND_1LVL_REWARD_POPUP, 0.80, appium_driver)


    def test_daily_login(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        1) Входим в лобби
        2) Переходим в раздел дейли-логина
        3) Проверяем поочередно экран каждой недели
        """
        device_name.MainLobby.DAILY_LOGIN_ENTRY_POINT.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.DL_WEEK_1_SCREEN, 0.90, appium_driver)
        device_name.DailyLogin.WEEK_2_PAGE.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.DL_WEEK_2_SCREEN, 0.90, appium_driver)
        device_name.DailyLogin.WEEK_3_PAGE.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.DL_WEEK_3_SCREEN, 0.90, appium_driver)
        device_name.DailyLogin.WEEK_4_PAGE.tap(appium_driver)
        time.sleep(2)
        screen_is_match(device_templates.LobbyTemplates.DL_WEEK_4_SCREEN, 0.90, appium_driver)


    def test_search_and_add_friend(self, device_name, device_templates, enter_dev_lobby_without_popups, appium_driver):
        """
        """
        device_name.MainLobby.FRIEND_LIST_ENTRY_POINT.tap(appium_driver)
        time.sleep(1)
        device_name.FriendList.FIND_USER_TAB.tap(appium_driver)
        time.sleep(1)
        device_name.FriendList.ENTER_NICKNAME_STRING.tap(appium_driver)
        time.sleep(1)
        appium_driver.execute_script("mobile: type", {"text": str(200003071)})
        time.sleep(2)
        appium_driver.press_keycode(AndroidKey.ENTER)
        time.sleep(2)
        device_name.FriendList.FIND_USER_BUTTON.tap(appium_driver)
        time.sleep(1)
        screen_is_match(device_templates.LobbyTemplates.USER_SEARCH_SCREEN, 0.90, appium_driver)
        device_name.FriendList.FIRST_USER.tap(appium_driver)
        time.sleep(1)
        device_name.FriendList.ADD_FRIEND_BUTTON.tap(appium_driver)
        time.sleep(1)
        device_name.FriendList.SKIP_POPUP_AREA.tap(appium_driver)
        time.sleep(1)
        device_name.FriendList.FRIENDS_TAB.tap(appium_driver)
        time.sleep(5)
        screen_is_match(device_templates.LobbyTemplates.FRIEND_LIST_SCREEN, 0.90, appium_driver)


class TestLobbyFeaturesProd:
    """
    Набор для запуска на Prod окружении
    """
    pass