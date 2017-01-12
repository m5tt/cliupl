#!/bin/env python

import argparse
import webbrowser

import requests
from .baseplugin import UplSitePlugin

TIIKONI_DAYS_KEY = 'days'
TIIKONI_HOURS_KEY = 'hours'
TIIKONI_MINUTES_KEY = 'minutes'

TIIKONI_FILE_KEY = 'file'
TIIKONI_UPLOAD_URL = 'http://www.tiikoni.com/tis/upload/upload.php'

TIIKONI_DEFAULT_DAYS = '0'
TIIKONI_DEFAULT_HOURS = '4'
TIIKONI_DEFAULT_MINUTES = '0'


class Tiikoni(UplSitePlugin):
    def upload(self, img_file, args):
        parsed_args = self.parse_args(args)
        data = {
            TIIKONI_DAYS_KEY: parsed_args.expire_days,
            TIIKONI_HOURS_KEY: parsed_args.expire_hours,
            TIIKONI_MINUTES_KEY: parsed_args.expire_minutes
        }

        files = {
            TIIKONI_FILE_KEY: (img_file, open(img_file, 'rb'), 'image/png')
        }

        response = requests.post(TIIKONI_UPLOAD_URL, files=files, data=data)
        webbrowser.open(response.url)

        # TODO error handling

    def parse_args(self, args):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--expire-days', '-ed', default=TIIKONI_DEFAULT_DAYS,
                                required=False, type=str, help='How many days this will expire in')
        arg_parser.add_argument('--expire-hours', '-eh', default=TIIKONI_DEFAULT_HOURS,
                                required=False, type=str, help='How many hours this will expire in')
        arg_parser.add_argument('--expire-minutes', '-em', default=TIIKONI_DEFAULT_MINUTES,
                                required=False, type=str, help='How many minutes this will expire in')

        return arg_parser.parse_args(args=args)


