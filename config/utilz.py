recipes_prompt = [
    'recetas',
    'receta',
    'instrucciones',
    'instrucción',
    'ingredientes',
    'ingrediente',
]

recommendations_prompt = [
    'recomendaciones',
    'recomendacion',
    'recomendar',
    'recomienda',
    'recomendado',
    'recomendados',
    'recomendadas',
    'recomiendas',
    'recomiendame',
]


def analysis(user_input):
    user_input = user_input.lower()
    user_input = user_input.split(" ")
    if any(word in user_input for word in recipes_prompt):
        return 'recipes'
    if any(word in user_input for word in recommendations_prompt):
        return 'recommendations'
    return 'common_message'
