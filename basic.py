from utils import compare_with_template, get_screenshot
import logging


logger = logging.getLogger(__name__)


def screen_is_match(template_path, threshold, appium_driver) -> None:
    try:
        logger.info(f"Checking screen match for template: {template_path} with threshold: {threshold}")

        is_found, match_value = compare_with_template(
            get_screenshot(appium_driver),
            template_path=template_path,
            threshold=threshold)

        if is_found:
            logger.info(f"Screen matched successfully. Match value: {match_value:.2f} (threshold: {threshold})")
        else:
            logger.warning(f"Screen does not match. Match value: {match_value:.2f} (required: ≥ {threshold})")
            raise AssertionError(
                f"Screen does not match. Match value: {match_value:.2f} (required: ≥ {threshold})"
            )

    except Exception as e:
        logger.critical(f"Screen matching failed: {str(e)}", exc_info=True)
        raise