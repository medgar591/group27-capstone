import sqlite3, csv

from sqlite3 import Error


# create the database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# create the function to run queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")

        rows = cursor.fetchall()
        for row in rows:
            for col in row:
                print
                "%s," % col
            print
            "\n"
    except Error as e:
        print(f"The error '{e}' occurred")


# break the csv document into chunks
def chunks(data, rows=10000):
    """ Divides the data into 10000 rows each """
    # get rid of the header of the file
    for j in range(1, len(data), rows):
        yield data[j:j+rows]


def select_all_tasks(conn, table_name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name + " LIMIT 10")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def insert_data():
    conn = sqlite3.connect("capstone.sqlite")
    # conn.text_factory = str  # bugger 8-bit bytestrings
    cur = conn.cursor()

    for i in range(9):
        filename = "Data " + str(i) + " .csv"
        csvData = csv.reader(open(filename, "r"))
        csvData = list(csvData)

        divData = chunks(csvData)  # divide into 10000 rows each

        for chunk in divData:
            cur.execute('BEGIN TRANSACTION')

            for PATIENT_ID, BED_ID, HEART_RATE, O2, BLOOD_PRESSURE, TIME in chunk:
                cur.execute(
                    'INSERT INTO Data (PATIENT_ID, BED_ID, HEART_RATE, O2, BLOOD_PRESSURE, TIME) VALUES (?,?,?,?,?,?)',
                    (PATIENT_ID, BED_ID, HEART_RATE, O2, BLOOD_PRESSURE, TIME))

            cur.execute('COMMIT')

    select_all_tasks(conn, "Data")


def insert_patient():
    conn = sqlite3.connect("capstone.sqlite")
    # conn.text_factory = str  # bugger 8-bit bytestrings
    cur = conn.cursor()

    csvData = csv.reader(open("PatientData.csv", "r"))
    csvData = list(csvData)

    divData = chunks(csvData)  # divide into 10000 rows each

    for chunk in divData:
        cur.execute('BEGIN TRANSACTION')

        for PATIENT_ID, AGE_WEEKS, GENDER, WEIGHT, HEIGHT in chunk:
            cur.execute(
                'INSERT INTO Patient (PATIENT_ID, AGE_WEEKS, GENDER, WEIGHT, HEIGHT) VALUES (?,?,?,?,?)',
                (PATIENT_ID, AGE_WEEKS, GENDER, WEIGHT, HEIGHT))

        cur.execute('COMMIT')

    select_all_tasks(conn, "Patient")

if __name__ == "__main__":
    # create a connection to the database
    connect = create_connection("capstone.sqlite")

    create_patient_table = """
    CREATE TABLE IF NOT EXISTS Patient (
      PATIENT_ID INTEGER,
      AGE_WEEKS TEXT NOT NULL,
      GENDER TEXT,
      WEIGHT TEXT,
      HEIGHT TEXT
    );
    """

    create_data_table = """
    CREATE TABLE IF NOT EXISTS Data (
      PATIENT_ID INTEGER , 
      BED_ID INTEGER,
      HEART_RATE INTEGER,
      O2 INTEGER,
      BLOOD_PRESSURE TEXT,
      TIME INTEGER
    );
    """

    # create the data tables
    execute_query(connect, create_patient_table)
    execute_query(connect, create_data_table)

    insert_data()
    insert_patient()
