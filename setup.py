import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terrence_bosco", # Replace with your own username
    version="0.0.1",
    author="Terrence_bosco",
    author_email="Terrencebosco@gmail.com",
    description="test upload",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Terrencebosco/lambdata-terrence-bosco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)