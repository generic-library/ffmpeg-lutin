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
	    'ffmpeg/libavcodec/012v.c',
	    'ffmpeg/libavcodec/4xm.c',
	    'ffmpeg/libavcodec/8bps.c',
	    'ffmpeg/libavcodec/8svx.c',
	    'ffmpeg/libavcodec/a64multienc.c',
	    'ffmpeg/libavcodec/aac_ac3_parser.c',
	    'ffmpeg/libavcodec/aac_adtstoasc_bsf.c',
	    'ffmpeg/libavcodec/aac_parser.c',
	    'ffmpeg/libavcodec/aacadtsdec.c',
	    'ffmpeg/libavcodec/aaccoder.c',
	    'ffmpeg/libavcodec/aacdec.c',
	    'ffmpeg/libavcodec/aacdec_fixed.c',
	    'ffmpeg/libavcodec/aacenc.c',
	    'ffmpeg/libavcodec/aacenc_is.c',
	    'ffmpeg/libavcodec/aacenc_ltp.c',
	    'ffmpeg/libavcodec/aacenc_pred.c',
	    'ffmpeg/libavcodec/aacenc_tns.c',
	    'ffmpeg/libavcodec/aacenctab.c',
	    'ffmpeg/libavcodec/aacps_fixed.c',
	    'ffmpeg/libavcodec/aacps_float.c',
	    'ffmpeg/libavcodec/aacpsdsp_fixed.c',
	    'ffmpeg/libavcodec/aacpsdsp_float.c',
	    'ffmpeg/libavcodec/aacpsy.c',
	    'ffmpeg/libavcodec/aacsbr.c',
	    'ffmpeg/libavcodec/aacsbr_fixed.c',
	    'ffmpeg/libavcodec/aactab.c',
	    'ffmpeg/libavcodec/aandcttab.c',
	    'ffmpeg/libavcodec/aasc.c',
	    'ffmpeg/libavcodec/ac3.c',
	    'ffmpeg/libavcodec/ac3_parser.c',
	    'ffmpeg/libavcodec/ac3dec_data.c',
	    'ffmpeg/libavcodec/ac3dec_fixed.c',
	    'ffmpeg/libavcodec/ac3dec_float.c',
	    'ffmpeg/libavcodec/ac3dsp.c',
	    'ffmpeg/libavcodec/ac3enc.c',
	    'ffmpeg/libavcodec/ac3enc_fixed.c',
	    'ffmpeg/libavcodec/ac3enc_float.c',
	    'ffmpeg/libavcodec/ac3tab.c',
	    'ffmpeg/libavcodec/acelp_filters.c',
	    'ffmpeg/libavcodec/acelp_pitch_delay.c',
	    'ffmpeg/libavcodec/acelp_vectors.c',
	    'ffmpeg/libavcodec/adpcm.c',
	    'ffmpeg/libavcodec/adpcm_data.c',
	    'ffmpeg/libavcodec/adpcmenc.c',
	    'ffmpeg/libavcodec/adx.c',
	    'ffmpeg/libavcodec/adx_parser.c',
	    'ffmpeg/libavcodec/adxdec.c',
	    'ffmpeg/libavcodec/adxenc.c',
	    'ffmpeg/libavcodec/aic.c',
	    'ffmpeg/libavcodec/alac.c',
	    'ffmpeg/libavcodec/alac_data.c',
	    'ffmpeg/libavcodec/alacdsp.c',
	    'ffmpeg/libavcodec/alacenc.c',
	    'ffmpeg/libavcodec/aliaspixdec.c',
	    'ffmpeg/libavcodec/aliaspixenc.c',
	    'ffmpeg/libavcodec/allcodecs.c',
	    'ffmpeg/libavcodec/alsdec.c',
	    'ffmpeg/libavcodec/amrnbdec.c',
	    'ffmpeg/libavcodec/amrwbdec.c',
	    'ffmpeg/libavcodec/anm.c',
	    'ffmpeg/libavcodec/ansi.c',
	    'ffmpeg/libavcodec/apedec.c',
	    'ffmpeg/libavcodec/ass.c',
	    'ffmpeg/libavcodec/ass_split.c',
	    'ffmpeg/libavcodec/assdec.c',
	    'ffmpeg/libavcodec/assenc.c',
	    'ffmpeg/libavcodec/asv.c',
	    'ffmpeg/libavcodec/asvdec.c',
	    'ffmpeg/libavcodec/asvenc.c',
	    'ffmpeg/libavcodec/atrac.c',
	    'ffmpeg/libavcodec/atrac1.c',
	    'ffmpeg/libavcodec/atrac3.c',
	    'ffmpeg/libavcodec/atrac3plus.c',
	    'ffmpeg/libavcodec/atrac3plusdec.c',
	    'ffmpeg/libavcodec/atrac3plusdsp.c',
	    'ffmpeg/libavcodec/audio_frame_queue.c',
	    'ffmpeg/libavcodec/audioconvert.c',
	    'ffmpeg/libavcodec/audiodsp.c',
	    'ffmpeg/libavcodec/aura.c',
	    'ffmpeg/libavcodec/avdct.c',
	    'ffmpeg/libavcodec/avfft.c',
	    'ffmpeg/libavcodec/avpacket.c',
	    'ffmpeg/libavcodec/avpicture.c',
	    'ffmpeg/libavcodec/avrndec.c',
	    'ffmpeg/libavcodec/avs.c',
	    'ffmpeg/libavcodec/avuidec.c',
	    'ffmpeg/libavcodec/avuienc.c',
	    'ffmpeg/libavcodec/bethsoftvideo.c',
	    'ffmpeg/libavcodec/bfi.c',
	    'ffmpeg/libavcodec/bgmc.c',
	    'ffmpeg/libavcodec/bink.c',
	    'ffmpeg/libavcodec/binkaudio.c',
	    'ffmpeg/libavcodec/binkdsp.c',
	    'ffmpeg/libavcodec/bintext.c',
	    'ffmpeg/libavcodec/bitstream.c',
	    'ffmpeg/libavcodec/bitstream_filter.c',
	    'ffmpeg/libavcodec/bitstream_filters.c',
	    'ffmpeg/libavcodec/blockdsp.c',
	    'ffmpeg/libavcodec/bmp.c',
	    'ffmpeg/libavcodec/bmp_parser.c',
	    'ffmpeg/libavcodec/bmpenc.c',
	    'ffmpeg/libavcodec/bmvaudio.c',
	    'ffmpeg/libavcodec/bmvvideo.c',
	    'ffmpeg/libavcodec/brenderpix.c',
	    'ffmpeg/libavcodec/bsf.c',
	    'ffmpeg/libavcodec/bswapdsp.c',
	    'ffmpeg/libavcodec/c93.c',
	    'ffmpeg/libavcodec/cabac.c',
	    'ffmpeg/libavcodec/canopus.c',
	    'ffmpeg/libavcodec/cavs.c',
	    'ffmpeg/libavcodec/cavs_parser.c',
	    'ffmpeg/libavcodec/cavsdata.c',
	    'ffmpeg/libavcodec/cavsdec.c',
	    'ffmpeg/libavcodec/cavsdsp.c',
	    'ffmpeg/libavcodec/cbrt_data.c',
	    'ffmpeg/libavcodec/cbrt_data_fixed.c',
	    'ffmpeg/libavcodec/ccaption_dec.c',
	    'ffmpeg/libavcodec/cdgraphics.c',
	    'ffmpeg/libavcodec/cdxl.c',
	    'ffmpeg/libavcodec/celp_filters.c',
	    'ffmpeg/libavcodec/celp_math.c',
	    'ffmpeg/libavcodec/cfhd.c',
	    'ffmpeg/libavcodec/cfhddata.c',
	    'ffmpeg/libavcodec/cga_data.c',
	    'ffmpeg/libavcodec/chomp_bsf.c',
	    'ffmpeg/libavcodec/cinepak.c',
	    'ffmpeg/libavcodec/cinepakenc.c',
	    'ffmpeg/libavcodec/cljrdec.c',
	    'ffmpeg/libavcodec/cljrenc.c',
	    'ffmpeg/libavcodec/cllc.c',
	    'ffmpeg/libavcodec/cngdec.c',
	    'ffmpeg/libavcodec/cngenc.c',
	    'ffmpeg/libavcodec/codec_desc.c',
	    'ffmpeg/libavcodec/cook.c',
	    'ffmpeg/libavcodec/cook_parser.c',
	    'ffmpeg/libavcodec/cpia.c',
	    'ffmpeg/libavcodec/cscd.c',
	    'ffmpeg/libavcodec/cyuv.c',
	    'ffmpeg/libavcodec/d3d11va.c',
	    'ffmpeg/libavcodec/dca.c',
	    'ffmpeg/libavcodec/dca_core.c',
	    'ffmpeg/libavcodec/dca_core_bsf.c',
	    'ffmpeg/libavcodec/dca_exss.c',
	    'ffmpeg/libavcodec/dca_lbr.c',
	    'ffmpeg/libavcodec/dca_parser.c',
	    'ffmpeg/libavcodec/dca_xll.c',
	    'ffmpeg/libavcodec/dcadata.c',
	    'ffmpeg/libavcodec/dcadct.c',
	    'ffmpeg/libavcodec/dcadec.c',
	    'ffmpeg/libavcodec/dcadsp.c',
	    'ffmpeg/libavcodec/dcaenc.c',
	    'ffmpeg/libavcodec/dcahuff.c',
	    'ffmpeg/libavcodec/dct.c',
	    'ffmpeg/libavcodec/dct32_fixed.c',
	    'ffmpeg/libavcodec/dct32_float.c',
	    'ffmpeg/libavcodec/dds.c',
	    'ffmpeg/libavcodec/dfa.c',
	    'ffmpeg/libavcodec/dirac.c',
	    'ffmpeg/libavcodec/dirac_arith.c',
	    'ffmpeg/libavcodec/dirac_dwt.c',
	    'ffmpeg/libavcodec/dirac_parser.c',
	    'ffmpeg/libavcodec/diracdec.c',
	    'ffmpeg/libavcodec/diracdsp.c',
	    'ffmpeg/libavcodec/diractab.c',
	    'ffmpeg/libavcodec/dnxhd_parser.c',
	    'ffmpeg/libavcodec/dnxhddata.c',
	    'ffmpeg/libavcodec/dnxhddec.c',
	    'ffmpeg/libavcodec/dnxhdenc.c',
	    'ffmpeg/libavcodec/dpcm.c',
	    'ffmpeg/libavcodec/dpx.c',
	    'ffmpeg/libavcodec/dpx_parser.c',
	    'ffmpeg/libavcodec/dpxenc.c',
	    'ffmpeg/libavcodec/dsd.c',
	    'ffmpeg/libavcodec/dsddec.c',
	    'ffmpeg/libavcodec/dsicinaudio.c',
	    'ffmpeg/libavcodec/dsicinvideo.c',
	    'ffmpeg/libavcodec/dss_sp.c',
	    'ffmpeg/libavcodec/dstdec.c',
	    'ffmpeg/libavcodec/dump_extradata_bsf.c',
	    'ffmpeg/libavcodec/dv.c',
	    'ffmpeg/libavcodec/dv_profile.c',
	    'ffmpeg/libavcodec/dvaudio_parser.c',
	    'ffmpeg/libavcodec/dvaudiodec.c',
	    'ffmpeg/libavcodec/dvbsub.c',
	    'ffmpeg/libavcodec/dvbsub_parser.c',
	    'ffmpeg/libavcodec/dvbsubdec.c',
	    'ffmpeg/libavcodec/dvd_nav_parser.c',
	    'ffmpeg/libavcodec/dvdata.c',
	    'ffmpeg/libavcodec/dvdec.c',
	    'ffmpeg/libavcodec/dvdsub_parser.c',
	    'ffmpeg/libavcodec/dvdsubdec.c',
	    'ffmpeg/libavcodec/dvdsubenc.c',
	    'ffmpeg/libavcodec/dvenc.c',
	    'ffmpeg/libavcodec/dxa.c',
	    'ffmpeg/libavcodec/dxtory.c',
	    'ffmpeg/libavcodec/dxv.c',
	    'ffmpeg/libavcodec/eac3_data.c',
	    'ffmpeg/libavcodec/eac3enc.c',
	    'ffmpeg/libavcodec/eacmv.c',
	    'ffmpeg/libavcodec/eaidct.c',
	    'ffmpeg/libavcodec/eamad.c',
	    'ffmpeg/libavcodec/eatgq.c',
	    'ffmpeg/libavcodec/eatgv.c',
	    'ffmpeg/libavcodec/eatqi.c',
	    'ffmpeg/libavcodec/elbg.c',
	    'ffmpeg/libavcodec/elsdec.c',
	    'ffmpeg/libavcodec/error_resilience.c',
	    'ffmpeg/libavcodec/escape124.c',
	    'ffmpeg/libavcodec/escape130.c',
	    'ffmpeg/libavcodec/evrcdec.c',
	    'ffmpeg/libavcodec/exif.c',
	    'ffmpeg/libavcodec/exr.c',
	    'ffmpeg/libavcodec/faandct.c',
	    'ffmpeg/libavcodec/faanidct.c',
	    'ffmpeg/libavcodec/faxcompr.c',
	    'ffmpeg/libavcodec/fdctdsp.c',
	    'ffmpeg/libavcodec/fft_fixed.c',
	    'ffmpeg/libavcodec/fft_fixed_32.c',
	    'ffmpeg/libavcodec/fft_float.c',
	    'ffmpeg/libavcodec/fft_init_table.c',
	    'ffmpeg/libavcodec/ffv1.c',
	    'ffmpeg/libavcodec/ffv1dec.c',
	    'ffmpeg/libavcodec/ffv1enc.c',
	    'ffmpeg/libavcodec/ffwavesynth.c',
	    'ffmpeg/libavcodec/fic.c',
	    'ffmpeg/libavcodec/flac.c',
	    'ffmpeg/libavcodec/flac_parser.c',
	    'ffmpeg/libavcodec/flacdata.c',
	    'ffmpeg/libavcodec/flacdec.c',
	    'ffmpeg/libavcodec/flacdsp.c',
	    'ffmpeg/libavcodec/flacenc.c',
	    'ffmpeg/libavcodec/flashsv.c',
	    'ffmpeg/libavcodec/flashsv2enc.c',
	    'ffmpeg/libavcodec/flashsvenc.c',
	    'ffmpeg/libavcodec/flicvideo.c',
	    'ffmpeg/libavcodec/flvdec.c',
	    'ffmpeg/libavcodec/flvenc.c',
	    'ffmpeg/libavcodec/fmtconvert.c',
	    'ffmpeg/libavcodec/frame_thread_encoder.c',
	    'ffmpeg/libavcodec/fraps.c',
	    'ffmpeg/libavcodec/frwu.c',
	    'ffmpeg/libavcodec/g2meet.c',
	    'ffmpeg/libavcodec/g722.c',
	    'ffmpeg/libavcodec/g722dec.c',
	    'ffmpeg/libavcodec/g722dsp.c',
	    'ffmpeg/libavcodec/g722enc.c',
	    'ffmpeg/libavcodec/g723_1.c',
	    'ffmpeg/libavcodec/g723_1dec.c',
	    'ffmpeg/libavcodec/g723_1enc.c',
	    'ffmpeg/libavcodec/g726.c',
	    'ffmpeg/libavcodec/g729_parser.c',
	    'ffmpeg/libavcodec/g729dec.c',
	    'ffmpeg/libavcodec/g729postfilter.c',
	    'ffmpeg/libavcodec/gif.c',
	    'ffmpeg/libavcodec/gifdec.c',
	    'ffmpeg/libavcodec/golomb.c',
	    'ffmpeg/libavcodec/gsm_parser.c',
	    'ffmpeg/libavcodec/gsmdec.c',
	    'ffmpeg/libavcodec/gsmdec_data.c',
	    'ffmpeg/libavcodec/h261.c',
	    'ffmpeg/libavcodec/h261_parser.c',
	    'ffmpeg/libavcodec/h261data.c',
	    'ffmpeg/libavcodec/h261dec.c',
	    'ffmpeg/libavcodec/h261enc.c',
	    'ffmpeg/libavcodec/h263.c',
	    'ffmpeg/libavcodec/h263_parser.c',
	    'ffmpeg/libavcodec/h263data.c',
	    'ffmpeg/libavcodec/h263dec.c',
	    'ffmpeg/libavcodec/h263dsp.c',
	    'ffmpeg/libavcodec/h264.c',
	    'ffmpeg/libavcodec/h2645_parse.c',
	    'ffmpeg/libavcodec/h264_cabac.c',
	    'ffmpeg/libavcodec/h264_cavlc.c',
	    'ffmpeg/libavcodec/h264_direct.c',
	    'ffmpeg/libavcodec/h264_loopfilter.c',
	    'ffmpeg/libavcodec/h264_mb.c',
	    'ffmpeg/libavcodec/h264_mp4toannexb_bsf.c',
	    'ffmpeg/libavcodec/h264_parse.c',
	    'ffmpeg/libavcodec/h264_parser.c',
	    'ffmpeg/libavcodec/h264_picture.c',
	    'ffmpeg/libavcodec/h264_ps.c',
	    'ffmpeg/libavcodec/h264_refs.c',
	    'ffmpeg/libavcodec/h264_sei.c',
	    'ffmpeg/libavcodec/h264_slice.c',
	    'ffmpeg/libavcodec/h264chroma.c',
	    'ffmpeg/libavcodec/h264data.c',
	    'ffmpeg/libavcodec/h264dsp.c',
	    'ffmpeg/libavcodec/h264idct.c',
	    'ffmpeg/libavcodec/h264pred.c',
	    'ffmpeg/libavcodec/h264qpel.c',
	    'ffmpeg/libavcodec/hap.c',
	    'ffmpeg/libavcodec/hapdec.c',
	    'ffmpeg/libavcodec/hevc.c',
	    'ffmpeg/libavcodec/hevc_cabac.c',
	    'ffmpeg/libavcodec/hevc_data.c',
	    'ffmpeg/libavcodec/hevc_filter.c',
	    'ffmpeg/libavcodec/hevc_mp4toannexb_bsf.c',
	    'ffmpeg/libavcodec/hevc_mvs.c',
	    'ffmpeg/libavcodec/hevc_parser.c',
	    'ffmpeg/libavcodec/hevc_ps.c',
	    'ffmpeg/libavcodec/hevc_refs.c',
	    'ffmpeg/libavcodec/hevc_sei.c',
	    'ffmpeg/libavcodec/hevcdsp.c',
	    'ffmpeg/libavcodec/hevcpred.c',
	    'ffmpeg/libavcodec/hnm4video.c',
	    'ffmpeg/libavcodec/hpeldsp.c',
	    'ffmpeg/libavcodec/hq_hqa.c',
	    'ffmpeg/libavcodec/hq_hqadata.c',
	    'ffmpeg/libavcodec/hq_hqadsp.c',
	    'ffmpeg/libavcodec/hqx.c',
	    'ffmpeg/libavcodec/hqxdsp.c',
	    'ffmpeg/libavcodec/hqxvlc.c',
	    'ffmpeg/libavcodec/htmlsubtitles.c',
	    'ffmpeg/libavcodec/huffman.c',
	    'ffmpeg/libavcodec/huffyuv.c',
	    'ffmpeg/libavcodec/huffyuvdec.c',
	    'ffmpeg/libavcodec/huffyuvdsp.c',
	    'ffmpeg/libavcodec/huffyuvenc.c',
	    'ffmpeg/libavcodec/huffyuvencdsp.c',
	    'ffmpeg/libavcodec/idcinvideo.c',
	    'ffmpeg/libavcodec/idctdsp.c',
	    'ffmpeg/libavcodec/iff.c',
	    'ffmpeg/libavcodec/iirfilter.c',
	    'ffmpeg/libavcodec/imc.c',
	    'ffmpeg/libavcodec/imdct15.c',
	    'ffmpeg/libavcodec/imgconvert.c',
	    'ffmpeg/libavcodec/imx_dump_header_bsf.c',
	    'ffmpeg/libavcodec/indeo2.c',
	    'ffmpeg/libavcodec/indeo3.c',
	    'ffmpeg/libavcodec/indeo4.c',
	    'ffmpeg/libavcodec/indeo5.c',
	    'ffmpeg/libavcodec/intelh263dec.c',
	    'ffmpeg/libavcodec/interplayacm.c',
	    'ffmpeg/libavcodec/interplayvideo.c',
	    'ffmpeg/libavcodec/intrax8.c',
	    'ffmpeg/libavcodec/intrax8dsp.c',
	    'ffmpeg/libavcodec/ituh263dec.c',
	    'ffmpeg/libavcodec/ituh263enc.c',
	    'ffmpeg/libavcodec/ivi.c',
	    'ffmpeg/libavcodec/ivi_dsp.c',
	    'ffmpeg/libavcodec/j2kenc.c',
	    'ffmpeg/libavcodec/jacosubdec.c',
	    'ffmpeg/libavcodec/jfdctfst.c',
	    'ffmpeg/libavcodec/jfdctint.c',
	    'ffmpeg/libavcodec/jni.c',
	    'ffmpeg/libavcodec/jpeg2000.c',
	    'ffmpeg/libavcodec/jpeg2000dec.c',
	    'ffmpeg/libavcodec/jpeg2000dsp.c',
	    'ffmpeg/libavcodec/jpeg2000dwt.c',
	    'ffmpeg/libavcodec/jpegls.c',
	    'ffmpeg/libavcodec/jpeglsdec.c',
	    'ffmpeg/libavcodec/jpeglsenc.c',
	    'ffmpeg/libavcodec/jpegtables.c',
	    'ffmpeg/libavcodec/jrevdct.c',
	    'ffmpeg/libavcodec/jvdec.c',
	    'ffmpeg/libavcodec/kbdwin.c',
	    'ffmpeg/libavcodec/kgv1dec.c',
	    'ffmpeg/libavcodec/kmvc.c',
	    'ffmpeg/libavcodec/lagarith.c',
	    'ffmpeg/libavcodec/lagarithrac.c',
	    'ffmpeg/libavcodec/latm_parser.c',
	    'ffmpeg/libavcodec/lcldec.c',
	    'ffmpeg/libavcodec/lclenc.c',
	    'ffmpeg/libavcodec/ljpegenc.c',
	    'ffmpeg/libavcodec/loco.c',
	    'ffmpeg/libavcodec/lossless_audiodsp.c',
	    'ffmpeg/libavcodec/lossless_videodsp.c',
	    'ffmpeg/libavcodec/lpc.c',
	    'ffmpeg/libavcodec/lsp.c',
	    'ffmpeg/libavcodec/lzf.c',
	    'ffmpeg/libavcodec/lzw.c',
	    'ffmpeg/libavcodec/lzwenc.c',
	    'ffmpeg/libavcodec/m101.c',
	    'ffmpeg/libavcodec/mace.c',
	    'ffmpeg/libavcodec/magicyuv.c',
	    'ffmpeg/libavcodec/mathtables.c',
	    'ffmpeg/libavcodec/mdct_fixed.c',
	    'ffmpeg/libavcodec/mdct_fixed_32.c',
	    'ffmpeg/libavcodec/mdct_float.c',
	    'ffmpeg/libavcodec/mdec.c',
	    'ffmpeg/libavcodec/me_cmp.c',
	    'ffmpeg/libavcodec/metasound.c',
	    'ffmpeg/libavcodec/metasound_data.c',
	    'ffmpeg/libavcodec/microdvddec.c',
	    'ffmpeg/libavcodec/mimic.c',
	    'ffmpeg/libavcodec/mjpeg2jpeg_bsf.c',
	    'ffmpeg/libavcodec/mjpeg_parser.c',
	    'ffmpeg/libavcodec/mjpega_dump_header_bsf.c',
	    'ffmpeg/libavcodec/mjpegbdec.c',
	    'ffmpeg/libavcodec/mjpegdec.c',
	    'ffmpeg/libavcodec/mjpegenc.c',
	    'ffmpeg/libavcodec/mjpegenc_common.c',
	    'ffmpeg/libavcodec/mlp.c',
	    'ffmpeg/libavcodec/mlp_parser.c',
	    'ffmpeg/libavcodec/mlpdec.c',
	    'ffmpeg/libavcodec/mlpdsp.c',
	    'ffmpeg/libavcodec/mmvideo.c',
	    'ffmpeg/libavcodec/motion_est.c',
	    'ffmpeg/libavcodec/motionpixels.c',
	    'ffmpeg/libavcodec/movsub_bsf.c',
	    'ffmpeg/libavcodec/movtextdec.c',
	    'ffmpeg/libavcodec/movtextenc.c',
	    'ffmpeg/libavcodec/mp3_header_decompress_bsf.c',
	    'ffmpeg/libavcodec/mpc.c',
	    'ffmpeg/libavcodec/mpc7.c',
	    'ffmpeg/libavcodec/mpc8.c',
	    'ffmpeg/libavcodec/mpeg12.c',
	    'ffmpeg/libavcodec/mpeg12data.c',
	    'ffmpeg/libavcodec/mpeg12dec.c',
	    'ffmpeg/libavcodec/mpeg12enc.c',
	    'ffmpeg/libavcodec/mpeg4_unpack_bframes_bsf.c',
	    'ffmpeg/libavcodec/mpeg4audio.c',
	    'ffmpeg/libavcodec/mpeg4video.c',
	    'ffmpeg/libavcodec/mpeg4video_parser.c',
	    'ffmpeg/libavcodec/mpeg4videodec.c',
	    'ffmpeg/libavcodec/mpeg4videoenc.c',
	    'ffmpeg/libavcodec/mpeg_er.c',
	    'ffmpeg/libavcodec/mpegaudio.c',
	    'ffmpeg/libavcodec/mpegaudio_parser.c',
	    'ffmpeg/libavcodec/mpegaudiodata.c',
	    'ffmpeg/libavcodec/mpegaudiodec_fixed.c',
	    'ffmpeg/libavcodec/mpegaudiodec_float.c',
	    'ffmpeg/libavcodec/mpegaudiodecheader.c',
	    'ffmpeg/libavcodec/mpegaudiodsp.c',
	    'ffmpeg/libavcodec/mpegaudiodsp_data.c',
	    'ffmpeg/libavcodec/mpegaudiodsp_fixed.c',
	    'ffmpeg/libavcodec/mpegaudiodsp_float.c',
	    'ffmpeg/libavcodec/mpegaudioenc_fixed.c',
	    'ffmpeg/libavcodec/mpegaudioenc_float.c',
	    'ffmpeg/libavcodec/mpegpicture.c',
	    'ffmpeg/libavcodec/mpegutils.c',
	    'ffmpeg/libavcodec/mpegvideo.c',
	    'ffmpeg/libavcodec/mpegvideo_enc.c',
	    'ffmpeg/libavcodec/mpegvideo_motion.c',
	    'ffmpeg/libavcodec/mpegvideo_parser.c',
	    'ffmpeg/libavcodec/mpegvideodata.c',
	    'ffmpeg/libavcodec/mpegvideodsp.c',
	    'ffmpeg/libavcodec/mpegvideoencdsp.c',
	    'ffmpeg/libavcodec/mpl2dec.c',
	    'ffmpeg/libavcodec/mqc.c',
	    'ffmpeg/libavcodec/mqcdec.c',
	    'ffmpeg/libavcodec/mqcenc.c',
	    'ffmpeg/libavcodec/msgsmdec.c',
	    'ffmpeg/libavcodec/msmpeg4.c',
	    'ffmpeg/libavcodec/msmpeg4data.c',
	    'ffmpeg/libavcodec/msmpeg4dec.c',
	    'ffmpeg/libavcodec/msmpeg4enc.c',
	    'ffmpeg/libavcodec/msrle.c',
	    'ffmpeg/libavcodec/msrledec.c',
	    'ffmpeg/libavcodec/mss1.c',
	    'ffmpeg/libavcodec/mss12.c',
	    'ffmpeg/libavcodec/mss2.c',
	    'ffmpeg/libavcodec/mss2dsp.c',
	    'ffmpeg/libavcodec/mss3.c',
	    'ffmpeg/libavcodec/mss34dsp.c',
	    'ffmpeg/libavcodec/mss4.c',
	    'ffmpeg/libavcodec/msvideo1.c',
	    'ffmpeg/libavcodec/msvideo1enc.c',
	    'ffmpeg/libavcodec/mvcdec.c',
	    'ffmpeg/libavcodec/mxpegdec.c',
	    'ffmpeg/libavcodec/nellymoser.c',
	    'ffmpeg/libavcodec/nellymoserdec.c',
	    'ffmpeg/libavcodec/nellymoserenc.c',
	    'ffmpeg/libavcodec/noise_bsf.c',
	    'ffmpeg/libavcodec/nuv.c',
	    'ffmpeg/libavcodec/on2avc.c',
	    'ffmpeg/libavcodec/on2avcdata.c',
	    'ffmpeg/libavcodec/options.c',
	    'ffmpeg/libavcodec/opus.c',
	    'ffmpeg/libavcodec/opus_celt.c',
	    'ffmpeg/libavcodec/opus_parser.c',
	    'ffmpeg/libavcodec/opus_silk.c',
	    'ffmpeg/libavcodec/opusdec.c',
	    'ffmpeg/libavcodec/pafaudio.c',
	    'ffmpeg/libavcodec/pafvideo.c',
	    'ffmpeg/libavcodec/pamenc.c',
	    'ffmpeg/libavcodec/parser.c',
	    'ffmpeg/libavcodec/pcm-bluray.c',
	    'ffmpeg/libavcodec/pcm-dvd.c',
	    'ffmpeg/libavcodec/pcm.c',
	    'ffmpeg/libavcodec/pcx.c',
	    'ffmpeg/libavcodec/pcxenc.c',
	    'ffmpeg/libavcodec/pgssubdec.c',
	    'ffmpeg/libavcodec/pictordec.c',
	    'ffmpeg/libavcodec/pixblockdsp.c',
	    'ffmpeg/libavcodec/png.c',
	    'ffmpeg/libavcodec/png_parser.c',
	    'ffmpeg/libavcodec/pngdec.c',
	    'ffmpeg/libavcodec/pngdsp.c',
	    'ffmpeg/libavcodec/pngenc.c',
	    'ffmpeg/libavcodec/pnm.c',
	    'ffmpeg/libavcodec/pnm_parser.c',
	    'ffmpeg/libavcodec/pnmdec.c',
	    'ffmpeg/libavcodec/pnmenc.c',
	    'ffmpeg/libavcodec/profiles.c',
	    'ffmpeg/libavcodec/proresdata.c',
	    'ffmpeg/libavcodec/proresdec2.c',
	    'ffmpeg/libavcodec/proresdec_lgpl.c',
	    'ffmpeg/libavcodec/proresdsp.c',
	    'ffmpeg/libavcodec/proresenc_anatoliy.c',
	    'ffmpeg/libavcodec/proresenc_kostya.c',
	    'ffmpeg/libavcodec/psymodel.c',
	    'ffmpeg/libavcodec/pthread.c',
	    'ffmpeg/libavcodec/pthread_frame.c',
	    'ffmpeg/libavcodec/pthread_slice.c',
	    'ffmpeg/libavcodec/ptx.c',
	    'ffmpeg/libavcodec/qcelpdec.c',
	    'ffmpeg/libavcodec/qdm2.c',
	    'ffmpeg/libavcodec/qdrw.c',
	    'ffmpeg/libavcodec/qpeg.c',
	    'ffmpeg/libavcodec/qpeldsp.c',
	    'ffmpeg/libavcodec/qsv_api.c',
	    'ffmpeg/libavcodec/qtrle.c',
	    'ffmpeg/libavcodec/qtrleenc.c',
	    'ffmpeg/libavcodec/r210dec.c',
	    'ffmpeg/libavcodec/r210enc.c',
	    'ffmpeg/libavcodec/ra144.c',
	    'ffmpeg/libavcodec/ra144dec.c',
	    'ffmpeg/libavcodec/ra144enc.c',
	    'ffmpeg/libavcodec/ra288.c',
	    'ffmpeg/libavcodec/ralf.c',
	    'ffmpeg/libavcodec/rangecoder.c',
	    'ffmpeg/libavcodec/ratecontrol.c',
	    'ffmpeg/libavcodec/raw.c',
	    'ffmpeg/libavcodec/rawdec.c',
	    'ffmpeg/libavcodec/rawenc.c',
	    'ffmpeg/libavcodec/rdft.c',
	    'ffmpeg/libavcodec/realtextdec.c',
	    'ffmpeg/libavcodec/remove_extradata_bsf.c',
	    'ffmpeg/libavcodec/resample.c',
	    'ffmpeg/libavcodec/resample2.c',
	    'ffmpeg/libavcodec/rl.c',
	    'ffmpeg/libavcodec/rl2.c',
	    'ffmpeg/libavcodec/rle.c',
	    'ffmpeg/libavcodec/roqaudioenc.c',
	    'ffmpeg/libavcodec/roqvideo.c',
	    'ffmpeg/libavcodec/roqvideodec.c',
	    'ffmpeg/libavcodec/roqvideoenc.c',
	    'ffmpeg/libavcodec/rpza.c',
	    'ffmpeg/libavcodec/rscc.c',
	    'ffmpeg/libavcodec/rtjpeg.c',
	    'ffmpeg/libavcodec/rv10.c',
	    'ffmpeg/libavcodec/rv10enc.c',
	    'ffmpeg/libavcodec/rv20enc.c',
	    'ffmpeg/libavcodec/rv30.c',
	    'ffmpeg/libavcodec/rv30dsp.c',
	    'ffmpeg/libavcodec/rv34.c',
	    'ffmpeg/libavcodec/rv34_parser.c',
	    'ffmpeg/libavcodec/rv34dsp.c',
	    'ffmpeg/libavcodec/rv40.c',
	    'ffmpeg/libavcodec/rv40dsp.c',
	    'ffmpeg/libavcodec/s302m.c',
	    'ffmpeg/libavcodec/s302menc.c',
	    'ffmpeg/libavcodec/samidec.c',
	    'ffmpeg/libavcodec/sanm.c',
	    'ffmpeg/libavcodec/sbrdsp.c',
	    'ffmpeg/libavcodec/sbrdsp_fixed.c',
	    'ffmpeg/libavcodec/screenpresso.c',
	    'ffmpeg/libavcodec/sgidec.c',
	    'ffmpeg/libavcodec/sgienc.c',
	    'ffmpeg/libavcodec/sgirledec.c',
	    'ffmpeg/libavcodec/sheervideo.c',
	    'ffmpeg/libavcodec/shorten.c',
	    'ffmpeg/libavcodec/simple_idct.c',
	    'ffmpeg/libavcodec/sinewin.c',
	    'ffmpeg/libavcodec/sinewin_fixed.c',
	    'ffmpeg/libavcodec/sipr.c',
	    'ffmpeg/libavcodec/sipr16k.c',
	    'ffmpeg/libavcodec/smacker.c',
	    'ffmpeg/libavcodec/smc.c',
	    'ffmpeg/libavcodec/smvjpegdec.c',
	    'ffmpeg/libavcodec/snappy.c',
	    'ffmpeg/libavcodec/snow.c',
	    'ffmpeg/libavcodec/snow_dwt.c',
	    'ffmpeg/libavcodec/snowdec.c',
	    'ffmpeg/libavcodec/snowenc.c',
	    'ffmpeg/libavcodec/sonic.c',
	    'ffmpeg/libavcodec/sp5xdec.c',
	    'ffmpeg/libavcodec/srtdec.c',
	    'ffmpeg/libavcodec/srtenc.c',
	    'ffmpeg/libavcodec/startcode.c',
	    'ffmpeg/libavcodec/subviewerdec.c',
	    'ffmpeg/libavcodec/sunrast.c',
	    'ffmpeg/libavcodec/sunrastenc.c',
	    'ffmpeg/libavcodec/svq1.c',
	    'ffmpeg/libavcodec/svq13.c',
	    'ffmpeg/libavcodec/svq1dec.c',
	    'ffmpeg/libavcodec/svq1enc.c',
	    'ffmpeg/libavcodec/svq3.c',
	    'ffmpeg/libavcodec/synth_filter.c',
	    'ffmpeg/libavcodec/tak.c',
	    'ffmpeg/libavcodec/tak_parser.c',
	    'ffmpeg/libavcodec/takdec.c',
	    'ffmpeg/libavcodec/takdsp.c',
	    'ffmpeg/libavcodec/targa.c',
	    'ffmpeg/libavcodec/targa_y216dec.c',
	    'ffmpeg/libavcodec/targaenc.c',
	    'ffmpeg/libavcodec/tdsc.c',
	    'ffmpeg/libavcodec/textdec.c',
	    'ffmpeg/libavcodec/texturedsp.c',
	    'ffmpeg/libavcodec/tiertexseqv.c',
	    'ffmpeg/libavcodec/tiff.c',
	    'ffmpeg/libavcodec/tiff_common.c',
	    'ffmpeg/libavcodec/tiff_data.c',
	    'ffmpeg/libavcodec/tiffenc.c',
	    'ffmpeg/libavcodec/tmv.c',
	    'ffmpeg/libavcodec/tpeldsp.c',
	    'ffmpeg/libavcodec/truemotion1.c',
	    'ffmpeg/libavcodec/truemotion2.c',
	    'ffmpeg/libavcodec/truemotion2rt.c',
	    'ffmpeg/libavcodec/truespeech.c',
	    'ffmpeg/libavcodec/tscc.c',
	    'ffmpeg/libavcodec/tscc2.c',
	    'ffmpeg/libavcodec/tta.c',
	    'ffmpeg/libavcodec/ttadata.c',
	    'ffmpeg/libavcodec/ttadsp.c',
	    'ffmpeg/libavcodec/ttaenc.c',
	    'ffmpeg/libavcodec/twinvq.c',
	    'ffmpeg/libavcodec/twinvqdec.c',
	    'ffmpeg/libavcodec/txd.c',
	    'ffmpeg/libavcodec/ulti.c',
	    'ffmpeg/libavcodec/utils.c',
	    'ffmpeg/libavcodec/utvideo.c',
	    'ffmpeg/libavcodec/utvideodec.c',
	    'ffmpeg/libavcodec/utvideoenc.c',
	    'ffmpeg/libavcodec/v210dec.c',
	    'ffmpeg/libavcodec/v210enc.c',
	    'ffmpeg/libavcodec/v210x.c',
	    'ffmpeg/libavcodec/v308dec.c',
	    'ffmpeg/libavcodec/v308enc.c',
	    'ffmpeg/libavcodec/v408dec.c',
	    'ffmpeg/libavcodec/v408enc.c',
	    'ffmpeg/libavcodec/v410dec.c',
	    'ffmpeg/libavcodec/v410enc.c',
	    'ffmpeg/libavcodec/vb.c',
	    'ffmpeg/libavcodec/vble.c',
	    'ffmpeg/libavcodec/vc1.c',
	    'ffmpeg/libavcodec/vc1_block.c',
	    'ffmpeg/libavcodec/vc1_loopfilter.c',
	    'ffmpeg/libavcodec/vc1_mc.c',
	    'ffmpeg/libavcodec/vc1_parser.c',
	    'ffmpeg/libavcodec/vc1_pred.c',
	    'ffmpeg/libavcodec/vc1data.c',
	    'ffmpeg/libavcodec/vc1dec.c',
	    'ffmpeg/libavcodec/vc1dsp.c',
	    'ffmpeg/libavcodec/vc2enc.c',
	    'ffmpeg/libavcodec/vc2enc_dwt.c',
	    'ffmpeg/libavcodec/vcr1.c',
	    'ffmpeg/libavcodec/videodsp.c',
	    'ffmpeg/libavcodec/vima.c',
	    'ffmpeg/libavcodec/vmdaudio.c',
	    'ffmpeg/libavcodec/vmdvideo.c',
	    'ffmpeg/libavcodec/vmnc.c',
	    'ffmpeg/libavcodec/vorbis.c',
	    'ffmpeg/libavcodec/vorbis_data.c',
	    'ffmpeg/libavcodec/vorbis_parser.c',
	    'ffmpeg/libavcodec/vorbisdec.c',
	    'ffmpeg/libavcodec/vorbisdsp.c',
	    'ffmpeg/libavcodec/vorbisenc.c',
	    'ffmpeg/libavcodec/vp3.c',
	    'ffmpeg/libavcodec/vp3_parser.c',
	    'ffmpeg/libavcodec/vp3dsp.c',
	    'ffmpeg/libavcodec/vp5.c',
	    'ffmpeg/libavcodec/vp56.c',
	    'ffmpeg/libavcodec/vp56data.c',
	    'ffmpeg/libavcodec/vp56dsp.c',
	    'ffmpeg/libavcodec/vp56rac.c',
	    'ffmpeg/libavcodec/vp6.c',
	    'ffmpeg/libavcodec/vp6dsp.c',
	    'ffmpeg/libavcodec/vp8.c',
	    'ffmpeg/libavcodec/vp8_parser.c',
	    'ffmpeg/libavcodec/vp8dsp.c',
	    'ffmpeg/libavcodec/vp9.c',
	    'ffmpeg/libavcodec/vp9_parser.c',
	    'ffmpeg/libavcodec/vp9_superframe_bsf.c',
	    'ffmpeg/libavcodec/vp9dsp.c',
	    'ffmpeg/libavcodec/vp9dsp_10bpp.c',
	    'ffmpeg/libavcodec/vp9dsp_12bpp.c',
	    'ffmpeg/libavcodec/vp9dsp_8bpp.c',
	    'ffmpeg/libavcodec/vqavideo.c',
	    'ffmpeg/libavcodec/wavpack.c',
	    'ffmpeg/libavcodec/wavpackenc.c',
	    'ffmpeg/libavcodec/webp.c',
	    'ffmpeg/libavcodec/webvttdec.c',
	    'ffmpeg/libavcodec/webvttenc.c',
	    'ffmpeg/libavcodec/wma.c',
	    'ffmpeg/libavcodec/wma_common.c',
	    'ffmpeg/libavcodec/wma_freqs.c',
	    'ffmpeg/libavcodec/wmadec.c',
	    'ffmpeg/libavcodec/wmaenc.c',
	    'ffmpeg/libavcodec/wmalosslessdec.c',
	    'ffmpeg/libavcodec/wmaprodec.c',
	    'ffmpeg/libavcodec/wmavoice.c',
	    'ffmpeg/libavcodec/wmv2.c',
	    'ffmpeg/libavcodec/wmv2data.c',
	    'ffmpeg/libavcodec/wmv2dec.c',
	    'ffmpeg/libavcodec/wmv2dsp.c',
	    'ffmpeg/libavcodec/wmv2enc.c',
	    'ffmpeg/libavcodec/wnv1.c',
	    'ffmpeg/libavcodec/wrapped_avframe.c',
	    'ffmpeg/libavcodec/ws-snd1.c',
	    'ffmpeg/libavcodec/x86/aacpsdsp_init.c',
	    'ffmpeg/libavcodec/x86/ac3dsp_init.c',
	    'ffmpeg/libavcodec/x86/alacdsp_init.c',
	    'ffmpeg/libavcodec/x86/audiodsp_init.c',
	    'ffmpeg/libavcodec/x86/blockdsp_init.c',
	    'ffmpeg/libavcodec/x86/bswapdsp_init.c',
	    'ffmpeg/libavcodec/x86/cavsdsp.c',
	    'ffmpeg/libavcodec/x86/constants.c',
	    'ffmpeg/libavcodec/x86/dcadsp_init.c',
	    'ffmpeg/libavcodec/x86/dct_init.c',
	    'ffmpeg/libavcodec/x86/dirac_dwt_init.c',
	    'ffmpeg/libavcodec/x86/diracdsp_init.c',
	    'ffmpeg/libavcodec/x86/dnxhdenc_init.c',
	    'ffmpeg/libavcodec/x86/fdct.c',
	    'ffmpeg/libavcodec/x86/fdctdsp_init.c',
	    'ffmpeg/libavcodec/x86/fft_init.c',
	    'ffmpeg/libavcodec/x86/flacdsp_init.c',
	    'ffmpeg/libavcodec/x86/fmtconvert_init.c',
	    'ffmpeg/libavcodec/x86/g722dsp_init.c',
	    'ffmpeg/libavcodec/x86/h263dsp_init.c',
	    'ffmpeg/libavcodec/x86/h264_intrapred_init.c',
	    'ffmpeg/libavcodec/x86/h264_qpel.c',
	    'ffmpeg/libavcodec/x86/h264chroma_init.c',
	    'ffmpeg/libavcodec/x86/h264dsp_init.c',
	    'ffmpeg/libavcodec/x86/hevcdsp_init.c',
	    'ffmpeg/libavcodec/x86/hpeldsp_init.c',
	    'ffmpeg/libavcodec/x86/huffyuvdsp_init.c',
	    'ffmpeg/libavcodec/x86/huffyuvencdsp_mmx.c',
	    'ffmpeg/libavcodec/x86/idctdsp_init.c',
	    'ffmpeg/libavcodec/x86/jpeg2000dsp_init.c',
	    'ffmpeg/libavcodec/x86/lossless_audiodsp_init.c',
	    'ffmpeg/libavcodec/x86/lossless_videodsp_init.c',
	    'ffmpeg/libavcodec/x86/lpc.c',
	    'ffmpeg/libavcodec/x86/me_cmp_init.c',
	    'ffmpeg/libavcodec/x86/mlpdsp_init.c',
	    'ffmpeg/libavcodec/x86/mpegaudiodsp.c',
	    'ffmpeg/libavcodec/x86/mpegvideo.c',
	    'ffmpeg/libavcodec/x86/mpegvideodsp.c',
	    'ffmpeg/libavcodec/x86/mpegvideoenc.c',
	    'ffmpeg/libavcodec/x86/mpegvideoencdsp_init.c',
	    'ffmpeg/libavcodec/x86/pixblockdsp_init.c',
	    'ffmpeg/libavcodec/x86/pngdsp_init.c',
	    'ffmpeg/libavcodec/x86/proresdsp_init.c',
	    'ffmpeg/libavcodec/x86/qpeldsp_init.c',
	    'ffmpeg/libavcodec/x86/rv34dsp_init.c',
	    'ffmpeg/libavcodec/x86/rv40dsp_init.c',
	    'ffmpeg/libavcodec/x86/sbrdsp_init.c',
	    'ffmpeg/libavcodec/x86/simple_idct.c',
	    'ffmpeg/libavcodec/x86/snowdsp.c',
	    'ffmpeg/libavcodec/x86/svq1enc_init.c',
	    'ffmpeg/libavcodec/x86/synth_filter_init.c',
	    'ffmpeg/libavcodec/x86/takdsp_init.c',
	    'ffmpeg/libavcodec/x86/ttadsp_init.c',
	    'ffmpeg/libavcodec/x86/v210-init.c',
	    'ffmpeg/libavcodec/x86/v210enc_init.c',
	    'ffmpeg/libavcodec/x86/vc1dsp_init.c',
	    'ffmpeg/libavcodec/x86/vc1dsp_mmx.c',
	    'ffmpeg/libavcodec/x86/videodsp_init.c',
	    'ffmpeg/libavcodec/x86/vorbisdsp_init.c',
	    'ffmpeg/libavcodec/x86/vp3dsp_init.c',
	    'ffmpeg/libavcodec/x86/vp6dsp_init.c',
	    'ffmpeg/libavcodec/x86/vp8dsp_init.c',
	    'ffmpeg/libavcodec/x86/vp9dsp_init.c',
	    'ffmpeg/libavcodec/x86/vp9dsp_init_10bpp.c',
	    'ffmpeg/libavcodec/x86/vp9dsp_init_12bpp.c',
	    'ffmpeg/libavcodec/x86/vp9dsp_init_16bpp.c',
	    'ffmpeg/libavcodec/x86/xvididct_init.c',
	    'ffmpeg/libavcodec/xan.c',
	    'ffmpeg/libavcodec/xbmdec.c',
	    'ffmpeg/libavcodec/xbmenc.c',
	    'ffmpeg/libavcodec/xface.c',
	    'ffmpeg/libavcodec/xfacedec.c',
	    'ffmpeg/libavcodec/xfaceenc.c',
	    'ffmpeg/libavcodec/xiph.c',
	    'ffmpeg/libavcodec/xl.c',
	    'ffmpeg/libavcodec/xsubdec.c',
	    'ffmpeg/libavcodec/xsubenc.c',
	    'ffmpeg/libavcodec/xvididct.c',
	    'ffmpeg/libavcodec/xwddec.c',
	    'ffmpeg/libavcodec/xwdenc.c',
	    'ffmpeg/libavcodec/xxan.c',
	    'ffmpeg/libavcodec/y41pdec.c',
	    'ffmpeg/libavcodec/y41penc.c',
	    'ffmpeg/libavcodec/ylc.c',
	    'ffmpeg/libavcodec/yop.c',
	    'ffmpeg/libavcodec/yuv4dec.c',
	    'ffmpeg/libavcodec/yuv4enc.c',
	    'ffmpeg/libavcodec/zerocodec.c',
	    'ffmpeg/libavcodec/zmbv.c',
	    'ffmpeg/libavcodec/zmbvenc.c',
	    ])
	"""
	my_module.add_optionnal_depend('vdpau', src_file=[
	    'ffmpeg/libavcodec/vdpau.c',
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
	    'ffmpeg-avswresample',
	    'ffmpeg-avutil',
	    ])

	return True