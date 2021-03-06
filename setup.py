from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='template_package',
    version='0.0.1',
    description='Template for a wheel-ready Python package.',
    py_modules=["helloworld"],
    package_dir={'':'src'}, 
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public  License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    url="",
    author="Keith Helsabeck",
    author_email="admin@mylawdb.com",
)
