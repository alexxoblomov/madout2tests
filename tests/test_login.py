import time, pytest, logging
from basic import screen_is_match


logger = logging.getLogger(__name__)


class TestLoginDev:
    """
    Набор для запуска тестов на Dev окружении
    """
    def test_login_screen_state(self, device_name, device_templates, enter_dev_login_screen_without_popups, log_test_start_end, appium_driver):
        """
        1) Входим на экран логина в игру
        2) Проверяем его состояние
        """
        screen_is_match(device_templates.LoginTemplates.LOGIN_SCREEN, 0.90, appium_driver)


    @pytest.mark.skip
    def test_go_ftue(self, device_name, device_templates, enter_dev_login_screen_without_popups, log_test_start_end, appium_driver):
        """
        1) Входим в игру
        2) Проверяем, что оказались во FTUE
        """
        device_name.LoginScreen.GUEST_LOGIN_BUTTON.tap(appium_driver)
        time.sleep(30)
        device_name.LoginScreen.PROLOGUE_SKIP_CUTSCENE.tap(appium_driver)
        time.sleep(35)
        screen_is_match(device_templates.LoginTemplates.FTUE_START_SCREEN, 0.80, appium_driver)


class TestShopsProd:
    """
    Набор для запуска на Prod окружении
    """
    pass