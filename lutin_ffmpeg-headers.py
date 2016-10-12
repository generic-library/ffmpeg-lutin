#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

import lutinLib_ffmpegCommon

def get_type():
	return "LIBRARY"

def get_desc():
	return "FFMPEG library header"

def get_licence():
	return "LGPL-2.1"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "ffmpeg"

def get_maintainer():
	return "authors.txt"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_header_file([
	    'ffmpeg/*.h',
	    ],
	    recursive=True)
	return True