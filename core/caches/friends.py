"""
MIT License

Copyright (c) 2020 MyerFire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time

from tinydb import Query, where

import core.caches.static


async def find_friends_data(uuid):
    result = core.caches.static.friends_cache_db_cache.search(where("uuid") == uuid)
    if result:
        return result[0]
    else:
        return None


async def save_friends_data(uuid, friends):
    Friends = Query()
    if core.caches.static.friends_cache_db_cache.search(where("uuid") == uuid):
        core.caches.static.friends_cache_db_cache.update({"time": time.time(), "friends": friends},
                                                         Friends.uuid == uuid)
    elif core.caches.static.friends_cache_db_cache.search(where("friends") == friends):
        core.caches.static.friends_cache_db_cache.remove(Friends.friends == friends)
        core.caches.static.friends_cache_db_cache.insert({"uuid": uuid, "time": time.time(), "friends": friends})
    else:
        core.caches.static.friends_cache_db_cache.insert({"uuid": uuid, "time": time.time(), "friends": friends})
