from pages.login_page import LoginPage

# link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" ссылка которую проверяем

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()