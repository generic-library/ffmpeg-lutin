#!/usr/bin/python
import realog.debug as debug
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
	
	generated_path = os.path.join("generated", target.get_name())
	generated_path_bs = os.path.join("generated", target.get_name() + "_" + str(target.get_bus_size()))
	if os.path.exists(os.path.join(os.path.dirname(__file__), generated_path_bs)) == True:
		#my_module.add_path(generated_path_bs)
		my_module.add_header_file([
		    generated_path_bs + "/*",
		    ],
		    recursive=True)
	elif os.path.exists(os.path.join(os.path.dirname(__file__), generated_path)) == True:
		#my_module.add_path(generated_path)
		my_module.add_header_file([
		    generated_path + "/*",
		    ],
		    recursive=True)
	else:
		debug.warning("get default Path for type: " + str(target.get_type()))
		#my_module.add_path("generated/Linux")
		my_module.add_header_file([
		    "generated/Linux/*",
		    ],
		    recursive=True)
	
	return True