'''Brain of the Project'''

from db import Database
from models import User, Task, Submission, Review, MapReviewToSubmission
from repository import UserRepository, TaskRepository, SubmissionRepository, ReviewRepository

class PeerReviewService:
    '''A Peer review service to review submissions and show leaderboard'''
    def __init__(self):
        # DB connection
        self.db = Database()
        self.user_repo = UserRepository(self.db)
        self.task_repo = TaskRepository(self.db)
        self.submission_repo = SubmissionRepository(self.db)
        self.review_repo = ReviewRepository(self.db)

    def _validate_user(self, user_id):
        user = self.user_repo.get_user(user_id)

        if not user:
            raise ValueError(f"User with user id {user_id} doesn't exist!")

        return user

    def create_user(self, user_name=None):
        '''Create user'''
        if not user_name:
            raise ValueError("User name cannot be empty")

        # Model and Repo objects
        user = User(user_name)

        user_id = self.user_repo.add_user(user.user_name) # Add user into the database
        user.user_id = user_id

        self._validate_user(user.user_id)

        return user

    def _validate_task(self, task_id):
        task = self.task_repo.get_task(task_id)

        if not task:
            raise ValueError(f"Task with task id {task_id} doesn't exist!")

        return task

    def create_task(self, task_name, task_score, task_deadline):
        '''Create task'''
        if not task_name:
            raise ValueError("Task name cannot be empty")

        task = Task(task_name, task_score, task_deadline)

        task_id = self.task_repo.add_task(task.task_name, task.task_score, task.task_deadline)
        task.task_id = task_id

        self._validate_task(task.task_id)

        return task

    def get_user(self, user_id):
        '''Get user from users table'''
        return self._validate_user(user_id)

    def get_task(self, task_id):
        '''Get task from tasks table'''
        return self._validate_task(task_id)

    def _validate_submission(self, submission_id):
        submission = self.submission_repo.get_submission(submission_id)

        if not submission:
            raise ValueError(f"Submission with submission_id {submission_id} doesn't exist!")

        return submission

    def submit_task(self, user_id, task_id):
        '''Submit a task'''
        submission = Submission(user_id, task_id)

        submission_id = self.submission_repo.add_submission(submission.user_id, submission.task_id)
        submission.submission_id = submission_id

        self._validate_submission(submission_id)

        return submission

    def get_reviewable_submissions(self, user_id):
        '''Get the list of pending submissions for a user to review'''
        pending_requests = self.submission_repo.get_submissions_status(status="PENDING")


    def _update_submission_status(self, submission_id):
        # status should be updated only when condition for APPROVE / REJECT passes
        # submission = self.submission_repo.update_submission_status(
        #     submission_id,
        #     submission_status
        # )

        # self._validate_submission(submission_id)
        # return submission
        pass


    def add_review(self, reviewer_id, submission_id, review_type):
        '''Add a review to a submission'''
        review = Review(submission_id, reviewer_id, review_type)

        review_id = self.review_repo.add_review(
            review.reviewer_id,
            review.submission_id,
            review.review_status
        )

        review.review_id = review_id

        self._update_submission_status(submission_id)

        return review

    def get_leaderboard(self):
        '''Get the leaderboard'''
