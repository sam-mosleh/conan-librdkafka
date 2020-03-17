
# Conan-LibRdKafka

[![Download](https://api.bintray.com/packages/sam-mosleh/conan/librdkafka%3Amosleh/images/download.svg)](https://bintray.com/sam-mosleh/conan/librdkafka%3Amosleh/_latestVersion) [![Build Status](https://travis-ci.com/sam-mosleh/conan-librdkafka.svg?branch=release%2F1.3.0)](https://travis-ci.com/sam-mosleh/conan-librdkafka) [![Build status](https://ci.appveyor.com/api/projects/status/psbsuol9360sdn79/branch/release/1.3.0?svg=true)](https://ci.appveyor.com/project/sam-mosleh/conan-librdkafka/branch/release/1.3.0) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Conan C/C++ package for [LibRdKafka](https://github.com/edenhill/librdkafka) library.

## Getting Started

In order to use this package you have to add my repo to your remote list.
```
conan remote add mosleh-repo https://api.bintray.com/conan/sam-mosleh/conan
```

### Installation

For basic package installation:

```
conan install librdkafka/1.3.0@mosleh/stable
```
You can read about using Conan packages [here](https://docs.conan.io/en/latest/using_packages/conanfile_txt.html).

### Options

Key | Default Value | Description
--- | --- | :--
`shared` | False | Use dynamic linkage
`zlib` | False | Enables Zlib compression.
`zstd` | False | Enables ZStd compression.
`plugins` | False | Enables plugin for the package.
`ssl` | False | Enables SSL for the package
`sasl` | False | Enables SASL.
`lz4` | False | Enables LZ4 compression.

Read about [options](https://docs.conan.io/en/latest/creating_packages/getting_started.html?highlight=options#settings-vs-options).

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details
