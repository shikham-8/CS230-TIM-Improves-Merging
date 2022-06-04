####################
# This code is from HTTPie, an open source HTTP client
# It is being used for the purposes of testing crosshair tools
# on real world examples, and evaluating its efficacy
# This example focuses on dictionaries and custom types
#####################
from inspect import _void
from math import floor, sqrt, log10
import os
import base64
import json
import mimetypes
import re
import sys
import time
import tempfile
import sysconfig

from collections import OrderedDict
from contextlib import contextmanager
from http.cookiejar import parse_ns_headers
from pathlib import Path
from pprint import pformat
from types import FunctionType
from urllib.parse import urlsplit
from typing import Any, Dict, List, Optional, Tuple, Generator, Callable, Iterable, IO, TypeVar, Mapping


RE_COOKIE_SPLIT = re.compile(r', (?=[^ ;]+=)')
Item = Tuple[str, Any]
Items = List[Item]
T = TypeVar("T")

###### added dictionary type below -- need this for crosshair to succeed ######


class dictionary:
    x: int
    y: int


def dictionary_test(d: dictionary) -> int:
    if (1 in d.keys):
        return 1
    elif (2 in d.keys):
        return 2
    else:
        return 3


# HTTPie real-world example for dictionaries
def split_cookies(cookies):
    """
    When ``requests`` stores cookies in ``response.headers['Set-Cookie']``
    it concatenates all of them through ``, ``.
    This function splits cookies apart being careful to not to
    split on ``, `` which may be part of cookie value.
    """
    if not cookies:
        return []
    return RE_COOKIE_SPLIT.split(cookies)


def get_expired_cookies(
    cookies: str,
    now: float = None
) -> List[dict]:

    now = now or time.time()

    def is_expired(expires: Optional[float]) -> bool:
        return expires is not None and expires <= now

    attr_sets: List[Tuple[str, str]] = parse_ns_headers(
        split_cookies(cookies)
    )

    cookies = [
        # The first attr name is the cookie name.
        dict(attrs[1:], name=attrs[0][0])
        for attrs in attr_sets
    ]

    _max_age_to_expires(cookies=cookies, now=now)

    return [
        {
            'name': cookie['name'],
            'path': cookie.get('path', '/')
        }
        for cookie in cookies
        if is_expired(expires=cookie.get('expires'))
    ]


def _max_age_to_expires(cookies: dict, now: float) -> _void:
    """
    Translate `max-age` into `expires` for Requests to take it into account.
    HACK/FIXME: <https://github.com/psf/requests/issues/5743>
    """
    for cookie in cookies:
        if 'expires' in cookie:
            continue
        max_age = cookie.get('max-age')
        if max_age and max_age.isdigit():
            cookie['expires'] = now + float(max_age)

# run: crosshair cover dictionary.<functionName>
