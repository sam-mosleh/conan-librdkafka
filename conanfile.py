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
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    sources_folder = "sources"

    def configure(self):
        pass

    def requirements(self):
        pass

    def source(self):
        download_url = "{}/archive/v{}.tar.gz".format(self.homepage,
                                                      self.version)
        tools.get(download_url)
        os.rename("{}-{}".format(self.name, self.version), self.sources_folder)

    def build(self):
        cmake = CMake(self)
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
        pass
