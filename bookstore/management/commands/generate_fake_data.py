from django.core.management.base import BaseCommand
from faker import Faker
from django.conf import settings
from django.contrib.auth import get_user_model
from bookstore.models import Book, Author, Comment

class Command(BaseCommand):
    help = 'Generate fake data for Books, Authors, and Comments'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake users
        User = get_user_model()
        for _ in range(10):  # Adjust the number of users to create
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80)
            )
            print(f"Created user: {user.username}")

            # Create fake authors for the users
            author = Author.objects.create(user=user, bio=fake.text())
            print(f"Created author for user: {user.username}")

            # Create fake books
            for _ in range(3):  # Adjust the number of books per author
                book = Book.objects.create(
                    user=user,
                    title=fake.catch_phrase(),
                    author=author,
                    publication_year=fake.year(),
                    price=fake.random_number(digits=3),
                    currency='USD',
                    quantity=fake.random_int(min=1, max=10)
                )
                print(f"Created book: {book.title}")

                # Create fake comments for the books
                for _ in range(5):  # Adjust the number of comments per book
                    comment = Comment.objects.create(
                        book=book,
                        user=user,
                        content=fake.text(),
                        text=fake.sentence(),
                        is_active=fake.boolean()
                    )
                    print(f"Created comment for book: {book.title}")

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))
