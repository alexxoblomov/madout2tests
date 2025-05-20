from buttons import PocoX6
from madout_apk.apk_path import MadOutV16


DEVICES = {
    "poco_x6": {
        "platform_name": "Android",
        "device_name": "PZW8WWFE49ZXLJDI",
        "platform_version": "14.0",
        "app": MadOutV16.APP_PATH,
        "automation_name": "UiAutomator2",
        "no_reset": False,
    }
}

def get_device_class(device_name):
    devices = {
        "poco_x6": PocoX6
    }
    return devices.get(device_name.lower())



