# API Clients and Services Demonstration

This project demonstrates the usage of various API clients and services, including a client for the JSONPlaceholder API, a message service, and an email verification service.

## JSONPlaceholderClient
main.py

The `JSONPlaceholderClient` is a client for interacting with the JSONPlaceholder API. It provides methods to retrieve user information, get user posts, and create new posts on the JSONPlaceholder API.

### Usage Example

```python
if __name__ == '__main__':
    # Create an instance of the JSONPlaceholderClient
    client = JSONPlaceholderClient()

    # Get user information by user ID
    user_info = client.get_user(1)
    print('User Info:', user_info)

    # Get posts associated with a user by user ID
    user_posts = client.get_posts(1)
    print('User Posts:', user_posts)

    # Create a new post for a user
    new_post = client.create_post(1, 'New Post Title', 'New Post Body')
    print('New Post:', new_post)
```

## MessageService
message_client.py

The `MessageService` is a simple message service that allows saving and retrieving messages.

### Usage Example

```python
# Create an instance of the MessageService
client_message = MessageService()

# Save a message
client_message.save_message('Hello, World!')

# Get all saved messages
all_messages = client_message.get_messages
print('All Messages:', all_messages)
```
## EmailVerificationClient
verifier_email.py

The `EmailVerificationClient` demonstrates how to use an email verification service. It includes a service for email verification and a client for interacting with the service.

### Usage Example

```python
    # Set email and API key for verification
    email = 'test@gmail.com'
    api_key = 'ccdb948b48cfc21558ac8f92d30a649c82cdb32d'

    # Create instances of EmailVerificationService and EmailVerificationClient
    email_service = EmailVerificationService()
    email_client = EmailVerificationClient(service=email_service)

    # Verify and store the email
    verification_result = email_client.verify_and_store_email(email, api_key)
    print(verification_result)
```

## EmailVerificationService
verifier_email.py

The `EmailVerificationService` is a service class for verifying email addresses, including CRUD operations for managing verification results.

### CRUD Operations
```python
#Save a Result
EmailVerificationService.save_result(verification_result)

#Get All Results
results = EmailVerificationService.get_all_results

#Update Result for Specific Email
updated_result = EmailVerificationService.update_result(email, new_data)

#Delete Result for Specific Email
deletion_result = EmailVerificationService.delete_result(email)
```