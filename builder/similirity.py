
from register.models import User

import pandas as pd
from collections import defaultdict

from surprise import NormalPredictor
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import SVD

from time import sleep

class Predictions:
	def __init__(self):
		self.predictions = []
	def getPrediction(UserId):
		return self.predictions[UserId]
	def startGenerating():
		
		while (True):
			def get_top_n(predictions, n=10):
			    top_n = defaultdict(list)
			    for uid, iid, true_r, est, _ in predictions:
			        top_n[uid].append((iid, est))
			    for uid, user_ratings in top_n.items():
			        user_ratings.sort(key=lambda x: x[1], reverse=True)
			        top_n[uid] = user_ratings[:n]
			    return top_n

			ratings_dict = {
				"userID": [1,1,3,4,4,6],
				"POIID":  [1,2,1,4,2,6],
				"rating": [5,5,1,4,5,3],
			}

			users = User.objects()
			for user in users:
				print(user)
				'''
				for rating in user:
					rating_dict.POIId.append(rating.POIId)
					rating_dict.userId.append(user.id)
					rating_dict.raging.append(rating) '''


			frame = pd.DataFrame(ratings_dict)

			print(frame)
			reader = Reader(rating_scale=(1, 5))

			data = Dataset.load_from_df(frame[['userID', 'POIID', 'rating']], reader)

			cross_validate(NormalPredictor(), data, cv=2)


			trainset = data.build_full_trainset()
			algo = SVD()
			algo.fit(trainset)

			testset = trainset.build_anti_testset()
			predictions = algo.test(testset)

			top_n = get_top_n(predictions, n=10)
			print(predictions)
			for uid, user_ratings in top_n.items():
			    print(uid, [iid for (iid, _) in user_ratings])
			sleep(10)


