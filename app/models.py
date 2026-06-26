from database import get_connection

def add_note(title, content):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s)",
            (title, content)
        )
    connection.close()

def get_all_notes():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
        notes = cursor.fetchall()
    connection.close()
    return notes

def get_note_by_id(note_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
        note = cursor.fetchone()
    connection.close()
    return note

def update_note(note_id, title, content):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE notes SET title = %s, content = %s WHERE id = %s",
            (title, content, note_id)
        )
    connection.close()

def delete_note(note_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    connection.close()

def search_notes(keyword):
    connection = get_connection()
    with connection.cursor() as cursor:
        like_pattern = f"%{keyword}%"
        cursor.execute(
            "SELECT * FROM notes WHERE title LIKE %s OR content LIKE %s ORDER BY created_at DESC",
            (like_pattern, like_pattern)
        )
        results = cursor.fetchall()
    connection.close()
    return results
