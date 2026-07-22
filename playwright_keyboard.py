from playwright.sync_api import sync_playwright

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(AppRoute.LOGIN)

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in settings.test_user.email:
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")

    # Ждём 5 секунд для наглядности результата
    page.wait_for_timeout(5000)
