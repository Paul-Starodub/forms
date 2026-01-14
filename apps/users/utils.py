import os
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify


def profile_image_file_path(instance: User, filename: str) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.username)}-{uuid.uuid4()}{extension}"
    return os.path.join("profile/users/", filename)
