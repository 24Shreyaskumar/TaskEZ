# 🚀 TaskEZ – Peer Review Based Task Management System

TaskEZ is a backend-focused system that allows users to complete tasks and get them validated through a **peer review mechanism**.
The system ensures fairness by requiring **majority approval** before accepting a submission.

**NOTE:** This project was created **WITHOUT the use of AI tools**. Completely designed by a HUMAN (Profile : [https://github.com/24Shreyaskumar]())

---

## 🧠 Problem Statement

In collaborative environments, validating task completion can be subjective and biased.

TaskEZ solves this by:

- Introducing a **peer-review based validation system**
- Using **majority consensus** to approve or reject submissions
- Maintaining a **leaderboard** based on performance

---

## ⚙️ Features

### 👤 User Management

- Create users
- Fetch user details

### 📝 Task Management

- Create tasks with scores and deadlines
- Assign tasks to users

### 📤 Submission System

- Users submit completed tasks
- Each submission is tracked with timestamp and status

### 🔍 Peer Review System

- Users can review others' submissions
- Self-review is not allowed
- Duplicate reviews are prevented

### ✅ Approval Logic

- Submission is:
  - **APPROVED** if ≥ ceil(n/2) users approve
  - **REJECTED** if ≥ ceil(n/2) users reject
  - Otherwise remains **PENDING**

### 🏆 Leaderboard

- Users ranked based on **total score of approved submissions**
- Sorting: `Score DESC`

---

## 🏗️ Architecture

The project follows a clean layered architecture:
Models → Repository → Service → (UI/API)

### 📦 Layers Explained

- **Models**
  - Define core entities (User, Task, Submission, Review)

- **Repository Layer**
  - Handles all database operations (SQLite)
  - Encapsulates SQL queries

- **Service Layer**
  - Contains business logic
  - Handles validation, workflows, and state transitions

---

## 🗄️ Database Design

### Tables:

- `users`
- `tasks`
- `submissions`
- `reviews`

### Key Constraints:

- `UNIQUE(reviewer_id, submission_id)` → prevents duplicate reviews
- `CHECK` constraints for valid statuses
- `FOREIGN KEY` with `ON DELETE CASCADE`

---

## 🔄 Workflow

```text
Create User → Create Task → Submit Task
→ Peer Reviews → Majority Decision
→ Leaderboard Update
```
