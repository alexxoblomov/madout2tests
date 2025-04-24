import inspect, os, cv2
from datetime import datetime
from typing import Optional, Tuple


def get_screenshot(driver, filename: Optional[str] = None, save_dir: str = "screenshots") -> str:
    os.makedirs(save_dir, exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = None
        stack = inspect.stack()

        for frame in stack:
            if frame.function.startswith("test_"):
                test_name = frame.function
                break

        if test_name:
            filename = f"{test_name}_{timestamp}.png"
        else:
            filename = f"screenshot_{timestamp}.png"

    filepath = os.path.join(save_dir, filename)

    screenshot = driver.get_screenshot_as_png()
    with open(filepath, "wb") as file:
        file.write(screenshot)

    os.path.abspath(filepath)
    return os.path.abspath(filepath)


def compare_with_template(screenshot_path: str, template_path: str, threshold: float = 0.8) -> Tuple[bool, float]:
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_COLOR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    if screenshot is None or template is None:
        raise FileNotFoundError("Не удалось загрузить изображения")

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    return max_val >= threshold, max_val