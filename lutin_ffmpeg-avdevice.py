#!/usr/bin/python
import lutin.module as module
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

# create the module
# @param[in] target reference on the Target that is currently build
# @param[in] module_name Name of the module that is extract from the file name (to be generic)
def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/libavdevice/alldevices.c',
	    ])
	my_module.add_optionnal_depend('alsa', src_file=[
	    'ffmpeg/libavdevice/alsa.c',
	    'ffmpeg/libavdevice/alsa_dec.c',
	    'ffmpeg/libavdevice/alsa_enc.c',
	    ])
	my_module.add_src_file([
	    'ffmpeg/libavdevice/avdevice.c',
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
	    'ffmpeg/libavdevice/lavfi.c',
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
	    'ffmpeg/libavdevice/timefilter.c',
	    'ffmpeg/libavdevice/utils.c',
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
	
	"""
	my_module.add_header_file([
	    'module-name/file1.h',
	    'module-name/file2.h'
	    ])
	"""
	my_module.compile_version("c", 1999, gnu=True)
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ffmpeg"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generated"))
	my_module.add_flag('c', [
	    "-D_ISOC99_SOURCE",
	    "-D_FILE_OFFSET_BITS=64",
	    "-D_LARGEFILE_SOURCE",
	    "-D_POSIX_C_SOURCE=200112",
	    "-D_XOPEN_SOURCE=600",
	    "-DZLIB_CONST",
	    "-DHAVE_AV_CONFIG_H",
	    "-D_GNU_SOURCE=1",
	    "-D_REENTRANT",
	    "-DPIC",
	    ])
	#-I/usr/include/SDL
	my_module.add_flag('c', [
	    "-Wdeclaration-after-statement",
	    "-Wall",
	    "-Wdisabled-optimization",
	    "-Wpointer-arith",
	    "-Wredundant-decls",
	    "-Wwrite-strings",
	    "-Wtype-limits",
	    "-Wundef",
	    "-Wmissing-prototypes",
	    "-Wno-pointer-to-int-cast",
	    "-Wstrict-prototypes",
	    "-Wempty-body",
	    "-Wno-parentheses",
	    "-Wno-switch",
	    "-Wno-format-zero-length",
	    "-Wno-pointer-sign",
	    "-Wno-unused-const-variable",
	    "-fno-math-errno",
	    "-fno-signed-zeros",
	    "-Werror=format-security",
	    "-Werror=implicit-function-declaration",
	    "-Werror=missing-prototypes",
	    "-Werror=return-type",
	    "-Werror=vla",
	    "-Wformat",
	    "-fdiagnostics-color=auto",
	    ])
	if target.get_compilator() == "clang":
		my_module.add_flag('c', [ "-Wno-uninitialized"])
	else:
		my_module.add_flag('c', [ "-Wno-maybe-uninitialized"])
	if "Linux" in target.get_type():
		# TODO: Check the real impact ...
		my_module.add_flag('link-dynamic', ["-Wl,-Bsymbolic"])
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	my_module.add_depend('ffmpeg-avfilter')
	
	return my_module