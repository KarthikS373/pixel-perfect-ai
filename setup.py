import setuptools
from pathlib import Path

web_files = Path("pixel-perfect-ai/app/build/").glob("**/*")
web_files = [str(it).replace("pixel_perfect_ai/", "") for it in web_files]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def load_requirements():
    requirements_file_name = "./config/requirements.txt"
    requires = []
    with open(requirements_file_name) as f:
        for line in f:
            if line:
                requires.append(line.strip())
    return requires


setuptools.setup(
    name="pixel-perfect-ai",
    version="0.0.1",
    author="NetSurfers",
    author_email="lit2021012@iiitl.ac.in",
    description="Image inpainting tool using AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KarthikS373/pixel-perfect-ai",
    packages=setuptools.find_packages("./"),
    package_data={"pixel_perfect_ai": web_files},
    install_requires=load_requirements(),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["pixel-perfect-ai=pixel_perfect_ai:entry_point"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
