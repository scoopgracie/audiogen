#!/usr/bin/env python

from setuptools import setup, find_packages

required_modules = []
extras_require = {
	'soundcard_playback': ['pyaudio'],
}

with open("README.md", "rb") as f:
	readme = f.read().decode('utf8')

setup(
	name="genaudio",
	version="0.1.2",
	description="Generator based tools for working with audio clips. Fork of AudioGen.",
	author="Samuel Sloniker",
	author_email="scoopgracie@gmail.com",
	url="https://github.com/scoopgracie/genaudio",

	packages=find_packages(exclude='tests'),
	install_requires=required_modules,
	extras_require=extras_require,

	tests_require=["nose"],
	test_suite="nose.collector",

	long_description=readme,
	classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Intended Audience :: Developers",
		"Topic :: Multimedia :: Sound/Audio",
	]
)

