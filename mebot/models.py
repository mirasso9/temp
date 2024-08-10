from django.db import models

# Create your models here.


class TelegramUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.username} (@{self.chat_id})"



class TelegramUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.username} (@{self.chat_id})"

class Update(models.Model):
    message_id = models.IntegerField()  # Store message ID for potential reference
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    callback_query_id = models.CharField(max_length=255, blank=True)  # For callback queries
    data = models.TextField(blank=True)  # For callback query data
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='updates')
    created_at = models.DateTimeField(auto_now_add=True)

class UserState(models.Model):
    user = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, primary_key=True)
    state = models.CharField(max_length=255)
    step = models.IntegerField(default=0)  # Track conversation progress

    def __str__(self, step=None, user=None, state=None):
        return f"{user.username} - State: {state}, Step: {step}"

class Membership(models.Model):
    user = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, primary_key=True)
    member = models.BooleanField(default=False)

class Admin(models.Model):
    chat_id = models.BigIntegerField(unique=True)  # Can store multiple admins if needed



from django.db import models

class User(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    step = models.CharField(max_length=50, default='no')
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.telegram_id

class Channel(models.Model):
    chat_id = models.CharField(max_length=50, unique=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
