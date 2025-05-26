import time, pytest, questionary
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver import Remote
from devices import get_device_class, DEVICES
from templates.templates import PocoX6

DEVICE_TEMPLATES = {
    "poco_x6": PocoX6,
}


def get_device_templates(device_name):
    return DEVICE_TEMPLATES.get(device_name)


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


@pytest.fixture(scope="session")
def device_templates(request):
    get_device_name = request.config.getoption("--device")
    templates = get_device_templates(get_device_name)
    if not templates:
        pytest.skip(f"No templates found for device: {get_device_name}")
    return templates


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


def enter_login_screen_with_popups(device_name, appium_driver: object) -> None:
    """
    Вход на экран логина с включенными поп-апами
    """
    time.sleep(8)
    device_name.EnvScreen.ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.ACTIVE_SYSTEMS_FLAGS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.LOGS_REPORTER.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.AUTO_PRESENTATION.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_LOADING_UI.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE_ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)
    device_name.LoginScreen.WELCOME_SCREEN_BUTTON.tap(appium_driver)
    time.sleep(3)


def enter_login_screen_without_popups(device_name, appium_driver: object) -> None:
    """
    Вход на экран логина с отключенными попапами
    """
    time.sleep(8)
    device_name.EnvScreen.ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.ACTIVE_SYSTEMS_FLAGS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.LOGS_REPORTER.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.AUTO_PRESENTATION.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_LOADING_UI.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE_ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(2)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)
    device_name.LoginScreen.WELCOME_SCREEN_BUTTON.tap(appium_driver)
    time.sleep(3)


def enter_dev_lobby_with_popups(device_name, appium_driver: object) -> None:
    """
    Логин гостем на дев-окружение с включенными попапами
    """
    time.sleep(8)
    device_name.EnvScreen.ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.ACTIVE_SYSTEMS_FLAGS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.LOGS_REPORTER.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.AUTO_PRESENTATION.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_LOADING_UI.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE_ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device_name.LoginScreen.WELCOME_SCREEN_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GUEST_LOGIN_BUTTON.tap(appium_driver)
    time.sleep(45)
    device_name.LoginScreen.PROLOGUE_SKIP_BUTTON.tap(appium_driver)
    time.sleep(5)

    # может меняться время от времени, просто комментить
    device_name.MainLobby.GROW_FOUND_POPUP_CLOSE.tap(appium_driver)
    time.sleep(5)
    device_name.MainLobby.DAILY_LOGIN_REWARD_POPUP_CLOSE.tap(appium_driver)
    time.sleep(5)
    device_name.MainLobby.CLAIM_REWARD_POPUP_BUTTON.tap(appium_driver)


def enter_dev_lobby_without_popups(device_name, appium_driver: object) -> None:
    """
    Логин гостем на дев-окружение с отключенными попапами
    """
    time.sleep(8)
    device_name.EnvScreen.ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.ACTIVE_SYSTEMS_FLAGS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.LOGS_REPORTER.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.AUTO_PRESENTATION.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_LOADING_UI.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.SHOW_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE_ACTIVE_SYSTEMS.tap(appium_driver)
    time.sleep(1)

    device_name.EnvScreen.DEV.tap(appium_driver)
    time.sleep(1)
    device_name.EnvScreen.CLOSE.tap(appium_driver)
    time.sleep(2)

    device_name.LoginScreen.WELCOME_SCREEN_BUTTON.tap(appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GUEST_LOGIN_BUTTON.tap(appium_driver)
    time.sleep(45)
    device_name.LoginScreen.PROLOGUE_SKIP_BUTTON.tap(appium_driver)
    time.sleep(5)


def enter_with_google_login_with_popups(device_name, appium_driver):
    """
    Логин через гугл на дев-окружение с включенными попапами
    """
    enter_login_screen_with_popups(device_name, appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GOOGLE_LOGIN_BUTTON.tap(appium_driver)
    time.sleep(5)
    device_name.LoginScreen.GOOGLE_ACCOUNT_BUTTON.tap(appium_driver)
    time.sleep(35)
    device_name.LoginScreen.PROLOGUE_SKIP_BUTTON.tap(appium_driver)
    time.sleep(5)


def enter_with_google_login_without_popups(device_name, appium_driver):
    """
    Логин через гугл на дев-окружение c отключенными попапами
    """
    enter_login_screen_without_popups(device_name, appium_driver)
    time.sleep(2)
    device_name.LoginScreen.GOOGLE_LOGIN_BUTTON.tap(appium_driver)
    time.sleep(5)
    device_name.LoginScreen.GOOGLE_ACCOUNT_BUTTON.tap(appium_driver)
    time.sleep(35)
    device_name.LoginScreen.PROLOGUE_SKIP_BUTTON.tap(appium_driver)
    time.sleep(5)


def enter_prod_lobby(device_name, appium_driver: object) -> None:
    pass


def enter_with_facebook_login(device_name, appium_driver: object) -> None:
    pass

