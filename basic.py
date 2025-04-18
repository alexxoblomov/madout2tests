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