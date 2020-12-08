from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

sample_users = {
    'user_one': 'user_one_password',
    'user_two': 'user_two_password',
    'user_three': 'user_three_password',
}


class Command(BaseCommand):
    help = 'creates the sample users of the webapp'

    def handle(self, *args, **kwargs):
        model = get_user_model()
        for user_name, password in sample_users.items():
            user = model.objects.create_user(username=user_name, password=password)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            self.stdout.write(f'{user_name} created successfully')

