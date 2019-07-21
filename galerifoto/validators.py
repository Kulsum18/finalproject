from django.core.exceptions import ValidationError


def validate_file_size():
    filesize = value.size

    if filesize > 2097152:
        raise ValidationError("Image Maksimum yang dapat diupload yaitu 2MB")
    else:
            return value
