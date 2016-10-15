"""
Analyze word frequency in subreddit post titles
Outputs the number of times a word is seen and orders them
by the most used words.

Quick and dirty script that is not optimized
nanodano@devdungeon.com
www.devdungeon.com
"""
min_word_length = 5 # Ignore words shorter than this length
min_word_frequency = 4 # Only show words seen at least this many times
subreddit = 'houston'
request_limit = 1000 # Max 1000

import operator
import praw
import re

user_agent = ("Houston Subreddit Analyzer/0.1 by nanodano@devdungeon.com")
reddit = praw.Reddit(user_agent=user_agent)

wordbank = dict()
count = 1

posts = reddit.get_subreddit(subreddit).get_hot(limit=request_limit)
for post in posts:
	count += 1
	title = str(post).split(' :: ')[1] # First value is upvotes followed by ::
	words = title.split()
	for word in words:
		# Strip special chars
		word = re.sub('[^a-zA-Z0-9]', '', word)
		# Ignore anything less than 4 chars
		if len(word) < min_word_length:
			continue
		# Lowercase to normalize
		word = word.lower()
		if not word in wordbank:
			wordbank[word] = 1
		else:
			wordbank[word] += 1

sorted_words = sorted(wordbank.items(), key=operator.itemgetter(1))
sorted_words.reverse()

print "Processed " + repr(count) + " post titles."
for word in sorted_words:
	# Ignore word that were seen less than X times
	if word[1] > min_word_frequency - 1:
		print repr(word[1]) + " " + word[0]
