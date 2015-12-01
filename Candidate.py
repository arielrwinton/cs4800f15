class Candidate():
	
	def __init__(self, firstName, lastName, polParty, twitterHandle):
		self.first_name = firstName
		self.last_name = lastName
		self.party = polParty
		self.twitter_handle = twitterHandle
		self.total_mentions = 0

	def out(self):
		print self.first_name

#Class representing a candidate
#Fields:
#	first_name
#	last_name
#	party
#	twitter_handle
#	total_mentions
#	total_positive_mentions
#	total_negative_mentions
#	percent_positive
#	percent_negative


#Returns the number of tweets with mentions about this candidate before a given debate
#Input: Debate
#Output: Count of Tweets

#Returns the number of tweets with mentions about this candidate after a given debate
#Input: Debate
#Output: Count of Tweets

#Returns the number of tweets with mentions about this candidate before a given debate with a given sentiment
#Input: Debate, Sentiment
#Output: Count of Tweets

#Returns the number of tweets with mentions about this candidate after a given debate with a given sentiment
#Input: Debate, Sentiment
#Output: Count of Tweets
