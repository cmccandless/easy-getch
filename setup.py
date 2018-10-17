import subprocess
import sys
import setuptools
from changelog import changelog
from easy_getch.__version__ import VERSION


if __name__ == '__main__':
    with open("README.md", "r") as fh:
        long_description = fh.read()
    try:
        subprocess.check_call('git')
        long_description += '\n'.join(changelog())
    except subprocess.CalledProcessError:
        pass

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
        url="https://github.com/cmccandless/easy-getch",
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
