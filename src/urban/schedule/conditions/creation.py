# -*- coding: utf-8 -*-
from Products.urban.interfaces import IIntentionToSubmitAmendedPlans
from imio.schedule.content.condition import CreationCondition


class IsCODT2024(CreationCondition):
    """Validate that the current licence is impacted by the new CODT reform"""

    def evaluate(self):
        licence = self.task_container
        return licence.is_CODT2024()


class IsNotCODT2024(CreationCondition):
    """Validate that the current licence is not impacted by the new CODT reform"""

    def evaluate(self):
        licence = self.task_container
        return licence.is_CODT2024() is not True


class HasAmendedPlans(CreationCondition):
    """"""

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(IIntentionToSubmitAmendedPlans)
        return event is not None


class IsPloneMeetingMeetingDone(CreationCondition):
    pass


class IsPloneMeetingCollegeDone(IsPloneMeetingMeetingDone):
    pass


class IsPloneMeetingCouncilDone(IsPloneMeetingMeetingDone):
    pass
