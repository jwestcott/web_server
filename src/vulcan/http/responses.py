from typing import Dict

from vulcan.utils import TimestampMixin

class BaseResponse(TimestampMixin):
    """
    Base class for all response objects. Uses the TimestampMixin to provide timestamp capabilitites.
    """

    def __init__(self):
        super().__init__()


class HTTPResponse(BaseResponse):
    pass