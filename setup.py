from setuptools import setup


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="olx-api-wrapper",
    version="0.3.0",
    description="Unofficial Wrapper for OLX API",
    author="Paweł Stawikowski",
    author_email="pawikoski@gmail.com",
    packages=["olx"],
    url="https://github.com/Pawikoski/olx-api-wrapper",
    install_requires=["requests", "dacite"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
