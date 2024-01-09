
"""Main module for demonstrating various API clients and services."""

import requests

from message_service import MessageService
from verifier_email import EmailVerificationClient, EmailVerificationService


class JSONPlaceholderClient(object):
    """
    A client for interacting with the JSONPlaceholder API.

    This client provides methods to retrieve user information, get user posts,
    and create new posts on the JSONPlaceholder API.

    Args:
        base_url (str, optional): The base URL of the JSONPlaceholder API.
            Defaults to 'https://jsonplaceholder.typicode.com'.
    """

    def __init__(self, base_url='https://jsonplaceholder.typicode.com') -> None:
        """
        Initialize a new instance of the JSONPlaceholderClient.

        Args:
            base_url (str, optional): The base URL of the JSONPlaceholder API.
                Defaults to 'https://jsonplaceholder.typicode.com'.
        """
        self.base_url = base_url

    def get_user(self, user_id: int) -> dict:
        """
        Get information about a user by user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict: JSON response containing user information.
        """
        endpoint = '/users/{0}'.format(user_id)
        return self._make_request(requests.get, endpoint)

    def get_posts(self, user_id: int) -> list:
        """
        Get posts associated with a user by user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: List of posts associated with the user.
        """
        endpoint = '/posts?userId={0}'.format(user_id)
        return self._make_request(requests.get, endpoint)

    def create_post(self, user_id: int, title: str, body: str) -> dict:
        """
        Create a new post for a user.

        Args:
            user_id (int): The ID of the user for whom the post is created.
            title (str): The title of the new post.
            body (str): The body/content of the new post.

        Returns:
            dict: JSON response containing information about the created post.
        """
        endpoint = '/posts'
        post_data = {
            'userId': user_id,
            'title': title,
            'body': body,
        }
        return self._make_request(requests.post, endpoint, post_data)

    def _make_request(self, method, endpoint, post_data=None) -> dict | list:
        """
        Make a request to the specified endpoint using the given HTTP method.

        Args:
            method (callable): The HTTP method function (e.g., requests.get, requests.post).
            endpoint (str): The API endpoint to send the request to.
            post_data (dict, optional): The data to be sent with the request as JSON. Defaults to None.

        Returns:
            dict: JSON response from the API.
        """
        url = self.base_url + endpoint
        response = method(url, json=post_data) if post_data else method(url)
        return response.json()


if __name__ == '__main__':
    client = JSONPlaceholderClient()

    user_info = client.get_user(1)
    print('User Info:', user_info)

    user_posts = client.get_posts(1)
    print('User Posts:', user_posts)

    new_post = client.create_post(1, 'New Post Title', 'New Post Body')
    print('New Post:', new_post)

    client_message = MessageService()
    client_message.save_message(new_post)

    email = 'test@gmail.com'
    api_key = 'ccdb948b48cfc21558ac8f92d30a649c82cdb32d'
    email_service = EmailVerificationService()
    email_client = EmailVerificationClient(service=email_service)

    print(email_client.verify_and_store_email(email, api_key))
