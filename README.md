# Twitter Clone Backend API Project

This project is a Twitter clone backend API created using the Flask library of Python and MySQL database. The API provides endpoints for various Twitter functionalities such as user authentication, posting tweets, following and unfollowing other users, and getting a user's timeline.
Requirements

To run this project, you will need to have the following installed on your system:

    Python 3.6+
    Flask 2.0+
    MySQL 8.0+

Installation

    Clone the repository:

bash
git clone https://github.com/your-username/twitter-clone-backend-api.git

    Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate

    Install the dependencies:

bash
pip install -r requirements.txt

    Create a MySQL database and update the config.py file with the database details.

    Run the Flask app:

bash
python app.py

The API should now be available at http://localhost:5000.
Endpoints

    /auth/register - Register a new user.
    /auth/login - Log in an existing user.
    /auth/logout - Log out the currently logged in user.
    /tweets - Get all tweets or post a new tweet.
    /users/<int:id>/followers - Get all followers of a specific user.
    /users/<int:id>/following - Get all users a specific user is following.

Contributing

Contributions to this project are welcome! If you would like to contribute, please submit a pull request.
