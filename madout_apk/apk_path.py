from pathlib import Path

class MadoutAPK:
    APP_PATH_V17 = str(Path(__file__).parent.parent / "madout_apk" / "Android-versions_17-e7452e7ca7-1750852652.apk")
    APP_PATH_MASTER = str(Path(__file__).parent.parent / "madout_apk" / "Android-master-afaf633586-1749558929.apk")

    """
    Попробовать создавать динамические пути через параметры
    Не срочно, но стоит задуматься
    """
    @classmethod
    def get_apk_path(cls, version):
        return {
            "v17": cls.APP_PATH_V17,
            "master": cls.APP_PATH_MASTER
        }.get(version)