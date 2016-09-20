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
	    'ffmpeg/libswscale/x86/hscale_fast_bilinear_simd.c',
	    'ffmpeg/libswscale/x86/rgb2rgb.c',
	    'ffmpeg/libswscale/x86/swscale.c',
	    'ffmpeg/libswscale/x86/yuv2rgb.c',
	    'ffmpeg/libswscale/yuv2rgb.c',
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