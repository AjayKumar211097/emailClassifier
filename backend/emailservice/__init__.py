# emailservice/__init__.py allows direct import usage:
# from emailservice import send_email

from .mailer import send_email

__all__ = ["send_email"]