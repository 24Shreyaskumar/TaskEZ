'''Database Repositories'''

from datetime import datetime, timezone

class UserRepository:
    '''User repository to manage users'''
    def __init__(self, db):
        self.db = db

    def create_table(self):
        '''Create users table'''
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL)
        """)

    def add_user(self, user_name):
        '''add given user to users'''
        cursor = self.db.execute("""
            INSERT INTO users (user_name) VALUES (?)""", (user_name,)
        )

        return cursor.lastrowid

    def get_user(self, user_id):
        '''get given user from users'''
        cursor = self.db.execute("""
            SELECT * FROM users WHERE user_id = (?)""", (user_id,)
        )

        return cursor.fetchone()

    def delete_user(self, user_id):
        '''delete given user from users'''
        self.db.execute("""
            DELETE FROM users WHERE user_id = (?)""", (user_id,)
        )

    def reset_table(self):
        '''reset users table'''
        self.db.execute("""
            DELETE FROM users
        """)

    def delete_table(self):
        '''delete user table'''
        self.db.execute("""
            DROP TABLE users
        """)


class TaskRepository:
    '''Task repository to manage tasks'''
    def __init__(self, db):
        self.db = db

    def create_table(self):
        '''create tasks table'''
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                task_score INTEGER DEFAULT 0,
                task_deadline DATETIME DEFAULT NULL)
        """)

    def add_task(self, task_name, task_score=0, task_deadline=None):
        '''add task to tasks'''
        cursor = self.db.execute("""
            INSERT INTO tasks (task_name, task_score, task_deadline) VALUES (?, ?, ?)""", 
            (task_name, task_score, task_deadline,)
        )

        return cursor.lastrowid

    def get_task(self, task_id):
        '''get a task from tasks'''
        cursor = self.db.execute("""
            SELECT * FROM tasks WHERE task_id = (?)""", (task_id,)
        )

        return cursor.fetchone()

    def delete_task(self, task_id):
        '''delete given task from tasks'''
        self.db.execute("""
            DELETE FROM tasks WHERE task_id = (?)""", (task_id,)
        )

    def reset_table(self):
        '''reset tasks table'''
        self.db.execute("""
            DELETE FROM tasks
        """)

    def delete_table(self):
        '''delete tasks table'''
        self.db.execute("""
            DROP TABLE tasks
        """)


class SubmissionRepository:
    '''Submission repository to manage submissions'''
    def __init__(self, db):
        self.db = db

    def create_table(self):
        '''create submissions table'''
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                task_id INTEGER,
                completion_time DATETIME,
                status TEXT,
                        
                CHECK (status in ('PENDING', 'APPROVED', 'REJECTED')),
        
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (task_id) REFERENCES tasks(task_id))""")

    def add_submission(self, user_id, task_id):
        '''add given submission into submissions'''
        cursor = self.db.execute("""
            INSERT INTO submissions (user_id, task_id, completion_time, status)
            VALUES (?, ?, ?, ?)""",
            (user_id, task_id, datetime.now(timezone.utc).isoformat(), "PENDING"))

        return cursor.lastrowid

    def update_submission_status(self, submission_id, submission_status):
        '''Update the submission status for a submission that was already made'''
        self.db.execute("""
            UPDATE submissions SET status = (?) WHERE submission_id = (?)""",
            (submission_status, submission_id))

        return self.get_submission(submission_id)

    def get_submission(self, submission_id):
        '''get the given submission from submissions'''
        cursor = self.db.execute("""
            SELECT * FROM submissions WHERE submission_id = (?)""", (submission_id,)
        )

        return cursor.fetchone()

    def get_submissions_status(self, status="PENDING"):
        '''Get all the submission records, whose submission status is  -
        PENDING / APPROVED / REJECTED'''
        cursor = self.db.execute("""
            SELECT * FROM submissions WHERE status = (?)""", (status,))

        return cursor

    def delete_submission(self, submission_id):
        '''delete a given submission from submissions'''
        self.db.execute("""
            DELETE FROM submissions WHERE submission_id = (?)""", (submission_id,)
        )

    def reset_table(self):
        '''reset submission table'''
        self.db.execute("""
            DELETE FROM submissions
        """)

    def delete_table(self):
        '''delete submissions table'''
        self.db.execute("""
            DROP TABLE submissions
        """)


class ReviewRepository:
    '''Review repository to manage reviews'''
    def __init__(self, db):
        self.db = db

    def create_table(self):
        '''create review table'''
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                reviewer_id INTEGER,
                submission_id INTEGER,
                review_status TEXT,
                timestamp DATETIME,
                        
                UNIQUE(reviewer_id, submission_id),
                CHECK(review_status in ('APPROVE', 'REJECT')),
                        
                FOREIGN KEY (reviewer_id) REFERENCES users(user_id),
                FOREIGN KEY (submission_id) REFERENCES submissions(submission_id))""")

    def add_review(self, reviewer_id, submission_id, review_status):
        '''add the given review into reviews'''
        cursor = self.db.execute("""
            INSERT INTO reviews (reviewer_id, submission_id, review_status, timestamp)
            VALUES
            (?, ?, ?, ?)""",
            (reviewer_id, submission_id, review_status, datetime.now(timezone.utc).isoformat()))

        return cursor.lastrowid

    def get_review(self, review_id):
        '''get the given review from reviews'''
        cursor = self.db.execute("""
            SELECT * FROM reviews WHERE review_id = (?)""", (review_id,)
        )

        return cursor.fetchone()

    def delete_review(self, review_id):
        '''delete the given review from reviews'''
        self.db.execute("""
            DELETE FROM reviews WHERE review_id = (?)""", (review_id,)
        )

    def reset_table(self):
        '''reset reviews table'''
        self.db.execute("""
            DELETE FROM reviews
        """)

    def delete_table(self):
        '''delete reviews table'''
        self.db.execute("""
            DROP TABLE reviews
        """)
