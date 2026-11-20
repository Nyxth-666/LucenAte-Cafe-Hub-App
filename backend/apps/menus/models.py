from django.db import models


class MenuItem(models.Model):
    class Category(models.TextChoices):
        FOOD = "FOOD", "Food"
        DRINKS = "DRINKS", "Drinks"
        DESSERTS = "DESSERTS", "Desserts"
        OTHERS = "OTHERS", "Others"

    business = models.ForeignKey(
        "businesses.Business",
        on_delete=models.CASCADE,
        related_name="menu_items",
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHERS,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    image = models.ImageField(
        upload_to="menu_items/",
        blank=True,
        null=True,
    )
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} - {self.business.name}"
