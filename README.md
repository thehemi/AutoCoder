# AutoCoder

AutoCoder is a powerful GPT-4 powered code tool that will revolutionize the way you handle your coding projects. With no token limits, it can work on entire repositories or individual files to cleanup, optimize, comment, convert languages, convert frameworks, and much more! Get ready to experience a new era of coding with AutoCoder!

## Features

* Write new code, or optimize, comment, organize, convert languages, convert frameworks, etc with existing code!
* Supports entire repositories and files of any size, even on GPT-4 8k
* Optimize, comment, organize, convert languages, implement new features in one click
* Extremely reliable - uses a number of tricks to prevent bad code, such as multiple iterations, self-checking
* Compile errors are passed back to GPT to fix
* Unit tests - figures out the types of data your functions need and creates unit tests before/after
* Automatically fixes errors in files or repos - just drag and drop file or directory (Supported: Python, C#, ...)
* Can make git submissions and output diff files or updated files

## Installation

To get started with AutoCoder, simply run the following command:

```
pip install autocoder
```

## Usage

### Basic Example

Here's a simple example of how to use AutoCoder to optimize and comment a Python file:

```python
from autocoder import AutoCoder

ac = AutoCoder()
ac.optimize_and_comment("example.py")
```

### Advanced Example

In this example, we'll convert a Python file to C#, optimize it, comment it, and create unit tests:

```python
from autocoder import AutoCoder

ac = AutoCoder()
ac.convert_language("example.py", "C#")
ac.optimize_and_comment("example_converted.cs")
ac.create_unit_tests("example_converted.cs")
```

## Supported Languages and Frameworks

AutoCoder currently supports the following languages and frameworks:

* Python
* C#
* JavaScript
* TypeScript
* Java

More languages and frameworks are being added regularly. If you'd like to see support for a specific language or framework, feel free to open an issue or contribute to the project!

## Contributing

We welcome contributions to AutoCoder! If you'd like to get involved, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute.

## License

AutoCoder is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the software as long as you adhere to the terms of the license.

## Support and Feedback

If you encounter any issues, have feature requests, or simply want to provide feedback, please open an issue on our GitHub repository. We'll be more than happy to help!

(Written by Autocoder - To remove this watermark, please upgrade to autocoder pro j/k it's free I wrote this part)

Happy coding with AutoCoder! 🚀
