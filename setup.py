from setuptools import setup, find_packages

setup(
    name='luper',
    version='0.0.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'src = brute_forcer:main',
        ],
    },
    install_requires=[
        'requests',
    ],
    description='Luper: Discovery Enumaration',
    author='Jabes Eduardo',
    author_email='jabfxcomercial@gmail.com',
    url='https://github.com/ujxz/luper',
)