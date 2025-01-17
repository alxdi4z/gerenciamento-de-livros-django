from django.db import models

class Address(models.Model):
    description = models.CharField(max_length=60, blank=False)
    address1 = models.CharField(max_length=250, blank=False)
    address2 = models.CharField(max_length=250)
    country = models.CharField(max_length=60, blank=False)
    city = models.CharField(max_length=180, blank=False)
    postal_code = models.CharField(max_length=30, blank=False)
    state_region = models.CharField(max_length=60, blank=False)
    is_main_address = models.BooleanField(default=False)

    def __str__(self):
        return f"""
            Description: {self.description}
            Address: {self.address1} {self.address2}
            City: {self.city}
            State/Region: {self.state_region}
            Country: {self.country}
            Postal Code: {self.postal_code}
            Main Address: {"Yes" if self.is_main_address else "No"}
        """