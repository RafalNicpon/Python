import pytest
from product import Product

@pytest.fixture
def product_discount():
    """Tworzy produkt o cenie 100.0 do testów rabatów."""
    return Product("Testowy", 100.0, 1)

# Testy poprawnych wartości rabatu
@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),    # 0% - cena bez zmian
    (50, 50.0),    # 50% - połowa ceny
    (100, 0.0)     # 100% - cena = 0
])
def test_apply_discount_parametrized(product_discount, percent, expected_price):
    product_discount.apply_discount(percent)
    # Używamy pytest.approx dla bezpieczeństwa przy liczbach zmiennoprzecinkowych
    assert product_discount.price == pytest.approx(expected_price)

# Testy wartości nieprawidłowych (ValueError)
@pytest.mark.parametrize("invalid_percent", [
    (-1),    # Wartości ujemne
    (101),   # Wartości > 100
    (150)
])
def test_apply_discount_invalid_value(product_discount, invalid_percent):
    with pytest.raises(ValueError):
        product_discount.apply_discount(invalid_percent)