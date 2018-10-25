import praw
import logging

logger = logging.getLogger('reddit_replier')

class RedditReplier(object):
    def __init__(self,username,password,client_id,client_secret, subreddit='all'):
        """Initialize RedditReplier

        :param username: Username used to authenticate to reddit.
        :param password: Password used to authenticate to reddit.
        :param client_id: Client Id used to authenticate to reddit.
        :param client_secret: Client Secret used to authenticate to reddit.
        :param subreddit: Subreddits to subscribe to. (Default value = 'all')
        """
        self.reddit = praw.Reddit(user_agent="redditreplier",
                                  client_id=client_id,
                                  client_secret=client_secret,
                                  username=username,
                                  password=password)
        self.subreddit = subreddit
 
    def run(self,match_function,comment_function):
        """Runs the bot
        """
        handled = []
        comments = self.reddit.subreddit(self.subreddit).stream.comments()
        for comment in comments:
            if match_function(comment) and comment.id not in handled:
                #print(comment.body)
                print(comment.__dict__)
                comment.reply(comment_function(comment))
                handled.append(comment.id)
        return True    
