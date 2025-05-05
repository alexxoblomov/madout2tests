from pathlib import Path

"""
Рассмотреть возможность объединения шаблонов в разные классы-устройства
На случай, если единственный класс Template не будет подходить для нашего парка
"""

class Templates:
    BASE_DIR = Path(__file__).parent.parent
    TEMPLATES_DIR = BASE_DIR / "templates"

    # test_guest_login_and_check_server_list
    LOBBY_SCREEN = TEMPLATES_DIR / "test_lobby" / "test_guest_login_and_check_server_list" / "lobby_screen.png"
    EMPTY_SERVER_LIST = TEMPLATES_DIR / "test_lobby" / "test_guest_login_and_check_server_list" / "empty_server_list.png"

    # test_google_login

    # test_clans_quick_join
    CLAN_ENTRY = TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "clan_entry.png"
    QUICK_JOIN = TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "quick_join.png"
    CLAN_META = TEMPLATES_DIR / "test_clans" / "test_clans_quick_join" / "clan_meta.png"

    # test_login_screen_state
    LOGIN_SCREEN = TEMPLATES_DIR / "test_login" / "test_login_screen_state" / "login_screen.png"

    # test_tos_and_privacy_policy
    WELCOME_SCREEN = TEMPLATES_DIR / "test_login" / "test_tos_and_privacy_policy" / "welcome_screen.png"
    # PRIVACY_POLICY = TEMPLATES_DIR / "test_login" / "test_tos_and_privacy_policy" / "privacy_policy.png"
    # TERMS_OF_SERVICE = TEMPLATES_DIR / "test_login" / "test_tos_and_privacy_policy" / "terms_of_service.png"

    # test_buy_some_stuff
    CAR_BUGGY_REWARD_POPUP = TEMPLATES_DIR / "test_buy_some_stuff" /"car_shop" / "car_buggy_reward_popup.png"
    GOLD_CHAIN_REWARD_POPUP = TEMPLATES_DIR / "test_buy_some_stuff" / "appearance_shop" / "gold_chain_reward_popup.png"
    FNP_45_REWARD_POPUP = TEMPLATES_DIR / "test_buy_some_stuff" / "weapon_shop" / "fnp_45_reward_popup.png"

    # test_enter_shops
    APPEARANCE_PRESETS = TEMPLATES_DIR / "test_enter_shops" / "appearance_shop" / "appearance_presets.png"
    WEAPON_SHOP = TEMPLATES_DIR / "test_enter_shops" / "weapon_shop" / "weapon_shop.png"
    CAR_SHOP_CITIZEN = TEMPLATES_DIR / "test_enter_shops" / "car_shop" / "car_shop_citizen.png"

    # test_attention_marks
    ATTENTION_MARK_UNSEEN = TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark_unseen.png"
    ATTENTION_MARK = TEMPLATES_DIR / "test_shops" / "test_attention_marks" / "attention_mark.png"

    # test_claim_battle_pass_reward
    BATTLE_PASS_ENTRY = TEMPLATES_DIR / "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_entry.png"
    BATTLE_PASS_MAIN = TEMPLATES_DIR /  "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_main.png"
    BATTLE_PASS_1LVL_REWARD = TEMPLATES_DIR /  "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_1lvl_reward.png"
    BATTLE_PASS_BUY_PREMIUM = TEMPLATES_DIR /  "test_lobby" / "test_claim_battle_pass_reward" / "battle_pass_buy_premium.png"

    # test_daily_login
    WEEK_1 = TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "week_1.png"
    WEEK_2 = TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "week_2.png"
    WEEK_3 = TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "week_3.png"
    WEEK_4 = TEMPLATES_DIR / "test_lobby" / "test_daily_login" / "week_4.png"

    # test_claim_client_quest
    QUESTS_ENTRY = TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "quests_entry.png"
    CLAIM_ALL_REWARDS = TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "claim_all_rewards.png"
    QUEST_REWARD_POPUP = TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "quest_reward_popup.png"
    CLAIM_ALL_REWARDS_DISABLED = TEMPLATES_DIR / "test_lobby" / "test_claim_client_quest" / "claim_all_rewards_disabled.png"

    # test_claim_grow_found_reward
    GROW_FOUND_ENTRY = TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_entry.png"
    GROW_FOUND_MAIN = TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_main.png"
    GROW_FOUND_1LVL_REWARD = TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "grow_found_1lvl_reward.png"
    CLAIMED_1LVL_FREE_REWARD = TEMPLATES_DIR / "test_lobby" / "test_claim_grow_found_reward" / "claimed_1lvl_free_reward.png"