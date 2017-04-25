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
	    'ffmpeg/libavutil/xga_font_data.c',
	    'ffmpeg/libavutil/xtea.c',
	    ])
	if target.get_arch() == "x86":
		my_module.add_src_file([
		    'ffmpeg/libavutil/x86/cpu.c',
		    'ffmpeg/libavutil/x86/fixed_dsp_init.c',
		    'ffmpeg/libavutil/x86/float_dsp_init.c',
		    'ffmpeg/libavutil/x86/lls_init.c',
		    'ffmpeg/libavutil/x86/pixelutils_init.c',
		    ])
	elif     target.get_arch() == "arm" \
	     and target.get_bus_size() == "32":
		my_module.add_src_file([
		    'ffmpeg/libavutil/arm/float_dsp_init_arm.c',
		    'ffmpeg/libavutil/arm/float_dsp_init_neon.c',
		    'ffmpeg/libavutil/arm/float_dsp_init_vfp.c',
		    'ffmpeg/libavutil/arm/float_dsp_neon.S',
		    'ffmpeg/libavutil/arm/float_dsp_vfp.S',
		    'ffmpeg/libavutil/arm/cpu.c',
		    ])
		my_module.add_header_file([
		    'ffmpeg/libavutil/arm/asm.S',
		    ],
		    destination_path="libavutil/arm")
	elif     target.get_arch() == "arm" \
	     and target.get_bus_size() == "64":
		my_module.add_src_file([
		    'ffmpeg/libavutil/aarch64/cpu.c',
		    'ffmpeg/libavutil/aarch64/float_dsp_init.c',
		    'ffmpeg/libavutil/aarch64/float_dsp_neon.S',
		    'ffmpeg/libavutil/arm/cpu.c',
		    ])
		my_module.add_header_file([
		    'ffmpeg/libavutil/aarch64/asm.S',
		    ],
		    destination_path="libavutil/aarch64")
	else:
		debug.warning("unknow architecture ...");
	my_module.compile_version("c", 1999)
	
	lutinLib_ffmpegCommon.add_common_property(target, my_module);
	
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	my_module.add_depend('ffmpeg-headers')

	return True