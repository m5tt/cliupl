#!/bin/env python

import argparse
import importlib

PLUGIN_DIR = 'plugins'
DEFAULT_UPLSITE = 'tiikoni'


def strip_exif(img_file):
    """
    strip exif data from file using exiftool,
    providing its present
    """
    pass    # TODO


def load_plugin(plugin_name):
    plugin_full_name = PLUGIN_DIR + '.' + plugin_name
    return getattr(importlib.import_module(plugin_full_name),
                   plugin_name.capitalize())()


def get_args():
    arg_parser = argparse.ArgumentParser(description='A command line image uploader')
    arg_parser.add_argument('--img-file', required=True, type=str,
                            help='Image to upload')
    arg_parser.add_argument('--site', default=DEFAULT_UPLSITE, required=False, type=str,
                            help='Specify a upload site plugin')
    arg_parser.add_argument('--strip', action='store_true', required=False, help='Strip exif data before uploading')
    return arg_parser.parse_known_args()


def main():
    args = get_args()
    img_file = args[0].img_file
    plugin_name = args[0].site
    strip = args[0].strip

    if strip:
        strip_exif(img_file)

    plugin = load_plugin(plugin_name)
    plugin.upload(img_file, args[1])



if __name__ == '__main__':
    main()
