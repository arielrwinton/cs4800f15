from TwitterSearch import *
import datetime
from candidate import Candidate


class DataPuller():

	start_time = datetime.date(2015, 11, 14)
	two_days_after_start = datetime.date(start_time.year, start_time.month, start_time.day + 2)
	hillary_clinton = Candidate('Hillary', 'Clinton', 'democratic', '@HillaryClinton')
	martin_omalley = Candidate('Martin', 'O\'Malley', 'democratic', '@MartinOMalley')
	bernie_sanders = Candidate('Bernie', 'Sanders', 'democratic', '@BernieSanders')
	donald_trump = Candidate('Donald', 'Trump', 'republican', '@realDonaldTrump')
	ben_carson = Candidate('Ben', 'Carson', 'republican', '@RealBenCarson')
	marco_rubio = Candidate('Marco', 'Rubio', 'republican', '@marcorubio')
	ted_cruz = Candidate('Ted', 'Cruz', 'republican', '@tedcruz')
	jeb_bush = Candidate('Jeb', 'Bush', 'republican', '@JebBush')
	list_of_candidates = [hillary_clinton, martin_omalley, bernie_sanders, donald_trump, ben_carson, marco_rubio, ted_cruz, jeb_bush]
	f1 = 'hillary_metadata.txt'
	f2 = 'martin_metadata.txt'
	f3 = 'bernie_metadata.txt'
	f4 = 'donald_metadata.txt'
	f5 = 'ben_metadata.txt'
	f6 = 'marco_metadata.txt'
	f7 = 'ted_metadata_copy.txt'
	f8 = 'jeb_metadata_copy.txt'
	list_of_files = [f1, f2, f3, f4, f5, f6, f7, f8]

	for i in range(0, len(list_of_candidates)):
		this_candidate = list_of_candidates[i]
		this_file = open(list_of_files[i], 'w')

		tso = TwitterSearchOrder() 
		tso.set_keywords([this_candidate.twitter_handle]) 
		tso.set_language('en') 
		tso.set_until(two_days_after_start)

		tso.set_include_entities(False) 

		ts = TwitterSearch(consumer_key='qOV5dW3fa19JjjN3XgmJvU0OI',
			consumer_secret='c79hpJmSq9XNvXPVsHJSZ6GJvkarNy4LWekI8CaQuKOGIYR4ap',
			access_token='2326087195-KICgFqT7Io8uEiQkKLsWMJZDyzWHvsubFvCdqkf',
			access_token_secret='Rj7qWlNZD1jlUADMeVD8cBgxJXaGY0XgWJ7aLpbgDmaBt')

		for tweet in ts.search_tweets_iterable(tso):
			data_to_write = 'Date: ' + tweet['created_at'] + ', Text: ' + tweet['text'] + ', '
			this_file.write(data_to_write.encode('utf-8'))
			this_candidate.total_mentions = this_candidate.total_mentions + 1
		total_mentions_to_write = 'Total mentions: ' + str(this_candidate.total_mentions)
		this_file.write(total_mentions_to_write.encode('utf-8'))
		this_file.close()

	for candidate in list_of_candidates:
		print 'Candidate: ' + candidate.first_name + ' Mentions: ' + str(candidate.total_mentions) + '\n'

#Get all of the Tweets for 24 hours before the debate start time
#Input: None
#Output: List of Tweets

#Get all of the Tweets for 24 hours after the debate start time 
#Input: None
#Output: List of Tweets

#Return a list of candidates in order of positive mentions as a percentage of all 
#mentions given a sort order and a designation of pre-debate or post-debate
#Input: Sort Order, Period 
#Output: Ordered List of Candidates

#Return a list of candidates in order of negative mentions as a percentage of all
#mentions given a sort order and a designation of pre-debate or post-debate
#Input: Sort Order, Period 
#Output: Ordered List of Candidates

#Return a list of candidates in order of number of mentions given a sort order
#and a designation of pre-debate or post-debate
#Input: Sort Order, Period 
#Output: Ordered List of Candidates

#Returns a list of candidates by number of positive mentions as a percentage of all positive mentions
#given a sort order and a designation of pre-debate or post-debate
#Input: Sort Order, Period
#Output: Ordered List of Candidates
