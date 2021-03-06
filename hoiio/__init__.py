import urllib
import urllib2

import service.voice
import service.sms
import service.fax
import service.ivr
import service.number
import service.account

class Hoiio(object):

    # Services as class attributes
    voice = service.voice.Voice()
    sms = service.sms.Sms()
    number = service.number.Number()
    fax = service.fax.Fax()
    ivr = service.ivr.Ivr()
    account = service.account.Account()

    services = [voice, sms, number, fax, ivr, account]

    @staticmethod
    def init(app_id, access_token):
        for service in Hoiio.services:
            service.set_auth(app_id, access_token)
            service._Hoiio = Hoiio

    # Other configurations
    # Implicit phone number prefix
    prefix = '1'
    # Set debuglevel to 1 to print logs
    debuglevel = 0

class CallStatus:
    """ The Call Status"""
    ANSWERED = 'answered'
    UNANSWERED = 'unanswered'
    FAILED = 'failed'
    BUSY = 'busy'
    ONGOING = 'ongoing'

class SmsStatus:
    """ The SMS Status"""
    QUEUED = 'queued'
    DELIVERED = 'delivered'
    FAILED = 'failed'
    ERROR = 'error'
    RECEIVED = 'received'

class FaxStatus:
    """ The Fax Status"""
    ANSWERED = 'answered'
    UNANSWERED = 'unanswered'
    FAILED = 'failed'
    BUSY = 'busy'
    ONGOING = 'ongoing'


