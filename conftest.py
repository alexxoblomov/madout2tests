import time, pytest, questionary
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from device_config import DEVICES
from appium.webdriver import Remote

"""
Подумать над тем, чтобы для каждого девайса сделать свою фикстуру
Например - def poco_x6_appium_driver()
"""


def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        required=True,
        choices=list(DEVICES.keys()),
        help="Укажите устройство для тестов. Доступные варианты: %(choices)s"
    )

def pytest_configure(config):
    if config.getoption("--device") is None:
        device = questionary.select(
            "Выберите устройство:",
            choices=list(DEVICES.keys()),
        ).ask()
        config.option.device = device

@pytest.fixture
def appium_driver(request):
    device_name = request.config.getoption("--device")
    device_config = DEVICES[device_name]

    if device_config["platform_name"] == "Android":
        options = UiAutomator2Options()
    else:
        options = XCUITestOptions()

    for key, value in device_config.items():
        setattr(options, key, value)

    driver = Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def enter_login_screen(device, appium_driver: object) -> None:
    time.sleep(8)

    device.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device.LoginScreen.TOS_CONFIRM.tap(appium_driver)
    time.sleep(3)

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
