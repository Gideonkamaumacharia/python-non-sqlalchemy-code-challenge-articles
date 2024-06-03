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
        #articles =[]
        self._articles = []

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

    def articles(self):
        return self._articles
    
    def add_article(self, magazine, title):
       article = Article(self,magazine,title)
       self._articles.append(article)
       return article
    
    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Magazine category must be a non-empty string")

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        self._contributors.add(author)
        return article

    def articles(self):
        return self._articles

    def contributors(self):
        return list(self._contributors)

    def article_titles(self):
         return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_dict = {}
        for article in self._articles:
            if article.author in authors_dict:
                authors_dict[article.author] += 1
            else:
                authors_dict[article.author] = 1
        return [author for author, count in authors_dict.items() if count > 2]




author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine = Magazine("Vogue", "Fashion")


article_1 = Article(author_1, magazine, "How to wear a tutu with style")
author_1.add_article(article_1,"How to wear a tutu with style")

article_2 = Article(author_1, magazine, "Dating life in NYC")
author_1.add_article(article_2, "Dating life in NYC")

article_3 = Article(author_2, magazine, "How to be single and happy")
author_2.add_article(article_3,"How to be single and happy")

print(article_3.__dict__)
print(article_1.__dict__)
print(article_2.__dict__)