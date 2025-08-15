#!/usr/bin/env python3
"""
Setup script for Grocery Webapp
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("backend/requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="grocery-webapp",
    version="1.0.0",
    author="Grocery Webapp Team",
    author_email="your.email@example.com",
    description="A modern, full-stack grocery management web application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/grocery-webapp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "grocery-webapp=backend.app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "backend": ["*.txt", "*.md"],
    },
    keywords="flask, webapp, grocery, inventory, management",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/grocery-webapp/issues",
        "Source": "https://github.com/yourusername/grocery-webapp",
        "Documentation": "https://github.com/yourusername/grocery-webapp#readme",
    },
)
