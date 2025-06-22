"""
main.py
---------
This script serves as the test suite entry point for running all automated test cases in the framework.
"""

import pytest
import sys
from utils.logger import Logger

# Initialize logger
log = Logger.get_logger(__name__)

if __name__ == "__main__":
    log.info("Starting automation test suite...")

    # Run all test cases inside the 'tests' folder with verbose output
    run_result = pytest.main([
        "tests/",
        "-v",                # Verbose output for detailed test steps
        "--tb=short",        # Shorter error tracebacks
        # "--html=reports/report.html",       # Optional: Enable for HTML reporting
        # "--self-contained-html"             # Optional: Embed all assets into the report
    ])

    if run_result == 0:
        log.info("All tests passed successfully.")
    else:
        log.warning(f"Some tests failed. Exit code: {run_result}")

    sys.exit(run_result)
