import argparse
from reddit_replier.reddit_replier import RedditReplier
from reddit_replier.logger import logger

__version__ = '0.0.0'

def match_function(comment):
    return any(string in comment.body.lower() for string in ['find the thing silly bot'])
def comment_function(comment):
    return "I'm a bot, and this is a comment."

def main():
    parser = argparse.ArgumentParser(description='Auto reply to reddit.')
    parser.add_argument('username', help='username used to authenticate the bot')
    parser.add_argument('password', help='password used to authenticate the bot')
    parser.add_argument('client_id', help='client_id used to authenticate the bot')
    parser.add_argument('client_secret', help='client_secret used to authenticate the bot')
    parser.add_argument('-s','--subreddit', default='all', help='subreddit for the bot to listen on. Default all')
    args = parser.parse_args()
    replier = RedditReplier(args.username,args.password,args.client_id, args.client_secret)
    replier.run(match_function,comment_function)

if __name__ == '__main__':
    try: main()
    except: raise
