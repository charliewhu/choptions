from contextlib import contextmanager
import time
import pytest
from playwright.sync_api import Page
import requests


APP_URL = "http://localhost:8501"


@pytest.fixture(scope="module", autouse=True)
def before_module():
    # Run the streamlit app before each module
    with run_app():
        yield


@pytest.fixture(scope="function", autouse=True)
def before_test(page: Page):
    page.goto(APP_URL)


def wait_for_app_to_come_up():
    """Give the app URL 10 seconds to come up"""
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return requests.get(APP_URL)
        except requests.exceptions.ConnectionError:
            print("\nConnection Error. Sleeping...")
            time.sleep(0.1)
    pytest.fail("API never came up")


@contextmanager
def run_app():
    """Run the Streamlit app"""
    import subprocess

    p = subprocess.Popen(
        [
            "streamlit",
            "run",
            "src/options/app.py",
        ]
    )

    try:
        wait_for_app_to_come_up()
        yield 1
    finally:
        p.kill()
