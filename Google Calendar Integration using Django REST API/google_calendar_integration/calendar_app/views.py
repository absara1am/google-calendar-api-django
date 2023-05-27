from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os

# Set up OAuth2 client ID and secret
CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'

# Set up OAuth2 scope and flow
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
flow = Flow.from_client_config(
    client_config={
        'installed': {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uris': [REDIRECT_URI],
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://accounts.google.com/o/oauth2/token',
        }
    },
    scopes=SCOPES,
    redirect_uri=REDIRECT_URI,
)

class GoogleCalendarInitView(View):
    def get(self, request):
        # Generate authorization URL and redirect user to Google authorization page
        authorization_url, _ = flow.authorization_url(prompt='consent')
        return redirect(authorization_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        # Get authorization code from query parameters
        code = request.GET.get('code')
        # Exchange authorization code for access token
        flow.fetch_token(code=code)
        credentials = flow.credentials
        # Use access token to retrieve a list of events from the user's calendar
        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])
        # Render events in response (you can customize this to fit your needs)
        response = ''
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            response += f'{event["summary"]} ({start})<br>'
        return HttpResponse(response)
