import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Vulnerable query
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)

    data = cursor.fetchall()
    conn.close()
    return data

username_input = input("Enter your username: ")
print(get_user_data(username_input))
