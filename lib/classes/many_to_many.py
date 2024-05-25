class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        #self.set_title(title)
        Article.all.append(self)

    def set_title(self, title):
        if not isinstance(title, str) and (5 <= len(title) <= 50):
            raise ValueError("Title must be a string and must be between 5 and 50 characters long")
        
        self._title = title

    @property
    def title(self):
        return self._title
    
 

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Author's name must be a string")
        elif hasattr(self,"_name"):
            raise AttributeError("Author's name cannot be changed")
        else:
            self._name = value

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass