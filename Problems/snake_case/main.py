import re

pattern = re.compile('([a-z])([A-Z])')
phrase = input()
snake_case = pattern.sub(r'\1_\2', phrase).lower()
print(snake_case)
