# -*- coding: utf-8 -*-
from Products.urban.interfaces import ICessionEvent
from Products.urban.interfaces import IProvisionOfSecurity
from imio.schedule.content.condition import StartCondition


class CessionEventCreated(StartCondition):
    """Validate that a cession event has been created on the licence"""

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(ICessionEvent)
        return event is not None


class ProvisionOfSecurityEventCreated(StartCondition):
    """Validate that a provision of security event has been created on the licence
    (ACTE_CONSTITUTION_SURETE_COMMUNE notification received)"""

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(IProvisionOfSecurity)
        return event is not None
