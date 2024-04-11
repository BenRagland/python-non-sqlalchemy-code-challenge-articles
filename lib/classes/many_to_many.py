# import ipdb
class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        self.authors = [author]
        self.magazines = [magazine]

        if ( 4< len(self._title) < 51 ):
             raise ValueError("Article not correct length")
        if not isinstance(title, str):
            raise ValueError("article must be a string")
       
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        [ author for author in self.authors if isinstance(author,Author)]
        
    @author.setter
    def author(self,article):
        if not isinstance(article,Author):
            raise TypeError("not of type Author")
        else:
            self.authors.append(article)

    @property
    def magazine(self):
        { magazine for magazine in self.magazines if isinstance(magazine,Magazine)}
        
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine,Magazine):
            raise TypeError("not of type Author")
        else:
            self.magazine.append(magazine)
            
    @author.setter
    def author(self,author):
        if not isinstance(Article,Author):
            raise TypeError("not of type Author")
        else:
            self.authors.append(author)
        
    @property
    def magazine(self):
        return self._magazine


        
class Author:

    def __init__(self,name):
        self._name = name
        if len(name) == 0:
            raise Exception("must be longer than 0")
        if not isinstance(name, str):
            raise Exception("name must be string")
        self._articles = []


    @property
    def name(self):
        return self.name

    @property
    def articles(self):
        [ article for article in self.articles if isinstance(article,Article)]


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
        self._name = name
        self._category = category
        self._articles=[]
        self._contributors=[]

        if not ( 1< len(name) < 17 ) :
            raise Exception("not correct name length") 
        if not isinstance(name, str):
            raise Exception("Magazine name must be string")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if ((len(name) > 1 and len(name)> 16 ) and type(name)==str):
            self.name = name
        else:
            print("incorrect name format")
    
    @property
    def category(self):
       return self._category

    def articles(self):
        [ article for article in self._articles if isinstance(article,Article)]
        

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

# ipdb.set_trace()