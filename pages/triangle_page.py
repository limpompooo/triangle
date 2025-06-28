from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrianglePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_triangle_sides(self, a, b, c):
        a_input = self.driver.find_element(By.CLASS_NAME, "js_a")
        b_input = self.driver.find_element(By.CLASS_NAME, "js_b")
        c_input = self.driver.find_element(By.CLASS_NAME, "js_c")
        a_input.clear()
        b_input.clear()
        c_input.clear()
        a_input.send_keys(a)
        b_input.send_keys(b)
        c_input.send_keys(c)

    def submit(self):
        btn = self.driver.find_element(By.CLASS_NAME, "btn-submit")
        btn.click()

    def get_result(self):
        # Лучше подождать появления текста, чтобы не ловить пустое значение
        wait = WebDriverWait(self.driver, 6)
        wait.until(lambda d: d.find_element(By.CLASS_NAME, "info").text.strip() != "")
        return self.driver.find_element(By.CLASS_NAME, "info").text.strip()