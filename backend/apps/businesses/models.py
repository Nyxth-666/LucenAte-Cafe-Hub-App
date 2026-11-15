from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class BusinessFeature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Business(models.Model):

    class BusinessType(models.TextChoices):
        CAFE = "CAFE", "Cafe"
        RESTAURANT = "RESTAURANT", "Restaurant"

    class PriceRange(models.TextChoices):
        BUDGET = "₱", "₱"
        MODERATE = "₱₱", "₱₱"
        EXPENSIVE = "₱₱₱", "₱₱₱"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"
        SUSPENDED = "SUSPENDED", "Suspended"

    class BusinessHours(models.Model):
        opening = models.IntegerField()
        closing = models.IntegerField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="businesses",
    )

    name = models.CharField(max_length=150)

    business_type = models.CharField(
        max_length=20,
        choices=BusinessType.choices,
    )

    price_range = models.CharField(
        max_length=10,
        choices=PriceRange.choices,
    )

    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    description = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    features = models.ManyToManyField(
        BusinessFeature,
        blank=True,
        related_name="businesses",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BusinessOperatingHours(models.Model):

    class DayOfWeek(models.IntegerChoices):
        MONDAY = 0, "Monday"
        TUESDAY = 1, "Tuesday"
        WEDNESDAY = 2, "Wednesday"
        THURSDAY = 3, "Thursday"
        FRIDAY = 4, "Friday"
        SATURDAY = 5, "Saturday"
        SUNDAY = 6, "Sunday"

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="operating_hours",
    )

    day = models.IntegerField(choices=DayOfWeek.choices)

    opening = models.TimeField(null=True, blank=True)
    closing = models.TimeField(null=True, blank=True)

    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ["day"]
        constraints = [
            models.UniqueConstraint(
                fields=["business", "day"],
                name="unique_business_operating_day",
            )
        ]

    def __str__(self):
        return f"{self.business.name} - {self.get_day_display()}"

def validate_file_size(file):
    max_size = 5 * 1024 * 1024

    if file.size > max_size:
        raise ValidationError("File size cannot exceed 5 MB.")

class BusinessDocument(models.Model):

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    document = models.FileField(
        upload_to="business_documents/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "jpg", "jpeg", "png"]
            ),
            validate_file_size,
        ],
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - Verification Document"
