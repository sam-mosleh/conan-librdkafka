from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="missing",
                                 upload_dependencies="all",
                                 visual_runtimes=["MD"])
    builder.add_common_builds(shared_option_name="librdkafka:shared",
                              pure_c=False,
                              build_all_options_values=[
                                  "librdkafka:zlib",
                                  "librdkafka:zstd",
                                  "librdkafka:ssl",
                              ])
    builder.run()
