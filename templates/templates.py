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
        # test_guest_login_and_check_server_list
        LOBBY_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_guest_login_and_check_server_list" / "lobby_screen.png"
        EMPTY_SERVER_LIST = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_guest_login_and_check_server_list" / "empty_server_list.png"

        # test_google_login
        SINGLE_MODE_HOUSE = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_google_login_and_go_single_mode" / "single_mode_house.png"

        # test_login_screen_state
        LOGIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_login_screen_state" / "login_screen.png"

        # test_tos_and_privacy_policy
        WELCOME_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_login" / "test_tos_and_privacy_policy" / "welcome_screen.png"


    class ClansTemplates(BaseTemplates):
        """
        Общие шаблоны для нескольких тестов:
        CLAN_ENTRY_POINT = TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "clan_entry_point.png"
        CLAN_META_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_meta_screen.png"
        """

        # test_clans_quick_join
        QUICK_JOIN_BUTTON = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "quick_join_button.png"
        CLAN_META_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "clan_meta_screen.png"

        # test_clan_create_and_delete
        CLAN_ENTRY_POINT = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_entry_point.png"
        CREATE_CLAN_BUTTON = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "create_clan_button.png"
        CREATE_CLAN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "create_clan_screen.png"
        CLAN_DELETE_POPUP = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_delete_popup.png"
        CLAN_DELETED_POPUP = BaseTemplates.TEMPLATES_DIR / "test_clans" / "test_clan_create_and_delete" / "clan_deleted_popup.png"


    class LobbyTemplates(BaseTemplates):
        """

        """
        # test_claim_battle_pass_reward
        BATTLE_PASS_ENTRY_POINT = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_entry_point.png"
        BATTLE_PASS_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_main_screen.png"
        BATTLE_PASS_1LVL_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_1lvl_reward_popup.png"
        BATTLE_PASS_BUY_PREMIUM_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_buy_premium_screen.png"

        # test_daily_login
        DL_WEEK_1_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "dl_week_1_screen.png"
        DL_WEEK_2_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "dl_week_2_screen.png"
        DL_WEEK_3_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "dl_week_3_screen.png"
        DL_WEEK_4_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "dl_week_4_screen.png"

        # test_claim_client_quest
        CLIENTS_QUESTS_ENTRY = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "quests_entry_point.png"
        CLAIM_ALL_REWARDS_BUTTON = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "claim_all_rewards_button.png"
        QUEST_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "client_quest_reward_popup.png"
        CLAIM_ALL_REWARDS_BUTTON_DISABLED = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "claim_all_rewards_disabled_button.png"

        # test_claim_grow_found_reward
        GROW_FOUND_ENTRY_POINT = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_entry_point.png"
        GROW_FOUND_MAIN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_main_screen.png"
        GROW_FOUND_1LVL_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_1lvl_reward_popup.png"
        CLAIMED_1LVL_FREE_REWARD = BaseTemplates.TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "claimed_1lvl_free_reward.png"


    class ShopTemplates(BaseTemplates):
        """

        """
        # test_buy_some_stuff
        CAR_BUGGY_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_buy_some_stuff"  / "car_buggy_reward_popup.png"
        GOLD_CHAIN_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_buy_some_stuff" / "gold_chain_reward_popup.png"
        FNP_45_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_buy_some_stuff" / "fnp_45_reward_popup.png"

        # test_enter_shops
        APPEARANCE_PRESETS_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "appearance_presets_screen.png"
        WEAPON_SHOP_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "weapon_shop_screen.png"
        CAR_SHOP_CITIZEN_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_enter_shops" / "car_shop_citizen_screen.png"

        # test_attention_marks
        ATTENTION_MARK_UNSEEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark_unseen.png"
        ATTENTION_MARK = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark.png"

        # test_install_car_upgrade
        UPGRADE_CAR_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgrade_car_screen.png"
        UPGRADED_CAR_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgraded_car_screen.png"
        UPGRADE_BUY_CONFIRM_SCREEN = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgrade_buy_confirm_screen.png"
        UPGRADE_REWARD_POPUP = BaseTemplates.TEMPLATES_DIR / "test_shops" / "test_install_car_upgrade" / "upgrade_reward_popup.png"

