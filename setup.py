from setuptools import setup, find_namespace_packages

setup(
    name="massive_serve",
    version="0.1.14",
    packages=find_namespace_packages(include=['massive_serve*']),
    package_data={
        'massive_serve': [
            'api/**/*',
            'src/**/*',
            'contriever/**/*',
            'utils/**/*',
            'contriever/src/**/*',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "click",  # Required for CLI
        "faiss-cpu",  # or faiss-gpu if you're using GPU
        "tqdm",
        "flask",
        "flask-cors",
        "torch",
        "transformers",
        "numpy",
        "sentence-transformers",
    ],
    extras_require={
        'st': ['sentence-transformers'],
    },
    entry_points={
        'console_scripts': [
            'massive-serve=massive_serve.cli:cli',
        ],
    },
    author="Rulin Shao",
    author_email="rulins@cs.washington.edu",
    description="A package for massive serving",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RulinShao/massive-serve",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 
