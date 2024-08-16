from google_play_scraper import reviews, app, Sort
from textblob import TextBlob
from summarizer_code import summarize

appid = input("Enter the App Link: ")[46:].split('&pcampaignid=')[0]
N = 1000  # reviews count

result = reviews(
    appid,
    count=N,
    country='us',
    lang='en'
)


if len(result[0]) == N:
    s = 0
    content = []
    for review in result[0]:
        text = review['content']
        pol = TextBlob(text).sentiment.polarity
        s += pol

        if pol < 0:
            content.append(text)

    if s / N >= 0:
        print('Not fraudulent')

    else:
        print('likely fraudulent')
        print('\nReviews Summary\n')
        print(summarize(content))
else:
    print("The Reviews are less than the threshold to check whether the application if fraudulent or not!\n")
    about_app = app(appid)
    details = ["title", "containsAds", "developer", "developerEmail", "developerWebsite", "free", "genre",
               "inAppProductPrice", "realInstalls", "released", "score"]

    for cat in details:
        print(f'{cat.title()}: {about_app[cat]}')
