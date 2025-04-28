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

    # test_ways_to_login
    LOGIN_SCREEN = TEMPLATES_DIR / "test_login" / "test_ways_to_login" / "login_screen.png"
    GOOGLE_LOGIN = TEMPLATES_DIR / "login_screen" / "test_ways_to_login" / "google_login.png"
    FACEBOOK_LOGIN = TEMPLATES_DIR / "login_screen" / "test_ways_to_login" / "facebook_login.png"
    GOOGLE_ACCOUNTS = TEMPLATES_DIR / "login_screen" / "test_ways_to_login" / "google_accounts.png"
    FACEBOOK_HEADER = TEMPLATES_DIR / "login_screen" / "test_ways_to_login" / "facebook_header.png"

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