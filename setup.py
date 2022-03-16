from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

setup(
    name="calc_kevin",
    version="0.0.1",
    author="Kevin Gonçalves",
    author_email="kevingtxz@gmail.com",
    description="Simple calculator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevingtxz/building_python_package",
    packages=find_packages(),
    # install_requires=requirements,
    # python_requires='>=3.9',
)