import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindows:

    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title('Check the ability to open new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'New tab has not opened'

        @allure.title('Check the ability to open new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', 'New window has not opened'

    @allure.feature('Alerts')
    class TestAlerts:

        @allure.title('Check alert button')
        def test_alert_button(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_button()
            assert alert_text == 'You clicked a button', 'Alert has not appeared'

        @allure.title('Check 5 sec alert button')
        def test_alert_5_sec_button(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert has not appeared in 5 ces'

        @allure.title('Check confirm alert')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'Confirm box has not appeared'

        @allure.title('Check prompt alert')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_box()
            assert text in alert_text, 'Prompt box has not appeared'

    @allure.feature('Frames')
    class TestFrames:

        @allure.title('Check frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'First frame did not appeared'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'Second frame did not appeared'

    @allure.feature('Nested Frames')
    class TestNestedFrames:

        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Parent frame has not appeared'
            assert child_text == 'Child Iframe', 'Child Iframe has not appeared'

    @allure.feature('Modal Dialogs')
    class TestModalDialogs:

        @allure.title('Check modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[0] == 'Small Modal', 'The header is not "Small modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large modal"'
            assert small[1] < large[1], 'Text from large dialog is less then text from small dialog'
