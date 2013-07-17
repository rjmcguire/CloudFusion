'''
Created on 30.08.2011

@author: joe
'''
import setuptools
setuptools.setup(
    name = "CloudFusion",
    packages = setuptools.find_packages(),
    include_package_data = True,
    install_requires = ['mechanize', 'nose', 'oauth', 'poster', 'simplejson'],
    version = "1.0.0",
    description = "Filesystem interface to cloud storage services",
    author = "Johannes Mueller",
    author_email = "johannes.mueller1@mail.inf.tu-dresden.de",
    url = "https://github.com/joe42/CloudFusion",
    download_url = "https://github.com/joe42/CloudFusion/archive/master.zip",
    keywords = ["encoding", "i18n", "xml"],
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Operating System :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Filesystems",
        ],
    long_description = """\
CloudFusion lets you access your Dropbox or Sugarsync files from Linux like any file on your desktop.
"""
)
