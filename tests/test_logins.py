import asyncio
import pytest
from playwright.async_api import expect, Browser, Page

from torrenting_logins.sites import torrent_leech
from torrenting_logins.sites import the_geeks
from torrenting_logins.login import login


@pytest.mark.asyncio
async def test_tl(async_webkit):
    browser = await anext(async_webkit)
    page = await login({"webkit": browser}, torrent_leech)

    for category in ("Movies", "TV", "Games", "Apps", "Education"):
        expect(page.locator(f"//div[contains(text(), {category})]")).to_be_visible()


@pytest.mark.asyncio
async def test_needs_submit(async_chromium, async_firefox, async_webkit):
    page = await login(
        {
            "chromium": await anext(async_chromium),
            "firefox": await anext(async_firefox),
            "webkit": await anext(async_webkit),
        },
        the_geeks,
    )
    await asyncio.sleep(1000)
