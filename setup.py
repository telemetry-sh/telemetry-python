from setuptools import setup, find_packages

setup(
    name="telemetry-sh",
    version="1.0.9",
    description="A simple telemetry logging SDK for Python.",
    author="JR R",
    author_email="thebuilderjr93@gmail.com",
    url="https://github.com/telemetry-sh/telemetry-python",
    packages=find_packages(),
    install_requires=[
        "requests",
        "aiohttp",
        "async_timeout"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
