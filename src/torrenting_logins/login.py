import asyncio
from typing import List, Dict
from playwright.async_api import Browser, Page

from torrenting_logins.sites import SiteConfig


async def login(browsers: Dict[str, Browser], site_config: List[SiteConfig]) -> Page:
    page = await browsers[site_config.browser].new_page()
    await page.goto(site_config.url)
    await site_config.user.get_field(page).type(site_config.user.username)
    await site_config.password.get_field(page).type(site_config.password.password)
    if site_config.captcha:
        print(
            f"Click enter once you complete the user required parts of login for {site_config.name}"
        )
        input()
    if site_config.submit:
        await site_config.submit.get_field(page).click()
    return page


async def login_multi(browsers: Dict[str, Browser], sites: List[SiteConfig]):
    for site in sites:
        asyncio.create_task(login(browsers, site))
