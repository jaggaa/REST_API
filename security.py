from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user = UserModel.find_by_username(username)         # instead of using in memory databse, now sqlite is used
    if user and safe_str_cmp(user.password, password):      # for string comparision(normally bhi kar sakte the)
        return user


def identity(payload):   # takes in the payload(the data encoded in the JWT—which by default is just the user ID)
    user_id = payload['identity']  # extract the user_id
    return UserModel.find_by_id(user_id)

