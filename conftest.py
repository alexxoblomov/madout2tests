import time, pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from madout_apk import apk_path
from madout_apk.apk_path import MadOutV16

"""
Подумать над тем, чтобы для каждого девайса сделать свою фикстуру
Например - def poco_x6_appium_driver()
"""


@pytest.fixture
def poco_x6_appium_driver():
    options = UiAutomator2Options()  # Для Android
    # options = XCUITestOptions()  # Для iOS

    options.platform_name = 'Android'
    options.device_name = 'PZW8WWFE49ZXLJDI'
    options.platform_version = '14.0'
    options.app = MadOutV16.app
    options.automation_name = 'UiAutomator2'
    options.no_reset = False

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=options
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def enter_dev_lobby(device, appium_driver: object) -> None:
    """
    +++ ~60 sec. to the test, where used
    Подумать над превращением этой функции в фикстуру
    """
    time.sleep(8)

    device.EnvScreen.DEV.tap(appium_driver)
    time.sleep(1)
    device.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device.LoginScreen.TOS_CONFIRM.tap(appium_driver)
    time.sleep(2)
    device.LoginScreen.GUEST_LOGIN.tap(appium_driver)
    time.sleep(35)
    device.LoginScreen.PROLOGUE_SKIP.tap(appium_driver)
    time.sleep(5)

    device.MainLobby.GROW_FOUND_POPUP_CLOSE.tap(appium_driver)
    time.sleep(1)
    device.MainLobby.UPPER_RIGHT_CORNER.tap(appium_driver)
    time.sleep(3)
    device.MainLobby.DAILY_LOGIN_REWARD_POPUP_CLOSE.tap(appium_driver)
    time.sleep(1)


def enter_prod_lobby(device, appium_driver: object) -> None:
    """
    +++ ~60 sec. to the test, where used
    Подумать над превращением этой функции в фикстуру
    """
    pass
