from setuptools import setup

setup(
    name='pygqlmap',
    version='1.1.0',
    url='https://github.com/dapalex/py-graphql-mapper/',
    author='Alex Dap',
    author_email='shlisi2017@gmail.com',
    description='A python library to call GraphQL APIs without using hardcoded strings',
    include_package_data=True,
    packages=['pygqlmap', 'pygqlmap.src', 'codegen', 'codegen.src', 'codegen.src.templates'],
    data_files=[('', ['pygqlmap/config.ini'])],
    python_requires='>=3.10',
    classifiers=[
    "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)