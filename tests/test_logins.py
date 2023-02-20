import asyncio
import pytest
from playwright.async_api import expect, Browser, Page

from torrenting_logins.sites import torrent_leech
from torrenting_logins.login import login


@pytest.mark.asyncio
async def test_tl(async_webkit):
    browser = await anext(async_webkit)
    page = await login({"webkit": browser}, torrent_leech)

    for category in ("Movies", "TV", "Games", "Apps", "Education"):
        expect(page.locator(f"//div[contains(text(), {category})]")).to_be_visible()
