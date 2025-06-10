from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="olx-api-wrapper",
    version="1.3.2",
    description="Unofficial Wrapper for OLX API",
    author="Paweł Stawikowski",
    author_email="pawikoski@gmail.com",
    packages=find_packages(),
    url="https://github.com/Pawikoski/olx-api-wrapper",
    install_requires=[
        "requests>=2.32.3",
        "dacite>=1.9.2",
        "py-moneyed>=3.0",
        "fake_useragent>=2.2.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    keywords="olx api wrapper unofficial",
    project_urls={
        "Documentation": "https://github.com/Pawikoski/olx-api-wrapper#readme",
        "Issue Tracker": "https://github.com/Pawikoski/olx-api-wrapper/issues",
    },
)
