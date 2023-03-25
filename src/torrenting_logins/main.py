import asyncio
from typing import List
from playwright.async_api import async_playwright
from torrenting_logins.login import login_multi
from torrenting_logins.sites import (
    aither,
    alpha_ratio,
    animez,
    anthelion,
    ab_torrents,
    bit_sexy,
    cathode_ray_tube,
    file_list,
    the_geeks,
    hd_torrents,
    hd_space,
    learn_flakes,
    lst,
    my_anonamouse,
    old_toons_world,
    orpheus,
    reel_flix,
    sports_cult,
    torrent_leech,
)

default_timeout = 10**10


async def tv_movie(browsers):
    group = (
        aither,
        alpha_ratio,
        animez,
        anthelion,
        cathode_ray_tube,
        file_list,
        hd_torrents,
        hd_space,
        lst,
        reel_flix,
        torrent_leech,
    )
    asyncio.create_task(login_multi(browsers, group))
    asyncio.create_task(login_multi(browsers, (old_toons_world,)))


async def edu(browsers):
    print("CONFIRM YOU ARENT ON VPN")
    input()

    group = (learn_flakes, file_list, the_geeks, torrent_leech)
    asyncio.create_task(login_multi(browsers, group))


async def books(browsers):
    print("CONFIRM YOU ARENT ON VPN")
    input()

    group = (ab_torrents, my_anonamouse)
    asyncio.create_task(login_multi(browsers, group))


async def sports(browsers):
    group = (sports_cult,)
    asyncio.create_task(login_multi(browsers, group))


async def pn(browsers):
    group = (bit_sexy,)
    asyncio.create_task(login_multi(browsers, group))


async def music(browsers):
    group = (orpheus,)
    asyncio.create_task(login_multi(browsers, group))


async def main(timeout=default_timeout):
    browser_contexts = {}
    launch_options = {"headless": False}

    async with async_playwright() as pw:
        for browser_type in ("chromium", "firefox", "webkit"):
            browser = await getattr(pw, browser_type).launch(
                **launch_options, downloads_path="./downloads"
            )
            context = await browser.new_context(no_viewport=True)
            browser_contexts[browser_type] = context
        # asyncio.create_task(music(browser_contexts))
        # asyncio.create_task(pn(browser_contexts))
        # asyncio.create_task(sports(browser_contexts))
        asyncio.create_task(tv_movie(browser_contexts))
        # asyncio.create_task(books(browser_contexts))
        # asyncio.create_task(edu(browser_contexts))
        await asyncio.sleep(timeout)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        asyncio.gather(main(timeout=default_timeout))
    )
