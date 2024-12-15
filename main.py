# Import the required classes and functions
from oop_file import InternetSpeedTwitterBot  # Import the class for the bot
from dotenv import load_dotenv  # Import dotenv to load environment variables
import os  # Import os to access environment variables

# Load environment variables from a .env file
load_dotenv()

# Retrieve the email, password, and username from environment variables
EMAIL = os.environ["MY_EMAIL_OF_TWITTER"]  # Email used to sign in to Twitter
PASSWORD = os.environ["MY_PASSWORD_OF_TWITTER"]  # Twitter password
USER_NAME = os.environ["USER_NAME"]  # Twitter username

# Initialize the InternetSpeedTwitterBot instance
poss = InternetSpeedTwitterBot()

# Get the internet speed (download and upload)
poss.get_speed()

# Post the speed test results on Twitter
poss.tweet_at_provider(EMAIL, PASSWORD, USER_NAME)
