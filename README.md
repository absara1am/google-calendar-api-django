# Google Calendar Integration
This project provides a Django web application that integrates with the Google Calendar API, allowing users to authenticate and retrieve a list of events from their Google Calendar. The application follows the OAuth2 authorization flow to obtain access tokens and make requests to the Google Calendar API.

# Project Demo

To see a video demonstration of the project in action, click [here](<https://drive.google.com/file/d/1eI4WRP3HkWEqll4ni9wX9YBN9jyhcIgf/view?usp=share_link>).

## Prerequisites
Before running the project, ensure that you have the following installed:

Python (version 3.x)
Django (version 3.x)
Required libraries: google-auth, google-auth-oauthlib, google-api-python-client

## Installation
Clone the repository to your local machine or download the source code.
Navigate to the project folder 'google_calendar_integration'.

## Setting up the virtual environment
Create a virtual environment named '.venv' by running the appropriate command for your operating system:
Windows: 'py -3 -m venv .venv'

Activate the virtual environment:
Windows: '.venv\scripts\activate'

## Installing dependencies
Upgrade pip to the latest version:
python -m pip install --upgrade pip

Install the project dependencies by running the following command:
pip install -r requirements.txt

## Setting up environment variables
Set the environment variables 'GOOGLE_CLIENT_ID' and 'GOOGLE_CLIENT_SECRET' with the corresponding values of your Google Cloud project's client ID and client secret. These variables are used for OAuth2 authentication.

## Database migration
Apply the database migrations to create the necessary tables:
Copy code
python manage.py migrate

## Running the application
Start the Django development server:
python manage.py runserver

Access the application in your web browser at http://127.0.0.1:8000/rest/v1/calendar/init/. This URL initiates the authentication process with Google.

Grant access to the Google Calendar integration by logging in with a Google account associated with the authorized test users specified in your Google Cloud project.

After successful authentication, you should be able to see a list of events from your Google Calendar on the webpage.

## Project Structure
The project folder structure is as follows:


#google_calendar_integration/
 #├── calendar_app/
 #│   ├── __init__.py
 #│   ├── admin.py
 │   ├── apps.py
 │   ├── models.py
 │   ├── tests.py
 │   └── views.py  # Contains the main view code
 ├── google_calendar_integration/
 │   ├── __init__.py
 │   ├── asgi.py
 │   ├── settings.py
 │   ├── urls.py  # Add your URL patterns here
 │   └── wsgi.py
 ├── manage.py
 ├── requirements.txt  # Contains project dependencies
 └── README.md  # Documentation and instructions
 '''
## Customization
If you want to modify the application's behavior or add additional features, you can modify the 'views.py' file inside the 'calendar_app' directory.
You can customize the authentication and authorization settings by adjusting the environment variables 'GOOGLE_CLIENT_ID' and 'GOOGLE_CLIENT_SECRET' in your operating system.

## Troubleshooting
If you encounter any issues or errors while running the project, please ensure that you have followed the installation instructions correctly and that you have provided valid Google Cloud project credentials.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgments
This project was developed as part of an assignment or learning exercise. It utilizes the Google Calendar API and various libraries to integrate Google Calendar functionality into a Django web application.
