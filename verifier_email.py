"""
Module for Email Verification Service and Client.

This module provides classes for verifying email addresses using the Hunter.io API.
"""

import requests


class EmailVerificationService(object):
    """
    Service class for verifying email addresses.

    Attributes:
        email_results (list): A list to store verification results.

    Methods:
        __init__: Initialize the EmailVerificationService.
        save_result: Save a verification result to the results list.
        get_all_results: Get all stored verification results.
        verify_email: Verify an email address using the Hunter.io API.
        get_result: Get the verification result for a specific email address.
        update_result: Update the verification result for a specific email address.
        delete_result: Delete the verification result for a specific email address.
    """

    email_results = []

    def __init__(self, base_url='https://api.hunter.io/v2/email-verifier?') -> None:
        """
        Initialize the EmailVerificationService.

        Args:
            base_url (str): The base URL for the Hunter.io API.
        """
        self.base_url = base_url

    @classmethod
    def save_result(cls, verification_result: dict) -> None:
        """
        Save a verification result to the email_results list.

        Args:
            verification_result (dict): Verification result to be saved.
        """
        cls.email_results.append(verification_result)

    @property
    def get_all_results(self) -> list[dict]:
        """
        Get all stored verification results.

        Returns:
            list: List of all stored verification results.
        """
        return self.email_results

    def verify_email(self, email: str, api_key: str) -> dict:
        """
        Verify an email address using the Hunter.io API.

        Args:
            email (str): The email address to be verified.
            api_key (str): The API key for authentication.

        Returns:
            dict: JSON response containing the verification result.
        """
        endpoint = 'email={0}&api_key={1}'.format(email, api_key)
        url = self.base_url + endpoint
        response = requests.get(url, timeout=10)

        verification_result = response.json()
        self.save_result(verification_result)

        return verification_result

    def get_result(self, email: str) -> dict:
        """
        Get the verification result for a specific email address.

        Args:
            email (str): The email address for which to retrieve the result.

        Returns:
            dict: JSON response containing the verification result.
        """
        for result_data in self.email_results:
            if result_data.get('data', {}).get('email') == email:
                return result_data
        return {'status': 'not found', 'message': 'Result not found.'}

    def update_result(self, email: str, new_data: dict) -> dict:
        """
        Update the verification result for a specific email address.

        Args:
            email (str): The email address for which to update the result.
            new_data (dict): New data to be merged into the existing result.

        Returns:
            dict: JSON response indicating the success or failure of the update.
        """
        for result_data in self.email_results:
            if result_data.get('data', {}).get('email') == email:
                result_data.update(new_data)
                return {'status': 'success', 'message': 'Result updated successfully.'}
        return {'status': 'not found', 'message': 'Result not found.'}

    def delete_result(self, email: str) -> dict:
        """
        Delete the verification result for a specific email address.

        Args:
            email (str): The email address for which to delete the result.

        Returns:
            dict: JSON response indicating the success or failure of the deletion.
        """
        for result_data in self.email_results:
            if result_data.get('data', {}).get('email') == email:
                self.email_results.remove(result_data)
                return {'status': 'success', 'message': 'Result deleted successfully.'}
        return {'status': 'not found', 'message': 'Result not found.'}


class EmailVerificationClient(object):
    """
    Client for interacting with the EmailVerificationService.

    This client allows you to verify email addresses using the EmailVerificationService
    and retrieve or store the verification results.

    Args:
        service (EmailVerificationService): An instance of the EmailVerificationService.

    Methods:
        verify_and_store_email: Verify an email address using the service and store the result.

    Attributes:
        service (EmailVerificationService): The EmailVerificationService instance associated with the client.
    """

    def __init__(self, service: EmailVerificationService) -> None:
        """
        Initialize the EmailVerificationClient.

        Args:
            service (EmailVerificationService): An instance of the EmailVerificationService.
        """
        self.service = service

    def verify_and_store_email(self, email: str, api_key: str) -> dict:
        """
        Verify an email address using the EmailVerificationService and store the result.

        Args:
            email (str): The email address to be verified.
            api_key (str): The API key for authentication.

        Returns:
            dict: JSON response containing the verification result.
        """
        return self.service.verify_email(email, api_key)
