# -*- coding: utf-8 -*-

from urban.schedule import utils

import logging

logger = logging.getLogger("urban.events: migrations")


def import_schedule_config(context):
    utils.import_all_config()


def update_reception(context):
    logger.info("starting : Update reception tasks")
    if "standard" in utils.get_configs():
        utils.import_all_config(
            base_json_path="./profiles/config/standard",
            handle_existing_content=utils.ExistingContent.UPDATE,
            match_filename="reception.json",
        )
    else:
        logger.info("nothing to upgrade")
    logger.info("upgrade done!")
