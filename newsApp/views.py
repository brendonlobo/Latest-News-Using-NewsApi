from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='e9d34bc76bc34a49b2650c4e4c6a7a4a')
    headLines = newsApi.get_top_headlines(sources='google-news-in,hacker-news,the-hindu,the-times-of-india')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img,url)

    return render(request, "main/index.html", context={"mylist": mylist})

# Entertainment

def entertainment(request):
    newsApi = NewsApiClient(api_key='e9d34bc76bc34a49b2650c4e4c6a7a4a')
    headLines = newsApi.get_top_headlines(sources='buzzfeed,entertainment-weekly,ign,the-lad-bible')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img,url)

    return render(request, "main/entertainment.html", context={"mylist": mylist})

# Sports
def sports(request):
    newsApi = NewsApiClient(api_key='e9d34bc76bc34a49b2650c4e4c6a7a4a')
    headLines = newsApi.get_top_headlines(sources='espn-cric-info,bbc-sport,bleacher-report,espn,fox-sports,the-sport-bible')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img,url)

    return render(request, "main/sports.html", context={"mylist": mylist})

# technology
def technology(request):
    newsApi = NewsApiClient(api_key='e9d34bc76bc34a49b2650c4e4c6a7a4a')
    headLines = newsApi.get_top_headlines(sources='ars-technica,crypto-coins-news,engadget,hacker-news,new-scientist')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    mylist = zip(news, desc, img,url)

    return render(request, "main/technology.html", context={"mylist": mylist})