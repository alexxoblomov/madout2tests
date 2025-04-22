from pathlib import Path


class Templates:
    BASE_DIR = Path(__file__).parent.parent
    TEMPLATES_DIR = BASE_DIR / "templates"

    # clans
    CLAN_ENTRY = TEMPLATES_DIR / "clans" / "clan_entry.png"
    QUICK_JOIN = TEMPLATES_DIR / "clans" / "quick_join.png"
    CLAN_META = TEMPLATES_DIR / "clans" / "clan_meta.png"

    # login screen
    WELCOME_SCREEN = TEMPLATES_DIR / "login_screen" / "welcome_screen.png"
    LOGIN_SCREEN = TEMPLATES_DIR / "login_screen" / "login_screen.png"
    GOOGLE_LOGIN = TEMPLATES_DIR / "login_screen" / "google_login.png"
    FACEBOOK_LOGIN = TEMPLATES_DIR / "login_screen" / "facebook_login.png"
    GOOGLE_ACCOUNTS = TEMPLATES_DIR / "login_screen" / "google_accounts.png"
    FACEBOOK_HEADER = TEMPLATES_DIR / "login_screen" / "facebook_header.png"
    PRIVACY_POLICY = TEMPLATES_DIR / "login_screen" / "privacy_policy.png"
    TERMS_OF_SERVICE = TEMPLATES_DIR / "login_screen" / "terms_of_service.png"

    # main lobby