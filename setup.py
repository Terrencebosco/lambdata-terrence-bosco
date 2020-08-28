from setuptools import find_packages, setup

with open ("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TEST",
    version="1.0",
    auther="Terrence",
    auther_email="Terrencebosco@gmail.com",
    description="test set up",
    long_description=long_description,
    long_desctiption_content_type="text/markdown",
    url="https://github.com/Terrencebosco/lambdata-terrence-bosco",
    packages=find_packages()
)