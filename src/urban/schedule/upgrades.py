# -*- coding: utf-8 -*-

from urban.schedule.utils import import_all_config
from plone import api


def import_schedule_config(context):
    import_all_config()
