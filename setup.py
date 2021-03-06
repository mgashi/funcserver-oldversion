from setuptools import setup, find_packages

long_description = ""
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='markdown_github')
except:
    print """
    README.md could not be converted to rst format.
    Make sure pypandoc is installed.
    """

version = '0.2.1'
setup(
    name="funcserver",
    version=version,
    description="Simple and opiniated way to build APIs in Python",
    long_description=long_description,
    keywords='funcserver',
    author='Prashanth Ellina',
    author_email="Use the github issues",
    url="https://github.com/mgashi/funcserver-oldversion.git",
    download_url="https://github.com/mgashi/funcserver-oldversion.git",
    license='MIT License',
    install_requires=[
        'gevent',
        'statsd',
        'requests',
        'tornado',
        'msgpack-python',
        'basescript',
    ],
    package_dir={'funcserver': 'funcserver'},
    packages=find_packages('.'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ]
)
