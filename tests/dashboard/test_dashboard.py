import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
