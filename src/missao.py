def calcular_bateria(bateria_atual, duracao_missao, consumo_por_minuto):
    if not 0 <= bateria_atual <= 100 or duracao_missao <= 0 or consumo_por_minuto <= 0:
        print("valor invalido")
        return

    consumo_total = duracao_missao * consumo_por_minuto

    if consumo_total <= bateria_atual:
        bateria_restante = bateria_atual - consumo_total
        print(f"A missao pode ser concluida. Bateria restante: {bateria_restante:g}%")
    else:
        bateria_faltante = consumo_total - bateria_atual
        print(f"A missao n pode ser concluida. Faltam {bateria_faltante:g}%")


bateria_atual = float(input("digite a porcentagem da bateria atual: "))
duracao_missao = float(input("digite a duracao prevista na missao (em minutos): "))
consumo_por_minuto = float(input("digite o consumo medio por minuto: "))

calcular_bateria(bateria_atual, duracao_missao, consumo_por_minuto)
