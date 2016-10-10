#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

import lutinLib_ffmpegCommon

def add_generate_path(target, my_module):
	generated_path = os.path.join("generated", target.get_name())
	generated_path_bs = os.path.join("generated", target.get_name() + "_" + str(target.get_bus_size()))
	if os.path.exists(os.path.join(os.path.dirname(__file__), generated_path_bs)) == True:
		my_module.add_path(generated_path_bs)
	elif os.path.exists(os.path.join(os.path.dirname(__file__), generated_path)) == True:
		my_module.add_path(generated_path)
	else:
		debug.warning("get default Path for type: " + str(target.get_type()))
		my_module.add_path("generated/Linux")


def add_common_property(target, my_module):
	add_generate_path(target, my_module)
	
	my_module.add_flag('c', [
	    "-D_ISOC99_SOURCE",
	    "-D_FILE_OFFSET_BITS=64",
	    "-D_LARGEFILE_SOURCE",
	    "-D_POSIX_C_SOURCE=200112",
	    "-D_XOPEN_SOURCE=600",
	    "-DHAVE_AV_CONFIG_H",
	    ])
	if "Linux" in target.get_type():
		my_module.add_flag('c', [
		    "-DZLIB_CONST",
		    "-D_GNU_SOURCE=1",
		    "-D_REENTRANT",
		    "-DPIC"
		    ])
	elif "Windows" in target.get_type():
		my_module.add_flag('c', [
		    "-U__STRICT_ANSI__",
		    "-D__USE_MINGW_ANSI_STDIO=1",
		    "-D__printf__=__gnu_printf__",
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
	if "Windows" in target.get_type():
		my_module.add_flag('c', [
		    "-fomit-frame-pointer",
		    "-Wno-maybe-uninitialized",
		    ])
	

	if target.get_compilator() == "clang":
		my_module.add_flag('c', [ "-Wno-uninitialized"])
	else:
		my_module.add_flag('c', [ "-Wno-maybe-uninitialized"])
	if "Linux" in target.get_type():
		# TODO: Check the real impact ...
		my_module.add_flag('link-dynamic', ["-Wl,-Bsymbolic"])