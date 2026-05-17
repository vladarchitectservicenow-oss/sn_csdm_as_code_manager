#!/usr/bin/env python3
"""
$name
Copyright (C) 2026  Vladimir Kapustin
License: AGPL-3.0
"""
import json, requests
from typing import List, Dict

class Engine:
    def __init__(self, sn_url: str, sn_user: str, sn_pass: str):
        self.sn_url = sn_url.rstrip("/")
        self.sn_auth = (sn_user, sn_pass)

    def fetch(self, table: str, limit=100) -> List[Dict]:
        url = f"{self.sn_url}/api/now/table/{table}"
        try:
            r = requests.get(url, params={"sysparm_limit": limit}, auth=self.sn_auth, headers={"Accept":"application/json"}, timeout=30)
            r.raise_for_status()
            return r.json().get("result", [])
        except Exception:
            return []

    def process(self, records: List[Dict]) -> Dict:
        return {"total": len(records), "items": records[:50]}

    def report(self, data: Dict, prefix: str):
        with open(f"{prefix}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        lines = [f"# ServiceNow Report", f"**Total:** {data['total']}", "", "## Items"]
        for i in data.get("items", []):
            lines.append(f"- {i.get('name', i.get('sys_id',''))}")
        open(f"{prefix}.md", "w", encoding="utf-8").write("\n".join(lines))
        return data

    def run(self, table: str, prefix: str):
        recs = self.fetch(table); data = self.process(recs); return self.report(data, prefix)
