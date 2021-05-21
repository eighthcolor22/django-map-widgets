from django.conf import settings as django_settings
from mapwidgets.settings import MapWidgetSettings, mw_settings

__all__ = (
    'get_google_maps_api_key',
)

def get_google_maps_api_key() -> str:
    google_key = mw_settings.GOOGLE_MAPS_API_KEY
    if 'constance' in django_settings.INSTALLED_APPS:
        from constance import config
        google_key =  getattr(config, 'GOOGLE_MAPS_API_KEY', None)
    return google_key

