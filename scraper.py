from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the CPCB website
driver.get("https://app.cpcbccr.com/AQI_India/")

# Wait for the CAPTCHA to be solved
input("Please solve the CAPTCHA and press Enter to continue...")

# Wait for the state dropdown to be clickable
state_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "states")))
state_dropdown.click()

# Select the state of Maharashtra
state_option = driver.find_element_by_xpath("//option[contains(text(), 'Maharashtra')]")
state_option.click()

# Wait for the city dropdown to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cities")))

# Select Mumbai from the city dropdown
city_dropdown = driver.find_element_by_id("cities")
city_dropdown.click()
city_option = driver.find_element_by_xpath("//option[contains(text(), 'Mumbai')]")
city_option.click()

# Click on the date picker
date_picker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "datepicker")))
date_picker.click()

# Select the start date
start_date = driver.find_element_by_xpath("//td[@data-handler='selectDay']/a[text()='1']")
start_date.click()

# Select the end date
end_date = driver.find_element_by_xpath("//td[@data-handler='selectDay']/a[text()='10']")
end_date.click()

# Click on the Download button
download_button = driver.find_element_by_xpath("//button[contains(text(), 'Download Data')]")
download_button.click()


# Close the webdriver
driver.quit()
