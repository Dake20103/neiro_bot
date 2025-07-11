import json
import os
from datetime import datetime, timedelta

USERS_FILE = "users.json"
VIP_DAYS = 30
FREE_VIDEO_LIMIT = 7

def load_users():
    if not os.path.exists(USERS_FILE):
            return {}
                with open(USERS_FILE, 'r') as f:
                        return json.load(f)

                        def save_users(users):
                            with open(USERS_FILE, 'w') as f:
                                    json.dump(users, f)

                                    def is_vip(user_id):
                                        users = load_users()
                                            user = users.get(str(user_id))
                                                if not user or not user.get("vip_until"):
                                                        return False
                                                            vip_until = datetime.strptime(user["vip_until"], "%Y-%m-%d")
                                                                return vip_until >= datetime.today()

                                                                def add_vip(user_id):
                                                                    users = load_users()
                                                                        vip_until = datetime.today() + timedelta(days=VIP_DAYS)
                                                                            users[str(user_id)] = {
                                                                                    "vip_until": vip_until.strftime("%Y-%m-%d"),
                                                                                            "used": 0
                                                                                                }
                                                                                                    save_users(users)

                                                                                                    def get_remaining_uses(user_id):
                                                                                                        users = load_users()
                                                                                                            user = users.get(str(user_id), {})
                                                                                                                return max(0, FREE_VIDEO_LIMIT - user.get("used", 0))

                                                                                                                def add_user_usage(user_id):
                                                                                                                    users = load_users()
                                                                                                                        if str(user_id) not in users:
                                                                                                                                users[str(user_id)] = {"used": 1}
                                                                                                                                    else:
                                                                                                                                            users[str(user_id)]["used"] = users[str(user_id)].get("used", 0) + 1
                                                                                                                                                save_users(users)
                                                                                                                                