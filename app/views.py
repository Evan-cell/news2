from flask import render_template
from app import app
from newsapi import NewsApiClient

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The latest news'
    newsapi = NewsApiClient(api_key='91a623008e664b6bb43be5edc7dfa6ec')
    
    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
    
    articles = top_headlines['articles']
    
    desc = []
    news = []
    img = []
    
    
    for i in range (len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img .append(myarticles['urlToImage'])
        
        
    mylist = zip(news,desc,img)    
    return render_template('index.html', context=mylist)