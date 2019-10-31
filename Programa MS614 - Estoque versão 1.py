import random
import math

def lucro (demanda, preco_de_venda, estocado, semana_atual, producao, custo_producao_unidade, custo_estocagem_unidade):
    carne_disponivel = producao + estocado[semana_atual]
    custo_producao = producao * custo_producao_unidade
    if carne_disponivel > demanda:
        estocado_final_da_semana = carne_disponivel - demanda
        custo_estocagem_final_da_semana = estocado_final_da_semana * custo_estocagem_unidade
        vendas = demanda*preco_de_venda
        
    else:
        estocado_final_da_semana = 0
        custo_estocagem_final_da_semana = estocado_final_da_semana * custo_estocagem_unidade
        vendas = carne_disponivel*preco_de_venda
    estocado.append(estocado_final_da_semana)
    return vendas - custo_estocagem_final_da_semana - custo_producao

#constantes do problema:
preco_de_venda = 45
estocado = []
estocado.append(0)
compra = int(input("Quantos kg de carne você quer comprar?\n"))

producao = compra
custo_compra_unitario = 10
custo_preparo_unitario = 2
custo_fixo_de_estoque_unitario = 3
custo_producao_unitario = custo_compra_unitario + custo_preparo_unitario + custo_fixo_de_estoque_unitario

custo_estocagem_unitario = 5


#simulação:
media = 0
for semana_atual in range(0, 12):
    demanda = 100 + 10*math.sin(random.randint(1,20000))
    lucro_semana = lucro(demanda, preco_de_venda, estocado, semana_atual, producao, custo_producao_unitario, custo_estocagem_unitario)
    print("A demanda foi de %.2f" % demanda, "kg de carne")
    print("Faturamento semanal = %.2f" % lucro_semana)
    print("O estoque no final do mes foi de %.2f" % estocado[semana_atual+1], "kg de carne\n")
    media += lucro_semana/12
    
print("Media do lucro semanal: %.2f" % media)