#!/usr/bin/python3
'''
    Backend webapi for the ll bot
'''
import os
import psycopg2
from urllib.parse import urlparse
from bottle import Bottle, abort
from backend import MessageHandler
from .bottle_helpers import webapi, picture
from db import DB
from bot_helpers import get_message_info


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.last_message = None
        self._app = Bottle()

        if "DATABASE_URL" in os.environ and os.environ.get('DATABASE_URL') is not None:
            db = DB(os.environ["DATABASE_URL"])
        else:
            db = None
        self.backend = MessageHandler(db)

    def start(self):
        ''' start the server '''
        self._app.run(host=self.host, port=self.port)

    @webapi('POST', '/messages')
    def get_messages(self, data):
        ''' Receive a message from a spark webhook '''
        try:
            message_id = data['data']['id']
        except KeyError:
            abort(400, 'expected message id')

        message_info = get_message_info(message_id)
        try:
            self.backend.parse_message(message_info)
        except Exception as err:
            print(err)

    @picture('/images/avatar')
    def sanders_pic(self):
        ''' picture to use for the bot avatar '''
        return 'chicken.png'
