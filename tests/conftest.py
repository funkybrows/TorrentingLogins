from typing import Dict, Generator

import pytest
from playwright.async_api import async_playwright, Browser
from pytest_playwright.pytest_playwright import artifacts_folder


@pytest.fixture(scope="session")
async def async_chromium(
    browser_type_launch_args: Dict,
) -> Generator[Browser, None, None]:
    launch_options = {**browser_type_launch_args}
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(**launch_options)
        yield browser

        await browser.close()
    artifacts_folder.cleanup()


@pytest.fixture(scope="session")
async def async_webkit(
    browser_type_launch_args: Dict,
) -> Generator[Browser, None, None]:
    launch_options = {**browser_type_launch_args}
    async with async_playwright() as pw:
        browser = await pw.webkit.launch(**launch_options)
        yield browser

        await browser.close()
    artifacts_folder.cleanup()
