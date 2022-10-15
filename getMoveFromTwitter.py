import tweepy
from collections import Counter
import time
import datetime

TWITTER_ID = 1581212127314038785

def get_replies(tweet_ID, client):
    query = f"conversation_id:{tweet_ID} is:reply"
    
    
    time = datetime.datetime.utcnow()
    start_time = time - datetime.timedelta(seconds=30)
    replies = client.search_recent_tweets(query=query, start_time = start_time)
    moves = []
    if not replies.data:
        return moves
    for reply in replies.data:
        moves.append(get_move_from_reply(reply.text))
    return moves

def get_move_from_reply(s):
    if s[0] == '@':
        s = s.split(' ')
        return s[1]
    else:
        return s
valid_moves = {"U", "D", "R","L", "F", "B","U'", "D'", "R'", "L'", "F'", "B'","U2", "D2", "R2", "L2", "F2", "B2"}
    
def most_popular_move(moves):
    if moves == []:
        return "No Move"
    data = Counter(moves)
    while data:
        most_popular =  max(moves, key=data.get)
        if most_popular not in valid_moves:
            data.remove(most_popular)
        else:
            return most_popular
    return "No Move"


def get_requested_move(tweet_id):
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAALPiAEAAAAAOGphw20VL7GidOsd8K6h83egE6M%3D0dwYQfywcTDifl55V9lM9KMTh4ntWvoUAR9fsZuiE4sxqoMyrH"
    client = tweepy.Client(bearer_token)
    replies = get_replies(tweet_id, client)
    move = most_popular_move(replies)
    return move

def write_move_to_file():
    TWITTER_ID = "1581226321992380421"
    f = open("move.txt", 'w')
    f.write(get_requested_move(TWITTER_ID))
    f.close()

def main():
    while True:
        write_move_to_file()
        time.sleep(30)
main()