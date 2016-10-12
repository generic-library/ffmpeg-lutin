#!/usr/bin/python
import lutin.tools as tools
import lutin.debug as debug
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
	    'ffmpeg/libswscale/alphablend.c',
	    'ffmpeg/libswscale/gamma.c',
	    'ffmpeg/libswscale/hscale.c',
	    'ffmpeg/libswscale/hscale_fast_bilinear.c',
	    'ffmpeg/libswscale/input.c',
	    'ffmpeg/libswscale/options.c',
	    'ffmpeg/libswscale/output.c',
	    'ffmpeg/libswscale/rgb2rgb.c',
	    'ffmpeg/libswscale/slice.c',
	    'ffmpeg/libswscale/swscale.c',
	    'ffmpeg/libswscale/swscale_unscaled.c',
	    'ffmpeg/libswscale/utils.c',
	    'ffmpeg/libswscale/vscale.c',
	    'ffmpeg/libswscale/yuv2rgb.c',
	    ])
	if target.get_arch() == "x86":
		my_module.add_src_file([
		    'ffmpeg/libswscale/x86/hscale_fast_bilinear_simd.c',
		    'ffmpeg/libswscale/x86/rgb2rgb.c',
		    'ffmpeg/libswscale/x86/swscale.c',
		    'ffmpeg/libswscale/x86/yuv2rgb.c',
		    ])
	elif target.get_arch() == "arm":
		my_module.add_src_file([
		    'ffmpeg/libswscale/arm/hscale.S',
		    'ffmpeg/libswscale/arm/output.S',
		    'ffmpeg/libswscale/arm/rgb2yuv_neon_16.S',
		    'ffmpeg/libswscale/arm/rgb2yuv_neon_32.S',
		    'ffmpeg/libswscale/arm/swscale.c',
		    'ffmpeg/libswscale/arm/swscale_unscaled.c',
		    'ffmpeg/libswscale/arm/yuv2rgb_neon.S',
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