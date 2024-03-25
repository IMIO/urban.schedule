# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from urban.schedule.utils import import_all_config

import os


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "urban.schedule:uninstall",
        ]


def post_install(context):
    """Post install script"""
    configs = os.environ.get("URBAN_SCHEDULE_CONFIGS", "default,standard")
    configs = configs.split(",")

    for config in configs:
        import_all_config(
            base_json_path="./profiles/config/{0}".format(config),
            base_context_path="portal_urban",
        )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
