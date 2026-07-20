import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.logger import logger


@pytest.mark.usefixtures('setup')
class Page01:

    radio_button = (By.NAME,"radioButton")
    text_box =(By.ID,"autocomplete")
    dropdown_button = (By.ID,"dropdown-class-example")
    select_multi_items = (By.ID,"multiSelect")
    male_label = (By.CSS_SELECTOR, "label[for='male']")
    female_label = (By.CSS_SELECTOR, "label[for='female']")
    switch_window = (By.ID, "openwindow")
    switch_tab1 = (By.ID,"opentab1")
    switch_tab2 = (By.ID, "opentab2")
    simple_alert = (By.ID, "simpleAlert")
    confirm_alert = (By.ID, "confirmAlert")
    prompt_alert = (By.ID, "promptAlert")
    date_picker = (By.ID, "datePicker")
    time_picker = (By.ID, "timePicker")
    submit_btn = (By.XPATH,"//button[@id='dateTimeBtn']")
    sec_wait_btn = (By.XPATH, "//button[@id='showTextBtn1']")
    random_wait_btn = (By.XPATH, "//button[@id='RandomWaitBtn']")
    mouse_hover = (By.ID, "mousehover")
    draggable = (By.ID, "draggable")
    droppable = (By.ID, "droppable")
    double_click = (By.ID, "doubleClickBox")
    right_click = (By.ID, "rightClickBox")
    click_hold= (By.ID, "clickHoldBox")
    iframe_example = (By.ID, "iframeExample")
    get_started_btn = (By.XPATH, "//button[text()='Get Started']")
    web_table_rows = (By.XPATH, "//table[@id='webTable']//tr")
    total_amount_text = (By.XPATH, "//b[contains(text(),'Total Amount')]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def test_verify_title(self):
        actual_title = self.driver.title
        expected_title = "Practice Page"
        logger.info(f"Verifying title: {actual_title}")
        assert actual_title == expected_title
        logger.info("Title verification passed")


    def test_radio_button(self):
        radios = self.driver.find_elements(*self.radio_button)
        radios[0].click()
        radios[1].click()
        radios[2].click()

    def test_text_box(self):
        text_box = self.driver.find_element(*self.text_box)
        text_box.click()
        text_box.clear()
        text_box.send_keys("Urvi Goel")

    def test_dropdown_button(self):
        dropdown = Select(self.driver.find_element(*self.dropdown_button))
        dropdown.select_by_visible_text("Option1")
        dropdown.select_by_visible_text("Option2")
        dropdown.select_by_visible_text("Option3")

    def test_select_items(self):
        items = Select(self.driver.find_element(*self.select_multi_items))
        items.select_by_index(0)
        items.select_by_index(1)
        items.select_by_index(2)
        items.select_by_index(3)
        items.select_by_index(4)

    def test_toggle_switch(self):
        self.driver.find_element(*self.male_label).click()
        self.driver.find_element(*self.female_label).click()

    def test_switch_window(self):
        open_window = self.driver.find_element(By.ID, "openwindow")
        open_window.click()
        time.sleep(2)
        self.wait.until(EC.number_of_windows_to_be(2))
        print(f"driver title : {self.driver.title}")
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])
        print(f"driver title : {self.driver.title}")

        print(self.driver.find_element(By.CLASS_NAME, "text-white").text)

        self.driver.switch_to.window(self.driver.window_handles[0])
        print(f"driver title : {self.driver.title}")
        time.sleep(2)

    def test_switch_tab(self):
        pass

    def test_switch_to_alert(self):
        self.wait.until(EC.visibility_of_element_located(self.prompt_alert)).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys("test input")
        alert.accept()
        # Agar dusra alert aata hai
        alert = self.wait.until(EC.alert_is_present())
        print(alert.text)
        alert.accept()

        self.wait.until(EC.visibility_of_element_located(self.simple_alert)).click()
        alert = self.wait.until(EC.alert_is_present())
        print("Alert text:", alert.text)
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        self.wait.until(EC.visibility_of_element_located(self.confirm_alert)).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()  # OK click
        time.sleep(5)

        alert = self.wait.until(EC.alert_is_present())
        print(alert.text)
        alert.accept()
        time.sleep(5)

    def test_calendar_and_time_picker(self):
        date = self.wait.until(EC.visibility_of_element_located(self.date_picker))
        date.click()
        date.send_keys("20/07/2008")
        print("Date :", date.get_attribute("value"))

        time_pick = self.wait.until(EC.visibility_of_element_located(self.time_picker))
        time_pick.click()
        time_pick.send_keys("11:11 AM")
        time.sleep(5)
        print("Time :", time_pick.get_attribute("value"))

        self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.sec_wait_btn)).click()

        time.sleep(6)
        self.wait.until(EC.text_to_be_present_in_element(
            (By.ID, "delayedText"),
            "This text appears after a delay of 5 secs!"))
        element = self.driver.find_element(By.ID, "delayedText")
        self.driver.save_screenshot("Screenshots/delay_btn_clicked.png")
        print(element.text)
        assert element.text == "This text appears after a delay of 5 secs!"

    def test_random_wait(self):
        self.wait.until(EC.element_to_be_clickable(self.random_wait_btn)).click()
        time.sleep(10)
        self.wait.until(EC.text_to_be_present_in_element(
            (By.ID, "level1Text"),
            "Text with random delay"))
        element = self.driver.find_element(By.ID, "level1Text")
        self.driver.save_screenshot("Screenshots/random_wait_btn_clicked.png")
        print(element.text)
        assert "Text with random delay" in element.text

    def test_mouse_hover(self):
        pass

    def test_drag_and_drop(self):
        source = self.driver.find_element(*self.draggable)
        target = self.driver.find_element(*self.droppable)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(alert.text)  # "Dropped successfully!"
            alert.accept()
            print("Drag and drop successful")
        except TimeoutException:
            print("Alert did not appear after drag and drop")

    def test_double_click(self):
        element = self.driver.find_element(*self.double_click)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
            print("Double click successful")
        except TimeoutException:
            print("No alert appeared after double click")

    def test_right_click(self):
        element = self.driver.find_element(*self.right_click)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
            print("Right click successful")
        except TimeoutException:
            print("No alert appeared after right click")

    def test_click_hold(self):
        element = self.driver.find_element(*self.click_hold)
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).perform()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
            print("Click and hold successful")
        except TimeoutException:
            print("No alert appeared after click and hold")

    def test_iframe_example(self):
        iframe = self.driver.find_element(*self.iframe_example)
        self.driver.switch_to.frame(iframe)

        element = self.driver.find_element(*self.get_started_btn)
        element.click()

        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(alert.text)
            alert.accept()
            print("iFrame click successful")
        except TimeoutException:
            print("No alert appeared after clicking Get Started")

        self.driver.switch_to.default_content()

    def test_web_table_amount(self):
        rows = self.driver.find_elements(*self.web_table_rows)

        total = 0
        for row in rows[1:]:  # skip header
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols and len(cols) == 4:
                amount_text = cols[3].text.replace("$", "").strip()
                total += int(amount_text)

        print(f"Calculated total: ${total}")

        displayed_total = self.driver.find_element(*self.total_amount_text).text
        print(f"Displayed total: {displayed_total}")

        assert str(total) in displayed_total


































