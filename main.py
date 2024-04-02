import pyshorteners

def shorten_url(long_url):
    """Shortens a given URL using the TinyURL API.

    Args:
        long_url (str): The URL to be shortened.

    Returns:
        str: The shortened URL.

    Raises:
        Exception: If there's an error shortening the URL.
    """

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        raise Exception(f"Error shortening URL: {e}")

# Example usage:
url_to_shorten = input("Enter the URL to shorten: ")
shortened_url = shorten_url(url_to_shorten)
print("Shortened URL:", shortened_url)
