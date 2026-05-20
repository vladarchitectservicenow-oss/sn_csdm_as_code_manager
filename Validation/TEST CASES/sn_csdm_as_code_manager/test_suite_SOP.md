# Test Suite SOP: sn_csdm_as_code_manager
Author: Vladimir Kapustin | License: AGPL-3.0

## Scenarios (10+)
1. **test_plugin_active** — verify required plugins loaded
2. **test_role_assigned** — verify role provisioning
3. **test_config_load** — configuration from properties
4. **test_rest_api** — endpoint availability
5. **test_report_generate** — report output format
6. **test_empty_data** — handle empty tables gracefully
7. **test_error_recovery** — API failure resilience
8. **test_performance_50concurrent** — load test
9. **test_auth_failure** — unauthorized access blocked
10. **test_delta_scan** — incremental execution
11. **test_boundary_maxrecords** — 50k record limit
12. **test_timeout_handling** — graceful timeout

## Priority
- P0: 1-4 (core functionality)
- P1: 5-8 (robustness)
- P2: 9-12 (edge cases)

## Execution
Run: `pytest tests/ -v`
Expected: 10/10 PASS minimum
