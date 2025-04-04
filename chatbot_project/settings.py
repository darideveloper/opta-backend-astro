import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup .env file
load_dotenv()
ENV = os.getenv('ENV')
env_path = os.path.join(BASE_DIR, f'.env.{ENV}')
load_dotenv(env_path)
print(f'\nEnvironment: {ENV}')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
STORAGE_AWS = os.environ.get("STORAGE_AWS") == "True"
LANDING_HOST = os.getenv('LANDING_HOST')

print(f"DEBUG: {DEBUG}")
print(f"STORAGE_AWS: {STORAGE_AWS}\n")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # Local apps
    'chatbot_app',
    'core',
    'jazzmin',
    
    # Modules
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'coreapi',
    
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Manage static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Cors
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatbot_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chatbot_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Enforce HTTPS
if not DEBUG:
    SECURE_SSL_REDIRECT = True

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# cors autherizations
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS').split(',')

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(',')


# # Permitir solicitudes desde cualquier origen (en un entorno de desarrollo,
# puedes limitarlo más tarde)
# CORS_ALLOW_ALL_ORIGINS = True

# Si deseas que las cookies se incluyan en las solicitudes
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'core.authentication.ExpiringTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Storage settings
if STORAGE_AWS:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'chatbot_project.storage_backends.StaticStorage'
    # s3 public media settings

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'chatbot_project.storage_backends.PublicMediaStorage'

    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = 'private'
    PRIVATE_FILE_STORAGE = 'chatbot_project.storage_backends.PrivateMediaStorage'
    
    STATIC_ROOT = None
    MEDIA_ROOT = None
else:
    # Local development (Windows or local server)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


# Jazzmin (layout template) settings
JAZZMIN_SETTINGS = {
    # Text
    "site_title": "OPTA Dashboard",
    "site_header": "Admin",
    "site_brand": "OPTA Dashboard",
    "welcome_sign": "Bienvenido a OPTA Dashboard",
    "copyright": "Powered by Dari Developer",

    # Media
    "site_logo": "core/imgs/logo.webp",
    "login_logo": "core/imgs/logo.webp",
    "login_logo_dark": "core/imgs/logo.webp",
    "site_logo_classes": "",
    "site_icon": "core/imgs/favicon.ico",
    
    # Search model in header
    "search_model": [],

    # Field name on user model that contains avatar
    # ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [
        {"name": "Opta App", "url": LANDING_HOST},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right
    # ("app" url type is not allowed)
    "usermenu_links": [
        # {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [
    ],

    # List of apps (and/or models) to base side menu ordering off of
    # (does not need to contain all apps/models)
    "order_with_respect_to": [],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        # "books": [{
        #     "name": "Make Messages",
        #     "url": "make_messages",
        #     "icon": "fas fa-comments",
        #     "permissions": ["books.view_book"]
        # }]
    },

    # Custom icons for side menu apps/models
    # See https://fontawesome.com/icons?d=gallery&m=free
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "core/css/custom.css",
    "custom_js": "core/js/custom.js",
    # Whether to link font from fonts.googleapis.com
    # (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {
    #     "auth.user": "horizontal_tabs",
    #     "auth.group": "carousel"
    # },
}


TOKEN_EXPIRED_AFTER_SECONDS = int(os.getenv('SESION_TIMEOUT', 9 * 60 * 60))
SESSION_COOKIE_AGE = int(os.getenv('SESION_TIMEOUT', 9 * 60 * 60))
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
