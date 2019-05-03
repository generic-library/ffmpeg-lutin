#!/usr/bin/python
import lutin.tools as tools
import realog.debug as debug
import os
import lutinLib_ffmpegCommon

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
	
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/libswresample/audioconvert.c',
	    'ffmpeg/libswresample/dither.c',
	    'ffmpeg/libswresample/options.c',
	    'ffmpeg/libswresample/rematrix.c',
	    'ffmpeg/libswresample/resample.c',
	    'ffmpeg/libswresample/resample_dsp.c',
	    'ffmpeg/libswresample/swresample.c',
	    'ffmpeg/libswresample/swresample_frame.c',
	    ])
	if target.get_arch() == "x86":
		my_module.add_src_file([
		    'ffmpeg/libswresample/x86/audio_convert_init.c',
		    'ffmpeg/libswresample/x86/rematrix_init.c',
		    'ffmpeg/libswresample/x86/resample_init.c',
		    ])
	elif     target.get_arch() == "arm" \
	     and target.get_bus_size() == "32":
		my_module.add_src_file([
		    'ffmpeg/libswresample/arm/audio_convert_init.c',
		    'ffmpeg/libswresample/arm/audio_convert_neon.S',
		    'ffmpeg/libswresample/arm/resample.S',
		    'ffmpeg/libswresample/arm/resample_init.c',
		    ])
	elif     target.get_arch() == "arm" \
	     and target.get_bus_size() == "64":
		my_module.add_src_file([
		    'ffmpeg/libswresample/aarch64/audio_convert_init.c',
		    'ffmpeg/libswresample/aarch64/audio_convert_neon.S',
		    'ffmpeg/libswresample/aarch64/neontest.c',
		    ])
	else:
		debug.warning("unknow architecture ...");
	my_module.compile_version("c", 1999)
	
	lutinLib_ffmpegCommon.add_common_property(target, my_module);
	
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	my_module.add_depend([
	    'ffmpeg-avutil',
	    'ffmpeg-headers',
	    ])
	return True
	


