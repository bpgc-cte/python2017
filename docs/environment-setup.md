---
layout: page
title: RL Environment Setup
permalink: /environment-setup/
---

## Linux Installation

If you are using any Linux systems (like Ubuntu) or Mac, please open the terminal and type `python` to find out if it is already installed and which version is installed. Newer versions of Ubuntu have both Python2 and Python3 installed. Later versions of Mac, only have python2 installed, which can be sorted within the class.

As said, there is a very low chance of python not being there. If this is the case, follow these simple steps to install Python:

1. Open a Web browser and go to https://www.python.org/downloads/.

2. Follow the link to download zipped source code available for Unix/Linux.

3. Download and extract files.

4. Editing the Modules/Setup file if you want to customize some options.

5. run ./configure script

6. make

7. make install

This installs Python at standard location /usr/local/bin and its libraries at /usr/local/lib/pythonXX where XX is the version of Python.

## Windows Installation

1. Open a Web browser and type [Python Installer](https://www.python.org/ftp/python/3.6.1/python-3.6.1-amd64.exe)

2. Click the installer to install Python in the system. 

3. You will be able to run code in the Python IDLE terminal which comes along with the install. Python IDLE is a unix-like shell which also allows you to use bash commands, and hence it is preferable to use IDLE.

NOT NECESSARY: If by any chance you want to run from the command prompt, you will have to set the environment variables on Windows.

## Package Installer

EITHER pip or conda can be used for this purpose. pip comes natively with the python installation. Check if it is present by typing either `pip` or `conda` on the terminal. If you don't have one, please contact the instructor of the course.

For a package installation, type the following command in the terminal depending on the package installer you have

```
<package installer> install <package>
```
where <package installer> can be conda or pip. <package> will be the package you desire to install.

For example, in the next tutorial, you will have to install numpy which can be done by the following command:

```
pip install numpy
```

## Virtual Environments

We'll be covering this in the class, when the need arises, to avoid confusion.




