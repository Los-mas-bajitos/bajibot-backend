def recipes(user_input):
    from model.responses import get_food_recipes
    return get_food_recipes(user_input)


def recommendations(user_input):
    from model.responses import get_food_recommendations
    return get_food_recommendations(user_input)


def common_message(user_input):
    from model.responses import get_common_message
    return get_common_message(user_input)
