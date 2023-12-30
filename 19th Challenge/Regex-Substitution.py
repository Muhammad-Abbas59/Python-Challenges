import re

def modify_text(match):
    operator = match.group(0)
    if operator == "&&":
        return "and"
    elif operator == "||":
        return "or"

n = int(input())
text_lines = [input() for _ in range(n)]

pattern = r"(?<= )(\&\&|\|\|)(?= )"

for line in text_lines:
    modified_line = re.sub(pattern, modify_text, line)
    print(modified_line)
