# -*- coding: utf-8 -*-
from Products.urban.interfaces import ICessionEvent
from imio.schedule.content.condition import EndCondition
from plone import api


class IsSuspended(EndCondition):
    """Validate that the current licence is impacted by the new CODT reform"""

    def evaluate(self):
        licence = self.task_container
        current_state = api.content.get_state(licence)
        return current_state == "suspension"


class CessionAcknowledgmentDone(EndCondition):
  

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(ICessionEvent, state="closed")
        return event is not None
