class Article:
    def __init__(self, article_id=None, title="", content="", author=None):
        self.__article_id = article_id
        self.__title = title
        self.__content = content
        self.__author = author

    @property
    def article_id(self):
        return self.__article_id

    @article_id.setter
    def article_id(self, value):
        self.__article_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Le titre de l'article ne peut pas être vide.")
        self.__title = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value is not None and not isinstance(value, Author):
            raise TypeError("L'attribut 'author' doit être une instance de la classe Author.")
        self.__author = value

    def __str__(self):
        nom_auteur = self.__author.name if self.__author else "Auteur Inconnu"
        return f"<Article {self.__article_id}: '{self.__title}' (par {nom_auteur})>"