from mastodon import Mastodon

access_tkn = input(f'Enter your access token: ')
api_url = input(f'Enter the Mastodon server URL you are logging into: ')

user_input = input(f'Please enter your toot: ')

Mastodon = Mastodon(access_token = access_tkn, api_base_url = api_url)
Mastodon.toot(user_input)

