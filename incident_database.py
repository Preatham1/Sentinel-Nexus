import json
from pathlib import Path
from datetime import datetime

DATABASE_FILE = Path("incidents.json")


def save_incident(
    filename,
    risk_level
):

    incidents = get_incidents()

    incidents.append(
        {
        "file": filename,
        "risk": risk_level,
        "date": datetime.now().strftime("%Y-%m-%d")
        }
    )

    with open(
        DATABASE_FILE,
        "w"
    ) as f:

        json.dump(
            incidents,
            f,
            indent=4
        )


def get_incidents():

    if not DATABASE_FILE.exists():

        return []

    with open(
        DATABASE_FILE,
        "r"
    ) as f:

        return json.load(f)