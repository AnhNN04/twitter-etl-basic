# import some essential libraries
import pandas as pd 
import tweepy
from datetime import datetime
import json

# keys for access twitter API
# consumer keys
api_key = "Byh5gA0G6zhyaDlRYyenAiOmn"
api_key_secret = "1R4dpkNzHGIZFudfnHThAAKyxVS2CWGEkJ0w2ANbXhZkEumylT"

# authentication tokens
# bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMPWtQEAAAAASFZXVA2vUTfiBVSODNVKhaYAbxw%3DPRwntLNJYsZJzX7kvmRxTtyG2TCz8yKe2ZpFHpu8Y8lHjyE9UY"

# access token and secret
access_token = "1782676636384759808-YpfcZSQWNPurM2eN9ZQDtTr9dsUpYz"
access_token_secret = "Yh2uQDJA2IdmuXL8wx338VCmknEER7mmZHbiadi2aPQWB"

# Twitter authentication
auth = tweepy.OAuth2UserHandler(access_token, access_token_secret)
auth.set_access_token(api_key, api_key_secret)

# create an API object
api = tweepy.API(auth)

tweets = api.home_timeline()
print(tweets)

