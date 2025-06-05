import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


def get_media_url(object_or_url: object) -> str:
    """ Return the media url for the image (local or s3).
    
    Args:
        url (object): image object or url string
        
    Returns:
        str: url of the image
    """
        
    # Get the url string
    url_str = ""
    if type(object_or_url) is str:
        url_str = object_or_url
    else:
        url_str = object_or_url.url
    
    if "s3.amazonaws.com" not in url_str:
        return f"{settings.HOST}{url_str}"
    return url_str


def get_test_file(file_name: str = "test.pdf") -> SimpleUploadedFile:
    app_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.dirname(app_path)
    media_path = os.path.join(project_path, 'media')
    
    file_path = os.path.join(media_path, file_name)
    image_file = SimpleUploadedFile(
        name=file_name,
        content=open(file_path, 'rb').read(),
        content_type='application/pdf' if file_name.endswith('.pdf') else 'image/webp'
    )
    
    return image_file