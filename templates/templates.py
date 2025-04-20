from pathlib import Path


class Templates:
    BASE_DIR = Path(__file__).parent.parent
    TEMPLATES_DIR = BASE_DIR / "templates"

    # clans
    CLAN_ENTRY = TEMPLATES_DIR / "clans" / "clan_entry.png"
    QUICK_JOIN = TEMPLATES_DIR / "clans" / "quick_join.png"
    CLAN_META = TEMPLATES_DIR / "clans" / "clan_meta.png"