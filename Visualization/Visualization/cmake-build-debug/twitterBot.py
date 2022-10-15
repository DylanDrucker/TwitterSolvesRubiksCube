from credentials import API_SECRET, API_KEY, ACCESS_TOKEN, ACCESS_SECRET

import tweepy
import logging
import os
import json

logger = logging.getLogger()

def create_api(API_SECRET, API_KEY, ACCESS_TOKEN, ACCESS_SECRET):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("credentials verified")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        print("error verifying credentials")
        raise e
    logger.info("API created")
    return api

# function to get tweets in mentions timeline that have the keyword
def get_tweets(api, keyword, latest_id_after_process):
    new_id = latest_id_after_process
    for twt in tweepy.Cursor(api.mentions_timeline, since_id=new_id).items():
        if twt.in_reply_to_status_id is not None and keyword in twt.text.lower():
            new_id = max(twt.id, new_id)
            
            replys = get_replys(api, twt.id)

            base_id = create_thread(api, replys[0], replys[1])
            
            reply_by_me = api.update_status(
                status="@{} Hi! Here's a thread with all the replies:"
                       " https://twitter.com/your_username/status/{}" #put the twitter username in place of "your_username" without @ with which API is authenticated 
                .format(twt.user.screen_name, base_id), in_reply_to_status_id=new_id)
            
            logger.info("reply to mention created")

    return new_id

# mini funcion to get 'sibling' tweets of the tweet id entered
def get_replys(api, twt_id):
    twt = api.get_status(id=twt_id)
    parent_twt_id = twt.in_reply_to_status_id
    parent_twt = api.get_status(id=parent_twt_id)
    replys = []
    req_count = 1
    for mention in tweepy.Cursor(api.search_tweets
                                 ,q="@{}".format(parent_twt.user.screen_name)
                                 ,since_id=parent_twt_id
                                 ,tweet_mode="extended"
                                 ,result_type='recent').items(500):
        req_count = req_count + 1
        logger.info("checking {} mentions of parent user".format(req_count))
        if req_count < 400:
            if mention.in_reply_to_status_id == parent_twt_id:
                range = mention.display_text_range
                reply_full_text = mention.full_text
                only_text = reply_full_text[range[0]:range[1]]
                tweeter_name = mention.user.screen_name
                reply = only_text + " | " + "by {}".format(tweeter_name)
                replys.append(reply)
                logger.info("sibling extracted")
            else:
                logger.info("no replys in mentions found")
        else:
            logger.info("request limit reached")
            time.sleep(1000)
            req_count = 0

    logger.info("recieved {} relpies".format(len(replys)))
    
    my_base_tweet = "{} asked {}".format(parent_twt.user.screen_name, parent_twt.full_text)
    
    return replys, my_base_tweet

def main():
    print(create_api(API_SECRET, API_KEY, ACCESS_TOKEN, ACCESS_SECRET))
main()
