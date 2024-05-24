from setuptools import setup, find_packages

setup(
    name="luper",
    version="1.0.0",
    description="Luper: A web page brute-force tool similar to gobuster and dirb",
    author="Seu Nome",
    author_email="seu_email@example.com",
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
