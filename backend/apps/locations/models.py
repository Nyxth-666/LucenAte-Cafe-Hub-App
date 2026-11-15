from django.db import models

class BusinessLocation(models.Model):

    business = models.ForeignKey(
        "businesses.Business",
        on_delete=models.CASCADE,
        related_name="locations",
    )

    street_address = models.CharField(max_length=255)
    barangay = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="Lucena City")
    province = models.CharField(max_length=100, default="Quezon")

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business.name} - {self.barangay}"
