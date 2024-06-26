from pages.base_page import BasePage
from pages.locators import StartPageLocators


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BasePage.alpha_url

    def open_browser(self):
        self.open(self.url)

    def click_person_button(self):
        self.click_element(StartPageLocators.PERSON_BUTTON)

    def hover_person_button(self):
        self.hover_element(StartPageLocators.PERSON_BUTTON)

    def get_tooltip_text_person_button(self):
        self.get_tooltip_text(StartPageLocators.PERSON_BUTTON)

    def click_s_m_business_button(self):
        self.click_element(StartPageLocators.S_M_BUSINESS_BUTTON)

    def click_for_corporations_button(self):
        self.click_element(StartPageLocators.FOR_CORPORATIONS_BUTTON)

    def click_for_financial_button(self):
        self.click_element(StartPageLocators.FOR_FINANCIAL_BUTTON)

    def click_more_button(self):
        self.click_element(StartPageLocators.MORE_BUTTON)

    def click_alpha_club_button(self):
        self.hover_and_click_element(StartPageLocators.ALPHA_CLUB_BUTTON)
