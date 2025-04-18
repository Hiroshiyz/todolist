import sqlite3
from models.task import Task

DATABASE_NAME = ("todo.db")


def get_connection():
    return sqlite3.connect(DATABASE_NAME)

# 初始創建表格


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """create table if not exists tasks (id integer primary key, title text not null , done integer default 0)""")
        conn.commit()


# 新增功能

def add_task(title):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""insert into tasks (title) values(?)""", (title,))
        conn.commit()

# 更新資訊 if done or not done


def mark_task_done(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""update tasks set done=1 where id=?""", (task_id,))
        conn.commit()
# search task


def get_all_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""select * from tasks""")
        results = cursor.fetchall()
        # 將list 0 , 1, 2的值重新回傳TASK 在print出來
        return [Task(id=row[0], title=row[1], done=bool(row[2])) for row in results]


def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""delete from tasks where id=?""", (task_id,))
        conn.commit()
