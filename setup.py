import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HomPolys",
    version="0.0.1",
    author="Madelyn Andersen",
    author_email="mandersen@hmc.edu",
    description="A package to compute polynomial representation of homomorphism numbers for graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madelynandersen/HomomorphismPolynomials",
    project_urls={
        "Bug Tracker": "https://github.com/madelynandersen/HomomorphismPolynomials/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)