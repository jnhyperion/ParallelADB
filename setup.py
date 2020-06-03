import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parallel-adb",
    version="0.0.1",
    author="Johnny Huang",
    author_email="jnhyperion@gmail.com",
    description="Enable adb command parallel run in all connected devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jnhyperion/WikiBot",
    keywords='atlassian confluence modification',
    packages=setuptools.find_packages(),
    install_requires=[
        'atlassian-python-api',
        'beautifulsoup4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
