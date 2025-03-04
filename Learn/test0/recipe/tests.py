from django.test import TestCase
from faker import Faker
from django.contrib.auth.models import User
from .models import Recipe
import random

# Create your tests here.

fake = Faker()

def fake_recipe():
    if not User.objects.exists():
        for i in range(10):
            user = User.objects.create_user(username=fake.name(), email=fake.email(), password="password")
            user.save()
    users = User.objects.all()
    
    for i in range(10):
        user = random.choice(users)
        recipe = Recipe.objects.create(user=user, title=fake.sentence(), description=fake.text())
        recipe.save()
    
    print("Recipes created")
    
    if __name__ == "__main__":
        fake_recipe()