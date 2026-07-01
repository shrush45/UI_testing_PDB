from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

# -------------------------------
# TEST 1 - Search Hemoglobin
# -------------------------------
print("\nTEST 1 : Search Hemoglobin")

driver.get("https://www.rcsb.org/")
time.sleep(3)

try:
    search_box = driver.find_element(By.ID,"search-bar-input-text")
    search_box.send_keys("hemoglobin")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    result = driver.find_element(By.CSS_SELECTOR, "span[class='sc-eGCcFJ FVXco'] span strong")

    print("Results Found :", result.text)
    print("PASS : Search completed successfully")

except:
    print("FAIL : Search could not be completed")

driver.quit()


# -------------------------------
# TEST 2 - Open PDB Structure
# -------------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

print("\nTEST 2 : Open PDB Entry")

driver.get("https://www.rcsb.org/structure/1HHO")
time.sleep(5)

try:
    print("Page Title :", driver.title)

    title = driver.find_element(By.ID, "structureTitle").text
    print("Structure Title :", title)

    print("PASS : Structure page opened")

except:
    print("FAIL : Structure page not loaded")

driver.quit()


# -------------------------------
# TEST 3 - Check Download Button
# -------------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

print("\nTEST 3 : Check Download Button")

driver.get("https://www.rcsb.org/structure/1HHO")
time.sleep(5)

try:
    download = driver.find_element(By.ID, "DownloadFilesButton")

    if download.is_displayed():
        print("PASS : Download button is present")

except:
    print("FAIL : Download button not found")

driver.quit()