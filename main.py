import requests
from send_email import send_email

topic = "tesla"

api_key = "101530b15c094fceb483edde1cb6ae98"
url = ("https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2025-06-30&" \
       "sortBy=publishedAt&" \
       "apiKey=101530b15c094fceb483edde1cb6ae98&" \
       "language=en")

#Make a request
request = requests.get(url)

#Get a structured dictionary with data
content = request.json()

#Access the articles titles and description
body = ""
for article in content['articles']:
    if article['title'] and article['description']:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)