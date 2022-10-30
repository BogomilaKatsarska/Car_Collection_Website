# from django.core import exceptions
#
#
# def validate_min_len_profile_username(value):
#     len_username = list(value)
#     if len(len_username) < 2:
#         raise exceptions.ValidationError('The username must be a minimum of 2chars')
#
#
# def validate_car_year_in_range(value):
#     if value < 1980 or value > 2049:
#         raise exceptions.ValidationError('Year must be between 1980 and 2049')
