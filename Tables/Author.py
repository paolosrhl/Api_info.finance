class Author:
    def __init__(self, author_id=None, name="", email="", specialities=None, company_name=None):
        self.__author_id = author_id
        self.__name = name
        self.__email = email
        self.__specialities = specialities
        self.__company_name = company_name

    @property
    def author_id(self):
        return self.__author_id

    @author_id.setter
    def author_id(self, value):
        self.__author_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Le nom de l'auteur ne peut pas être vide.")
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def specialities(self):
        return self.__specialities

    @specialities.setter
    def specialities(self, value):
        self.__specialities = value

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    def __str__(self):
        return f"<Author {self.__author_id}: {self.__name}>"