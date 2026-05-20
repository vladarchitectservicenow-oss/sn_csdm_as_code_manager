# Edge Cases: sn_csdm_as_code_manager

1. **Empty table** — zero records in scope
2. **50k+ records** — maximum batch size exceeded
3. **Null values** — missing config properties
4. **Missing plugin** — dependency not activated
5. **Timeout** — scan exceeds threshold
6. **Special chars** — unicode in field names
7. **Concurrent scans** — race condition prevention
