from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 8)


def delete_batch():
    # Select
    select = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Select']")
        )
    )
    select.click()
    time.sleep(1)

    # Checkboxes
    boxes = driver.find_elements(
        By.XPATH,
        "//div[@role='button' and @aria-label='Toggle checkbox']"
    )

    if not boxes:
        return 0

    count = 0

    for box in boxes[:20]:
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                box
            )
            box.click()
            count += 1
            time.sleep(0.1)
        except Exception:
            pass

    if count == 0:
        return 0

    # Unlike
    unlike = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Unlike']")
        )
    )
    unlike.click()
    time.sleep(1)

    # Confirmation
    buttons = driver.find_elements(By.TAG_NAME, "button")

    for button in buttons:
        if button.text.strip() in ["Unlike", "Delete", "Remove", "Yes"]:
            button.click()
            break

    time.sleep(3)
    return count


try:
    print("Opening Instagram...")
    driver.get("https://www.instagram.com/")

    input("Log in to Instagram, then press Enter...")

    driver.get(
        "https://www.instagram.com/your_activity/interactions/likes/"
    )
    time.sleep(3)

    total = 0

    while True:
        try:
            deleted = delete_batch()

            if deleted == 0:
                print("No more posts.")
                break

            total += deleted
            print(f"Deleted: {deleted} | Total: {total}")

            driver.refresh()
            time.sleep(3)

        except Exception as e:
            print(f"Error: {e}")
            print("Retrying...")
            driver.refresh()
            time.sleep(4)

    print(f"\nFinished. Total deleted: {total}")

except KeyboardInterrupt:
    print(f"\nStopped. Total deleted: {total}")

finally:
    driver.quit()
