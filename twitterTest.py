import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "niJqBHvcmyePEiiD1LHFI1HnO",
    "consumer_secret"     : "ug2mObU0N2NQ0RzSSlF5J0w0QOliFmdDjQA7FWYd4zKk2qWjit",
    "access_token"        : "25709895-Qy9pZeLoOXGHZT9D3C1LNKZcLDc0DbqQpkBjooLka",
    "access_token_secret" : "74AA4gcJDMbNfExZhBEE3XeCDlJhwnnKaga51wU9nTr2p" 
    }

  api = get_api(cfg)
  tweet = "oi alex teste"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()