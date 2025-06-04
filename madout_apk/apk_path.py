from pathlib import Path

class MadoutAPK:
    APP_PATH_V16 = str(Path(__file__).parent.parent / "madout_apk" / "Android-versions_16-fecbec7989-1748936515.apk")
    APP_PATH_MASTER = str(Path(__file__).parent.parent / "madout_apk" / "Android-master-7a480dab54-1749030586.apk")

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