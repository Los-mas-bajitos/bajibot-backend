import json

from chatbot.settings import settings

custom_response = """
Debes responder en español.
Sí lo que se pregunta no hace referencia a comida o a recetas,
debes responder con "Soy un chefbot, no puedo responder a eso".
"""


def get_food_recipes(user_input):
    data = {
        'prompt': user_input + custom_response + """
                  Using this JSON schema:
                  Recipe = {
                  recipe_name: str
                  ingredients: list[str]
                  instructions: list[str]
                  }
                  Return a `Recipe`
                  """,
        'max_tokens': 50
    }

    response = settings.model.generate_content(data.get('prompt'))
    print(response.text)
    return json.loads(response.text)


def get_food_recommendations(user_input):
    data = {
        'prompt': user_input + custom_response + """
                      Using this JSON schema:
                      Recommendations = {
                        recipe_name: str
                        description: str
                      }
                      Return a `List[Recommendations]`
                      """,
        'max_tokens': 50
    }
    response = settings.model.generate_content(data.get('prompt'))
    print(response.text)
    return json.loads(response.text)


def get_food_recommendation(user_input):
    data = {
        'prompt': user_input + custom_response + """
                      Using this JSON schema:
                      Recommendation = {
                        recipe_name: str
                        description: str
                      }
                      Return a `Recommendation`
                      """,
        'max_tokens': 50
    }
    response = settings.model.generate_content(data.get('prompt'))
    print(response.text)
    return json.loads(response.text)


def get_common_message(user_input):
    data = {
        'prompt': user_input + custom_response + """
                      Using this JSON schema:
                      CommonMessage = {
                        message: str
                      }
                      Return a `CommonMessage`
                      """,
        'max_tokens': 50
    }
    response = settings.model.generate_content(data.get('prompt'))
    print(response.text)
    return json.loads(response.text)
