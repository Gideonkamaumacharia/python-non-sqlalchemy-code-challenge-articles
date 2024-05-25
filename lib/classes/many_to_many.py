class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    
    def title(self):
        return self._title

    def title(self,title):
        if isinstance(title,str) and (5<= len(title)<= 25):
            self._title = title
            #return (( "How to wear a tutu with style"))
        print
#article_1 = Article('author','magazine', "How to wear a tutu with style")          
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

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