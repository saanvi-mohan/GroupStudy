
# GroupStudy: Collaborative Study Room Web Application

GroupStudy is a web application built using Django, HTML, and CSS that enables users to create and join study rooms, collaborate with others, and stay updated on recent activities. This README provides an overview of the application's features, installation instructions, and usage guidelines.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### User Management

- **User Registration**: New users can register for an account, providing the necessary details.
- **User Login**: Registered users can log in to their accounts securely.

### Study Rooms

- **Create Rooms**: Users can create study rooms, specifying room names, topics, and room descriptions.
- **Search Rooms**: Users can search for study rooms by names, topics, or room descriptions.
- **Delete Rooms**: Room creators can delete rooms they own.

### Messaging

- **Post Messages**: Users can post messages within a room for collaborative study discussions.
- **Edit Messages**: Users can edit their messages to correct or update information.
- **See Participants**: Users can view the list of participants in a room.

### Recent Activity

- **View Recent Activity**: Users can stay updated on recent activities and discussions across all rooms.

### User Dashboard

- **Edit Room Names**: Users can edit the names of rooms they own.
- **View Owned Rooms**: Users can see a list of all the rooms they have created.
- **View Past Activity**: Users can see their past activity, including messages and room creation history.

## Installation

To run GroupStudy locally on your machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/GroupStudy.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GroupStudy
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000/`.

## Usage

1. Register for an account or log in with your existing credentials.
2. Create a study room or search for existing ones.
3. Join a study room to collaborate with others.
4. Post messages, edit messages, and view room participants.
5. Stay updated on recent activities across all rooms.
6. Access your user dashboard to edit room names, view owned rooms, and see past activity.

## Contributing

Contributions to GroupStudy are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code follows best practices and includes relevant documentation.

