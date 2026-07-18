from core.broker.base import Broker
from core.logger import log

from brokers.hdfc.auth import HDFCAuth


class HDFCBroker(Broker):
    """
    HDFC Sky Broker Implementation
    """

    def __init__(self):
        self.auth = HDFCAuth()

        log.info("Initializing HDFC Sky Broker")

    def login(self):
        log.info("Login requested")
        raise NotImplementedError("Login API not implemented yet.")

    def logout(self):
        log.info("Logout requested")
        raise NotImplementedError("Logout API not implemented yet.")