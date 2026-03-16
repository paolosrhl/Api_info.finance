class Article_Impact:
    def __init__(self, impact_id=None, ticker="", price=0.0, percent_change=0.0, article_id=None):
        self.__impact_id = impact_id
        self.__ticker = ticker
        self.__price = price
        self.__percent_change = percent_change
        self.__article_id = article_id

    @property
    def impact_id(self):
        return self.__impact_id

    @impact_id.setter
    def impact_id(self, value):
        self.__impact_id = value

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
    def percent_change(self):
        return self.__percent_change

    @percent_change.setter
    def percent_change(self, value):
        if value is None:
            raise ValueError("Le pourcentage de changement ne peut pas être vide.")
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Le pourcentage de changement doit être un nombre.")
        self.__percent_change = value

    @property
    def article_id(self):
        return self.__article_id

    @article_id.setter
    def article_id(self, value):
        if value is None:
            raise ValueError("L'article_id ne peut pas être vide.")
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError("L'article_id doit être un entier.")
        self.__article_id = value

    def __str__(self):
        return f"<Article_Impact {self.__impact_id}: {self.__ticker}, Price={self.__price}, Change={self.__percent_change}%, Article_id={self.__article_id}>"