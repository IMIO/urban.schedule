from imio.schedule.content.delay import BaseCalculationDelay

class CalculationDelayOpinionFd(BaseCalculationDelay):
    """
    """
    def calculate_delay(self):
        licence = self.task_container
        delay = 35
        if licence.is_CODT2024() is True:
            delay = 30
        return delay
