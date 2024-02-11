from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to your ChromeDriver executable
chrome_driver_path = 'chromedriver.exe'

# Start the ChromeDriver service
service = Service(chrome_driver_path)
service.start()

# Create a new Chrome session
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get('https://www.example.com')

# Execute JavaScript to refresh the page 10,000 times
for _ in range(10000):
    driver.execute_script("location.reload();")

# Close the browser
driver.quit()