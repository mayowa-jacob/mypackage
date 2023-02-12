from setuptools import setup, find_packages

setup(
    name="myPackage",
    version="0.1",
    packages=find_packages(exclude=["test"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    url="http://github.com/<mayowa-jacob>/<package-name>",
    author="<Mayowa Jacob>",
    author_email="<mayowa360@gmail.com>"
)
