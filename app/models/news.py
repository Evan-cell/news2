class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,id,title,name,author,description,url,publishedAt,content):
        self.id =id
        self.name = name
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content