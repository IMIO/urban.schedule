# -*- coding: utf-8 -*-
from Products.urban.interfaces import ICessionEvent
from imio.schedule.content.condition import StartCondition


class CessionEventCreated(StartCondition):

    def evaluate(self):
        licence = self.task_container
        event = licence.getLastEvent(ICessionEvent)
        return event is not None
