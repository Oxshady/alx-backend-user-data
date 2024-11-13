from models.base import Base
from models.user import User

u1 = User(
        email= "bob@hbtn.io",
        _password=  "H0lbertonSchool98!",
        first_name=  "null",
        last_name=  "null",
)
x= u1.to_json()
print(x)
u1.save()