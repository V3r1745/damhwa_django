class EmptyResult(Exception):

  def __init__(self):
    super().__init__("Error: Empty Result")

class EmptyQuery(Exception):

  def __init__(self, *args):
    super().__init__(" ".join(["Error: Empty Value", *args]))

class SameAccountException(Exception):

  def __init__(self, id):
    super().__init__(f"Error {id} is Already Exist")

class WrongSyntax(Exception):

  def __init__(self, *args):
    super().__init__(" ".join(["Wrong Syntax check", *args]))

class NotMatched(Exception):

  def __init__(self):
    super().__init__("Not Matched")
