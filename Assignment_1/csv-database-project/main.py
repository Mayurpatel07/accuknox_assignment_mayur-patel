import csv
from database import create_database, insert_users, get_users

users = []

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        users.append({
            "name": row["name"],
            "email": row["email"]
        })

create_database()
insert_users(users)

users = get_users()

for user in users:
    print(user)