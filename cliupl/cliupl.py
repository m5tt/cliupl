#!/bin/env python

import argparse
import importlib

PLUGIN_DIR = 'plugins'
DEFAULT_UPLSITE = 'tiikoni'

class UplSitePlugin:
    """
    Abstract class for a upload site
    """

    def upload(self, img_file, args):
        raise NotImplementedError(
            f'Class {self.__class__.__name__} doesnt implement upload()')

    def parse_args(self, arg_group):
        raise NotImplementedError(
            f'Class {self.__class__.__name__} doesnt implement set_args()')


def strip_exif(img_file):
    """
    strip exif data from file using exiftool,
    providing its present
    """
    pass    # TODO


def main():
    arg_parser = argparse.ArgumentParser(description='A command line image uploader')
    arg_parser.add_argument('--img-file', required=True, type=str,
                            help='Image to upload')
    arg_parser.add_argument('--site', default=DEFAULT_UPLSITE, required=False, type=str,
                            help='Specify a upload site plugin')
    arg_parser.add_argument('--strip', action='set_true', required=False, type=str,
                            help='Strip exif data before uploading')

    args = arg_parser.parse_known_args()
    img_file = args[0].img_file
    plugin_name = args[0].site
    strip = args[0].strip_exif

    if strip:
        strip_exif(img_file)

    plugin = importlib.import_module(plugin_name, package=PLUGIN_DIR)
    plugin.upload(img_file, args)


if __name__ == '__main__':
    main()
