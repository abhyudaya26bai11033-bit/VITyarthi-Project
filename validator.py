def check_text(user_input):
    cleaned = user_input.strip()
    if len(cleaned)== 0:
        return False
    return cleaned
def check_number(user_choice, max_items):
    if not user_choice.isdigit():
        return False
    num = int(user_choice)
    if num > 0 and num <= max_items:
        return num - 1
    return False
