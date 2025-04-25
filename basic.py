from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import appium_driver
from utils import compare_with_template, get_screenshot


def element_is_present(template_path, threshold, appium_driver) -> None:
    is_found, match_value = compare_with_template(
        get_screenshot(appium_driver),
        template_path=template_path,
        threshold=threshold)

    assert is_found, (
        # поменять на NoElementFoundException
        f"Элемент не найден на экране! Уровень совпадения: {match_value:.2f} (требуется ≥ 0.90)\n"
    )

def element_is_not_present(template_path, threshold, appium_driver) -> None:
    is_found, match_value = compare_with_template(
        get_screenshot(appium_driver),
        template_path=template_path,
        threshold=threshold)

    assert not is_found, (
        f"Элемент найден на экране, хотя не должен был быть! Уровень совпадения: {match_value:.2f} (требуется < {threshold})\n"
    )

def check_element_by_xpath(appium_driver, xpath, timeout=10):
    try:
        element = WebDriverWait(appium_driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        if not element.is_displayed():
            return False
        return True

    except NoSuchElementException:
        print(f"Элемент не найден (NoSuchElementException): {xpath}")
        return False