class SameUserBucketError(Exception):

  def __init__(self, user_id):
    super().__init__(f"user bucket is already exist {user_id}")

class CookieIsNoneException(Exception):

  def __init__(self):
    super().__init__("Error cookie is not exist")

class UserBucketIsNotFound(Exception):

  def __init__(self):
    super().__init__("Error User Bucket Is Not Found")

class SameIdIsExist(Exception):

  def __init__(self, user_id):
    super().__init__(f"Same Id is exist {user_id}")

class ParameterNoneError(Exception):

  def __init__(self):
    super().__init__("Error Parameter Missing")

class AlreadyItemIsExist(Exception):

  def __init__(self, item):
    super().__init__(f"Error {item} is Already Exist")
