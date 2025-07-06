from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="%(class)s_sender")
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="%(class)s_receiver")
