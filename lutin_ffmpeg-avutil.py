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
	    'ffmpeg/libavutil/adler32.c',
	    'ffmpeg/libavutil/aes.c',
	    'ffmpeg/libavutil/aes_ctr.c',
	    'ffmpeg/libavutil/audio_fifo.c',
	    'ffmpeg/libavutil/avstring.c',
	    'ffmpeg/libavutil/base64.c',
	    'ffmpeg/libavutil/blowfish.c',
	    'ffmpeg/libavutil/bprint.c',
	    'ffmpeg/libavutil/buffer.c',
	    'ffmpeg/libavutil/camellia.c',
	    'ffmpeg/libavutil/cast5.c',
	    'ffmpeg/libavutil/channel_layout.c',
	    'ffmpeg/libavutil/color_utils.c',
	    'ffmpeg/libavutil/cpu.c',
	    'ffmpeg/libavutil/crc.c',
	    'ffmpeg/libavutil/des.c',
	    'ffmpeg/libavutil/dict.c',
	    'ffmpeg/libavutil/display.c',
	    'ffmpeg/libavutil/downmix_info.c',
	    'ffmpeg/libavutil/error.c',
	    'ffmpeg/libavutil/eval.c',
	    'ffmpeg/libavutil/fifo.c',
	    'ffmpeg/libavutil/file.c',
	    'ffmpeg/libavutil/file_open.c',
	    'ffmpeg/libavutil/fixed_dsp.c',
	    'ffmpeg/libavutil/float_dsp.c',
	    'ffmpeg/libavutil/frame.c',
	    'ffmpeg/libavutil/hash.c',
	    'ffmpeg/libavutil/hmac.c',
	    'ffmpeg/libavutil/hwcontext.c',
	    'ffmpeg/libavutil/imgutils.c',
	    'ffmpeg/libavutil/integer.c',
	    'ffmpeg/libavutil/intmath.c',
	    'ffmpeg/libavutil/lfg.c',
	    'ffmpeg/libavutil/lls.c',
	    'ffmpeg/libavutil/log.c',
	    'ffmpeg/libavutil/log2_tab.c',
	    'ffmpeg/libavutil/lzo.c',
	    'ffmpeg/libavutil/mastering_display_metadata.c',
	    'ffmpeg/libavutil/mathematics.c',
	    'ffmpeg/libavutil/md5.c',
	    'ffmpeg/libavutil/mem.c',
	    'ffmpeg/libavutil/murmur3.c',
	    'ffmpeg/libavutil/opt.c',
	    'ffmpeg/libavutil/parseutils.c',
	    'ffmpeg/libavutil/pixdesc.c',
	    'ffmpeg/libavutil/pixelutils.c',
	    'ffmpeg/libavutil/random_seed.c',
	    'ffmpeg/libavutil/rational.c',
	    'ffmpeg/libavutil/rc4.c',
	    'ffmpeg/libavutil/reverse.c',
	    'ffmpeg/libavutil/ripemd.c',
	    'ffmpeg/libavutil/samplefmt.c',
	    'ffmpeg/libavutil/sha.c',
	    'ffmpeg/libavutil/sha512.c',
	    'ffmpeg/libavutil/stereo3d.c',
	    'ffmpeg/libavutil/tea.c',
	    'ffmpeg/libavutil/threadmessage.c',
	    'ffmpeg/libavutil/time.c',
	    'ffmpeg/libavutil/timecode.c',
	    'ffmpeg/libavutil/tree.c',
	    'ffmpeg/libavutil/twofish.c',
	    'ffmpeg/libavutil/utils.c',
	    'ffmpeg/libavutil/x86/cpu.c',
	    'ffmpeg/libavutil/x86/fixed_dsp_init.c',
	    'ffmpeg/libavutil/x86/float_dsp_init.c',
	    'ffmpeg/libavutil/x86/lls_init.c',
	    'ffmpeg/libavutil/x86/pixelutils_init.c',
	    'ffmpeg/libavutil/xga_font_data.c',
	    'ffmpeg/libavutil/xtea.c',
	    ])
	my_module.compile_version("c", 1999, gnu=True)
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ffmpeg"), export=True)
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generated"), export=True)
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

	return my_module