#!/usr/bin/python
import lutin.tools as tools
import lutin.debug as debug
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "FFMPEG library"

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
	
	# or other user lib:
	my_module.add_depend([
	    'ffmpeg-avcodec',
	    'ffmpeg-avfilter',
	    'ffmpeg-avswresample',
	    'ffmpeg-avutil',
	    'ffmpeg-avdevice',
	    'ffmpeg-avformat',
	    'ffmpeg-avswscale',
	    ])
	
	return True

