import configparser
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union

from playwright.async_api import Locator, Page

config = configparser.ConfigParser()
config.read(f"{Path(__file__).parent.parent.parent}/credentials.ini")


class SelectorType(Enum):
    XPATH = "xpath"


selector_types = {
    SelectorType.XPATH: lambda page, *args, **kwargs: page.locator(*args, **kwargs)
}


class SiteConfig:
    class SiteConfigMember:
        def get_field(self, page: Page) -> Locator:
            """
            Obtain Locator element using get_field params obtained on __init__.
            """
            return selector_types[self._selector_type](
                page, *(self._get_field_args or []), **(self._get_field_kwargs or {})
            )

        def __init__(
            self,
            selector_type: str,
            get_field_args: List[Any] = None,
            get_field_kwargs: Dict[str, Any] = None,
            **fields: Dict[str, Any],
        ):
            self._selector_type = SelectorType(selector_type)
            self._get_field_args = get_field_args
            self._get_field_kwargs = get_field_kwargs
            for key, value in fields.items():
                setattr(self, key, value)

    class User(SiteConfigMember):
        def __init__(
            self,
            username: str,
            selector_type: str,
            get_field_args: Iterable[Any] = None,
            get_field_kwargs: Dict[str, Any] = None,
        ):
            super().__init__(
                selector_type, get_field_args, get_field_kwargs, username=username
            )

    class Password(SiteConfigMember):
        def __init__(
            self,
            password: str,
            selector_type,
            get_field_args: Iterable[Any] = None,
            get_field_kwargs: Dict[str, Any] = None,
        ):
            super().__init__(
                selector_type, get_field_args, get_field_kwargs, password=password
            )

    def __init__(
        self,
        name,
        url,
        user_info: Dict[str, Union[str, Iterable[Any], Dict[str, Any]]],
        password_info: Dict[str, Union[str, Iterable[Any], Dict[str, Any]]],
        submit_info: Dict[str, Union[str, Iterable[Any], Dict[str, Any]]] = None,
        browser: str = "chromium",
    ):
        self.name = name
        self.url = url
        self.user = self.User(**user_info)
        self.password = self.Password(**password_info)
        self.submit = self.SiteConfigMember(**submit_info)
        self.browser = browser


aither = SiteConfig(
    "aither",
    "https://aither.cc",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='username']"],
        "username": config["aither"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='password']"],
        "password": config["aither"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//button[@type='submit']"],
    },
)

alpha_ratio = SiteConfig(
    "alpha-ratio",
    "https://alpharatio.cc",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='username']"],
        "username": config["alpha-ratio"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='password']"],
        "password": config["alpha-ratio"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@type='submit']"],
    },
)

cathode_ray_tube = SiteConfig(
    "cathode-ray-tube",
    "https://cathode-ray.tube/login",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='username']"],
        "username": config["cathode-ray-tube"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='password']"],
        "password": config["cathode-ray-tube"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@type='submit']"],
    },
)

file_list = SiteConfig(
    "file-list",
    "https://filelist.io",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='username']"],
        "username": config["file-list"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='password']"],
        "password": config["file-list"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@type='submit']"],
    },
)

hd_torrents = SiteConfig(
    "hd-torrents",
    "https://hd-torrents.org",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='uid']"],
        "username": config["hd-torrents"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='pwd']"],
        "password": config["hd-torrents"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@type='submit']"],
    },
)

hd_space = SiteConfig(
    "hd-space",
    "https://hd-space.org",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@id='want_username1']"],
        "username": config["hd-space"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@id='want_password1']"],
        "password": config["hd-space"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@type='submit']"],
    },
    browser="firefox",
)

torrent_leech = SiteConfig(
    "torrent-leech",
    "https://torrentleech.org",
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='username']"],
        "username": config["torrent-leech"]["username"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//input[@name='password']"],
        "password": config["torrent-leech"]["password"],
    },
    {
        "selector_type": "xpath",
        "get_field_args": ["//button[@type='submit']"],
    },
    browser="webkit",
)
