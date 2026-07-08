import os
import requests


def build_greeting(name):
    return "Hello, " + name + "!"


def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")