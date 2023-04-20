from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id='messageWindowButton']")

    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
