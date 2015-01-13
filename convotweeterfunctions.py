import requests
import re
import time
from datetime import date
from time import strftime

def RetrieveTodaysDate():
    today = date.today()
    today = today.strftime("%m/%d")
    today = "1/23"
    return today

def NotFound(curr_speaker, todays_date):
    speaker_date = re.search('[0-9]+/[0-9]+', str(curr_speaker)).group(0)
    print "Speaker date " + speaker_date
    print "Today's date " + todays_date
    if (speaker_date == todays_date):
        return False
    else:
        # print "Speaker date not matched"
        return True


def ComposeTweet(curr_speaker, todays_date):
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


def TweetTweet(tweet):
    post = api.request('statuses/update', {'status': tweet})

    print('SUCCESS' if post.status_code == 200 else 'FAILURE')
