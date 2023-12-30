import re
def is_valid_credit_card(card_number):
    if re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', card_number):
        cleaned_card_number = re.sub(r'-', '', card_number)
        if re.search(r'(\d)\1{3,}', cleaned_card_number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        card_number = input().strip()
        result = is_valid_credit_card(card_number)
        print(result)