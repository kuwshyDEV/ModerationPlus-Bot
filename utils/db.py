import json
import os
from pathlib import Path

class CaseDB:
    """JSON database for case management."""
    def __init__(self, file: str="../database/cases.json"):
        self.file = Path(file)
        self.cases = self._load()

    def _load(self) -> dict:
        """Load cases from JSON or init empty."""
        if not self.file.exists():
            return {"cases": [], "next_id": 1}
        try:
            with self.file.open("r") as f:
                return json.load(f)
        except Exception as e:
            print(f"DB load error: {e}")
            return {"cases": [], "next_id": 1}

    def _save(self):
        """Save cases to JSON."""
        try:
            with self.file.open("w") as f:
                json.dump(self.cases, f, indent=2)
        except Exception as e:
            print(f"DB save error: {e}")

    def add_case(self, mod_id: int, tgt_id: int, c_type: str, reason: str, files: list[str]) -> str:
        """Add case, return ID."""
        case_id = str(self.cases["next_id"])
        self.cases["cases"].append({
            "id": case_id,
            "mod_id": mod_id,
            "tgt_id": tgt_id,
            "type": c_type,
            "reason": reason,
            "files": files
        })
        self.cases["next_id"] += 1
        self._save()
        return case_id

    def get_case(self, case_id: str) -> dict | None:
        """Retrieve case by ID."""
        for case in self.cases["cases"]:
            if case["id"] == case_id:
                return case
        return None