# teste.py

# Aqui você puxa a função do arquivo vizinho
from atv import partition

# Cenário de teste do Codewars
animals = ["cat", "dog", "duck", "cow", "donkey"]

# Executa e valida
resultado = partition(animals, lambda x: len(x) == 3)

print("Resultado obtido:", resultado)

# Validação com o assert nativo do Python
assert resultado == (['cat', 'dog', 'cow'], ['duck', 'donkey']), "O teste falhou!"
print("Teste passou com sucesso! 🎉")