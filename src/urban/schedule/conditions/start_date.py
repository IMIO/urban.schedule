# -*- coding: utf-8 -*-
from datetime import timedelta

from Products.urban.interfaces import IIntentionToSubmitAmendedPlans
from imio.schedule.content.logic import StartDate
from imio.schedule.interfaces import ICalculationDelay

from zope.component import queryMultiAdapter


class AcknowledgmentLimitDate(StartDate):
    """
    Acknowledgment limit date is the deposit date + (20 or 30).
    If there is modified blueprints,
    the limit date is the old licence notification limit date.
    """

    def start_date(self):
        # XXX: executed 5 times at licence creation during test; why ?
        licence = self.task_container
        limit_date = None
        if (
            hasattr(licence, "getHasModifiedBlueprints")
            and not licence.getHasModifiedBlueprints()
        ):
            deposit = licence.getLastDeposit()
            date = deposit and deposit.getEventDate()
            delay = 20
            if licence.is_CODT2024() is True:
                delay = 30
            limit_date = date and date + delay or None
        elif hasattr(licence, "getLastAcknowledgment"):
            # XXX Need review for CODT 2024
            ack = licence.getLastAcknowledgment(state="closed")
            annonced_delay = queryMultiAdapter(
                (licence, self.task),
                ICalculationDelay,
                "urban.schedule.delay.annonced_delay",
            )
            annonced_delay = (
                annonced_delay
                and annonced_delay.calculate_delay(with_modified_blueprints=False)
                or 0
            )
            limit_date = ack and ack.getEventDate() + annonced_delay
        return limit_date


class AmendedPlansLimitDate(StartDate):
    """
    Returns amended plans event's limit date, or its receipt date + 180 days
    """

    def start_date(self):
        licence = self.task_container
        event = licence.getLastEvent(IIntentionToSubmitAmendedPlans)
        limit_date = None

        if event:
            ultime_date = event.getUltimeDate()
            if ultime_date:
                limit_date = ultime_date
            else:
                receipt_date = event.getReceiptDate()
                if receipt_date:
                    limit_date = receipt_date + 180

        return limit_date
