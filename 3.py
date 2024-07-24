import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  
            user='root',        
            password='1777',    
            port='3306',        
            database='employe'  
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_students_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                age INT,
                grade FLOAT
            )
        """)
        print("Table 'students' created successfully.")

        cursor.close()

    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

def insert_student(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES ('Alice', 'Smith', 18, 95.5)
        """)
        connection.commit()

        cursor.close()
        print("Student record inserted successfully.")

    except mysql.connector.Error as e:
        print(f"Error inserting student record: {e}")

def update_grade(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE students
            SET grade = 97.0
            WHERE first_name = 'Alice'
        """)
        connection.commit()

        cursor.close()
        print("Grade updated successfully.")

    except mysql.connector.Error as e:
        print(f"Error updating grade: {e}")

def delete_student(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM students
            WHERE last_name = 'Smith'
        """)
        connection.commit()

        cursor.close()
        print("Student deleted successfully.")

    except mysql.connector.Error as e:
        print(f"Error deleting student: {e}")

def fetch_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print("\nStudent Records:")
        for student in students:
            print(student)

        cursor.close()

    except mysql.connector.Error as e:
        print(f"Error fetching students: {e}")

def main():

    connection = connect_to_database()
    if not connection:
        return
    create_students_table(connection)
    insert_student(connection)
    update_grade(connection)
    delete_student(connection)
    fetch_students(connection)

    # Close connection
    connection.close()

if __name__ == "__main__":
    main()
