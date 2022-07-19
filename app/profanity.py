import logging
import random


def check_post_for_foul_language(paragraphs: list[str]) -> str:
    """Simulates the profanity API that checks each paragraph of a blog post

    Args:
        paragraphs (list[str]): List of paragraphs in blog post request

    Returns:
        str: Either "yes", "no", or "unknown" if API fails
    """
    for paragraph in paragraphs:
        hasFoulLanguage = random.choice(["yes", "no", "unknown"])
    if hasFoulLanguage == "unknown":
        logging.warning("Set hasFoulLanguage = 'unknown' as profanity API is down")
    return hasFoulLanguage
