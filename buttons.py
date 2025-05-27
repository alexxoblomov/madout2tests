from dataclasses import dataclass

@dataclass
class Button:
    x: int
    y: int

    def tap(self, driver):
        driver.tap([(self.x, self.y)])


class PocoX6:
    class MainLobby:
        # entry points
        CLANS_ENTRY_POINT = Button(x=2022, y=1080)
        BATTLE_PASS_ENTRY_POINT = Button(x=1355, y=1093)
        DAILY_LOGIN_ENTRY_POINT = Button(x=1136, y=69)
        QUESTS_ENTRY_POINT = Button(x=2404, y=400)
        GROW_FOUND_ENTRY_POINT = Button(x=318, y=231)

        # popups
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)
        BATTLE_PASS_POPUP_CLOSE = Button(x=2510, y=56)
        GROW_FOUND_POPUP_CLOSE = Button(x=2322, y=219)
        DAILY_LOGIN_REWARD_POPUP_CLOSE = Button(x=2485, y=69)

        # shops
        MAIN_SHOP = Button(x=387, y=1111)
        CAR_SHOP_AREA = Button(x=1130, y=640)
        APPEARANCE_SHOP_AREA = Button(x=1598, y=400)
        WEAPON_SHOP_AREA = Button(x=1885, y=581)

        # gameplay features
        GAME_MODE = Button(x=2404, y=965)
        SINGLE_MODE = Button(x=724, y=624)
        SERVER_LIST = Button(x=2060, y=934)

    class MainShop:
        BACK_BUTTON = Button(x=175, y=56)
        ADS = Button(x=318, y=1118)

    class MainClans:
        CLAN_CREATE_CONFIRM_BUTTON = Button(x=1355, y=1055)
        CLAN_SETTINGS_BUTTON = Button(x=768, y=1105)
        CLAN_DELETE_BUTTON = Button(x=1267, y=169)
        CLAN_DELETE_STRING = Button(x=1355, y=599)
        CLAN_DELETE_CONFIRM_BUTTON = Button(x=1118, y=905)

    class CreateClan:
        CLAN_NAME_STRING = Button(x=549, y=243)
        CREATE_CLAN_BUTTON = Button(x=624, y=1130)

    class ClansSearch:
        CLAN_QUICK_JOIN_BUTTON = Button(x=1666, y=1112)
        CREATE_CLAN_BUTTON = Button(x=2322, y=1111)

    class GrowFound:
        CLAIM_1LVL_REWARD_BUTTON = Button(x=1330, y=468)
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)

    class Quests:
        CLAIM_ALL_REWARDS_BUTTON = Button(x=2254, y=1130)
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)

    class DailyLogin:
        WEEK_2_PAGE = Button(x=1274, y=1093)
        WEEK_3_PAGE = Button(x=1679, y=1093)
        WEEK_4_PAGE = Button(x=2135, y=1093)

    class BattlePass:
        CLAIM_REWARDS_BUTTON = Button(x=1873, y=1118)
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)

    class CarShop:
        # pages
        ALREADY_HAVE_PAGE = Button(x=306, y=331)
        SPECIAL_PAGE = Button(x=312, y=1118)
        APPEARANCE_SHOP_PAGE = Button(x=169, y=805)

        # options and items
        REVEAL_LIST = Button(x=780, y=724)
        CAR_BUGGY = Button(x=1698, y=518)

        # general
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)
        BUY_BUTTON = Button(x=2397, y=1130)
        UPGRADE_BUTTON = Button(x=2010, y=1130)
        BUY_UPGRADE_BUTTON = Button(x=2340, y=1130)
        BUY_UPGRADE_CONFIRM_BUTTON = Button(x=1700, y=1130)

    class AppearanceShop:
        APPEARANCE_PRESETS_PAGE = Button(x=306, y=1118)
        APPEARANCE_ACCESSORIES_PAGE = Button(x=312, y=955)
        APPEARANCE_ACCESSORIES_CHAINS = Button(x=755, y=1130)
        APPEARANCE_ACCESSORIES_CHAINS_GOLD_CHAIN = Button(x=980, y=630)
        BUY_BUTTON = Button(x=2397, y=1130)
        WEAPON_SHOP_PAGE = Button(x=181, y=955)

    class WeaponShop:
        # general
        BUY_AMMO_BUTTON = Button(x=1873, y=1130)
        BUY_AMMO_MIN_PRICE_BUTTON = Button(x=1879, y=968)
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)
        UPGRADE_WEAPON_BUTTON = Button(x=2360, y=1130)
        CONFIRM_UPGRADE_WEAPON_BUTTON = Button(x=1829, y=1105)
        SKIP_WEAPON_UPGRADE_ANIMATION_TAP = Button(x=1355, y=1005)

        ARMOR_SHOWCASE = Button(x=618, y=243)
        M4A1_SHOWCASE = Button(x=649, y=456)

        PISTOL_CATEGORY_PAGE = Button(x=312, y=1118)
        FNP_45 = Button(x=643, y=668)

    class DeviceKeyboard:
        BACK_BUTTON = Button(x=2653, y=331)

    class LoginScreen:
        # DEV БИЛД
        WELCOME_SCREEN_BUTTON = Button(x=1342, y=855)
        GUEST_LOGIN_BUTTON = Button(x=780, y=880)
        PROLOGUE_SKIP_BUTTON = Button(x=24, y=1172)
        PROLOGUE_SKIP_CUTSCENE = Button(x=2516, y=1093)

        GOOGLE_LOGIN_BUTTON = Button(x=1542, y=880)
        GOOGLE_ACCOUNT_BUTTON = Button(x=1286, y=612)

        FACEBOOK_LOGIN_BUTTON = Button(x=1180, y=880)


    class EnvScreen:
        ACTIVE_SYSTEMS = Button(x=1349, y=1039)
        CLOSE_ACTIVE_SYSTEMS = Button(x=2366, y=81)

        ACTIVE_SYSTEMS_FLAGS = Button(x=705, y=69)
        LOGS_REPORTER = Button(x=219, y=306)
        AUTO_PRESENTATION = Button(x=955, y=318)
        SHOW_LOADING_UI = Button(x=955, y=755)
        SHOW_POPUPS = Button(x=1698, y=755)
        FTUE_ACTIVE = Button(x=1698, y=899)

        CLOSE = Button(x=2541, y=169)

        DEV = Button(x=431, y=755)
        DEV2 = Button(x=812, y=755)
        DEV3 = Button(x=1186, y=755)
        DEV4 = Button(x=1555, y=755)
        DEV5 = Button(x=1917, y=755)
        DEV6 = Button(x=2279, y=755)

        PROD = Button(x=643, y=231)
        STAGE = Button(x=1280, y=231)

