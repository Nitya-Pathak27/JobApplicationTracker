from db import db, cursor

# create new user
def create_user(name, email, hashed_password):
    query = """
        INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
    """
    values = (name, email, hashed_password)
    cursor.execute(query, values)
    db.commit()

# fetch user by email
def fetch_user_by_email(email):
    query = """
    SELECT * FROM users WHERE email = %s
    """
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    return user

def update_user_password(email, hashed_password):
    query = """
    UPDATE users SET password = %s WHERE email = %s
    """
    values = (hashed_password, email)
    cursor.execute(query, values)
    db.commit()