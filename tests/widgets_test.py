import time

import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite('Interactions')
class TestWidgets:

    @allure.feature('Accordian Page')
    class TestAccordianPage:

        @allure.title('Check accordian')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    @allure.feature('Auto Complete Page')
    class TestAutoCompletePage:

        @allure.title('Check fill multi autocomplet')
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'the added colors are missing in the input'

        @allure.title('Check remove value from multi')
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'value was not deleted'

        @allure.title('Check filling single autocomplete')
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'the added colors are missing in the input'

    @allure.feature('Date Picker Page')
    class TestDatePickerPage:

        @allure.title('Check change date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'the date has not been changed'

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'the date and time has not been changed'

    @allure.feature('Slide Page')
    class TestSliderPage:

        @allure.title('Check slider')
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.check_slider()
            assert before != after, 'the slider value has not changed'

    @allure.feature('Progress Bar')
    class TestProgressBarPage:

        @allure.title('Check progress bar')
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.check_progress_bar()
            assert before != after, 'the progress_bar value has not changed'

    @allure.feature('Tabs Page')
    class TestTabsPage:

        @allure.title('Check tabs')
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_title, what_content = tabs.check_tabs('what')
            origin_title, origin_content = tabs.check_tabs('origin')
            use_title, use_content = tabs.check_tabs('use')
            assert what_title == 'What' and what_content > 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_title == 'Origin' and origin_content > 0, 'the tab "origin" was not pressed or the text is ' \
                                                                    'missing '
            assert use_title == 'Use' and use_content > 0, 'the tab "use" was not pressed or the text is missing'

    @allure.feature('Tool Tips Page')
    class TestToolTipsPage:

        @allure.title('Check tool tips')
        def test_tool_tips(self, driver):
            tool_tips = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips.open()
            button_text, field_text, contrary_link_text, section_link_text = tool_tips.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
            assert contrary_link_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert section_link_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'

    @allure.feature('Menu Page')
    class TestMenuPage:

        @allure.title('Check menu')
        def test_menu(self, driver):
            menu = MenuPage(driver, 'https://demoqa.com/menu')
            menu.open()
            data = menu.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'menu items do not exist or have not been selected '

#  class SelectMenuPage:
#     def test_select_menu(self, driver):
#        select_menu = SelectMenuPage(driver, "https://demoqa.com/select-menu")
#    select_menu.open()
#   p = select_menu.check_select_menu()
