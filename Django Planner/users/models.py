from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Creates a database table for profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # New users will use default.jpg as their profile picture
    # If they upload their own photos, it will be uploaded to the profile_pics folder
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Method to save profile picture
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Changes the image from RGBA to RGB to not get errors
        img = img.convert('RGB')

        if img.height > 300 or img.width > 300:

            # Resizes the image to 300 by 300 to save space
            output_size = (300, 300)

            img.thumbnail(output_size)
            img.save(self.image.path)
