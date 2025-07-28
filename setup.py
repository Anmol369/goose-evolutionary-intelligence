from setuptools import setup, find_packages

# Read requirements from files
try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    install_requires = []

try:
    with open("requirements-dev.txt", "r", encoding="utf-8") as f:
        dev_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    dev_requires = []

setup(
    name="goose-evolutionary-intelligence",
    version="0.1.1",
    description="Seven-Dimensional Self-Improving AI Agents for Goose",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Goose Team",
    author_email="team@goose.ai",
    url="https://github.com/goose-ai/goose-evolutionary-intelligence",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires,
    },
    entry_points={
        "console_scripts": [
            "goose-evo-demo=goose_evo.cli:main",
        ],
    },
)
