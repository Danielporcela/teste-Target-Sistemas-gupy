import json


faturamento_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0}
]
'''


faturamento = json.loads(faturamento_json)


faturamento_valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]


menor_valor = min(faturamento_valores)
maior_valor = max(faturamento_valores)


media_mensal = sum(faturamento_valores) / len(faturamento_valores)


dias_acima_da_media = len([dia for dia in faturamento_valores if dia > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
