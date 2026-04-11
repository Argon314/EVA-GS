from setuptools import setup, find_packages

setup(
    name="gdgs",
    version="1.0.0",
    author="Wentao Chen et al.",
    description="Geometry-Guided and Depth-Adaptive 3D Gaussian Splatting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Argon314/GD-GS",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
