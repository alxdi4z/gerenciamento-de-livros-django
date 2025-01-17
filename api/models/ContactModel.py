from django.db import models

class Contact(models.Model):
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    website = models.URLField(blank=True)
    is_main_contact = models.BooleanField(default=False)

    def __str__(self):
        return f"""
            Phone Number: {self.phone_number}
            E-mail: {self.email}
            Main Contact: {"Yes" if self.is_main_contact else "No"}
        """