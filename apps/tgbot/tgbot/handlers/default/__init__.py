from aiogram import Dispatcher

from .start import start_cmd
from .web import WebCheckerHandler
from .whois import whois_cmd
from .icmp import ICMPCheckerHandler
from .tcp import TCPCheckerHandler


def setup(dp: Dispatcher):
    dp.register_message_handler(start_cmd, is_forwarded=False, commands=['start'])
    dp.register_message_handler(WebCheckerHandler().handler, is_forwarded=False, commands=['web', 'http'])
    dp.register_message_handler(whois_cmd, is_forwarded=False, commands=['whois'])
    dp.register_message_handler(ICMPCheckerHandler().handler, is_forwarded=False, commands=['icmp', 'ping'])
    dp.register_message_handler(TCPCheckerHandler().handler, is_forwarded=False, commands=['tcp'])
