import subprocess
import sys
import setuptools
from easy_getch.__version__ import VERSION


def changelog():
    log =  subprocess.check_output('bin/changelog')
    if sys.version_info[0] == 3:
        log = log.decode()
    return log


if __name__ == '__main__':
    with open("README.md", "r") as fh:
        long_description = fh.read()
    long_description += changelog() + '\n'

    setuptools.setup(
        name="easy_getch",
        version=VERSION,
        author="Corey McCandless",
        author_email="crm1994@gmail.com",
        description=(
            "Easily get a single character"
        ),
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/cmccandless/easy_getch",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        entry_points={},
        install_requires=[],
        include_package_data=True
    )
