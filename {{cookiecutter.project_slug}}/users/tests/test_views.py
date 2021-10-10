from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from .util import generate_random_string
from ..serializers import UserRegistrationSerializer

client = Client()


class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        username = generate_random_string()
        data = {
            "email": f"{username}@test.com",
            "password": username,
            "profile": {"name": username},
        }
        response = client.post(path="/auth/signup", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(
            response.data["message"], "User registered successfully"
        )


class UserLoginTest(TestCase):
    def setUp(self):
        self.username = generate_random_string()
        data = {
            "email": f"{self.username}@test.com",
            "password": self.username,
            "profile": {"name": self.username},
        }
        serializer = UserRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_user_login(self):
        data = {
            "email": f"{self.username}@test.com",
            "password": {self.username},
        }
        response = client.post(path="/auth/signin", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], f"{self.username}@test.com")
        self.assertEqual(
            response.data["message"], "User logged in successfully"
        )


class UserProfileTest(TestCase):
    def setUp(self):
        self.username = generate_random_string()
        data = {
            "email": f"{self.username}@test.com",
            "password": self.username,
            "profile": {"name": self.username},
        }
        serializer = UserRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "email": f"{self.username}@test.com",
            "password": {self.username},
        }
        response = client.post(path="/auth/signin", data=data)
        self.token = response.data["token"]

    def test_user_profile(self):
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.token}",
        }
        response = client.get(path="/auth/profile", **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(
            response.data["message"], "User profile fetched successfully"
        )
        self.assertEqual(response.data["data"][0]["name"], self.username)
