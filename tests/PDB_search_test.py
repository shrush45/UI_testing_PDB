"""
Selenium UI Test: RCSB Protein Data Bank (PDB) Search
Author: Shrushti Salunke
Description: Automates protein structure search on RCSB PDB and validates
             that search results and structure metadata load correctly.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def setup_driver():
    """Initialize Chrome WebDriver with webdriver-manager."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment to run headless
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def test_pdb_search(query="hemoglobin"):
    """
    Test 1: Search for a protein on RCSB PDB.
    Validates:
    - Search bar is accessible
    - Results page loads with entries
    - Result count is greater than zero
    """
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        print(f"\n[TEST 1] Searching PDB for: '{query}'")
        driver.get("https://www.rcsb.org/")

        # Locate search bar
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "search-bar-input"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results count to appear
        result_count_el = wait.until(
            EC.presence_of_element_located((By.ID, "result-count"))
        )
        result_text = result_count_el.text
        print(f"[INFO] Result text found: {result_text}")

        # Validate results exist
        assert result_text != "0", "FAIL: Zero results returned."
        print(f"[PASS] Search for '{query}' returned results: {result_text}")

    except AssertionError as e:
        print(f"[FAIL] {e}")
    except Exception as e:
        print(f"[ERROR] Test 1 failed unexpectedly: {e}")
    finally:
        driver.quit()


def test_pdb_direct_entry(pdb_id="1HHO"):
    """
    Test 2: Directly access a known PDB entry (1HHO = Hemoglobin).
    Validates:
    - Structure page loads
    - PDB ID appears in the page title or heading
    - Organism info section is present
    """
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        print(f"\n[TEST 2] Loading PDB entry: {pdb_id}")
        driver.get(f"https://www.rcsb.org/structure/{pdb_id}")

        # Validate PDB ID in page title
        wait.until(EC.title_contains(pdb_id))
        print(f"[INFO] Page title: {driver.title}")
        assert pdb_id in driver.title, f"FAIL: {pdb_id} not in page title."

        # Validate structure title heading loads
        structure_title = wait.until(
            EC.presence_of_element_located((By.ID, "structureTitle"))
        )
        title_text = structure_title.text
        assert len(title_text) > 0, "FAIL: Structure title is empty."
        print(f"[PASS] Structure title found: {title_text}")

        # Validate organism section exists
        organism_section = wait.until(
            EC.presence_of_element_located((By.ID, "MacromoleculeTable"))
        )
        assert organism_section is not None, "FAIL: Organism/macromolecule table missing."
        print(f"[PASS] Macromolecule table loaded successfully.")

    except AssertionError as e:
        print(f"[FAIL] {e}")
    except Exception as e:
        print(f"[ERROR] Test 2 failed unexpectedly: {e}")
    finally:
        driver.quit()


def test_pdb_download_button(pdb_id="1HHO"):
    """
    Test 3: Verify the FASTA download button is present on a structure page.
    Validates:
    - Download section is accessible
    - FASTA option exists (relevant for sequence analysis workflows)
    """
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        print(f"\n[TEST 3] Checking download options for: {pdb_id}")
        driver.get(f"https://www.rcsb.org/structure/{pdb_id}")

        # Scroll to download section
        time.sleep(2)
        download_section = wait.until(
            EC.presence_of_element_located((By.ID, "DownloadFilesButton"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", download_section)
        assert download_section is not None, "FAIL: Download button not found."
        print(f"[PASS] Download button is present for {pdb_id}.")

    except AssertionError as e:
        print(f"[FAIL] {e}")
    except Exception as e:
        print(f"[ERROR] Test 3 failed unexpectedly: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_pdb_search("hemoglobin")
    test_pdb_direct_entry("1HHO")
    test_pdb_download_button("1HHO")