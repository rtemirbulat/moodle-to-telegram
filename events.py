from __future__ import print_function
import datetime
import pickle
import os.path
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
cnt = 5
def show_events():
    if True:
        global cnt 
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
       
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
          
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        #if you want to display specific events from specific calendar, paste your calendar id below, you can get it from calendar settings in google
        events_result = service.events().list(calendarId='', timeMin=now,
                                            maxResults=40, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')    
        list_tuple = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            date_event = start,event['summary']
            list_tuple.append(date_event)
        out = []
        for i in range(cnt-5,cnt):
            res = list_tuple[i]
            time = res[0]
            #by default outputs as yyyy:mm:dd hh:mm z (server time)
            time = time[:-4].strip().replace('T',' ')+' +6:00'
            desc = res[1]
            out.append(time + " " + desc)
        cnt = cnt+5
        return(str('\n'.join(out)))
