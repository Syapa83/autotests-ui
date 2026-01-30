from playwright.sync_api import Page, expect
from dataclasses import dataclass

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent

@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Карточка курса
        self.course_view = CourseViewComponent(page)

        # Меню курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

        # Пустой блок при отсутствии курсов
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
