from pathlib import Path

class MadoutAPK:
    APP_PATH_V16 = str(Path(__file__).parent.parent / "madout_apk" / "Android-versions_16_12_05_2025.apk")
    APP_PATH_MASTER = str(Path(__file__).parent.parent / "madout_apk" / "Android-master-bfbc65813d-1748440938.apk")

    """
    Попробовать создавать динамические пути через параметры
    Не срочно, но стоит задуматься
    """
    @classmethod
    def get_apk_path(cls, version):
        return {
            "v16": cls.APP_PATH_V16,
            "master": cls.APP_PATH_MASTER
        }.get(version)