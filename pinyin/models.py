from django.db import models

# Create your models here.

# The model should be a perfect replica of the SQL used to create the original db.

class PinyinCodes(models.Model):
    """This should be a table that's prepopulated before deploy, and not modificable after that by POST requests in the view."""
    character = models.TextField(primary_key=True)
    pinyin1 = models.TextField()
    number = models.IntegerField()
    pinyin2 = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['character'], name='character_index')
        ]
        verbose_name_plural = "Pinyin Database Model"

        # from pinyin.models import PinyinCodes
        # A = PinyinCodes.objects.get(character="怎") 

class UserInput(models.Model):
    """This field saves the user inputs."""
    created = models.DateTimeField(auto_now_add=True)
    input_string = models.TextField(max_length=200)
    ip_address = models.CharField(max_length=15)

    class Meta:
        ordering = ['created']
        db_table = 'user_input'
        indexes = [
            models.Index(fields=['created'], name='created_idx')
        ]
        verbose_name_plural = "User Input Model" # This shows up in django admin
