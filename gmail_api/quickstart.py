from googleapiclient import discovery, errors
from gmail_api.create_token import gmail_token


def get_labels():
    """ Get labels from gmail """
    creds = gmail_token()
    try:
        service = discovery.build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except errors.HttpError as error:
        print(f'An error occurred: {error}')
