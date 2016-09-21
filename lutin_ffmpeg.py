#!/usr/bin/python
import lutin.module as module
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

# create the module
# @param[in] target reference on the Target that is currently build
# @param[in] module_name Name of the module that is extract from the file name (to be generic)
def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/ffmpeg.c',
	    'ffmpeg/cmdutils.c',
	    'ffmpeg/ffmpeg_opt.c',
	    'ffmpeg/ffmpeg_filter.c',
	    'ffmpeg/ffmpeg_vaapi.c',
	    #'ffmpeg/ffmpeg_vdpau.c',
	    ])
	
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ffmpeg"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generated"))
	my_module.add_depend([
	    'ffmpeg-libs',
	    'va',
	    'vdpau',
	    ])
	return my_module


