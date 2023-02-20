import pytest
from playwright.async_api import expect

from torrenting_logins.sites import ab_torrents, old_toons_world, torrent_leech
from torrenting_logins.login import login


@pytest.mark.asyncio
async def test_tl(async_webkit):
    browser = await anext(async_webkit)
    page = await login({"webkit": browser}, torrent_leech)

    for category in ("movies", "tv", "games", "apps", "education"):
        await expect(
            page.locator(f"xpath=//a[contains(@href, 'torrents/{category}')]")
        ).to_be_visible(timeout=1000 * 5, visible=False)


@pytest.mark.asyncio
async def test_has_captcha(async_chromium, async_firefox, async_webkit):
    page = await login(
        {
            "chromium": await anext(async_chromium),
            "firefox": await anext(async_firefox),
            "webkit": await anext(async_webkit),
        },
        old_toons_world,
    )
    for info in ("Ratio", "Uploaded", "Downloaded"):
        await expect(page.locator(f"//font[contains(text(), {info})]")).to_be_visible(
            timeout=5, visible=False
        )


    page = await login(
        {
            "chromium": await anext(async_chromium),
            "firefox": await anext(async_firefox),
            "webkit": await anext(async_webkit),
        },
        the_geeks,
    )
    await asyncio.sleep(1000)
