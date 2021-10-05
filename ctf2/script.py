import hashlib
import json
import zlib
from base64 import b64decode
from functools import lru_cache
from typing import Union, AnyStr
from uuid import UUID

from flask.json.tag import TaggedJSONSerializer
from itsdangerous import base64_decode, URLSafeTimedSerializer, BadSignature, TimestampSigner

session={'logged_in':True}
secret='BABABooey'

print(URLSafeTimedSerializer(secret_key=secret,salt='cookie-session',serializer=TaggedJSONSerializer(),signer=TimestampSigner,signer_kwargs={'key_derivation':'hmac','digest_method':hashlib.sha1}).dumps(session))
