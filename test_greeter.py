from greeter import build_greeting, is_valid_url


def test_build_greeting():
    assert build_greeting("World") == "Hello, World!"


def test_is_valid_url():
    assert is_valid_url("https://example.com") is True
    assert is_valid_url("not-a-url") is False