"""
Setup file for the Gale-Shapley Algorithm package.
"""

from setuptools import setup, find_packages

setup(
    name="gale_shapley_algorithm",
    version="1.0.0",
    author="Aditya",
    description="Implementation of the Gale-Shapley algorithm for hospital-resident matching",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.0",
    ],
) 