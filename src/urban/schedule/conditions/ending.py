# -*- coding: utf-8 -*-
from Products.urban.interfaces import IAcknowledgmentOfTransfer
from Products.urban.interfaces import IReleaseOfSecurity
from imio.schedule.content.condition import EndCondition
from plone import api


class IsSuspended(EndCondition):
    """Validate that the current licence is impacted by the new CODT reform"""

    def evaluate(self):
        licence = self.task_container
        current_state = api.content.get_state(licence)
        return current_state == "suspension"


class CessionAcknowledgmentDone(EndCondition):
    """Validate that the cession acknowledgment event
    ('Prise de connaissance de la cession') is closed"""

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(IAcknowledgmentOfTransfer, state="closed")
        return event is not None


class ReleaseOfSecurityReceived(EndCondition):
    """Validate that a release of security event has been created on the licence
    (ACTE_LIBERATION_SURETE_COMMUNE notification received)"""

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(IReleaseOfSecurity)
        return event is not None
