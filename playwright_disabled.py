from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(AppRoute.LOGIN)

    # Проверяем, что кнопка Login не активна
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()
