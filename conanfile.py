from conans import ConanFile, CMake, tools


class ConcurrentqueueConan(ConanFile):
    name = "ConcurrentQueue"
    version = "1.0.0"
    license = "Boost Software License - Version 1.0"
    url = "https://github.com/microblink/concurrentqueue"
    description = "A fast multi-producer, multi-consumer lock-free concurrent queue for C++11"
    generators = "cmake"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    no_copy_source = True
    export_sources = "*.h"


    def package(self):
        self.copy("*.h", dst="include")

    def package_id(self):
        self.info.header_only()

