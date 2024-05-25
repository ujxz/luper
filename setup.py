from setuptools import setup, find_packages

setup(
    name="luper",
    version="0.0.1",
    description="Luper: A web page brute-force tool similar to gobuster and dirsearch",
    author="Jabes Eduardo",
    author_email="jabfxcomercial@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "luper=luper.brute_forcer:main",
        ],
    },
)
