import praw
from var_dump import var_dump

print "Initializing PRAW and User Agent"
user_agent = ("the_nano_bot/0.1 by nanodano")
r = praw.Reddit(user_agent=user_agent)

print "Loading User"
user_name = "nanodano"
user = r.get_redditor(user_name)

thing_limit = 200 
gen = user.get_comments(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
					+ thing.ups - thing.downs)

var_dump(karma_by_subreddit)