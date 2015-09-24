#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.version import LooseVersion
from django import get_version

import os

django_version = LooseVersion(get_version())

HELPER_SETTINGS = {
    'TIME_ZONE': 'Europe/Zurich',
    'LANGUAGES': (
        ('en', 'English'),
        ('de', 'German'),
        ('fr', 'French'),
    ),
    'INSTALLED_APPS': [
        'aldryn_apphook_reload',
        'aldryn_apphooks_config',
        'aldryn_categories',
        'aldryn_people',
        'aldryn_reversion',
        'djangocms_text_ckeditor',
        'easy_thumbnails',
        'filer',
        'mptt',
        'parler',
        'reversion',
        'sortedm2m',
        'taggit',
    ],
    'TEMPLATE_DIRS': (
        os.path.join(
            os.path.dirname(__file__),
            'aldryn_newsblog', 'tests', 'templates'),
    ),
    'ALDRYN_NEWSBLOG_TEMPLATE_PREFIXES': [('dummy', 'dummy'), ],
    'ALDRYN_BOILERPLATE_NAME': 'bootstrap3',
    # app-specific
    'PARLER_LANGUAGES': {
        1: (
            {'code': 'de', },
            {'code': 'fr', },
            {'code': 'en', },
        ),
        'default': {
            'hide_untranslated': True,  # PLEASE DO NOT CHANGE THIS
        }
    },
    'SITE_ID': 1,
    'CMS_LANGUAGES': {
        1: [
            {
                'code': 'de',
                'name': 'Deutsche',
                'fallbacks': ['en', ]  # FOR TESTING DO NOT ADD 'fr' HERE
            },
            {
                'code': 'fr',
                'name': u'Française',
                'fallbacks': ['en', ]  # FOR TESTING DO NOT ADD 'de' HERE
            },
            {
                'code': 'en',
                'name': 'English',
                'fallbacks': ['de', 'fr', ]
            },
            {
                'code': 'it',
                'name': 'Italiano',
                'fallbacks': ['fr', ]  # FOR TESTING, LEAVE AS ONLY 'fr'
            },
        ],
        'default': {
            'redirect_on_fallback': True,  # PLEASE DO NOT CHANGE THIS
        }
    },
    #
    # NOTE: The following setting `PARLER_ENABLE_CACHING = False` is required
    # for tests to pass.
    #
    # There appears to be a bug in Parler which leaves translations in Parler's
    # cache even after the parent object has been deleted. In production
    # environments, this is unlikely to affect anything, because newly created
    # objects will have new IDs. In testing, new objects are created with IDs
    # that were previously used, which reveals this issue.
    #
    'PARLER_ENABLE_CACHING': False,
    'ALDRYN_SEARCH_DEFAULT_LANGUAGE': 'en',
    'HAYSTACK_CONNECTIONS': {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
        'de': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    },
    'THUMBNAIL_HIGH_RESOLUTION': True,
    'THUMBNAIL_PROCESSORS': (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        # 'easy_thumbnails.processors.scale_and_crop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    ),
    # 'DATABASES': {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': 'mydatabase',
    #     },
    #     'mysql': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': 'newsblog_test',
    #         'USER': 'root',
    #         'PASSWORD': '',
    #         'HOST': '',
    #         'PORT': '3306',
    #     },
    #     'postgres': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'newsblog_test',
    #         'USER': 'test',
    #         'PASSWORD': '',
    #         'HOST': '127.0.0.1',
    #         'PORT': '5432',
    #     }
    # }
}


# This set of MW classes should work for Django 1.6 and 1.7.
MIDDLEWARE_CLASSES_17 = [
    'aldryn_apphook_reload.middleware.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

HELPER_SETTINGS['MIDDLEWARE_CLASSES'] = MIDDLEWARE_CLASSES_17


def run():
    from djangocms_helper import runner
    # --boilerplate option will ensure correct boilerplate settings are
    # added to settings
    runner.cms('aldryn_newsblog', extra_args=['--boilerplate'])

if __name__ == "__main__":
    run()
