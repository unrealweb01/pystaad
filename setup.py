from setuptools import setup, find_packages

# Read the contents of the README file (if you have one) for the long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python package for automating STAAD.Pro tasks using `win32com` and `openstaad`."

setup(
    name="pystaad",  # Name of the package
    version="0.1.0",  # Initial version
    author="Ragul",  # Your name
    author_email="testing010101@proton.me",  # Replace with your email
    description="A Python package to simplify STAAD.Pro automation",
    long_description=long_description,
    long_description_content_type="text/markdown",  # README content type
    url="https://github.com/unrealweb01/pystaad",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically find and include packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
    install_requires=[
        "pywin32>=304",  # Dependency for `win32com`
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "pystaad=pystaad.cli:main",  # CLI command (optional, if you have one)
        ],
    },
    include_package_data=True,  # Include files specified in MANIFEST.in
)
