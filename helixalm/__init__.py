"""
Helix ALM API Python Wrapper

helixalm is a python package that allows for simple access to Helix ALM's REST API.
"""

import sys

# Enforce Python 3.6+
if sys.verion_info.major != 3 or sys.verion_info.minor < 6:
    raise ImportError('Helix ALM package requires Python 3.6 or greater.')
