import random
import math

def lucro (demanda, preco_de_venda, estocado, producao, custo_producao_unidade, custo_desperdicio_unidade):
    carne_disponivel = producao + estocado
    custo_producao = producao * custo_producao_unidade
    if carne_disponivel > demanda:
        desperdicio_final_da_semana = carne_disponivel - demanda
        custo_desperdicio_final_da_semana = desperdicio_final_da_semana * custo_desperdicio_unidade
        vendas = demanda*preco_de_venda
        
    else:
        desperdicio_final_da_semana = 0
        custo_desperdicio_final_da_semana = desperdicio_final_da_semana * custo_desperdicio_unidade
        vendas = carne_disponivel*preco_de_venda
        
    return vendas - custo_desperdicio_final_da_semana - custo_producao

#constantes do problema:
preco_de_venda = 45
estocado = 0
compra = int(input("Quantos kg de carne você quer comprar por semana?\n"))

producao = compra
custo_compra_unitario = 10
custo_preparo_unitario = 2
custo_fixo_de_estoque_unitario = 3
custo_producao_unitario = custo_compra_unitario + custo_preparo_unitario + custo_fixo_de_estoque_unitario

custo_desperdicio_unitario = 5


#simulação:
media = 0
for semana_atual in range(0, 12):
    demanda = 100 + 10*math.sin(random.randint(1,2000000))
    lucro_semana = lucro(demanda, preco_de_venda, estocado, producao, custo_producao_unitario, custo_desperdicio_unitario)
    print("A demanda foi de %.2f" % demanda, "kg de carne")
    print("Faturamento semanal  = %.2f" % lucro_semana)
    print("O desperdício no final da semana foi de %.2f" % max(0, producao - demanda), "kg de carne\n")
    media += lucro_mes/12
    
print("Media do lucro semanal: %.2f" % media)