"""
Module for MessageService.

This module defines the MessageService class, which is used for saving and retrieving messages.
"""


class MessageService(object):
    """
    Class for handling messages.

    Attributes:
        messages (list): A list to store messages.

    Methods:
        save_message: Save a message to the messages list.
        get_messages: Get all saved messages.
    """

    messages = []

    @classmethod
    def save_message(cls, message: str) -> dict:
        """
        Save a message to the messages list.

        Args:
            message (str): The message to be saved.

        Returns:
            dict: A dictionary indicating the status of the save operation.
        """
        cls.messages.append(message)
        return {'status': 'success', 'message': 'Message saved successfully.'}

    @property
    def get_messages(self) -> list:
        """
        Get all saved messages.

        Returns:
            list: A list containing all saved messages.
        """
        return self.messages
