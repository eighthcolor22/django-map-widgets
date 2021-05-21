from django.conf import settings as django_settings
from mapwidgets.settings import MapWidgetSettings, mw_settings

__all__ = (
    'get_google_maps_api_key',
)

def get_google_maps_api_key() -> str:
    if 'constance' in django_settings.INSTALLED_APPS:
        from constance import config
        return getattr(config, 'GOOGLE_MAPS_API_KEY', mw_settings.GOOGLE_MAPS_API_KEY)

