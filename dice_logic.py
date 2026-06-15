import random
import re

def roll_dice(expression, character=None):
    # D&D 5e Modifiers mapping
    # characters table: (user_id, name, str, dex, con, int, wis, cha, hp_max, hp_cur)
    mods = {}
    if character:
        mods = {
            'for': (character[2] - 10) // 2,
            'des': (character[3] - 10) // 2,
            'con': (character[4] - 10) // 2,
            'int': (character[5] - 10) // 2,
            'sab': (character[6] - 10) // 2,
            'car': (character[7] - 10) // 2,
        }

    # Normalize expression
    expression = expression.lower().replace(' ', '')

    # Replace attributes with their modifiers
    # Sort keys by length descending to avoid partial replacement (e.g., 'sab' before 's')
    for attr in sorted(mods.keys(), key=len, reverse=True):
        val = mods[attr]
        # Use regex to replace only whole words to avoid issues if attributes were sub-strings
        expression = re.sub(rf'\b{attr}\b', f"{val:+}", expression)

    # Regex to find dice like 2d10 or d20 (treat as 1d20)
    pattern = r'(\d*)d(\d+)'
    
    def replace_dice(match):
        num_str = match.group(1)
        num = int(num_str) if num_str else 1
        sides = int(match.group(2))
        rolls = [random.randint(1, sides) for _ in range(num)]
        if len(rolls) > 1:
            return f"({'+'.join(map(str, rolls))})"
        else:
            return str(rolls[0])

    rolled_expression = re.sub(pattern, replace_dice, expression)
    
    # Check if there are any illegal characters left
    if not re.match(r'^[0-9+\-*/().]+$', rolled_expression):
        return None, f"Expressão inválida: {rolled_expression}"

    try:
        # Simple evaluation of the expression
        total = eval(rolled_expression)
        return rolled_expression, total
    except Exception as e:
        return None, str(e)
