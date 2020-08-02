import string
import random

lower_string = random.choices(string.ascii_lowercase, k=7)
upper_string = random.choices(string.ascii_uppercase, k=1)
digits_string = random.choices(string.digits, k=1)
spl_char = random.choices('!@#$%^&*()', k=1)

print(''.join(upper_string) + ''.join(lower_string) + ''.join(digits_string) + ''.join(spl_char))
