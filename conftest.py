import time, pytest, questionary
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver import Remote
from devices import get_device_class, DEVICES


def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        required=True,
        choices=list(DEVICES.keys()),
        help="Укажите устройство для тестов. Доступные варианты: %(choices)s"
    )


@pytest.fixture(scope="session")
def device_name(request):
    get_device_name = request.config.getoption("--device")
    return get_device_class(get_device_name)


def pytest_configure(config):
    if config.getoption("--device") is None:
        device = questionary.select(
            "Выберите устройство:",
            choices=list(DEVICES.keys()),
        ).ask()
        config.option.device = device


@pytest.fixture
def appium_driver(request):
    device = request.config.getoption("--device")
    device_config = DEVICES[device]

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


def enter_login_screen(device_name, appium_driver: object) -> None:
    time.sleep(8)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device_name.LoginScreen.WELCOME_SCREEN.tap(appium_driver)
    time.sleep(3)

def enter_dev_lobby(device_name, appium_driver: object) -> None:
    """
    +++ ~60 sec. to the test, where used
    Подумать над превращением этой функции в фикстуру
    """
    time.sleep(8)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device_name.LoginScreen.WELCOME_SCREEN.tap(appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GUEST_LOGIN.tap(appium_driver)
    time.sleep(25)
    device_name.LoginScreen.PROLOGUE_SKIP.tap(appium_driver)
    time.sleep(5)

    device_name.MainLobby.GROW_FOUND_POPUP_CLOSE.tap(appium_driver)
    time.sleep(1)
    device_name.MainLobby.UPPER_RIGHT_CORNER.tap(appium_driver)
    time.sleep(3)
    device_name.MainLobby.DAILY_LOGIN_REWARD_POPUP_CLOSE.tap(appium_driver)
    time.sleep(1)


def enter_prod_lobby(device, appium_driver: object) -> None:
    """
    +++ ~60 sec. to the test, where used
    Подумать над превращением этой функции в фикстуру
    """
    pass
