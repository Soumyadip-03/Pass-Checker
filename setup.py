from setuptools import setup, find_packages

setup(
    name="password-strength-checker",
    version="1.0.0",
    description="Enhanced Password Strength Checker built with Reflex",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "reflex>=0.4.0",
        "password-strength>=0.0.3",
        "zxcvbn>=4.4.28",
        "bcrypt>=4.1.2",
        "python-dotenv>=1.0.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "requests>=2.31.0"
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)