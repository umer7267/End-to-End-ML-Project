"""
Loads environment variables and app-wide settings
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "END-to-END ML Project"
    API_KEY = os.getenv("API_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    MODEL_PATH = "app/models/model.pkl"

settings = Settings()