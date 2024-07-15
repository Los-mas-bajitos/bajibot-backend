import os

import google.generativeai as genai
import typing_extensions as typing
from dotenv import load_dotenv

load_dotenv()


class Recipe(typing.TypedDict):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]


class CommonMessage(typing.TypedDict):
    message: str


class Settings:
    BOT_NAME = "FoodBot"
    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(
        'gemini-1.5-pro',
        generation_config={
            "response_mime_type": "application/json"
        }
    )


settings = Settings()
