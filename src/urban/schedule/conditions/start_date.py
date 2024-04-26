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
        elif licence.getLastEvent(IIntentionToSubmitAmendedPlans):
            deposit_event = licence.getLastDeposit()
            intention_event = licence.getLastEvent(IIntentionToSubmitAmendedPlans)

            if not deposit_event or not deposit_event.getEventDate():  # not supposed to happen
                return limit_date

            deposit_event_delay = 30 if licence.is_CODT2024() is True else 20

            # modified plans have been submitted
            if intention_event.getEventDate() < deposit_event.getEventDate():
                date = deposit_event.getEventDate()
                limit_date = date + deposit_event_delay
            else:
                # no modified plans received (either still waiting, or delay is over)
                ultime_date = intention_event.getUltimeDate()
                if ultime_date:
                    limit_date = ultime_date
                else:
                    receipt_date = intention_event.getReceiptDate()
                    if receipt_date:
                        limit_date = receipt_date + 180

                limit_date = limit_date + deposit_event_delay
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
