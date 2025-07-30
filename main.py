import requests

api_key = "101530b15c094fceb483edde1cb6ae98"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2025-06-30&sortBy=publishedAt&apiKey" \
       "=101530b15c094fceb483edde1cb6ae98")

#Make a request
request = requests.get(url)

#Get a structured dictionary with data
content = request.json()

#Access the articles titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])