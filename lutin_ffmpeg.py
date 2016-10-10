#!/usr/bin/python
import lutin.tools as tools
import lutin.debug as debug
import os
import lutinLib_ffmpegCommon

# configure windows: ./configure --arch=x86 --target-os=mingw32 --cross-prefix=i686-w64-mingw32- --pkg-config=pkg-config --disable-yasm --disable-programs --disable-doc --disable-schannel --disable-sdl --disable-securetransport --disable-xlib --disable-audiotoolbox --disable-d3d11va --disable-dxva2 --disable-vaapi --disable-vda --disable-vdpau --disable-videotoolbox --disable-bzlib --disable-iconv --disable-libxcb --disable-lzma --disable-xvmc
# configure Linux: ./configure --enable-shared --disable-yasm --disable-programs --disable-doc --disable-schannel --disable-sdl --disable-securetransport --disable-xlib --disable-audiotoolbox --disable-d3d11va --disable-dxva2 --disable-vaapi --disable-vda --disable-vdpau --disable-videotoolbox --disable-bzlib --disable-iconv --disable-libxcb --disable-lzma --disable-xvmc --enable-shared

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

def configure(target, my_module):
	
	# add the file to compile:
	my_module.add_src_file([
	    'ffmpeg/ffmpeg.c',
	    'ffmpeg/cmdutils.c',
	    'ffmpeg/ffmpeg_opt.c',
	    'ffmpeg/ffmpeg_filter.c',
	    #'ffmpeg/ffmpeg_vdpau.c',
	    ])
	if "Windows" not in target.get_type():
		my_module.add_src_file([
		    'ffmpeg/ffmpeg_vaapi.c',
		    ])
	
	my_module.add_path("ffmpeg")
	lutinLib_ffmpegCommon.add_generate_path(target, my_module)
	my_module.add_depend([
	    'ffmpeg-libs',
	    ])
	if "Windows" not in target.get_type():
		my_module.add_depend([
		    'va',
		    'vdpau',
		    ])
	else:
		my_module.add_depend([
		    'ws2',
		    'avicap',
		    'gdi',
		    'psapi',
		    'ole',
		    'strmiids',
		    'uuid',
		    'oleaut',
		    'advapi',
		    'shell',
		    'shlwapi',
		    ])
		    

		#-Wl,-rpath-link=libpostproc:libswresample:libswscale:libavfilter:libavdevice:libavformat:libavcodec:libavutil:libavresample
		my_module.add_flag("link", [
		    "-Wl,--nxcompat,--dynamicbase",
		    "-Wl,--high-entropy-va",
		    "-Wl,--as-needed",
		    "-Wl,--warn-common",
		    ])
	return True


