# FastAPI Task Manager

## Project Description

This project is a simple Task Manager API built with FastAPI, where you can:
- Create tasks
- List all tasks
- Retrieve a single task
- Update a task
- Delete tasks (bulk or single)

## Prerequisites

Make sure you have the following installed:
- Python 3.9+
- PostgreSQL (if using PostgreSQL as your database)
- `pip` (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Azathoth-11/waterdip_assignment_backend.git
    cd water_assignment_backend
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables. Create a `.env` file in the root directory with the following contents (adjust with your credentials):

    ```
    DATABASE_URL=postgresql://username:password@localhost/dbname
    ```

## Running the Server

To run the FastAPI server:
python main.py (from the root folder)
