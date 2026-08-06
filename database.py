import sqlite3

import os





# ==========================================

# Database Path

# ==========================================



DATABASE = os.path.join(

    os.path.dirname(__file__),

    "database.db"

)





# ==========================================

# Database Connection

# ==========================================



def get_connection():



    conn = sqlite3.connect(DATABASE)



    return conn







# ==========================================

# Create Users Table

# ==========================================
def create_users_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fullname TEXT NOT NULL,

        username TEXT UNIQUE NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()
# ==========================================

# Create Students Table

# ==========================================



def create_students_table():



    conn = get_connection()

    cursor = conn.cursor()





    cursor.execute("""

    CREATE TABLE IF NOT EXISTS students(



        id INTEGER PRIMARY KEY AUTOINCREMENT,



        name TEXT,



        attendance REAL,



        study_hours REAL,



        assignments INTEGER,



        internal_marks REAL,



        previous_gpa REAL,



        internet_usage REAL,



        gender TEXT,



        extracurricular TEXT,



        prediction TEXT,



        confidence REAL,



        performance REAL,



        grade TEXT,



        badge TEXT,



        risk TEXT



    )

    """)





    conn.commit()

    conn.close()







# ==========================================

# Register User

# ==========================================



def register_user(

        fullname,

        username,

        email,

        password

):



    conn = get_connection()

    cursor = conn.cursor()





    try:



        cursor.execute(

        """

        INSERT INTO users

        (

            fullname,

            username,

            email,

            password

        )



        VALUES(?,?,?,?)



        """,



        (

            fullname,

            username,

            email,

            password

        )

        )





        conn.commit()



        return True





    except sqlite3.IntegrityError:



        return False





    finally:



        conn.close()







# ==========================================

# Login User

# ==========================================
def login_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    print("LOGIN CHECK:")
    print("Username:", username)
    print("Password:", password)
    print("Result:", user)

    conn.close()

    return user
# ==========================================
# Add Student
# ==========================================

def add_student(student):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (
            name,
            attendance,
            study_hours,
            assignments,
            internal_marks,
            previous_gpa,
            internet_usage,
            gender,
            extracurricular,
            prediction
        )
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """,
        (
            student[1],   # name
            student[4],   # attendance
            student[5],   # study_hours
            student[6],   # assignments
            student[7],   # internal_marks
            student[8],   # previous_gpa
            student[9],   # internet_usage
            student[3],   # gender
            student[10],  # extracurricular
            student[11]   # result
        )
    )

    conn.commit()
    conn.close()
     
# ==========================================

# View Students

# ==========================================



def view_students():



    conn = get_connection()



    cursor = conn.cursor()





    cursor.execute(

        "SELECT * FROM students"

    )





    data = cursor.fetchall()





    conn.close()





    return data









# ==========================================

# Delete Student

# ==========================================



def delete_student(student_id):



    conn = get_connection()



    cursor = conn.cursor()





    cursor.execute(

    """

    DELETE FROM students

    WHERE id=?

    """,

    (student_id,)

    )





    conn.commit()



    conn.close()







# ==========================================

# Initialize Database

# ==========================================



def initialize_database():



    create_users_table()



    create_students_table()





    print("✅ Database created successfully")







if __name__ == "__main__":



    initialize_database()

