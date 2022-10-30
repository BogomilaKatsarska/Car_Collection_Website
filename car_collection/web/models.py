from django.db import models
from django.core import validators
# from car_collection.web.validators import validate_min_len_profile_username, validate_car_year_in_range


class Profile(models.Model):
    MAX_LEN_PROFILE = 10
    MAX_LEN_PASS = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30
    MIN_AGE_USER = 18

    username = models.CharField(
        max_length=MAX_LEN_PROFILE,
        # validators=validate_min_len_profile_username,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        # validators=validators.MinLengthValidator(MIN_AGE_USER),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASS,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_LEN_CAR = 10
    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2
    MIN_PRICE_CAR = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    )

    type = models.CharField(
        max_length=MAX_LEN_CAR,
        choices=TYPES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        # validators=validators.MinLengthValidator(MIN_LEN_MODEL),
        null=False,
        blank=False,
    )
    year = models.IntegerField(

        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        # validators=(
        #     validate_car_year_in_range,
        #     validators.MinLengthValidator(MIN_PRICE_CAR),
        #  ),
        null=False,
        blank=False,
    )
