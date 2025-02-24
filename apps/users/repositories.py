from apps.users.models import User
from django.contrib.auth.hashers import make_password
from .dtos import UserDTO

class UserRepository:
    @staticmethod
    def bulk_create_users(users: list[UserDTO]):
        user_instances = [
            User(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                phone=user.phone,
                default_address=user.default_address,
                typology=user.typology,
                username=user.email,
                password=make_password('12345')
            )
            for user in users
        ]
        User.objects.bulk_create(user_instances)
        return [user.email for user in user_instances]