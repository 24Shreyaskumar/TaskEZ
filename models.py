from enum import Enum
from datetime import datetime, timezone

class User:
    '''User Model'''
    def __init__(self, user_name, user_id=None):
        self.user_id: int = user_id
        self.user_name: str = user_name

class Task:
    '''Task Model'''
    def __init__(self, task_name, task_id=None):
        self.task_id: int = task_id
        self.task_name: str = task_name

class SubmissionStatus(Enum):
    '''Submission Staus mapping'''
    PENDING  = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Submission:
    '''Submission Model'''
    def __init__(self, user_id, task_id, submission_id=None):
        self.submission_id: int = submission_id
        self.user_id: int = user_id
        self.task_id: int = task_id
        self.status: SubmissionStatus = SubmissionStatus.PENDING
        self.completion_time: datetime = datetime.now(timezone.utc)
    
class ReviewType(Enum):
    '''Review Status mapping'''
    APPROVE = "APPROVE"
    REJECT  = "REJECT"

class Review:
    '''Review Model'''
    def __init__(self, submission_id, reviewer_id, review_type, review_id=None):
        self.review_id: int = review_id
        self.reviewer_id: int = reviewer_id
        self.submission_id: int = submission_id
        self.review_status: ReviewType = ReviewType(review_type.upper())
        self.timestamp: datetime = datetime.now(timezone.utc)