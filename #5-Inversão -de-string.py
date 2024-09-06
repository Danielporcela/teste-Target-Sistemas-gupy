def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado


string_original = input("Informe uma palavra: ")
string_invertida = inverter_string(string_original)

print(f"Palavra original: {string_original}")
print(f"Palavra invertida: {string_invertida}")
