class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title  

class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = {magazine.category for magazine in self.magazines()}
        return  list(topics) if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass