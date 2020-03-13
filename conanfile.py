import os

from conans import CMake, ConanFile, tools


class LibrdkafkaConan(ConanFile):
    name = "librdkafka"
    version = "1.3.0"
    license = "https://github.com/sam-mosleh/conan-librdkafka/blob/master/LICENSE"
    author = "Sam Mosleh sam.mosleh@ut.ac.ir"
    url = "https://github.com/sam-mosleh/conan-librdkafka"
    homepage = "https://github.com/edenhill/librdkafka"
    description = """This is a Kafka C client package.
    A fully featured, portable librdkafka library."""

    topics = ("kafka", "librdkafka")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "zlib": [True, False],
        "zstd": [True, False],
        "plugins": [True, False],
        "ssl": [True, False],
        "sasl": [True, False],
        "lz4": [True, False],
    }
    default_options = {
        "shared": False,
        "zlib": False,
        "zstd": False,
        "plugins": False,
        "ssl": False,
        "sasl": False,
        "lz4": False,
    }
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    sources_folder = "sources"
    sha256 = "465cab533ebc5b9ca8d97c90ab69e0093460665ebaf38623209cf343653c76d2"

    def configure(self):
        if self.options.ssl:
            self.options["openssl"].shared = self.options.shared

    def requirements(self):
        if self.options.zlib:
            self.requires.add("zlib/1.2.11")
        if self.options.zstd:
            self.requires.add("zstd/1.4.4")
        if self.options.ssl:
            self.requires.add("openssl/1.1.1d")
        if self.options.lz4:
            self.requires.add("lz4/1.9.2")

    def source(self):
        download_url = "{}/archive/v{}.tar.gz".format(self.homepage,
                                                      self.version)
        tools.get(download_url, sha256=self.sha256)
        os.rename("{}-{}".format(self.name, self.version), self.sources_folder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions[
            'WITHOUT_OPTIMIZATION'] = self.settings.build_type == "Debug"
        cmake.definitions['RDKAFKA_BUILD_STATIC'] = not self.options.shared
        cmake.definitions['RDKAFKA_BUILD_EXAMPLES'] = False
        cmake.definitions['RDKAFKA_BUILD_TESTS'] = False
        cmake.definitions['WITHOUT_WIN32_CONFIG'] = True

        cmake.definitions['WITH_ZLIB'] = self.options.zlib
        cmake.definitions['WITH_ZSTD'] = self.options.zstd
        cmake.definitions['WITH_PLUGINS'] = self.options.plugins
        cmake.definitions['WITH_SSL'] = self.options.ssl
        cmake.definitions['WITH_SASL'] = self.options.sasl
        cmake.definitions['ENABLE_LZ4_EXT'] = self.options.lz4

        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src=self.name)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rdkafka", "rdkafka++"]
