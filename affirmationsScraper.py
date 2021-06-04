import requests
from bs4 import BeautifulSoup


# This function gathers affirmations from "https://www.affirmations.dev/"
def get_affirmation():
    # Sets result as the Chippewa Facebook posts page
    result = requests.get("https://www.affirmations.dev/")

    # Grab the source for the page
    src = result.content

    # Parse the text for the affirmation
    content = BeautifulSoup(src, 'html.parser')

    # Format the affirmation
    content = str(content)
    content = content[15:]
    size = len(content)
    content = content[:size - 1]
    content = str(content)
    content = content.encode("ascii", "ignore")
    content = content.decode()

    # Return the affirmation
    return content
