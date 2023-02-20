from typing import List, Dict
from playwright.async_api import Browser, Page

from torrenting_logins.sites import SiteConfig


async def login(browsers: Dict[str, Browser], site_config: List[SiteConfig]) -> Page:
    page = await browsers[site_config.browser].new_page()
    await page.goto(site_config.url)
    await site_config.user.get_field(page).type(site_config.user.username)
    await site_config.password.get_field(page).type(site_config.password.password)
    await site_config.submit.get_field(page).click()
    return page
