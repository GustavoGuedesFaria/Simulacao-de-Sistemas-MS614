import random
import numpy
import math

def lucro (demanda, preco_de_venda, estocado, semana_atual, producao, custo_producao_unidade, custo_estocagem_unidade):
    carne_disponivel = producao + estocado[semana_atual]
    custo_producao = producao * custo_producao_unidade
    if carne_disponivel > demanda:
        estocado_final_da_semana = carne_disponivel - demanda
        custo_estocagem_final_da_semana = estocado_final_da_semana * custo_estocagem_unidade
        vendas = demanda*preco
        
    else:
        estocado_final_da_semana = 0
        custo_estocagem_final_da_semana = estocado_final_da_semana * custo_estocagem_unidade
        vendas = carne_disponivel*preco
    estocado.append(estocado_final_da_semana)
    return vendas - custo_estocagem_final_da_semana - custo_producao

#constantes do problema:
print("Qual o intervalo em que você quer buscar a melhor quantidade a comprar?\n")
intervalo_compra_inicial = int(input("De:\n"))
intervalo_compra_final = int(input("Até:\n"))
preco_de_venda = 45

custo_compra_unitario = 10
custo_preparo_unitario = 2
custo_fixo_de_estoque_unitario = 3
custo_producao_unitario = custo_compra_unitario + custo_preparo_unitario + custo_fixo_de_estoque_unitario

custo_estocagem_unitario = 5

numero_de_testes = int(input("Selecione o número de testes:\n"))

maior_lucro = -1000000000
compra_maior_lucro = -100000000
for compra in range(intervalo_compra_inicial, intervalo_compra_final+1):
    producao = compra
    soma = 0
    for testes in range (0,numero_de_testes):
        media = 0
        estocado = []
        estocado.append(0)
        for semana_atual in range(0, 12):
            demanda = 100 + 10*math.sin(random.randint(1,20000))
            lucro_semana = lucro(demanda, preco_de_venda, estocado, semana_atual, producao, custo_producao_unitario, custo_estocagem_unitario)
            media += lucro_semana/12
        soma += media
    lucro_medio = soma/numero_de_testes
    print("Média do lucro semanal comprando", compra,"kg: %.2f" %lucro_medio)
    if(lucro_medio > maior_lucro):
        maior_lucro = lucro_medio
        compra_maior_lucro = compra
        
print("Quantidade ideal de compra semanal é de", compra_maior_lucro, "unidades, com um lucro semanal de %.2f"% maior_lucro)