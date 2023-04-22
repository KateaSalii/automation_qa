from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id='messageWindowButton']")

    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')
