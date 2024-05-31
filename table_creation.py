import sqlite3

connection_obj = sqlite3.connect('database.db')

cursor_obj = connection_obj.cursor()

table = """ CREATE Table IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT NOT NULL); """
table2 = """ CREATE Table IF NOT EXISTS post (post_id INTEGER PRIMARY KEY, title TEXT NOT NULL, created_at
    TIMESTAMP, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id)); """
table3 = """ CREATE Table IF NOT EXISTS comment (comment_id INTEGER PRIMARY KEY, title TEXT NOT NULL, created_at TIMESTAMP, 
user_id INTEGER, parent_comment_id INTEGER REFERENCES comment(comment_id), is_parent BOOLEAN, post_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(post_id) REFERENCES post(post_id)); """
table4 = """ CREATE Table IF NOT EXISTS post_likes_dislikes (id INTEGER PRIMARY KEY, post_id INTEGER, knowledge_begin_date
    TIMESTAMP, likes INTEGER, dislikes INTEGER, FOREIGN KEY(post_id) REFERENCES post(post_id)); """
table5 = """ CREATE Table IF NOT EXISTS post_likes (id INTEGER PRIMARY KEY, user_id INTEGER, knowledge_begin_date TIMESTAMP, knowledge_end_date TIMESTAMP, post_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(post_id) REFERENCES post(post_id)); """
table6 = """ CREATE Table IF NOT EXISTS post_dislikes (id INTEGER PRIMARY KEY, user_id INTEGER, knowledge_begin_date TIMESTAMP, knowledge_end_date TIMESTAMP, post_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(post_id) REFERENCES post(post_id)); """
table7 = """ CREATE Table IF NOT EXISTS comment_likes (id INTEGER PRIMARY KEY, user_id INTEGER, knowledge_begin_date TIMESTAMP, knowledge_end_date TIMESTAMP, comment_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(comment_id) REFERENCES comment(comment_id)); """
table8 = """ CREATE Table IF NOT EXISTS comment_dislikes (id INTEGER PRIMARY KEY, user_id INTEGER, knowledge_begin_date TIMESTAMP, knowledge_end_date TIMESTAMP, comment_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(comment_id) REFERENCES comment(comment_id)); """
table9 = """ CREATE Table IF NOT EXISTS comment_likes_dislikes (id INTEGER PRIMARY KEY, comment_id INTEGER, knowledge_begin_date
    TIMESTAMP, likes INTEGER, dislikes INTEGER, FOREIGN KEY(comment_id) REFERENCES comment(comment_id)); """
# tabletemp = """ DROP TABLE user; """
# tabletemp1 = """ DROP TABLE post; """
# tabletemp2 = """ DROP TABLE comment; """
# tabletemp3 = """ DROP TABLE post_likes_dislikes; """
# tabletemp4 = """ DROP TABLE post_likes; """
# tabletemp5 = """ DROP TABLE post_dislikes; """
# tabletemp6 = """ DROP TABLE comment_likes; """
# tabletemp7 = """ DROP TABLE comment_dislikes; """
# tabletemp8 = """ DROP TABLE comment_likes_dislikes; """
# table10 = """ALTER TABLE comment ADD FOREIGN KEY(parent_comment_id) REFERENCES comment(comment_id)"""
# tabletemp9 = """PRAGMA foreign_keys = ON;"""


def creation():
    cursor_obj.execute(table)
    cursor_obj.execute(table2)
    cursor_obj.execute(table3)
    cursor_obj.execute(table4)
    cursor_obj.execute(table5)
    cursor_obj.execute(table6)
    cursor_obj.execute(table7)
    cursor_obj.execute(table8)
    cursor_obj.execute(table9)
    connection_obj.close()
