from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        # Set up Chrome options and initialize the Chrome WebDriver
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(40)
        self.up = 0  # Variable to store upload speed
        self.down = 0  # Variable to store download speed

    def get_speed(self):
        # Open the speedtest website
        self.driver.get(url='https://www.speedtest.net/')


        # Click the 'Go' button to start the speed test
        click_go = self.driver.find_element(By.XPATH,
                                            "//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]")
        click_go.click()


        # Extract the download speed
        get_download = self.driver.find_element(By.XPATH,
                                                "//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]")
        self.down = get_download.text

        # Extract the upload speed
        get_upload = self.driver.find_element(By.XPATH,
                                              "//*[@id=\"container\"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]")
        self.up = get_upload.text
        print("Speed test complete, speeds extracted")

    def tweet_at_provider(self, email, password, username):
        # Go to Twitter homepage and log in
        self.driver.get("https://x.com/home")

        try:
            # Close any pop-up that may appear
            close = self.driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div[1]/div/div/div/button")
            close.click()
        except Exception:
            pass


        sign_in = self.driver.find_element(By.CSS_SELECTOR, ".r-2o02ov a")
        sign_in.click()

        # Enter email and submit
        typing_email = self.driver.find_element(By.XPATH,
                                                "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        typing_email.send_keys(email, Keys.ENTER)


        # If username field appears, fill it out
        try:
            typing_user_name = self.driver.find_element(By.XPATH,
                                                        "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            typing_user_name.send_keys(username, Keys.ENTER)
        except NoSuchElementException:
            pass


        # Enter password and submit
        typing_password = self.driver.find_element(By.XPATH,
                                                   "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        typing_password.send_keys(password, Keys.ENTER)


        # Close any additional pop-ups that might appear
        try:
            close_2 = self.driver.find_element(By.XPATH,
                                               "//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button")
            close_2.click()
        except NoSuchElementException:
            pass

        # Wait for the tweet input field to appear
        tweet_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div"))
        )

        # Clear the tweet input if needed (just in case)
        tweet_input.clear()

        # Compose the tweet with speed details
        tweet_text = f"Hey @telecomegypt why is my internet speed {self.down} down/{self.up} up when I pay for 30 down?"
        tweet_input.send_keys(tweet_text)


        # Click the 'Tweet' button to post the tweet
        post_press = self.driver.find_element(By.XPATH,
                                              "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button")
        post_press.click()

        print("Tweet has been posted successfully.")








