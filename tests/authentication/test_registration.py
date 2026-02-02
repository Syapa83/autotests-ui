import allure
import pytest
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
class TestRegistration:

    @allure.title("Registration with correct email, username and password")
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user@gmail.com', username='username', password='password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.dashboard_title.check_visible()
