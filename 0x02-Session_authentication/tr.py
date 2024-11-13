from models.user import User
from datetime import datetime

# Data to insert into the database
user_data = {
    "af064164-9ec9-4f20-9a27-f34016109f00": {
        "id": "af064164-9ec9-4f20-9a27-f34016109f00",
        "created_at": "2024-11-12T17:51:00",
        "updated_at": "2024-11-12T17:51:00",
        "email": "bob@hbtn.io",
        "_password": "a5c904771b8617de27d3511d1f538094e26c120da663363b3f760f7b894f9d69",
        "first_name": None,
        "last_name": None
    }
}

# Extract user information
user_info = user_data["af064164-9ec9-4f20-9a27-f34016109f00"]

# Create a new User instance
user = User()

# Set user details
user.id = user_info["id"]
user.created_at = datetime.strptime(user_info["created_at"], "%Y-%m-%dT%H:%M:%S")
user.updated_at = datetime.strptime(user_info["updated_at"], "%Y-%m-%dT%H:%M:%S")
user.email = user_info["email"]
user.password = user_info["_password"]
user.first_name = user_info["first_name"]
user.last_name = user_info["last_name"]

# Save the user to the database
user.save()

print(f"User {user.id} inserted successfully!")
