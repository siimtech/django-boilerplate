from django.test import TestCase
from django.contrib.auth import get_user_model

class AppUserTestCase(TestCase):
    def test_create_and_remove_user(self):
        User = get_user_model()
        
        # Create a new user
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        
        # Check if the user was created successfully
        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword123'))
        
        # Remove the user
        user_id = user.id
        user.delete()
        
        # Check if the user was removed successfully
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user_id)