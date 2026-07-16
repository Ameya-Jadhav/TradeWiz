from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self):
        self.HDFC_API_KEY = os.getenv("HDFC_API_KEY")
        self.HDFC_API_SECRET = os.getenv("HDFC_API_SECRET")
        self.HDFC_CLIENT_CODE = os.getenv("HDFC_CLIENT_CODE")

        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()