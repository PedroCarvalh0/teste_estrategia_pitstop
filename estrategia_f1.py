def calcular_estrategia_pit_stop(voltas_totais, temp_asfalto, porcentagem_chuva, desgaste_pneu):
    if not 30 <= voltas_totais <= 80:
        raise ValueError("voltas_totais fora do intervalo válido")
    if not 10 <= temp_asfalto <= 60:
        raise ValueError("temp_asfalto fora do intervalo válido")

    if porcentagem_chuva >= 50:
        pneu = "Wet"
    elif temp_asfalto < 25 and desgaste_pneu >= 70:
        pneu = "Soft"
    elif temp_asfalto >= 25 or voltas_totais > 60:
        pneu = "Hard"
    else:
        pneu = "Hard"

    if desgaste_pneu >= 80:
        alerta = "Parada obrigatória na próxima volta"
    else:
        alerta = "Sem alerta"

    if pneu == "Wet":
        volta_parada = 10
    elif pneu == "Soft":
        volta_parada = 20
    else:
        volta_parada = 30

    return {
        "volta_parada": volta_parada,
        "pneu": pneu,
        "alerta_parada": alerta,
    }
