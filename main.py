"""
Main module for demonstrating various API clients and services.

This module initializes a JSONPlaceholderClient to interact with the JSONPlaceholder API,
creates a new post, saves the post message using MessageService, and verifies an email
using EmailVerificationClient and EmailVerificationService.

Note: Make sure to replace the placeholder values for email and api_key with actual values.
"""
from message_service import MessageService
from placeholder_client import JSONPlaceholderClient
from verifier_email import EmailVerificationClient, EmailVerificationService

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
