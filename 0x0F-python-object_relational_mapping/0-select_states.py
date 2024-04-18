import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)
        cursor = conn.cursor()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")
        sys.exit(1)

    # Query to retrieve states from the database
    query = "SELECT * FROM states ORDER BY states.id ASC"

    # Execute the query and fetch results
    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        sys.exit(1)

    # Display results
    for state in states:
        print(state)

    # Close connections
    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = 'root'
    password = 'root'
    database_name = 'hbtn_0e_0_usa'

    list_states(username, password, database_name)
