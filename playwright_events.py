from playwright.sync_api import sync_playwright, Request, Response

from tools.routes import AppRoute


# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")


# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    # Открываем браузер и создаём новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    page.on("response", log_response)  # Ответ получен

    # Переходим на страницу входа
    page.goto(AppRoute.LOGIN)

    # Задержка для завершения всех запросов
    page.wait_for_timeout(3000)
