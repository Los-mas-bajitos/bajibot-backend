import json

from chatbot.settings import settings


def get_food_recipes(user_input):
    data = {
        'prompt': user_input + """ 
                  Debes responder en español.
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
        'prompt': user_input + """ 
                      Debes responder en español.
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


def get_common_message(user_input):
    data = {
        'prompt': user_input + """ 
                      Debes responder en español.
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
