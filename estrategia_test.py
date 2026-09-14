import pytest

from estrategia_f1 import calcular_estrategia_pit_stop


@pytest.mark.parametrize(
    "voltas_totais,temp_asfalto,chuva,desgaste,expected_pneu,expected_alerta,expected_volta",
    [
        (50, 20, 0, 75, "Soft", "Sem alerta", 20),
        (60, 30, 0, 20, "Hard", "Sem alerta", 30),
        (70, 15, 0, 80, "Soft", "Parada obrigatória na próxima volta", 20),
        (45, 25, 0, 40, "Hard", "Sem alerta", 30),
        (50, 20, 55, 10, "Wet", "Sem alerta", 10),
        (75, 20, 0, 35, "Hard", "Sem alerta", 30),
    ],
)
def test_cenarios_validos(
    voltas_totais, temp_asfalto, chuva, desgaste, expected_pneu, expected_alerta, expected_volta
):
    resultado = calcular_estrategia_pit_stop(voltas_totais, temp_asfalto, chuva, desgaste)
    assert resultado["pneu"] == expected_pneu
    assert resultado["alerta_parada"] == expected_alerta
    assert resultado["volta_parada"] == expected_volta


@pytest.mark.parametrize(
    "voltas_totais,temp_asfalto,chuva,desgaste",
    [
        (29, 25, 0, 10),
        (81, 25, 0, 10),
        (50, 9, 0, 10),
        (50, 61, 0, 10),
    ],
)
def test_entradas_invalidas_geram_value_error(voltas_totais, temp_asfalto, chuva, desgaste):
    with pytest.raises(ValueError):
        calcular_estrategia_pit_stop(voltas_totais, temp_asfalto, chuva, desgaste)


def test_chuva_acima_de_50_forca_pneu_wet():
    resultado = calcular_estrategia_pit_stop(40, 30, 50, 10)
    assert resultado == {"volta_parada": 10, "pneu": "Wet", "alerta_parada": "Sem alerta"}


def test_desgaste_emergencial_ativa_alerta_na_proxima_volta():
    resultado = calcular_estrategia_pit_stop(45, 23, 0, 80)
    assert resultado["pneu"] == "Soft"
    assert resultado["alerta_parada"] == "Parada obrigatória na próxima volta"


def test_temperatura_alta_forca_pneu_hard():
    resultado = calcular_estrategia_pit_stop(55, 30, 0, 10)
    assert resultado == {"volta_parada": 30, "pneu": "Hard", "alerta_parada": "Sem alerta"}


def test_circuito_fresco_sem_desgaste_atinge_hard_fallback():
    resultado = calcular_estrategia_pit_stop(45, 20, 0, 60)
    assert resultado == {"volta_parada": 30, "pneu": "Hard", "alerta_parada": "Sem alerta"}


def test_voltas_mais_de_60_forca_hard():
    resultado = calcular_estrategia_pit_stop(65, 20, 0, 10)
    assert resultado["pneu"] == "Hard"
    assert resultado["volta_parada"] == 30
