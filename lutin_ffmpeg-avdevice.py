#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
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
	    'ffmpeg/libavdevice/alldevices.c',
	    'ffmpeg/libavdevice/avdevice.c',
	    'ffmpeg/libavdevice/lavfi.c',
	    'ffmpeg/libavdevice/utils.c',
	    ])
	if "Linux" in target.get_type():
		my_module.add_src_file([
		    'ffmpeg/libavdevice/timefilter.c',
		    ])
		my_module.add_optionnal_depend('alsa', src_file=[
		    'ffmpeg/libavdevice/alsa.c',
		    'ffmpeg/libavdevice/alsa_dec.c',
		    'ffmpeg/libavdevice/alsa_enc.c',
		    ])
		my_module.add_src_file([
		    'ffmpeg/libavdevice/dv1394.c',
		    ])
		my_module.add_src_file([
		    'ffmpeg/libavdevice/fbdev_common.c',
		    'ffmpeg/libavdevice/fbdev_dec.c',
		    'ffmpeg/libavdevice/fbdev_enc.c',
		    ])
		my_module.add_optionnal_depend('jack', src_file=[
		    'ffmpeg/libavdevice/jack.c',
		    ])
		my_module.add_src_file([
		    'ffmpeg/libavdevice/oss.c',
		    'ffmpeg/libavdevice/oss_dec.c',
		    'ffmpeg/libavdevice/oss_enc.c',
		    ])
		my_module.add_optionnal_depend('sdl', src_file=[
		    'ffmpeg/libavdevice/sdl.c',
		    ])
		my_module.add_src_file([
		    'ffmpeg/libavdevice/v4l2-common.c',
		    'ffmpeg/libavdevice/v4l2.c',
		    'ffmpeg/libavdevice/v4l2enc.c',
		    ])
		my_module.add_optionnal_depend('xcb', src_file=[
		    'ffmpeg/libavdevice/xcbgrab.c'
		    ])
		my_module.add_optionnal_depend('X11', src_file=[
		    'ffmpeg/libavdevice/xv.c'
		    ])
	if "Windows" in target.get_type():
		my_module.add_src_file([
		    'ffmpeg/libavdevice/dshow.c',
		    'ffmpeg/libavdevice/dshow_common.c',
		    'ffmpeg/libavdevice/dshow_crossbar.c',
		    'ffmpeg/libavdevice/dshow_enummediatypes.c',
		    'ffmpeg/libavdevice/dshow_enumpins.c',
		    'ffmpeg/libavdevice/dshow_filter.c',
		    'ffmpeg/libavdevice/dshow_pin.c',
		    'ffmpeg/libavdevice/gdigrab.c',
		    'ffmpeg/libavdevice/vfwcap.c',
		    ])
	"""
	my_module.add_header_file([
	    'module-name/file1.h',
	    'module-name/file2.h'
	    ])
	"""
	my_module.compile_version("c", 1999)
	my_module.add_path("ffmpeg")
	
	lutinLib_ffmpegCommon.add_common_property(target, my_module);
	
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	my_module.add_depend([
	    'ffmpeg-avfilter',
	    'ffmpeg-avutil',
	    ])
	
	return True