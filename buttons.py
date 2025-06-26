import logging
from dataclasses import dataclass


logger = logging.getLogger(__name__)


@dataclass
class Button:
    x: int
    y: int

    def tap(self, driver):
        logger.debug(f"Tapping at coordinates: (x={self.x}, y={self.y})")
        try:
            driver.tap([(self.x, self.y)])
            logger.debug("Tap successful")
        except Exception as e:
            logger.error(f"Failed to tap at (x={self.x}, y={self.y}): {str(e)}")
            raise


class PocoX6:
    class MainLobby:
        # entry points
        CLANS_ENTRY_POINT = Button(x=2022, y=1080)
        BATTLE_PASS_ENTRY_POINT = Button(x=1355, y=1093)
        DAILY_LOGIN_ENTRY_POINT = Button(x=1136, y=69)
        QUESTS_ENTRY_POINT = Button(x=2404, y=400)
        GROW_FOUND_ENTRY_POINT = Button(x=318, y=231)
        FRIEND_LIST_ENTRY_POINT = Button(x=643, y=75)
        PLAYER_PROFILE = Button(x=268, y=56)

        # popups
        CLAIM_REWARD_POPUP_BUTTON = Button(x=1355, y=1005)
        BATTLE_PASS_POPUP_CLOSE = Button(x=2510, y=56)
        GROW_FOUND_POPUP_CLOSE = Button(x=2322, y=219)
        DAILY_LOGIN_REWARD_POPUP_CLOSE = Button(x=2485, y=69)
        DAILY_LOGIN_SCREEN_CLOSE = Button(x=2360, y=144)
        SKIP_NEW_SYSTEM_POPUPS = Button(x=1629, y=50)

        # shops
        MAIN_SHOP_BUTTON = Button(x=387, y=1111)
        CAR_SHOP_AREA = Button(x=1130, y=640)
        APPEARANCE_SHOP_AREA = Button(x=1598, y=400)
        WEAPON_SHOP_AREA = Button(x=1885, y=581)

        # gameplay features
        GAME_MODE = Button(x=2404, y=965)
        SINGLE_MODE = Button(x=724, y=624)
        SERVER_LIST = Button(x=2060, y=934)
        FIRST_SERVER_IN_LIST = Button(x=805, y=393)

    class PlayerProfile:
        PROMO_CODES_STRING = Button(x=456, y=668)
        SEND_PROMO_CODE_BUTTON = Button(x=1942, y=662)
        DEVELOPER_POPUP_SKIP_AREA = Button(x=1667, y=81)
        BACK_TO_LOBBY_BUTTON = Button(x=181, y=50)

    class FriendList:
        FRIENDS_TAB = Button(x=368, y=175)
        REQUESTS_TAB = Button(x=862, y=175)
        FIND_USER_TAB = Button(x=1349, y=175)
        BLOCKED_USERS_TAB = Button(x=1854, y=175)
        FOLLOWERS_TAB = Button(x=2366, y=175)

        ENTER_NICKNAME_STRING = Button(x=556, y=331)
        FIND_USER_BUTTON = Button(x=2354, y=331)
        FIRST_USER = Button(x=468, y=493)
        ADD_FRIEND_BUTTON = Button(x=2060, y=362)
        SKIP_POPUP_AREA = Button(x=1611, y=112)

    class MainShop:
        DEV_TEST_BUY_BUTTON = Button(x=2235, y=649)

        # main page
        BACK_BUTTON = Button(x=175, y=56)
        ADS_CATEGORY_BUTTON = Button(x=318, y=1118)

        IN_APP_SOFT_OFFERS = Button(x=312, y=718)
        IN_APP_SOFT_1 = Button(x=687, y=1030)


        # ads category
        CLOSE_TEST_AD = Button(x=2547, y=56)
        MARATHON_CH1_ADS_BUTTON = Button(x=1430, y=1030)

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

        CLANS_SEARCH_STRING = Button(x=425, y=1111)
        REQUEST_OR_JOIN_1ST_CLAN_BUTTON = Button(x=2341, y=381)
        REQUEST_AND_INVITES_TAB = Button(x=805, y=194)

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
        FTUE_ACTIVE = Button(x=206, y=1043)

        CLOSE = Button(x=2541, y=169)

        DEV = Button(x=431, y=755)
        DEV2 = Button(x=812, y=755)
        DEV3 = Button(x=1186, y=755)
        DEV4 = Button(x=1555, y=755)
        DEV5 = Button(x=1917, y=755)
        DEV6 = Button(x=2279, y=755)

        PROD = Button(x=643, y=231)
        STAGE = Button(x=1280, y=231)

