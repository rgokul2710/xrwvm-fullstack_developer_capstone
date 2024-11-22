from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)  # New field
    established_year = models.IntegerField(
        validators=[
            MinValueValidator(1800),  # Cars likely started being produced after 1800
            MaxValueValidator(now().year)
        ],
        blank=True, null=True  # Optional field
    )
    logo = models.ImageField(upload_to='car_make_logos/', blank=True, null=True)  # Optional logo field

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="car_models")  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('PICKUP', 'Pickup Truck'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=now().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(now().year)
        ]
    )
    engine_type = models.CharField(
        max_length=50,
        choices=[
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('ELECTRIC', 'Electric'),
            ('HYBRID', 'Hybrid'),
            ('CNG', 'CNG'),
        ],
        default='PETROL'
    )  # New field
    seating_capacity = models.IntegerField(default=5)  # New field
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Price with 2 decimal places
    color_options = models.CharField(max_length=255, blank=True, null=True)  # Store color options as a comma-separated string
    fuel_efficiency = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )  # Fuel efficiency in km/l or equivalent

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"  # More descriptive string representation
