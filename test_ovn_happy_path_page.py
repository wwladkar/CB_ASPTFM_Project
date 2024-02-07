from pages.login_page import LoginPage


def test_ovn_happy_path(browser):
    login_page = LoginPage(browser)
    login_page.login("VKarpushkin", "kbepY5uLy")

    assert browser.current_url == "http://cbdev-ez/#/"