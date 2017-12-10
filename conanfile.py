from conans import ConanFile, tools
import os


class AsioConan(ConanFile):
	name = "Asio"
	version = "master"
	license = "Boost Software License - Version 1.0"
	url = "<Package recipe repository url here, for issues about the package>"
	description = "Asio is a cross-platform C++ library for network and low-level I/O programming that provides developers with a consistent asynchronous model using a modern C++ approach."
	# No settings/options are necessary, this is header only

	def source(self):
		self.run("git clone --depth 1 https://github.com/chriskohlhoff/asio.git")

	def package(self):
		self.copy('*.hpp', src='asio/asio/include', dst='include')
		self.copy('*.ipp', src='asio/asio/include', dst='include')
	
	def package_info(self):
		self.cpp_info.defines = ["ASIO_STANDALONE"]