"""Exemplo de testes com pytest para o capítulo profissional."""

from pacote_python.operacoes import multiplicar, dividir
from pacote_python.utilidades import formatar_texto


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5


def test_dividir():
    assert dividir(10, 2) == 5


def test_formatar_texto():
    assert formatar_texto('  python profissional ') == 'Python Profissional'


def test_dividir_por_zero():
    try:
        dividir(5, 0)
    except ValueError as erro:
        assert str(erro) == 'Divisor não pode ser zero'
    else:
        assert False, 'Esperava ValueError para divisor zero'
