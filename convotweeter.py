from TwitterAPI import TwitterAPI
consumer_key = "xEcJxElLrGa2dmeJqQhW9hL7K"
consumer_sec = "QOl78B7RhHoY4Js34zyHBihBqKl52bMyQSw46wbO3eb3jjBJF9"
access_key = "2950254105-FsJMleHL8q8aSE3wJj0I0uD8oeSg8M1IO9pJqv8"
access_sec = "KDmSQM6bgn0T1dJUQjU5XKu1uZ7PMljQVAJZDND51PDjq"

api = TwitterAPI(consumer_key, consumer_sec, access_key, access_sec)

count = 0

import requests
import re
from bs4 import BeautifulSoup
import time
from datetime import date
from time import strftime
data = requests.get("https://www.liberty.edu/index.cfm?PID=2586")
today = date.today()
today = today.strftime("%m/%d")
print today

# Todays Date
todays_date = str(today)
todays_date = "9/17"

# Grab the HTML content
html = data.text
soup = BeautifulSoup(html)

# Get the first speaker
curr_speaker = soup.h1.next_sibling.next_sibling
print curr_speaker

def NotFound():
    speaker_date = re.search('[0-9]+/[0-9]+', str(curr_speaker)).group(0)
    print "Speaker date " + speaker_date
    print "Today's date " + todays_date
    if (speaker_date == todays_date):
        return False
    else:
        # print "Speaker date not matched"
        return True


while NotFound():
    # Go to the next speaker in the list
    temp = curr_speaker.next_sibling
    curr_speaker = temp.next_sibling

def ComposeTweet():
    # Speakers Name
    speaker_name = curr_speaker.a.string
    print speaker_name

    # Speakers Website
    speaker_site = curr_speaker.a.get('href')
    print speaker_site

    # Topical Week
    if curr_speaker.find('em') == None:
        topic = ""
    else:
        topic = curr_speaker.em.extract()
    print topic

    # Description of the Speaker
    speaker_desc = re.search("[||].*", str(curr_speaker)).group(0)
    print speaker_desc
    speaker_desc = speaker_desc.replace("|", "").lstrip()
    result = re.search('<.*>',str(speaker_desc)).group(0)
    print "Result: " + result
    speaker_desc = speaker_desc.replace(result, "")
    print speaker_desc



    # Composed Tweet
    composed_tweet = todays_date + "\n" + speaker_name + "\n" + speaker_desc + "\n" + speaker_site

    return composed_tweet

def TweetTweet():
    tweet = api.request('statuses/update', {'status': ComposeTweet()})

    print('SUCCESS' if tweet.status_code == 200 else 'FAILURE')


TweetTweet()
