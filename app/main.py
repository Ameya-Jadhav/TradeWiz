from brokers.hdfc.client import HDFCBroker
from core.logger import log
from core.http.client import HTTPClient
from brokers.hdfc.constants import BASE_URL


def main():

    log.info("=" * 50)

    broker = HDFCBroker()

    http = HTTPClient(BASE_URL)

    log.info("TradeWiz initialized successfully.")

    log.info("=" * 50)


if __name__ == "__main__":
    main()