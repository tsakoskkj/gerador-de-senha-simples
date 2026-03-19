import random
import string


print("gerador de senhas simples")

letra = string.ascii_letters

k_random_letters_string = ''.join(random.choices(letra, k=random.randint(8,26)))

print(f"sua senha é {k_random_letters_string}")
