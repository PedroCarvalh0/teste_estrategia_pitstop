# Projeto de testes em telemetria de F1

Este projeto contém a implementação da função `calcular_estrategia_pit_stop` e uma suíte de testes em pytest para verificar as regras de negócio da estratégia de corrida.

## Como executar

```bash
python -m pytest -q
python -m pytest --cov=estrategia_f1 --cov-report=term-missing --cov-report=html -q
```

## Objetivo

Validar:
- intervalos de entrada
- seleção de pneu conforme clima e temperatura
- alerta de parada obrigatória
- cobertura total da lógica em branches e statements
