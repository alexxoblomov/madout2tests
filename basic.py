from conftest import appium_driver
from utils import compare_with_template, get_screenshot


def screen_is_match(template_path, threshold, appium_driver) -> None:
    is_found, match_value = compare_with_template(
        get_screenshot(appium_driver),
        template_path=template_path,
        threshold=threshold)

    assert is_found, (
        f"Экран не совпадает, процент совпадения: {match_value:.2f} (требуется порог ≥ {threshold})\n"
    )