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
	    'ffmpeg/libavformat/3dostr.c',
	    'ffmpeg/libavformat/4xm.c',
	    'ffmpeg/libavformat/a64.c',
	    'ffmpeg/libavformat/aacdec.c',
	    'ffmpeg/libavformat/aadec.c',
	    'ffmpeg/libavformat/ac3dec.c',
	    'ffmpeg/libavformat/acm.c',
	    'ffmpeg/libavformat/act.c',
	    'ffmpeg/libavformat/adp.c',
	    'ffmpeg/libavformat/ads.c',
	    'ffmpeg/libavformat/adtsenc.c',
	    'ffmpeg/libavformat/adxdec.c',
	    'ffmpeg/libavformat/aea.c',
	    'ffmpeg/libavformat/afc.c',
	    'ffmpeg/libavformat/aiffdec.c',
	    'ffmpeg/libavformat/aiffenc.c',
	    'ffmpeg/libavformat/aixdec.c',
	    'ffmpeg/libavformat/allformats.c',
	    'ffmpeg/libavformat/amr.c',
	    'ffmpeg/libavformat/anm.c',
	    'ffmpeg/libavformat/apc.c',
	    'ffmpeg/libavformat/ape.c',
	    'ffmpeg/libavformat/apetag.c',
	    'ffmpeg/libavformat/apngdec.c',
	    'ffmpeg/libavformat/apngenc.c',
	    'ffmpeg/libavformat/aqtitledec.c',
	    'ffmpeg/libavformat/asf.c',
	    'ffmpeg/libavformat/asfcrypt.c',
	    'ffmpeg/libavformat/asfdec_f.c',
	    'ffmpeg/libavformat/asfdec_o.c',
	    'ffmpeg/libavformat/asfenc.c',
	    'ffmpeg/libavformat/assdec.c',
	    'ffmpeg/libavformat/assenc.c',
	    'ffmpeg/libavformat/ast.c',
	    'ffmpeg/libavformat/astdec.c',
	    'ffmpeg/libavformat/astenc.c',
	    'ffmpeg/libavformat/async.c',
	    'ffmpeg/libavformat/au.c',
	    'ffmpeg/libavformat/audiointerleave.c',
	    'ffmpeg/libavformat/avc.c',
	    'ffmpeg/libavformat/avidec.c',
	    'ffmpeg/libavformat/avienc.c',
	    'ffmpeg/libavformat/avio.c',
	    'ffmpeg/libavformat/aviobuf.c',
	    'ffmpeg/libavformat/avlanguage.c',
	    'ffmpeg/libavformat/avr.c',
	    'ffmpeg/libavformat/avs.c',
	    'ffmpeg/libavformat/bethsoftvid.c',
	    'ffmpeg/libavformat/bfi.c',
	    'ffmpeg/libavformat/bink.c',
	    'ffmpeg/libavformat/bintext.c',
	    'ffmpeg/libavformat/bit.c',
	    'ffmpeg/libavformat/bmv.c',
	    'ffmpeg/libavformat/boadec.c',
	    'ffmpeg/libavformat/brstm.c',
	    'ffmpeg/libavformat/c93.c',
	    'ffmpeg/libavformat/cache.c',
	    'ffmpeg/libavformat/caf.c',
	    'ffmpeg/libavformat/cafdec.c',
	    'ffmpeg/libavformat/cafenc.c',
	    'ffmpeg/libavformat/cavsvideodec.c',
	    'ffmpeg/libavformat/cdg.c',
	    'ffmpeg/libavformat/cdxl.c',
	    'ffmpeg/libavformat/cinedec.c',
	    'ffmpeg/libavformat/concat.c',
	    'ffmpeg/libavformat/concatdec.c',
	    'ffmpeg/libavformat/crcenc.c',
	    'ffmpeg/libavformat/crypto.c',
	    'ffmpeg/libavformat/cutils.c',
	    'ffmpeg/libavformat/dashenc.c',
	    'ffmpeg/libavformat/data_uri.c',
	    'ffmpeg/libavformat/dauddec.c',
	    'ffmpeg/libavformat/daudenc.c',
	    'ffmpeg/libavformat/dcstr.c',
	    'ffmpeg/libavformat/dfa.c',
	    'ffmpeg/libavformat/diracdec.c',
	    'ffmpeg/libavformat/dnxhddec.c',
	    'ffmpeg/libavformat/dsfdec.c',
	    'ffmpeg/libavformat/dsicin.c',
	    'ffmpeg/libavformat/dss.c',
	    'ffmpeg/libavformat/dtsdec.c',
	    'ffmpeg/libavformat/dtshddec.c',
	    'ffmpeg/libavformat/dump.c',
	    'ffmpeg/libavformat/dv.c',
	    'ffmpeg/libavformat/dvbsub.c',
	    'ffmpeg/libavformat/dvbtxt.c',
	    'ffmpeg/libavformat/dvenc.c',
	    'ffmpeg/libavformat/dxa.c',
	    'ffmpeg/libavformat/eacdata.c',
	    'ffmpeg/libavformat/electronicarts.c',
	    'ffmpeg/libavformat/epafdec.c',
	    'ffmpeg/libavformat/ffmdec.c',
	    'ffmpeg/libavformat/ffmenc.c',
	    'ffmpeg/libavformat/ffmetadec.c',
	    'ffmpeg/libavformat/ffmetaenc.c',
	    'ffmpeg/libavformat/file.c',
	    'ffmpeg/libavformat/filmstripdec.c',
	    'ffmpeg/libavformat/filmstripenc.c',
	    'ffmpeg/libavformat/flac_picture.c',
	    'ffmpeg/libavformat/flacdec.c',
	    'ffmpeg/libavformat/flacenc.c',
	    'ffmpeg/libavformat/flacenc_header.c',
	    'ffmpeg/libavformat/flic.c',
	    'ffmpeg/libavformat/flvdec.c',
	    'ffmpeg/libavformat/flvenc.c',
	    'ffmpeg/libavformat/format.c',
	    'ffmpeg/libavformat/framecrcenc.c',
	    'ffmpeg/libavformat/framehash.c',
	    'ffmpeg/libavformat/frmdec.c',
	    'ffmpeg/libavformat/fsb.c',
	    'ffmpeg/libavformat/ftp.c',
	    'ffmpeg/libavformat/g722.c',
	    'ffmpeg/libavformat/g723_1.c',
	    'ffmpeg/libavformat/g729dec.c',
	    'ffmpeg/libavformat/genh.c',
	    'ffmpeg/libavformat/gif.c',
	    'ffmpeg/libavformat/gifdec.c',
	    'ffmpeg/libavformat/gopher.c',
	    'ffmpeg/libavformat/gsmdec.c',
	    'ffmpeg/libavformat/gxf.c',
	    'ffmpeg/libavformat/gxfenc.c',
	    'ffmpeg/libavformat/h261dec.c',
	    'ffmpeg/libavformat/h263dec.c',
	    'ffmpeg/libavformat/h264dec.c',
	    'ffmpeg/libavformat/hashenc.c',
	    'ffmpeg/libavformat/hdsenc.c',
	    'ffmpeg/libavformat/hevc.c',
	    'ffmpeg/libavformat/hevcdec.c',
	    'ffmpeg/libavformat/hls.c',
	    'ffmpeg/libavformat/hlsenc.c',
	    'ffmpeg/libavformat/hlsproto.c',
	    'ffmpeg/libavformat/hnm.c',
	    'ffmpeg/libavformat/http.c',
	    'ffmpeg/libavformat/httpauth.c',
	    'ffmpeg/libavformat/icecast.c',
	    'ffmpeg/libavformat/icodec.c',
	    'ffmpeg/libavformat/icoenc.c',
	    'ffmpeg/libavformat/id3v1.c',
	    'ffmpeg/libavformat/id3v2.c',
	    'ffmpeg/libavformat/id3v2enc.c',
	    'ffmpeg/libavformat/idcin.c',
	    'ffmpeg/libavformat/idroqdec.c',
	    'ffmpeg/libavformat/idroqenc.c',
	    'ffmpeg/libavformat/iff.c',
	    'ffmpeg/libavformat/ilbc.c',
	    'ffmpeg/libavformat/img2.c',
	    'ffmpeg/libavformat/img2_alias_pix.c',
	    'ffmpeg/libavformat/img2_brender_pix.c',
	    'ffmpeg/libavformat/img2dec.c',
	    'ffmpeg/libavformat/img2enc.c',
	    'ffmpeg/libavformat/ingenientdec.c',
	    'ffmpeg/libavformat/ipmovie.c',
	    'ffmpeg/libavformat/ircam.c',
	    'ffmpeg/libavformat/ircamdec.c',
	    'ffmpeg/libavformat/ircamenc.c',
	    'ffmpeg/libavformat/isom.c',
	    'ffmpeg/libavformat/iss.c',
	    'ffmpeg/libavformat/iv8.c',
	    'ffmpeg/libavformat/ivfdec.c',
	    'ffmpeg/libavformat/ivfenc.c',
	    'ffmpeg/libavformat/jacosubdec.c',
	    'ffmpeg/libavformat/jacosubenc.c',
	    'ffmpeg/libavformat/jvdec.c',
	    'ffmpeg/libavformat/latmenc.c',
	    'ffmpeg/libavformat/lmlm4.c',
	    'ffmpeg/libavformat/loasdec.c',
	    'ffmpeg/libavformat/lrc.c',
	    'ffmpeg/libavformat/lrcdec.c',
	    'ffmpeg/libavformat/lrcenc.c',
	    'ffmpeg/libavformat/lvfdec.c',
	    'ffmpeg/libavformat/lxfdec.c',
	    'ffmpeg/libavformat/m4vdec.c',
	    'ffmpeg/libavformat/matroska.c',
	    'ffmpeg/libavformat/matroskadec.c',
	    'ffmpeg/libavformat/matroskaenc.c',
	    'ffmpeg/libavformat/md5proto.c',
	    'ffmpeg/libavformat/metadata.c',
	    'ffmpeg/libavformat/mgsts.c',
	    'ffmpeg/libavformat/microdvddec.c',
	    'ffmpeg/libavformat/microdvdenc.c',
	    'ffmpeg/libavformat/mkvtimestamp_v2.c',
	    'ffmpeg/libavformat/mlpdec.c',
	    'ffmpeg/libavformat/mlvdec.c',
	    'ffmpeg/libavformat/mm.c',
	    'ffmpeg/libavformat/mmf.c',
	    'ffmpeg/libavformat/mms.c',
	    'ffmpeg/libavformat/mmsh.c',
	    'ffmpeg/libavformat/mmst.c',
	    'ffmpeg/libavformat/mov.c',
	    'ffmpeg/libavformat/mov_chan.c',
	    'ffmpeg/libavformat/movenc.c',
	    'ffmpeg/libavformat/movenccenc.c',
	    'ffmpeg/libavformat/movenchint.c',
	    'ffmpeg/libavformat/mp3dec.c',
	    'ffmpeg/libavformat/mp3enc.c',
	    'ffmpeg/libavformat/mpc.c',
	    'ffmpeg/libavformat/mpc8.c',
	    'ffmpeg/libavformat/mpeg.c',
	    'ffmpeg/libavformat/mpegenc.c',
	    'ffmpeg/libavformat/mpegts.c',
	    'ffmpeg/libavformat/mpegtsenc.c',
	    'ffmpeg/libavformat/mpegvideodec.c',
	    'ffmpeg/libavformat/mpjpeg.c',
	    'ffmpeg/libavformat/mpjpegdec.c',
	    'ffmpeg/libavformat/mpl2dec.c',
	    'ffmpeg/libavformat/mpsubdec.c',
	    'ffmpeg/libavformat/msf.c',
	    'ffmpeg/libavformat/msnwc_tcp.c',
	    'ffmpeg/libavformat/mtaf.c',
	    'ffmpeg/libavformat/mtv.c',
	    'ffmpeg/libavformat/musx.c',
	    'ffmpeg/libavformat/mux.c',
	    'ffmpeg/libavformat/mvdec.c',
	    'ffmpeg/libavformat/mvi.c',
	    'ffmpeg/libavformat/mxf.c',
	    'ffmpeg/libavformat/mxfdec.c',
	    'ffmpeg/libavformat/mxfenc.c',
	    'ffmpeg/libavformat/mxg.c',
	    'ffmpeg/libavformat/ncdec.c',
	    'ffmpeg/libavformat/network.c',
	    'ffmpeg/libavformat/nistspheredec.c',
	    'ffmpeg/libavformat/nsvdec.c',
	    'ffmpeg/libavformat/nullenc.c',
	    'ffmpeg/libavformat/nut.c',
	    'ffmpeg/libavformat/nutdec.c',
	    'ffmpeg/libavformat/nutenc.c',
	    'ffmpeg/libavformat/nuv.c',
	    'ffmpeg/libavformat/oggdec.c',
	    'ffmpeg/libavformat/oggenc.c',
	    'ffmpeg/libavformat/oggparsecelt.c',
	    'ffmpeg/libavformat/oggparsedaala.c',
	    'ffmpeg/libavformat/oggparsedirac.c',
	    'ffmpeg/libavformat/oggparseflac.c',
	    'ffmpeg/libavformat/oggparseogm.c',
	    'ffmpeg/libavformat/oggparseopus.c',
	    'ffmpeg/libavformat/oggparseskeleton.c',
	    'ffmpeg/libavformat/oggparsespeex.c',
	    'ffmpeg/libavformat/oggparsetheora.c',
	    'ffmpeg/libavformat/oggparsevorbis.c',
	    'ffmpeg/libavformat/oggparsevp8.c',
	    'ffmpeg/libavformat/oma.c',
	    'ffmpeg/libavformat/omadec.c',
	    'ffmpeg/libavformat/omaenc.c',
	    'ffmpeg/libavformat/options.c',
	    'ffmpeg/libavformat/os_support.c',
	    'ffmpeg/libavformat/paf.c',
	    'ffmpeg/libavformat/pcm.c',
	    'ffmpeg/libavformat/pcmdec.c',
	    'ffmpeg/libavformat/pcmenc.c',
	    'ffmpeg/libavformat/pjsdec.c',
	    'ffmpeg/libavformat/pmpdec.c',
	    'ffmpeg/libavformat/protocols.c',
	    'ffmpeg/libavformat/psxstr.c',
	    'ffmpeg/libavformat/pva.c',
	    'ffmpeg/libavformat/pvfdec.c',
	    'ffmpeg/libavformat/qcp.c',
	    'ffmpeg/libavformat/qtpalette.c',
	    'ffmpeg/libavformat/r3d.c',
	    'ffmpeg/libavformat/rawdec.c',
	    'ffmpeg/libavformat/rawenc.c',
	    'ffmpeg/libavformat/rawutils.c',
	    'ffmpeg/libavformat/rawvideodec.c',
	    'ffmpeg/libavformat/rdt.c',
	    'ffmpeg/libavformat/realtextdec.c',
	    'ffmpeg/libavformat/redspark.c',
	    'ffmpeg/libavformat/replaygain.c',
	    'ffmpeg/libavformat/riff.c',
	    'ffmpeg/libavformat/riffdec.c',
	    'ffmpeg/libavformat/riffenc.c',
	    'ffmpeg/libavformat/rl2.c',
	    'ffmpeg/libavformat/rm.c',
	    'ffmpeg/libavformat/rmdec.c',
	    'ffmpeg/libavformat/rmenc.c',
	    'ffmpeg/libavformat/rmsipr.c',
	    'ffmpeg/libavformat/rpl.c',
	    'ffmpeg/libavformat/rsd.c',
	    'ffmpeg/libavformat/rso.c',
	    'ffmpeg/libavformat/rsodec.c',
	    'ffmpeg/libavformat/rsoenc.c',
	    'ffmpeg/libavformat/rtmphttp.c',
	    'ffmpeg/libavformat/rtmppkt.c',
	    'ffmpeg/libavformat/rtmpproto.c',
	    'ffmpeg/libavformat/rtp.c',
	    'ffmpeg/libavformat/rtpdec.c',
	    'ffmpeg/libavformat/rtpdec_ac3.c',
	    'ffmpeg/libavformat/rtpdec_amr.c',
	    'ffmpeg/libavformat/rtpdec_asf.c',
	    'ffmpeg/libavformat/rtpdec_dv.c',
	    'ffmpeg/libavformat/rtpdec_g726.c',
	    'ffmpeg/libavformat/rtpdec_h261.c',
	    'ffmpeg/libavformat/rtpdec_h263.c',
	    'ffmpeg/libavformat/rtpdec_h263_rfc2190.c',
	    'ffmpeg/libavformat/rtpdec_h264.c',
	    'ffmpeg/libavformat/rtpdec_hevc.c',
	    'ffmpeg/libavformat/rtpdec_ilbc.c',
	    'ffmpeg/libavformat/rtpdec_jpeg.c',
	    'ffmpeg/libavformat/rtpdec_latm.c',
	    'ffmpeg/libavformat/rtpdec_mpa_robust.c',
	    'ffmpeg/libavformat/rtpdec_mpeg12.c',
	    'ffmpeg/libavformat/rtpdec_mpeg4.c',
	    'ffmpeg/libavformat/rtpdec_mpegts.c',
	    'ffmpeg/libavformat/rtpdec_qcelp.c',
	    'ffmpeg/libavformat/rtpdec_qdm2.c',
	    'ffmpeg/libavformat/rtpdec_qt.c',
	    'ffmpeg/libavformat/rtpdec_svq3.c',
	    'ffmpeg/libavformat/rtpdec_vc2hq.c',
	    'ffmpeg/libavformat/rtpdec_vp8.c',
	    'ffmpeg/libavformat/rtpdec_vp9.c',
	    'ffmpeg/libavformat/rtpdec_xiph.c',
	    'ffmpeg/libavformat/rtpenc.c',
	    'ffmpeg/libavformat/rtpenc_aac.c',
	    'ffmpeg/libavformat/rtpenc_amr.c',
	    'ffmpeg/libavformat/rtpenc_chain.c',
	    'ffmpeg/libavformat/rtpenc_h261.c',
	    'ffmpeg/libavformat/rtpenc_h263.c',
	    'ffmpeg/libavformat/rtpenc_h263_rfc2190.c',
	    'ffmpeg/libavformat/rtpenc_h264_hevc.c',
	    'ffmpeg/libavformat/rtpenc_jpeg.c',
	    'ffmpeg/libavformat/rtpenc_latm.c',
	    'ffmpeg/libavformat/rtpenc_mpegts.c',
	    'ffmpeg/libavformat/rtpenc_mpv.c',
	    'ffmpeg/libavformat/rtpenc_vc2hq.c',
	    'ffmpeg/libavformat/rtpenc_vp8.c',
	    'ffmpeg/libavformat/rtpenc_vp9.c',
	    'ffmpeg/libavformat/rtpenc_xiph.c',
	    'ffmpeg/libavformat/rtpproto.c',
	    'ffmpeg/libavformat/rtsp.c',
	    'ffmpeg/libavformat/rtspdec.c',
	    'ffmpeg/libavformat/rtspenc.c',
	    'ffmpeg/libavformat/samidec.c',
	    'ffmpeg/libavformat/sapdec.c',
	    'ffmpeg/libavformat/sapenc.c',
	    'ffmpeg/libavformat/sauce.c',
	    'ffmpeg/libavformat/sbgdec.c',
	    'ffmpeg/libavformat/sdp.c',
	    'ffmpeg/libavformat/sdr2.c',
	    'ffmpeg/libavformat/segafilm.c',
	    'ffmpeg/libavformat/segment.c',
	    'ffmpeg/libavformat/shortendec.c',
	    'ffmpeg/libavformat/sierravmd.c',
	    'ffmpeg/libavformat/siff.c',
	    'ffmpeg/libavformat/smacker.c',
	    'ffmpeg/libavformat/smjpeg.c',
	    'ffmpeg/libavformat/smjpegdec.c',
	    'ffmpeg/libavformat/smjpegenc.c',
	    'ffmpeg/libavformat/smoothstreamingenc.c',
	    'ffmpeg/libavformat/smush.c',
	    'ffmpeg/libavformat/sol.c',
	    'ffmpeg/libavformat/soxdec.c',
	    'ffmpeg/libavformat/soxenc.c',
	    'ffmpeg/libavformat/spdif.c',
	    'ffmpeg/libavformat/spdifdec.c',
	    'ffmpeg/libavformat/spdifenc.c',
	    'ffmpeg/libavformat/srtdec.c',
	    'ffmpeg/libavformat/srtenc.c',
	    'ffmpeg/libavformat/srtp.c',
	    'ffmpeg/libavformat/srtpproto.c',
	    'ffmpeg/libavformat/stldec.c',
	    'ffmpeg/libavformat/subfile.c',
	    'ffmpeg/libavformat/subtitles.c',
	    'ffmpeg/libavformat/subviewer1dec.c',
	    'ffmpeg/libavformat/subviewerdec.c',
	    'ffmpeg/libavformat/supdec.c',
	    'ffmpeg/libavformat/svag.c',
	    'ffmpeg/libavformat/swf.c',
	    'ffmpeg/libavformat/swfdec.c',
	    'ffmpeg/libavformat/swfenc.c',
	    'ffmpeg/libavformat/takdec.c',
	    'ffmpeg/libavformat/tcp.c',
	    'ffmpeg/libavformat/tedcaptionsdec.c',
	    'ffmpeg/libavformat/tee.c',
	    'ffmpeg/libavformat/thp.c',
	    'ffmpeg/libavformat/tiertexseq.c',
	    'ffmpeg/libavformat/tmv.c',
	    'ffmpeg/libavformat/tta.c',
	    'ffmpeg/libavformat/tty.c',
	    'ffmpeg/libavformat/txd.c',
	    'ffmpeg/libavformat/udp.c',
	    'ffmpeg/libavformat/uncodedframecrcenc.c',
	    ])
	if "Windows" not in target.get_type():
		my_module.add_src_file([
		    'ffmpeg/libavformat/unix.c',
		    ])
	my_module.add_src_file([
	    'ffmpeg/libavformat/url.c',
	    'ffmpeg/libavformat/urldecode.c',
	    'ffmpeg/libavformat/utils.c',
	    'ffmpeg/libavformat/v210.c',
	    'ffmpeg/libavformat/vag.c',
	    'ffmpeg/libavformat/vc1dec.c',
	    'ffmpeg/libavformat/vc1test.c',
	    'ffmpeg/libavformat/vc1testenc.c',
	    'ffmpeg/libavformat/vivo.c',
	    'ffmpeg/libavformat/voc.c',
	    'ffmpeg/libavformat/voc_packet.c',
	    'ffmpeg/libavformat/vocdec.c',
	    'ffmpeg/libavformat/vocenc.c',
	    'ffmpeg/libavformat/vorbiscomment.c',
	    'ffmpeg/libavformat/vpcc.c',
	    'ffmpeg/libavformat/vpk.c',
	    'ffmpeg/libavformat/vplayerdec.c',
	    'ffmpeg/libavformat/vqf.c',
	    'ffmpeg/libavformat/w64.c',
	    'ffmpeg/libavformat/wavdec.c',
	    'ffmpeg/libavformat/wavenc.c',
	    'ffmpeg/libavformat/wc3movie.c',
	    'ffmpeg/libavformat/webm_chunk.c',
	    'ffmpeg/libavformat/webmdashenc.c',
	    'ffmpeg/libavformat/webpenc.c',
	    'ffmpeg/libavformat/webvttdec.c',
	    'ffmpeg/libavformat/webvttenc.c',
	    'ffmpeg/libavformat/westwood_aud.c',
	    'ffmpeg/libavformat/westwood_vqa.c',
	    'ffmpeg/libavformat/wsddec.c',
	    'ffmpeg/libavformat/wtv_common.c',
	    'ffmpeg/libavformat/wtvdec.c',
	    'ffmpeg/libavformat/wtvenc.c',
	    'ffmpeg/libavformat/wv.c',
	    'ffmpeg/libavformat/wvdec.c',
	    'ffmpeg/libavformat/wvedec.c',
	    'ffmpeg/libavformat/wvenc.c',
	    'ffmpeg/libavformat/xa.c',
	    'ffmpeg/libavformat/xmv.c',
	    'ffmpeg/libavformat/xvag.c',
	    'ffmpeg/libavformat/xwma.c',
	    'ffmpeg/libavformat/yop.c',
	    'ffmpeg/libavformat/yuv4mpegdec.c',
	    'ffmpeg/libavformat/yuv4mpegenc.c',
	    ])
	#TODO : this is bad ...
	my_module.add_header_file([
	    #'ffmpeg/libavformat/protocol_list.c',
	    'generated/protocol_list.c',
	    ],
	    destination_path="libavformat")
	my_module.compile_version("c", 1999)
	
	lutinLib_ffmpegCommon.add_common_property(target, my_module);
	
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	if "Linux" in target.get_type():
		my_module.add_depend('rpc')
		my_module.add_depend('arpa')
	my_module.add_depend([
	    'ffmpeg-avcodec',
	    'ffmpeg-avutil',
	    'ffmpeg-headers',
	    ])

	return True