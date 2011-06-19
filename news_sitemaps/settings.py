from django.conf import settings

NAME = getattr(settings, 'PUBLICATION_NAME', 'The Example Times')
LANG = getattr(settings, 'PUBLICATION_LANGUAGE', getattr(settings, 'LANGUAGE_CODE', 'en'))

if not LANG in ('zh-cn','zh-tw'):
    LANG = LANG.split('-')[0]
