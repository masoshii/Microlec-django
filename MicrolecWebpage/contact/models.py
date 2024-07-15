from django.db import models

class ContactModel(models.Model):
    id_contact = models.BigAutoField(primary_key=True, null=False)
    name_contact = models.CharField(null=False, max_length=200)
    lastnames_contact = models.CharField(null=False, max_length=200)
    email_contact = models.EmailField(null=False)
    comment_contact = models.TextField(null=False, max_length=2000)
    timestamp_contact = models.DateTimeField(null=False)
    ip_contact = models.CharField(null=False, max_length=15, default=0)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.email_contact

