from brokers.hdfc.client import HDFCBroker
from core.logger import log


def main():

    log.info("=" * 50)

    broker = HDFCBroker()

    log.info("TradeWiz initialized successfully.")

    log.info("=" * 50)


if __name__ == "__main__":
    main()