from setuptools import setup, find_packages

setup(
    name="enterprize-fizzbuzz",
    version="1.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fizzbuzz=fizzbuzz.main:fizzbuzz_cli',
        ],
    },
    author="Rickard Armiento",
    author_email="gitcommits@armiento.net",
    description="An enterprise solution to the FizzBuzz problem",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
