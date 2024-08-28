import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="vmrunPacked",
    version="0.0.6",
    author="William",
    license="MIT",
    # author_email="ganeshanthavasigti1032000@gmail.com",
    description="Using vmrun to Control Virtual Machines. VmWare-vmrun execute actions use python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/THAVASIGTI/vmrunPacked.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
