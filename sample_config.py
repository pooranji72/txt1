import os

api_id = 24454391
api_hash = os.environ.get("API_HASH", "f1cc9ff726684360e45bdc612605f30b")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5330239547,6090912349")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5330239547,6090912349")
owner_users = [int(num) for num in osowner_users.split(",")]
