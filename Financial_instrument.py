class Financial_instrument:
    def __init__(self, ticker="",price=0.0, instrument_type="", sector=None, currency="USD", description=None, percent_change=0.0):
        self.ticker = ticker
        self.price = price
        self.instrument_type = instrument_type
        self.sector = sector
        self.currency = currency
        self.description = description
        self.percent_change = percent_change

    @property
    def ticker(self):
        return self.__ticker

    @ticker.setter
    def ticker(self, value):
        if not value:
            raise ValueError("Le ticker ne peut pas être vide.")
        if len(value) > 10:
            raise ValueError("Le ticker ne peut pas dépasser 10 caractères.")
        self.__ticker = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value is None:
            raise ValueError("Le prix ne peut pas être vide.")
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Le prix doit être un nombre.")
        self.__price = value

    @property
    def instrument_type(self):
        return self.__instrument_type

    @instrument_type.setter
    def instrument_type(self, value):
        allowed_types = ["Stock", "Crypto", "Currencies", "Commodity"]
        if not value:
            raise ValueError("Le type ne peut pas être vide.")
        if value not in allowed_types:
            raise ValueError(f"Le type doit être parmi : {', '.join(allowed_types)}.")
        self.__instrument_type = value

    @property
    def sector(self):
        return self.__sector

    @sector.setter
    def sector(self, value):
        if value is not None and len(value) > 100:
            raise ValueError("Le sector ne peut pas dépasser 100 caractères.")
        self.__sector = value

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value is None:
            self.__currency = "USD"
            return
        if len(value) != 3:
            raise ValueError("La currency doit contenir exactement 3 caractères.")
        self.__currency = value.upper()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def percent_change(self):
        return self.__percent_change

    @percent_change.setter
    def percent_change(self, value):
        if value is None:
            value = 0.0
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Le percent_change doit être un nombre.")
        self.__percent_change = value

    def __str__(self):
        return (
            f"<Financial_instrument {self.__ticker}: "
            f"Price={self.__price}, Type={self.__instrument_type}, "
            f"Sector={self.__sector}, Currency={self.__currency}, "
            f"Percent_Change={self.__percent_change}>"
        )