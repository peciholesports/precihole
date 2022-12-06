from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in precihole/__init__.py
from precihole import __version__ as version

setup(
	name="precihole",
	version=version,
	description="Precihole",
	author="Precihole",
	author_email="rehan@preciholesports.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
