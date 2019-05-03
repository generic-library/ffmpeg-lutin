#!/usr/bin/python
import lutin.tools as tools
import realog.debug as debug
import os
import lutinLib_ffmpegCommon

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
	return False
	if "Linux" not in target.get_type():
		return False
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/ffplay.c',
	    'ffmpeg/cmdutils.c',
	    ])
	my_module.add_path("ffmpeg")
	lutinLib_ffmpegCommon.add_generate_path(target, my_module)
	my_module.add_depend([
	    'ffmpeg-libs',
	    'va',
	    'SDL',
	    ])
	return True


