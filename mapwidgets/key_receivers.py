from django.conf import settings as django_settings

__all__ = (
    'get_google_maps_api_key',
)

def get_google_maps_api_key() -> str:
    key = None
    if 'constance' in django_settings.INSTALLED_APPS:
        from constance import config
        key = getattr(config, 'GOOGLE_MAPS_API_KEY', None)

    if not key:
        key = django_settings.GOOGLE_MAPS_API_KEY

    if not key:
        raise AttributeError("Invalid settings api key")

    return key
