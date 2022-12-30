"""Authomatic Oauth configuration file

Pull secret ids and keys from environment variables set in .env
"""

import os
import env
from authomatic import Authomatic
from authomatic.providers import oauth2

OAUTH_CONFIG = {
    "Facebook": {  # This name is arbitrary but is easier if it matches oauth provider name
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Facebook,  # Use authomatic's Facebook handshake
        "consumer_key": env.FACEBOOK_ID,
        "consumer_secret": env.FACEBOOK_SECRET,
    },
    "Google": {
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Google,
        "consumer_key": env.GOOGLE_ID,
        "consumer_secret": env.GOOGLE_SECRET,
        # Google requires a scope be specified to work properly
        "scope": ["profile", "email"],
    },
}

# Instantiate Authomatic.
authomatic = Authomatic(
    OAUTH_CONFIG,
    os.getenv("AUTHOMATIC_SECRET"),
    report_errors=True,  # Set to False in production
)
