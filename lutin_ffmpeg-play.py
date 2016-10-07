#!/usr/bin/python
import lutin.tools as tools
import lutin.debug as debug
import os

def get_type():
	#return "BINARY_SHARED"
	return "BINARY"

def get_desc():
	return "FFMPEG main application"

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
	
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/ffplay.c',
	    'ffmpeg/cmdutils.c',
	    ])
	
	my_module.add_path("ffmpeg")
	my_module.add_path("generated")
	my_module.add_depend([
	    'ffmpeg-libs',
	    'va',
	    'SDL',
	    ])
	return True


