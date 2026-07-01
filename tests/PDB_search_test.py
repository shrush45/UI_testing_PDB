from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

# -----------------------------------------------
# TEST 1 : Verify homepage loads successfully
# ----------------------------------------------
driver = webdriver.Chrome()
print("\n TEST 5 : Check if the homepage loads successfully or not")

driver.get("https://www.rcsb.org/")
time.sleep(8)

try:
    # Check Logo
    logo = driver.find_element(By.ID, "rcsblogo")
    if logo.is_displayed():
        print("Logo is visible")

    # Check Search Bar
    search_bar = driver.find_element(By.ID, "search-bar-input-text")
    if search_bar.is_displayed():
        print("Search bar is visible")

    # Check Navigation Menu
    nav_menu = driver.find_element(By.ID, "nav")
    if nav_menu.is_displayed():
        print("Navigation menu is visible")

    print("\nHomepage loaded successfully.")

except Exception as e:
    print("\nHomepage could not load properly.")
    print("Error:", e)

driver.quit()

# -----------------------------------------------
# TEST 2 - Search Hemoglobin and display results
# ----------------------------------------------
print("\nTEST 1 : Search Hemoglobin")

driver.get("https://www.rcsb.org/")
time.sleep(5)

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

# --------------------------------------------
# TEST - Search with Valid PDB ID 
# --------------------------------------------

driver = webdriver.Chrome()
print("\nTEST : Check for valid search using PDB ID")

driver.get("https://www.rcsb.org/")
time.sleep(5)

try:
    search_box = driver.find_element(By.ID,"search-bar-input-text")
    search_box.send_keys("1HHO")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    result = driver.find_element(By.CSS_SELECTOR, "span[class='sc-eGCcFJ FVXco'] span strong")

    print("Results Found :", result.text)
    print("PASS : Search completed successfully")

except:
    print("FAIL : Search could not be completed")

driver.quit()

# -----------------------------------------
# TEST 3 - Check invalid search
# -----------------------------------------
# -------------------------------
driver = webdriver.Chrome()
print("\nTEST 4 : Check for Invalid search")

driver.get("https://www.rcsb.org/")
time.sleep(5)

try:
    search_box = driver.find_element(By.ID,"search-bar-input-text")
    search_box.send_keys("asdfghjkl")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    search_output = driver.find_element(By.CSS_SELECTOR, "div[class='sc-iumHka dUBPff'] h4")

    print("Results Found :", search_output.text)
    print("PASS : Check completed successfully for invalid search")

except:
    print("FAIL : Search could not be completed")

driver.quit()

# -------------------------------
# TEST 4 - Open PDB Structure
# -------------------------------
driver = webdriver.Chrome()

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
# TEST 5 - Check Download Button
# -------------------------------
driver = webdriver.Chrome()

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

# --------------------------------------
# TEST 6 - Advanced search filter link is working 
# --------------------------------------

driver = webdriver.Chrome()
print("\nTEST : Check if the Advanced search result gives a valid results or not")

driver.get("https://www.rcsb.org/")

try:
    adv_search = driver.find_element(By.XPATH,"//tr[@id='search-bar-links']//a[normalize-space()='Advanced Search']")
    adv_search.click()
    print("Finds Advanced Search")
    search = driver.find_element(By.XPATH,"//input[@placeholder='Type to find an attribute or select from the list']")
    search.send_keys("Scientific Name of the Source Organism")
    search.send_keys(Keys.ENTER)
    search2 = driver.find_element(By.XPATH,"//input[@class='sc-tYrig fijtBY form-control']")
    search.send_keys("homo sapiens")
    search.send_keys(Keys.ENTER)
    time.sleep(8)
except:
    print("Fail")

driver.quit()

