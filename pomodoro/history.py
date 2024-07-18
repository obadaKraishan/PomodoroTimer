import json


class History:
    def __init__(self, filename='history.json'):
        """
        Initialize the History object with the given filename.

        :param filename: The name of the file where history will be saved and loaded from.
        """
        self.filename = filename
        self.data = self.load()

    def add_session(self, session):
        """
        Add a new session to the history and save it.

        :param session: A dictionary containing details of the session.
        """
        self.data.append(session)
        self.save()

    def save(self):
        """
        Save the current history data to the file.
        """
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def load(self):
        """
        Load history data from the file.

        :return: A list of session data if the file exists, otherwise an empty list.
        """
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
