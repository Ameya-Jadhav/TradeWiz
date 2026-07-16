from core.broker.base import Broker
from core.logger import log


class HDFCBroker(Broker):
    """
    HDFC Sky Broker Implementation
    """

    def __init__(self):
        log.info("Initializing HDFC Sky Broker")

    def login(self):
        log.info("Login requested")
        raise NotImplementedError("HDFC Login not implemented")

    def logout(self):
        log.info("Logout requested")
        raise NotImplementedError("HDFC Logout not implemented")