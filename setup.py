from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='genthumbs',
    version='0.1',
    description='CLI tool to generate thumbnails',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
    keywords='thumbnail image photo',
    long_description=readme(),
    url='http://github.com/timatooth/genthumbs',
    author='Tim Sullivan',
    author_email='tsullivan@timatooth.com',
    license='MIT',
    packages=['genthumbs'],
    install_requires=[
        'pillow'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': ['genthumbs=genthumbs.genthumbs:main']
    },
    include_package_data=True,
    zip_safe=True)
