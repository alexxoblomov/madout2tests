from dataclasses import dataclass

@dataclass
class Button:
    x: int
    y: int

    def tap(self, driver):
        driver.tap([(self.x, self.y)])

"""
Подумать над тем, чтобы выносить классы экранов в отдельный класс-девайс
Например - PocoX6.MainLobby.CLAN_ENTRY_BUTTON
"""

class PocoX6:
    class MainLobby:
        CLAN_ENTRY = Button(x=2022, y=1080)
        UPPER_RIGHT_CORNER = Button(x=2672, y=194)
        GROW_FOUND_POPUP_CLOSE = Button(x=2322, y=219)
        DAILY_LOGIN_REWARD_POPUP_CLOSE = Button(x=2485, y=69)

    class MainClans:
        pass

    class ClansSearch:
        CLAN_QUICK_JOIN = Button(x=1666, y=1112)

    class DeviceKeyboard:
        pass

    class LoginScreen:
        TOS_CONFIRM = Button(x=1342, y=855)
        GUEST_LOGIN = Button(x=780, y=880)
        PROLOGUE_SKIP = Button(x=37, y=1167)


    class EnvScreen:
        CLOSE = Button(x=2541, y=169)

        DEV = Button(x=431, y=755)
        DEV2 = Button(x=812, y=755)
        DEV3 = Button(x=1186, y=755)
        DEV4 = Button(x=1555, y=755)
        DEV5 = Button(x=1917, y=755)
        DEV6 = Button(x=2279, y=755)

        PROD = Button(x=643, y=231)
        STAGE = Button(x=1280, y=231)

