from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower = ingredients.lower()
    for item in allowed:
        if item in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
