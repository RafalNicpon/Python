class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # Walidacja ceny i ilości
        if price < 0 or quantity < 0:
            raise ValueError("Cena i ilość nie mogą być ujemne.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu."""
        if amount < 0:
            raise ValueError("Liczba dodawanych produktów nie może być ujemna.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu."""
        if amount < 0:
            raise ValueError("Liczba usuwanych produktów nie może być ujemna.")
        if amount > self.quantity:
            raise ValueError("Nie ma wystarczającej ilości produktów w magazynie.")
        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        """Obniża cenę o podany procent (0-100)."""
        if not (0 <= percent <= 100):
            raise ValueError("Procent musi być w zakresie od 0 do 100.")

        self.price -= self.price * (percent / 100)