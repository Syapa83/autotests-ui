import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    # Открываем браузер с использованием Playwright
    with sync_playwright() as playwright:

        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка заголовка "Courses"
        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()
        expect(courses_header).to_have_text("Courses")

        # Проверка наличия и текста блока "There is no results"
        no_results_header = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_header).to_be_visible()
        expect(no_results_header).to_have_text("There is no results")

        # Проверка наличия и видимости иконки пустого блока
        empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        # Проверка наличия и текста описания блока
        description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")
