def validate_url(url):
    """
    Validate a URL based on supported protocols and file extensions.

    Args:
        url (str): Input URL to be validated.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """

    # Supported protocols
    valid_protocols = ['http', 'https', 'ftp']

    # Supported file extensions
    valid_fileinfo = ['txt', 'csv', 'docx']

    # Split the input URL into parts
    parts = url.split('://')
    
    # Check if the URL has the correct number of parts
    if len(parts) != 2:
        return False  # Invalid URL format
    
    # Extract protocol and fileinfo
    protocol, rest = parts
    fileinfo = rest.split('/')[-1].split('.')[-1]

    # Check if the protocol is valid
    if protocol not in valid_protocols:
        return False  # Invalid protocol
    
    # Check if the file extension is valid
    if fileinfo not in valid_fileinfo:
        return False  # Invalid file extension
    
    # If both checks pass, the URL is valid
    return True

# Example usage:
url_to_validate = "https://example.com/data.csv"
if validate_url(url_to_validate):
    print(f"The URL '{url_to_validate}' is valid.")
else:
    print(f"The URL '{url_to_validate}' is not valid.")
