from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckboxTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.edge_service = EdgeService(executable_path=r"C:\msedgedriver.exe")
        cls.driver = webdriver.Edge(service=cls.edge_service)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def get_checkboxes(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.form-check-input')

    def test_toggle_select_all(self):
        self.driver.get(f"{self.live_server_url}/tasks/checkbox/")
        
        # Initial state - all unchecked
        checkboxes = self.get_checkboxes()
        self.assertFalse(any(cb.is_selected() for cb in checkboxes))

        # First click - select all
        toggle_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="toggle_all"]'))
        )
        toggle_btn.click()
        
        # Verify all selected
        checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.form-check-input'))
        )
        self.assertTrue(all(cb.is_selected() for cb in checkboxes))

        # Second click - deselect all
        toggle_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="toggle_all"]'))
        )
        toggle_btn.click()
        
        # Verify all deselected
        checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.form-check-input'))
        )
        self.assertFalse(any(cb.is_selected() for cb in checkboxes))

    def test_select_all_except_one(self):
        self.driver.get(f"{self.live_server_url}/tasks/checkbox/")
        
        # Click "Select All Except One"
        except_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="random_exclude"]'))
        )
        except_btn.click()

        # Verify exactly 4/5 are checked
        checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.form-check-input'))
        )
        checked_count = sum(1 for cb in checkboxes if cb.is_selected())
        self.assertEqual(checked_count, len(checkboxes) - 1)