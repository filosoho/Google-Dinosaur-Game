from selenium import webdriver
import time
import random
from selenium.common.exceptions import WebDriverException

# Initialize the Chrome WebDriver
try:
    driver = webdriver.Chrome()
except WebDriverException as e:
    print("Error initializing WebDriver:", e)
    driver = None

if driver:
    try:
        # Open the Dino Game by navigating to the chrome://dino URL
        driver.get("chrome://dino")
    except WebDriverException as e:
        pass  # Ignore the error if opening the Dino game fails

    # Give the game some time to load
    time.sleep(2)

    # Define the function to make the Dino jump using JavaScript
    def jump():
        try:
            driver.execute_script("document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'Space'}));")
        except WebDriverException:
            raise KeyboardInterrupt


    # Main game loop
    try:
        while True:
            # Randomly decide to jump or not (adjust the threshold as needed)
            if random.random() < 0.2:
                jump()

            # Adjust the sleep time to control the game's speed
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Game over!")

    # Close the browser window when done
    driver.quit()
