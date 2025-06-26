import sys
import time, pytest, questionary, logging
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver import Remote
from devices import get_device_class, DEVICES
from templates.templates import PocoX6


"""
Логгер и его настройки
logging.getLogger('appium') и т.д отключает поток лишних логов и оставляет только логи из тестов
"""

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log", mode='w'),
        logging.StreamHandler(sys.stdout)
    ],
    force=True,
)

logging.getLogger('appium').setLevel(logging.WARNING)
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def log_test_start_end(request):
    test_name = request.node.name
    logger.info(f"Starting test: {test_name}")
    yield
    logger.info(f"Finished test: {test_name}")


"""Словарь-хранилище шаблонов и функция-получение"""

DEVICE_TEMPLATES = {
    "poco_x6": PocoX6,
}

def get_device_templates(device_name):
    return DEVICE_TEMPLATES.get(device_name)


"""Вспомогательные функции, но не фикстуры"""

def dev_mode_enabled(device_name, appium_driver):
    pass



"""Основные фикстуры фреймворка"""

def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        required=True,
        choices=list(DEVICES.keys()),
        help="Укажите устройство для тестов. Доступные варианты: %(choices)s"
    )
    parser.addoption(
        "--apk",
        action="store",
        help="Укажите путь к APK файлу для тестирования"
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

    driver = Remote("http://127.0.0.1:4723",
                    options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def enter_dev_login_screen_with_popups(device_name, appium_driver: object) -> None:
    """
    Вход на экран логина с включенными попапами
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


@pytest.fixture
def enter_dev_login_screen_without_popups(device_name, appium_driver: object) -> None:
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


@pytest.fixture
def enter_dev_lobby_with_popups(device_name, appium_driver: object) -> None:
    """
    Логин гостем на дев-окружение с включенными попапами и отключенным прологом
    """
    logger.info("fixture 'enter_dev_lobby_with_popups' is running")

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
    device_name.EnvScreen.FTUE_ACTIVE.tap(appium_driver)
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
    time.sleep(20)

    """
    Код ниже может меняться время от времени, просто комментить его по необходимости
    Или что-то добавлять. Влияет в основном на тесты с попапами/покупками/сбором наград
    """
    device_name.MainLobby.GROW_FOUND_POPUP_CLOSE.tap(appium_driver)
    time.sleep(5)
    device_name.MainLobby.SKIP_NEW_SYSTEM_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.MainLobby.SKIP_NEW_SYSTEM_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.MainLobby.SKIP_NEW_SYSTEM_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.MainLobby.SKIP_NEW_SYSTEM_POPUPS.tap(appium_driver)
    time.sleep(1)
    device_name.MainLobby.SKIP_NEW_SYSTEM_POPUPS.tap(appium_driver)
    time.sleep(1)

    # device_name.MainLobby.BATTLE_PASS_POPUP_CLOSE.tap(appium_driver)
    # time.sleep(5)
    # device_name.MainLobby.DAILY_LOGIN_REWARD_POPUP_CLOSE.tap(appium_driver)
    # time.sleep(5)
    # device_name.MainLobby.CLAIM_REWARD_POPUP_BUTTON.tap(appium_driver)

    logger.info("fixture 'enter_dev_lobby_with_popups' executed successfully")

@pytest.fixture
def enter_dev_lobby_without_popups(device_name, appium_driver: object) -> None:
    """
    Логин гостем на дев-окружение с отключенными попапами
    """
    logger.info("fixture 'enter_dev_lobby_without_popups' is running")
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
    device_name.EnvScreen.FTUE_ACTIVE.tap(appium_driver)
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
    time.sleep(25)
    logger.info("fixture 'enter_dev_lobby_without_popups' executed successfully")

def enter_prod_lobby_with_popups(device_name, appium_driver: object) -> None:
    """
    """
    pass

def enter_prod_lobby_without_popups(device_name, appium_driver: object) -> None:
    """
    """
    pass


def enter_prod_login_screen_with_popups(device_name, appium_driver: object) -> None:
    """
    """
    pass

def enter_prod_login_screen_without_popups(device_name, appium_driver: object) -> None:
    """
    """
    pass

def enter_with_facebook_login(device_name, appium_driver: object) -> None:
    pass

