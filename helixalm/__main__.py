"""
Create an command line argument parser to handle module commands that will
enable users to generate the Basic authentication token.

Token is a base64 encoded byte string containing the phrase:
    "username:password"
"""

import base64

# TODO: Move this into it's own module later?
def example_for_implementing_later(username, password):
    token_string = f'{username}:{password}'.encode()
    return base64.b64encode(token_string).decode()
