from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import random
import time

# Path to the Edge WebDriver 
edge_driver_path = "C:\msedgedriver.exe"

# Function to toggle select/deselect all checkboxes
def toggle_select_deselect():
    # Set up the Edge WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service)

    driver.get("http://127.0.0.1:8000/tasks/checkbox")
    time.sleep(2)

    checkboxes = driver.find_elements(By.CLASS_NAME, "form-check-input")
    all_selected = all([checkbox.is_selected() for checkbox in checkboxes])

    for checkbox in checkboxes:
        if all_selected:
            if checkbox.is_selected():
                checkbox.click()  # Deselect
        else:
            if not checkbox.is_selected():
                checkbox.click()  # Select

    time.sleep(2)
    driver.quit()

# Function to select all checkboxes except one randomly
def select_all_except_one():
    # Set up the Edge WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service)

    driver.get("http://127.0.0.1:8000/tasks/checkbox")
    time.sleep(2)

    checkboxes = driver.find_elements(By.CLASS_NAME, "form-check-input")
    index_to_leave_unchecked = random.randint(0, len(checkboxes) - 1)

    for i, checkbox in enumerate(checkboxes):
        if i == index_to_leave_unchecked:
            if checkbox.is_selected():
                checkbox.click()  # Uncheck if selected
        else:
            if not checkbox.is_selected():
                checkbox.click()  # Check if not selected

    time.sleep(2)
    driver.quit()