#!/usr/bin/python
import realog.debug as debug
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
	    'ffmpeg/libavfilter/aeval.c',
	    'ffmpeg/libavfilter/af_adelay.c',
	    'ffmpeg/libavfilter/af_aecho.c',
	    'ffmpeg/libavfilter/af_aemphasis.c',
	    'ffmpeg/libavfilter/af_afade.c',
	    'ffmpeg/libavfilter/af_afftfilt.c',
	    'ffmpeg/libavfilter/af_aformat.c',
	    'ffmpeg/libavfilter/af_agate.c',
	    'ffmpeg/libavfilter/af_alimiter.c',
	    'ffmpeg/libavfilter/af_amerge.c',
	    'ffmpeg/libavfilter/af_amix.c',
	    'ffmpeg/libavfilter/af_anequalizer.c',
	    'ffmpeg/libavfilter/af_anull.c',
	    'ffmpeg/libavfilter/af_apad.c',
	    'ffmpeg/libavfilter/af_aphaser.c',
	    'ffmpeg/libavfilter/af_apulsator.c',
	    'ffmpeg/libavfilter/af_aresample.c',
	    'ffmpeg/libavfilter/af_asetnsamples.c',
	    'ffmpeg/libavfilter/af_asetrate.c',
	    'ffmpeg/libavfilter/af_ashowinfo.c',
	    'ffmpeg/libavfilter/af_astats.c',
	    'ffmpeg/libavfilter/af_atempo.c',
	    'ffmpeg/libavfilter/af_biquads.c',
	    'ffmpeg/libavfilter/af_channelmap.c',
	    'ffmpeg/libavfilter/af_channelsplit.c',
	    'ffmpeg/libavfilter/af_chorus.c',
	    'ffmpeg/libavfilter/af_compand.c',
	    'ffmpeg/libavfilter/af_compensationdelay.c',
	    'ffmpeg/libavfilter/af_dcshift.c',
	    'ffmpeg/libavfilter/af_dynaudnorm.c',
	    'ffmpeg/libavfilter/af_earwax.c',
	    'ffmpeg/libavfilter/af_extrastereo.c',
	    'ffmpeg/libavfilter/af_firequalizer.c',
	    'ffmpeg/libavfilter/af_flanger.c',
	    'ffmpeg/libavfilter/af_hdcd.c',
	    'ffmpeg/libavfilter/af_join.c',
	    'ffmpeg/libavfilter/af_pan.c',
	    'ffmpeg/libavfilter/af_replaygain.c',
	    'ffmpeg/libavfilter/af_sidechaincompress.c',
	    'ffmpeg/libavfilter/af_silencedetect.c',
	    'ffmpeg/libavfilter/af_silenceremove.c',
	    'ffmpeg/libavfilter/af_stereotools.c',
	    'ffmpeg/libavfilter/af_stereowiden.c',
	    'ffmpeg/libavfilter/af_tremolo.c',
	    'ffmpeg/libavfilter/af_vibrato.c',
	    'ffmpeg/libavfilter/af_volume.c',
	    'ffmpeg/libavfilter/af_volumedetect.c',
	    'ffmpeg/libavfilter/allfilters.c',
	    'ffmpeg/libavfilter/asink_anullsink.c',
	    'ffmpeg/libavfilter/asrc_anoisesrc.c',
	    'ffmpeg/libavfilter/asrc_anullsrc.c',
	    'ffmpeg/libavfilter/asrc_sine.c',
	    'ffmpeg/libavfilter/audio.c',
	    'ffmpeg/libavfilter/avf_ahistogram.c',
	    'ffmpeg/libavfilter/avf_aphasemeter.c',
	    'ffmpeg/libavfilter/avf_avectorscope.c',
	    'ffmpeg/libavfilter/avf_concat.c',
	    'ffmpeg/libavfilter/avf_showcqt.c',
	    'ffmpeg/libavfilter/avf_showfreqs.c',
	    'ffmpeg/libavfilter/avf_showspectrum.c',
	    'ffmpeg/libavfilter/avf_showvolume.c',
	    'ffmpeg/libavfilter/avf_showwaves.c',
	    'ffmpeg/libavfilter/avfilter.c',
	    'ffmpeg/libavfilter/avfiltergraph.c',
	    'ffmpeg/libavfilter/bbox.c',
	    'ffmpeg/libavfilter/buffersink.c',
	    'ffmpeg/libavfilter/buffersrc.c',
	    'ffmpeg/libavfilter/colorspacedsp.c',
	    'ffmpeg/libavfilter/drawutils.c',
	    'ffmpeg/libavfilter/dualinput.c',
	    'ffmpeg/libavfilter/f_bench.c',
	    'ffmpeg/libavfilter/f_drawgraph.c',
	    'ffmpeg/libavfilter/f_interleave.c',
	    'ffmpeg/libavfilter/f_loop.c',
	    'ffmpeg/libavfilter/f_metadata.c',
	    'ffmpeg/libavfilter/f_perms.c',
	    'ffmpeg/libavfilter/f_realtime.c',
	    'ffmpeg/libavfilter/f_reverse.c',
	    'ffmpeg/libavfilter/f_select.c',
	    'ffmpeg/libavfilter/f_sendcmd.c',
	    'ffmpeg/libavfilter/f_streamselect.c',
	    'ffmpeg/libavfilter/fifo.c',
	    'ffmpeg/libavfilter/formats.c',
	    'ffmpeg/libavfilter/framepool.c',
	    'ffmpeg/libavfilter/framesync.c',
	    'ffmpeg/libavfilter/generate_wave_table.c',
	    'ffmpeg/libavfilter/graphdump.c',
	    'ffmpeg/libavfilter/graphparser.c',
	    'ffmpeg/libavfilter/lavfutils.c',
	    'ffmpeg/libavfilter/lswsutils.c',
	    'ffmpeg/libavfilter/opencl_allkernels.c',
	    'ffmpeg/libavfilter/pthread.c',
	    'ffmpeg/libavfilter/setpts.c',
	    'ffmpeg/libavfilter/settb.c',
	    'ffmpeg/libavfilter/split.c',
	    'ffmpeg/libavfilter/src_movie.c',
	    'ffmpeg/libavfilter/transform.c',
	    'ffmpeg/libavfilter/trim.c',
	    'ffmpeg/libavfilter/vaf_spectrumsynth.c',
	    'ffmpeg/libavfilter/vf_alphamerge.c',
	    'ffmpeg/libavfilter/vf_aspect.c',
	    'ffmpeg/libavfilter/vf_atadenoise.c',
	    'ffmpeg/libavfilter/vf_bbox.c',
	    'ffmpeg/libavfilter/vf_blackdetect.c',
	    'ffmpeg/libavfilter/vf_blend.c',
	    'ffmpeg/libavfilter/vf_bwdif.c',
	    'ffmpeg/libavfilter/vf_chromakey.c',
	    'ffmpeg/libavfilter/vf_ciescope.c',
	    'ffmpeg/libavfilter/vf_codecview.c',
	    'ffmpeg/libavfilter/vf_colorbalance.c',
	    'ffmpeg/libavfilter/vf_colorchannelmixer.c',
	    'ffmpeg/libavfilter/vf_colorkey.c',
	    'ffmpeg/libavfilter/vf_colorlevels.c',
	    'ffmpeg/libavfilter/vf_colorspace.c',
	    'ffmpeg/libavfilter/vf_convolution.c',
	    'ffmpeg/libavfilter/vf_copy.c',
	    'ffmpeg/libavfilter/vf_crop.c',
	    'ffmpeg/libavfilter/vf_curves.c',
	    'ffmpeg/libavfilter/vf_datascope.c',
	    'ffmpeg/libavfilter/vf_dctdnoiz.c',
	    'ffmpeg/libavfilter/vf_deband.c',
	    'ffmpeg/libavfilter/vf_decimate.c',
	    'ffmpeg/libavfilter/vf_dejudder.c',
	    'ffmpeg/libavfilter/vf_deshake.c',
	    'ffmpeg/libavfilter/vf_detelecine.c',
	    'ffmpeg/libavfilter/vf_displace.c',
	    'ffmpeg/libavfilter/vf_drawbox.c',
	    'ffmpeg/libavfilter/vf_edgedetect.c',
	    'ffmpeg/libavfilter/vf_elbg.c',
	    'ffmpeg/libavfilter/vf_extractplanes.c',
	    'ffmpeg/libavfilter/vf_fade.c',
	    'ffmpeg/libavfilter/vf_fftfilt.c',
	    'ffmpeg/libavfilter/vf_field.c',
	    'ffmpeg/libavfilter/vf_fieldhint.c',
	    'ffmpeg/libavfilter/vf_fieldmatch.c',
	    'ffmpeg/libavfilter/vf_fieldorder.c',
	    'ffmpeg/libavfilter/vf_format.c',
	    'ffmpeg/libavfilter/vf_fps.c',
	    'ffmpeg/libavfilter/vf_framepack.c',
	    'ffmpeg/libavfilter/vf_framerate.c',
	    'ffmpeg/libavfilter/vf_framestep.c',
	    'ffmpeg/libavfilter/vf_gradfun.c',
	    'ffmpeg/libavfilter/vf_hflip.c',
	    'ffmpeg/libavfilter/vf_histogram.c',
	    'ffmpeg/libavfilter/vf_hqx.c',
	    'ffmpeg/libavfilter/vf_hue.c',
	    'ffmpeg/libavfilter/vf_hwdownload.c',
	    'ffmpeg/libavfilter/vf_hwupload.c',
	    'ffmpeg/libavfilter/vf_idet.c',
	    'ffmpeg/libavfilter/vf_il.c',
	    'ffmpeg/libavfilter/vf_lenscorrection.c',
	    'ffmpeg/libavfilter/vf_lut.c',
	    'ffmpeg/libavfilter/vf_lut3d.c',
	    'ffmpeg/libavfilter/vf_maskedmerge.c',
	    'ffmpeg/libavfilter/vf_mergeplanes.c',
	    'ffmpeg/libavfilter/vf_neighbor.c',
	    'ffmpeg/libavfilter/vf_noise.c',
	    'ffmpeg/libavfilter/vf_null.c',
	    'ffmpeg/libavfilter/vf_overlay.c',
	    'ffmpeg/libavfilter/vf_pad.c',
	    'ffmpeg/libavfilter/vf_palettegen.c',
	    'ffmpeg/libavfilter/vf_paletteuse.c',
	    'ffmpeg/libavfilter/vf_pixdesctest.c',
	    'ffmpeg/libavfilter/vf_psnr.c',
	    'ffmpeg/libavfilter/vf_qp.c',
	    'ffmpeg/libavfilter/vf_random.c',
	    'ffmpeg/libavfilter/vf_readvitc.c',
	    'ffmpeg/libavfilter/vf_remap.c',
	    'ffmpeg/libavfilter/vf_removegrain.c',
	    'ffmpeg/libavfilter/vf_removelogo.c',
	    'ffmpeg/libavfilter/vf_rotate.c',
	    'ffmpeg/libavfilter/vf_scale.c',
	    'ffmpeg/libavfilter/vf_selectivecolor.c',
	    'ffmpeg/libavfilter/vf_separatefields.c',
	    'ffmpeg/libavfilter/vf_setfield.c',
	    'ffmpeg/libavfilter/vf_showinfo.c',
	    'ffmpeg/libavfilter/vf_showpalette.c',
	    'ffmpeg/libavfilter/vf_shuffleframes.c',
	    'ffmpeg/libavfilter/vf_shuffleplanes.c',
	    'ffmpeg/libavfilter/vf_signalstats.c',
	    'ffmpeg/libavfilter/vf_ssim.c',
	    'ffmpeg/libavfilter/vf_stack.c',
	    'ffmpeg/libavfilter/vf_swaprect.c',
	    'ffmpeg/libavfilter/vf_swapuv.c',
	    'ffmpeg/libavfilter/vf_telecine.c',
	    'ffmpeg/libavfilter/vf_thumbnail.c',
	    'ffmpeg/libavfilter/vf_tile.c',
	    'ffmpeg/libavfilter/vf_transpose.c',
	    'ffmpeg/libavfilter/vf_unsharp.c',
	    'ffmpeg/libavfilter/vf_vectorscope.c',
	    'ffmpeg/libavfilter/vf_vflip.c',
	    'ffmpeg/libavfilter/vf_vignette.c',
	    'ffmpeg/libavfilter/vf_w3fdif.c',
	    'ffmpeg/libavfilter/vf_waveform.c',
	    'ffmpeg/libavfilter/vf_xbr.c',
	    'ffmpeg/libavfilter/vf_yadif.c',
	    'ffmpeg/libavfilter/vf_zoompan.c',
	    'ffmpeg/libavfilter/video.c',
	    'ffmpeg/libavfilter/vsink_nullsink.c',
	    'ffmpeg/libavfilter/vsrc_cellauto.c',
	    'ffmpeg/libavfilter/vsrc_life.c',
	    'ffmpeg/libavfilter/vsrc_mandelbrot.c',
	    'ffmpeg/libavfilter/vsrc_testsrc.c',
	    'ffmpeg/libavfilter/window_func.c',
	    ])
	if target.get_arch() == "x86":
		my_module.add_src_file([
		    'ffmpeg/libavfilter/x86/af_volume_init.c',
		    'ffmpeg/libavfilter/x86/avf_showcqt_init.c',
		    'ffmpeg/libavfilter/x86/colorspacedsp_init.c',
		    'ffmpeg/libavfilter/x86/vf_blend_init.c',
		    'ffmpeg/libavfilter/x86/vf_bwdif_init.c',
		    'ffmpeg/libavfilter/x86/vf_gradfun_init.c',
		    'ffmpeg/libavfilter/x86/vf_idet_init.c',
		    'ffmpeg/libavfilter/x86/vf_maskedmerge_init.c',
		    'ffmpeg/libavfilter/x86/vf_noise.c',
		    'ffmpeg/libavfilter/x86/vf_psnr_init.c',
		    'ffmpeg/libavfilter/x86/vf_removegrain_init.c',
		    'ffmpeg/libavfilter/x86/vf_ssim_init.c',
		    'ffmpeg/libavfilter/x86/vf_w3fdif_init.c',
		    'ffmpeg/libavfilter/x86/vf_yadif_init.c',
		    ])
	elif target.get_arch() == "arm":
		# no specific files
		pass
	else:
		debug.warning("unknow architecture ...");
	if "MacOs" in target.get_type():
		my_module.add_src_file([
		    'ffmpeg/libavfilter/vf_coreimage.m',
		    ])
	my_module.compile_version("c", 1999)
	
	lutinLib_ffmpegCommon.add_common_property(target, my_module);
	
	# add dependency of libraries:
	my_module.add_depend('c')
	my_module.add_depend('m')
	my_module.add_depend('z')
	my_module.add_depend('pthread')
	my_module.add_depend([
	    'ffmpeg-avcodec',
	    'ffmpeg-avutil',
	    'ffmpeg-avformat',
	    'ffmpeg-avswscale',
	    'ffmpeg-headers',
	    ])

	return True