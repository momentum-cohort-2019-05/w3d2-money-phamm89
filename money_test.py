import pytest
from money import Money, Currency, DifferentCurrencyError

USD = Currency("United States dollar", "USD", "$")
BHD = Currency("Bahraini dinar", "BHD", digits=3)


def test_create_dollar():
    dollar = Currency("United States dollar", "USD", "$")
    assert dollar.name == "United States dollar"
    assert dollar.code == "USD"
    assert dollar.symbol == "$"
    assert dollar.digits == 2


def test_create_peso():
    peso = Currency("Mexican peso", "MXN")
    assert peso.name == "Mexican peso"
    assert peso.code == "MXN"
    assert peso.symbol is None
    assert peso.digits == 2


def test_create_dinar():
    dinar = Currency("Bahraini dinar", "BHD", digits=3)
    assert dinar.name == "Bahraini dinar"
    assert dinar.code == "BHD"
    assert dinar.symbol is None
    assert dinar.digits == 3


def test_currency_equality():
    assert USD == Currency("United States dollar", "USD", "$")


def test_create_money():
    one_dollar = Money(1, USD)
    assert one_dollar.amount == 1
    assert one_dollar.currency == USD


def test_dollars_to_str():
    one_dollar = Money(1, USD)
    assert str(one_dollar) == "$1.00"


def test_dinar_to_str():
    dinar = Money(7.5, BHD)
    assert str(dinar) == "BHD 7.500"


def test_money_equality():
    assert Money(1, USD) == Money(1, USD)
    assert Money(2, USD) == Money(2, USD)


def test_money_inequality():
    assert Money(1, USD) != Money(2, USD)
    assert Money(2, USD) != Money(2, BHD)


def test_add_money():
    assert Money(1, USD).add(Money(1, USD)) == Money(2, USD)
    assert Money(1, USD).add(Money(2.5, USD)) == Money(3.5, USD)


def test_sub_money():
    assert Money(2, USD).sub(Money(1, USD)) == Money(1, USD)
    assert Money(10, USD).sub(Money(3.75, USD)) == Money(6.25, USD)


def test_add_different_currencies():
    with pytest.raises(DifferentCurrencyError):
        Money(1, USD).add(Money(1, BHD))


def test_sub_different_currencies():
    with pytest.raises(DifferentCurrencyError):
        Money(1, USD).sub(Money(1, BHD))


def test_mul_money():
    assert Money(2.75, USD).mul(3) == Money(8.25, USD)
    assert Money(3.81, USD).mul(4) == Money(15.24, USD)


def test_div_money():
    assert Money(3, USD).div(3) == Money(1, USD)
    assert Money(12, USD).div(4) == Money(3, USD)
