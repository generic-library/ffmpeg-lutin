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
	    'ffmpeg/libswresample/audioconvert.c',
	    'ffmpeg/libswresample/dither.c',
	    'ffmpeg/libswresample/options.c',
	    'ffmpeg/libswresample/rematrix.c',
	    'ffmpeg/libswresample/resample.c',
	    'ffmpeg/libswresample/resample_dsp.c',
	    'ffmpeg/libswresample/swresample.c',
	    'ffmpeg/libswresample/swresample_frame.c',
	    'ffmpeg/libswresample/x86/audio_convert_init.c',
	    'ffmpeg/libswresample/x86/rematrix_init.c',
	    'ffmpeg/libswresample/x86/resample_init.c',
	    ])
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
	    "-Wno-maybe-uninitialized",
	    ])
	if "Linux" in target.get_type():
		# TODO: Check the real impact ...
		my_module.add_flag('link-dynamic', ["-Wl,-Bsymbolic"])
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')

	return my_module