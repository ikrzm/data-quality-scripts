from setuptools import setup, find_packages

setup(
    name="data_quality_scripts",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.20.0',
        'pyyaml>=5.4.1',
    ],
    author="Ikram ZOUAOUI",
    author_email="ikramzouaoui95@gmail.com",
    description="A collection of Python scripts for automated data quality checks",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ikrzm/data-quality-scripts",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)