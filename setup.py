import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pysat_metamodel",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="famapy short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FaMaPy/pysat_metamodel",
    packages=setuptools.find_namespace_packages(include=['famapy.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
       'python-sat>=0.1.5.dev16'
    ],
    dependency_links=[
        'https://github.com/FaMaPy/core/tarball/master#egg=package-1.0'
    ]
)
