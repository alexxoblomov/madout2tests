from dataclasses import dataclass

@dataclass
class Button:
    x: int
    y: int

    def tap(self, driver):
        driver.tap([(self.x, self.y)])


class PocoX6:
    class MainLobby:
        CLAN_ENTRY_POINT = Button(x=2022, y=1080)
        BATTLE_PASS_ENTRY = Button(x=1355, y=1093)
        DAILY_LOGIN = Button(x=980, y=69)
        QUESTS_ENTRY = Button(x=2404, y=400)
        GROW_FOUND_ENTRY = Button(x=318, y=231)
        # CLOSE_REWARD_POPUP = Button(x=2672, y=194)

        CLAIM_REWARD_POPUP = Button(x=1355, y=1005)
        GROW_FOUND_POPUP_CLOSE = Button(x=2322, y=219)
        DAILY_LOGIN_REWARD_POPUP_CLOSE = Button(x=2485, y=69)

        MAIN_SHOP = Button(x=387, y=1111)
        CAR_SHOP = Button(x=1130, y=640)
        APPEARANCE_SHOP = Button(x=1598, y=400)
        WEAPON_SHOP = Button(x=1885, y=581)

        GAME_MODE = Button(x=2404, y=965)
        SINGLE_MODE = Button(x=724, y=624)
        SERVER_LIST = Button(x=2060, y=934)

    class MainShop:
        BACK = Button(x=175, y=56)
        ADS = Button(x=318, y=1118)

    class MainClans:
        CLAN_CREATE_CONFIRM = Button(x=1355, y=1055)
        CLAN_SETTINGS = Button(x=768, y=1105)
        CLAN_DELETE = Button(x=1267, y=169)
        CLAN_DELETE_STRING = Button(x=1355, y=599)
        CLAN_DELETE_CONFIRM = Button(x=1118, y=905)

    class CreateClan:
        # create screen
        CLAN_NAME = Button(x=549, y=243)
        CREATE_CLAN_BUTTON = Button(x=624, y=1130)

    class ClansSearch:
        CLAN_QUICK_JOIN = Button(x=1666, y=1112)
        CREATE_CLAN_BUTTON = Button(x=2322, y=1111)

    class GrowFound:
        CLAIM_1LVL_REWARD = Button(x=1330, y=468)
        CLAIM_REWARD_POPUP = Button(x=1355, y=1005)

    class Quests:
        CLAIM_ALL_REWARDS = Button(x=2254, y=1130)
        CLAIM_REWARD_POPUP = Button(x=1355, y=1005)

    class DailyLogin:
        WEEK_2 = Button(x=1274, y=1093)
        WEEK_3 = Button(x=1679, y=1093)
        WEEK_4 = Button(x=2135, y=1093)

    class BattlePass:
        CLAIM_REWARDS = Button(x=1873, y=1118)
        BUY_PREMIUM = Button(x=1367, y=1130)
        CLAIM_REWARD_POPUP = Button(x=1355, y=1005)

    class CarShop:
        ALREADY_HAVE = Button(x=306, y=331)
        SPECIAL = Button(x=312, y=1118)
        APPEARANCE_SHOP = Button(x=169, y=805)

        REVEAL_LIST = Button(x=780, y=724)
        CAR_BUGGY = Button(x=1698, y=518)

        CLAIM_REWARD_POPUP = Button(x=1355, y=1005)

        # Надо что-то с неймингом сделать, определенно
        BUY = Button(x=2397, y=1130)
        UPGRADE = Button(x=2010, y=1130)
        BUY_UPGRADE = Button(x=2340, y=1130)
        BUY_UPGRADE_CONFIRM = Button(x=1700, y=1130)

    class AppearanceShop:
        APPEARANCE_PRESETS = Button(x=306,y=1118)
        ACCESSORIES = Button(x=312,y=955)
        ACCESSORIES_CHAINS = Button(x=755, y=1130)
        ACCESSORIES_CHAINS_GOLD_CHAIN = Button(x=980, y=630)
        BUY = Button(x=2397, y=1130)
        WEAPON_SHOP = Button(x=181, y=955)

    class WeaponShop:
        PISTOL_CATEGORY = Button(x=312, y=1118)
        FNP_45 = Button(x=643, y=668)
        BUY_AMMO = Button(x=1873, y=1130)
        BUY_AMMO_MIN = Button(x=1879, y=968)

    class DeviceKeyboard:
        BACK = Button(x=2653, y=331)

    class LoginScreen:
        # DEV БИЛД
        WELCOME_SCREEN = Button(x=1342, y=855)
        GUEST_LOGIN = Button(x=780, y=880)
        PROLOGUE_SKIP = Button(x=24, y=1172)

        GOOGLE_LOGIN = Button(x=1542, y=880)
        GOOGLE_ACCOUNT = Button(x=1286, y=612)

        FACEBOOK_LOGIN = Button(x=1180, y=880)
        #

        TERMS_OF_SERVICE = Button(x=1186, y=568)
        TOS_XPATH = '//android.widget.TextView[@text="MadOut 2| Terms of Use"]'

        PRIVACY_POLICY = Button(x=1523, y=568)
        PP_XPATH = '//android.widget.TextView[@text="Madout 2 | Privacy Policy "]'


    class EnvScreen:
        ACTIVE_SYSTEMS = Button(x=1349, y=1039)
        CLOSE_ACTIVE_SYSTEMS = Button(x=2366, y=81)

        ACTIVE_SYSTEMS_FLAGS = Button(x=705, y=69)
        LOGS_REPORTER = Button(x=219, y=306)
        AUTO_PRESENTATION = Button(x=955, y=318)
        SHOW_LOADING_UI = Button(x=955, y=755)
        SHOW_POPUPS = Button(x=1698, y=755)

        CLOSE = Button(x=2541, y=169)

        DEV = Button(x=431, y=755)
        DEV2 = Button(x=812, y=755)
        DEV3 = Button(x=1186, y=755)
        DEV4 = Button(x=1555, y=755)
        DEV5 = Button(x=1917, y=755)
        DEV6 = Button(x=2279, y=755)

        PROD = Button(x=643, y=231)
        STAGE = Button(x=1280, y=231)

