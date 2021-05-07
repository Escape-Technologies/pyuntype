"""Print Escape Logo."""

from loguru import logger

MESSAGE = r"""

  _____  __   __ _     _ __   _ _______ __   __  _____  _______
 |_____]   \_/   |     | | \  |    |      \_/   |_____] |______
 |          |    |_____| |  \_|    |       |    |       |______
                                                                                       
            """


def title() -> None:
    """Main function."""

    logger.info(MESSAGE)
