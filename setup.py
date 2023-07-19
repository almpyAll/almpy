from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "numpy", "matplotlib"]

setup(
    name="almpy",
    version="0.0.1",
    author="Almaz Abdulhakov",
    author_email="ekzis1984@gmail.com",
    description="Geo package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/almpyAll/almpy",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
