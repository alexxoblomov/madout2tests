from pathlib import Path

"""
Рассмотреть возможность объединения шаблонов в разные классы-устройства
На случай, если единственный класс Template не будет подходить для нашего парка
"""


class BaseTemplates:
    BASE_DIR = Path(__file__).parent.parent
    TEMPLATES_DIR = BASE_DIR / "templates"

class PocoX6:
    class LoginTemplates (BaseTemplates):
        """
        """
        # test_check_server_list_and_go_online
        SERVER_LIST_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_check_server_list_and_go_online" / "server_list_screen.png"
        ONLINE_GAMEPLAY_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_check_server_list_and_go_online" / "online_gameplay_screen.png"

        # test_go_single_mode
        SINGLE_MODE_HOUSE = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_go_single_mode" / "single_mode_house.png"

        # test_login_screen_state
        LOGIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_login_screen_state" / "login_screen.png"

        # test_go_ftue
        FTUE_START_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_go_ftue" / "ftue_start_screen.png"


    class LobbyTemplates(BaseTemplates):
        """
        """
        # test_claim_battle_pass_reward
        BATTLE_PASS_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_battle_pass_reward" / "battle_pass_main_screen.png"
        BATTLE_PASS_1LVL_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_battle_pass_reward" / "battle_pass_1lvl_reward_popup.png"

        # test_claim_client_quest
        QUEST_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_client_quest" / "client_quest_reward_popup.png"
        CLAIM_ALL_REWARDS_BUTTON_DISABLED = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_client_quest" / "claim_all_rewards_disabled_button.png"

        # test_claim_grow_found_reward
        GROW_FOUND_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_grow_found_reward" / "grow_found_main_screen.png"
        GROW_FOUND_1LVL_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_claim_grow_found_reward" / "grow_found_1lvl_reward_popup.png"

        # test_daily_login
        DL_WEEK_1_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_daily_login" / "dl_week_1_screen.png"
        DL_WEEK_2_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_daily_login" / "dl_week_2_screen.png"
        DL_WEEK_3_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_daily_login" / "dl_week_3_screen.png"
        DL_WEEK_4_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_daily_login" / "dl_week_4_screen.png"

        # test_search_and_add_friend
        USER_SEARCH_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_search_and_add_friend" / "user_search_screen.png"
        FRIEND_LIST_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby_features" / "test_search_and_add_friend" / "friend_list_screen.png"


    class ShopTemplates(BaseTemplates):
        """
        """
        # test_buy_for_soft_and_hard
        ARMOR_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_buy_for_soft_and_hard"  / "armor_reward_popup.png"
        M4A1_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_buy_for_soft_and_hard" / "m4a1_reward_popup.png"

        # test_enter_shops
        CAR_SHOP_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "car_shop_main_screen.png"
        WEAPON_SHOP_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "weapon_shop_main_screen.png"
        APPEARANCE_SHOP_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "appearance_shop_main_screen.png"

        # test_attention_marks
        ATTENTION_MARK_UNSEEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark_unseen.png"
        ATTENTION_MARK = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark.png"

        # test_install_car_upgrade
        UPGRADE_BUY_CONFIRM_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgrade_buy_confirm_screen.png"
        UPGRADE_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgrade_reward_popup.png"

        # test_weapon_upgrade
        WEAPON_UPGRADE_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_weapon_upgrade" / "weapon_upgrade_main_screen.png"
        WEAPON_UPGRADED_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_weapon_upgrade" / "weapon_upgraded_screen.png"

        # test_watch_ads_marathon
        TEST_AD_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_watch_ads_marathon" / "test_ad_screen.png"
        AD_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_watch_ads_marathon" / "ad_reward_popup.png"

        # test_in_app_purchase
        IN_APP_SOFT_1_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_in_app_purchase" / "in_app_soft_1_reward_popup.png"


    class ClansTemplates(BaseTemplates):
        """
        """

        # test_clans_quick_join
        QUICK_JOIN_BUTTON = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "quick_join_button.png"
        CLAN_META_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "clan_meta_screen.png"

        # test_sent_to_join_request
        CLAN_TO_JOIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_sent_join_request" / "clan_to_join_screen.png"
        REQUEST_AND_INVITES_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_sent_join_request" / "request_and_invites_screen.png"

        # test_clan_manually_join
        OPEN_CLAN_TO_JOIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_manually_join" / "open_clan_to_join_screen.png"
        OPEN_CLAN_TO_JOIN_META_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_manually_join" / "open_clan_to_join_meta_screen.png"

        # test_clan_create_and_delete
        CLAN_ENTRY_POINT = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_entry_point.png"
        CREATE_CLAN_BUTTON = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "create_clan_button.png"
        CREATE_CLAN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "create_clan_screen.png"
        CLAN_DELETE_POPUP = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_delete_popup.png"
        CLAN_DELETED_POPUP = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_deleted_popup.png"