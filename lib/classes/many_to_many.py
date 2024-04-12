
class Article:
    def __init__(self, author, magazine, title):
        self.author = Author(author)
        self.magazine = Magazine(magazine,"default")
        self.title = title
        self.authors = [author]
        self.magazines = [magazine]

        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if ( 4< len(title) < 51 ):
             raise ValueError("Article not correct length")
        if not isinstance(title, str):
            raise TypeError("article must be a string")
        if hasattr(self,"title"):
            raise AttributeError("title attr already set")
        self._title = title
    
    @property
    def author(self):
        return [ author for author in self.authors if isinstance(author,Author)]
        
    @author.setter
    def author(self,article):
        if not isinstance(article,Author):
            raise TypeError("not of type Author")
        else:
            self.authors.append(article)

    # @property
    # def magazine(self):
    #    return { magazine for magazine in self.magazines if isinstance(magazine,Magazine)}
        
    # @magazine.setter
    # def magazine(self,magazine):
    #     if not isinstance(magazine,Magazine):
    #         raise TypeError("not of type Author")
    #     else:
    #         self.magazine.append(magazine)
    
class Author:

    def __init__(self,name):
        self.name = name
        self._articles = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self,"name"):
            raise AttributeError("Attribute can't be modified after creation")
        if len(name) == 0:
                raise Exception("must be longer than 0")
        if not isinstance(name, str):
            raise TypeError("name must be string")
        self._name = name

    @property
    def articles(self):
        return [ article for article in self.articles if isinstance(article,Article)]


    def magazines(self):
        {magazine for magazine in self.magazines if isinstance(magazine,Magazine)}
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})

    

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles=[]
        self.contributors=[]
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not ( 1< len(name) < 17 ) :
            raise ValueError("not correct name length") 
        if not isinstance(name, str):
            raise TypeError("Magazine name must be string")
       
    @property
    def category(self):
       return self._category
    
    @category.setter
    def category(self,category):
       if not (isinstance(category,str)):
           raise TypeError("Must be a string")
       
       self._category = category

    def articles(self):
        return [ article for article in self._articles if isinstance(article,Article)]
        

    def contributors(self):
         {contributor for contributor in self.contributors if isinstance(contributor,Author)}

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
        

    def contributing_authors(self):
        author_num = {}
        for article in self._articles:
            author = article.author
            author_num[author] = author_num.get(author, 0) + 1


        return [author for author, count in author_num.items() if count > 2] if author_num else None

import ipdb; ipdb.set_trace()