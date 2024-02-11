import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your ChromeDriver executable
chrome_driver_path = 'chromedriver.exe'

# Define the number of refreshes
num_refreshes = 100

def refresh_website(_):
    # Create a new Chrome session
    service = Service(chrome_driver_path)
    service.start()
    driver = webdriver.Chrome(service=service)

    # Open the website
    driver.get('https://www.example.com')

    # Refresh the website
    driver.refresh()

    # Close the browser
    driver.quit()

# Create a thread pool with a maximum of 10 workers
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Submit the refresh tasks to the thread pool
    executor.map(refresh_website, range(num_refreshes))
