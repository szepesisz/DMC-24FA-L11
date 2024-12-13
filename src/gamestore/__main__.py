import logging


logger = logging.getLogger(__name__)

__version__ = '0.1.0'

logging.basicConfig(level=logging.DEBUG)


def main():
    logger.info('Starting GameStore %s', __version__)

if __name__ == '__main__':
    main()
