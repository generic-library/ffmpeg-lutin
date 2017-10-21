#!/usr/bin/python
import lutin.tools as tools
import lutin.debug as debug
import os
import lutinLib_ffmpegCommon

# configure windows: ./configure --arch=x86 --target-os=mingw32 --cross-prefix=i686-w64-mingw32- --pkg-config=pkg-config --disable-yasm --disable-programs --disable-doc --disable-schannel --disable-sdl --disable-securetransport --disable-xlib --disable-audiotoolbox --disable-d3d11va --disable-dxva2 --disable-vaapi --disable-vda --disable-vdpau --disable-videotoolbox --disable-bzlib --disable-iconv --disable-libxcb --disable-lzma --disable-xvmc
# configure Linux: ./configure --enable-shared --disable-yasm --disable-programs --disable-doc --disable-schannel --disable-sdl --disable-securetransport --disable-xlib --disable-audiotoolbox --disable-d3d11va --disable-dxva2 --disable-vaapi --disable-vda --disable-vdpau --disable-videotoolbox --disable-bzlib --disable-iconv --disable-libxcb --disable-lzma --disable-xvmc --enable-shared
# configure Android: 
#      export NDKROOT=~/dev/perso/android/ndk
#      export ARCH=arm
#      export CPU=armv7-a
#      export TARGET_CFLAGS="-marm -march=armv7-a -mfloat-abi=softfp -mfpu=neon -mtune=cortex-a8 -mvectorize-with-neon-quad"
#      export TARGET_LDFLAGS="-Wl,--fix-cortex-a8"
#      export EABI="armeabi-v7a"
#      export PREBUILT=$NDKROOT/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64
#      export CC="$PREBUILT/bin/arm-linux-androideabi-gcc"
#      export CXX="$PREBUILT/bin/arm-linux-androideabi-g++"
#      export STRIP="$PREBUILT/bin/arm-linux-androideabi-strip"
#      export CROSS_PREFIX="$PREBUILT/bin/arm-linux-androideabi-"
#      export HOST="arm-linux-androideabi"
#      export PLATFORM=$NDKROOT/platforms/android-8/arch-arm
#      ./configure --target-os=linux --arch=$ARCH --cpu=$CPU --enable-shared --disable-static --disable-doc --disable-ffmpeg --disable-ffplay --disable-ffserver --disable-ffprobe \
#                  --disable-avdevice --disable-encoders --disable-muxers --disable-devices --disable-protocols --disable-avfilter --enable-optimizations --enable-protocol=file \
#                  --enable-protocol=http --enable-protocol=hls --enable-protocol=mmsh --enable-protocol=mmst --enable-protocol=rtmp --enable-protocol=rtmpe --enable-protocol=rtmps \
#                  --enable-protocol=rtmpt --enable-protocol=rtmpte --enable-protocol=rtmpts --enable-protocol=rtp --enable-protocol=rtsp --enable-protocol=udp \
#                  --enable-protocol=applehttp --enable-protocol=https --enable-protocol=tls --disable-avdevice --disable-decoder=dca --disable-demuxer=dts \
#                  --disable-parser=dca --disable-fast-unaligned --disable-symver --enable-cross-compile --sysroot=$PLATFORM --cc=$CC \
#                  --cross-prefix=$CROSS_PREFIX --extra-cflags="-I$PLATFORM/usr/include -fPIC -DANDROID -D_FILE_OFFSET_BITS=64 \
#                  -D_LARGEFILE_SOURCE $TARGET_CFLAGS" --extra-ldflags="$TARGET_LDFLAGS  -L$PLATFORM/usr/lib"
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
	return False
	
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


