# modules/ledger.py
import hashlib
import json
from datetime import datetime

def append_ledger(report_dict, ledger_file="reports/ledger.txt"):
    """
    Create a SHA-256 hash of the report (sorted keys), append to ledger with timestamp.
    Returns the hex digest.
    """
    payload = json.dumps(report_dict, sort_keys=True, default=str)
    h = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    timestamp = datetime.utcnow().isoformat() + "Z"
    line = json.dumps({"ts": timestamp, "hash": h, "report_id": report_dict.get("farmer_id", "NA")})
    with open(ledger_file, "a") as f:
        f.write(line + "\n")
    return h


