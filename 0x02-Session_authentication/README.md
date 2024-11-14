# Backend User Data Authentication System

This project implements an enhanced session authentication system for web applications, providing session expiration, session persistence, and different authentication mechanisms using environment variables for configuration. The main components are `SessionExpAuth` and `SessionDBAuth`.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
  - [Session Expiration (`SessionExpAuth`)](#1-session-expiration-sessionexpauth)
  - [Session Database Storage (`SessionDBAuth`)](#2-session-database-storage-sessiondbauth)
- [File Structure](#file-structure)
- [Environment Configuration](#environment-configuration)
- [Classes and Methods](#classes-and-methods)
  - [SessionExpAuth](#sessionexpauth)
  - [SessionDBAuth](#sessiondbauth)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Testing the Features](#testing-the-features)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to build a robust and flexible session authentication system using Flask. The system extends basic session authentication by:
1. Adding expiration handling through a `SessionExpAuth` class.
2. Persisting sessions in a database through a `SessionDBAuth` class to ensure sessions are maintained across server restarts.

## Features

### 1. Session Expiration (`SessionExpAuth`)

- **Functionality**:
  - Adds expiration handling to sessions.
  - The session duration is controlled by the `SESSION_DURATION` environment variable.
- **Location**: `api/v1/auth/session_exp_auth.py`

### 2. Session Database Storage (`SessionDBAuth`)

- **Functionality**:
  - Extends `SessionExpAuth` to persist sessions in a database.
  - Sessions are stored using a `UserSession` model.
- **Location**: `api/v1/auth/session_db_auth.py`

## File Structure

- `api/v1/auth/session_auth.py`: Base session authentication logic.
- `api/v1/auth/session_exp_auth.py`: Handles session expiration logic.
- `api/v1/auth/session_db_auth.py`: Extends session handling with database storage.
- `models/user_session.py`: Defines the `UserSession` model for storing session data.
- `api/v1/app.py`: Main entry point for the Flask app, updated to conditionally use different authentication classes.
- `README.md`: Documentation for the project.

## Environment Configuration

- **`SESSION_DURATION`**: Sets the duration (in seconds) before a session expires. If not set or invalid, sessions do not expire.
  - Example:
    ```bash
    export SESSION_DURATION=60
    ```
- **`AUTH_TYPE`**: Controls the type of authentication to use (`session_exp_auth` or `session_db_auth`).
  - Example:
    ```bash
    export AUTH_TYPE=session_exp_auth
    ```

## Classes and Methods

### `SessionExpAuth`

- **Location**: `api/v1/auth/session_exp_auth.py`
- **Methods**:
  - `__init__()`: Initializes the session duration from `SESSION_DURATION`.
  - `create_session(user_id=None)`: Creates a session with a `created_at` timestamp.
  - `user_id_for_session_id(session_id=None)`: Validates and retrieves a user ID based on session expiration.

### `SessionDBAuth`

- **Location**: `api/v1/auth/session_db_auth.py`
- **Methods**:
  - `create_session(user_id=None)`: Creates and stores a session in the database.
  - `user_id_for_session_id(session_id=None)`: Retrieves the user ID from the database.
  - `destroy_session(request=None)`: Deletes a stored session based on the request cookie.

### `UserSession`

- **Location**: `models/user_session.py`
- **Attributes**:
  - `user_id`: The ID of the user.
  - `session_id`: The session ID associated with the user.

## Usage

### Running the Application

1. Set the appropriate environment variables.
   ```bash
   export API_HOST=0.0.0.0
   export API_PORT=5000
   export AUTH_TYPE=session_exp_auth   # or session_db_auth
   export SESSION_DURATION=60          # Optional, for session expiration
