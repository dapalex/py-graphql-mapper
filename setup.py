from setuptools import setup

excluded = [
    './test/*'
]

setup(
    name='py-graphql-mapper',
    version='0.1.0',    
    description='Python-GraphQL Mapper',
    url='https://github.com/dapalex/py-graphql-mapper',
    author='Alex Dap',
    author_email='shlisi2017@gmail.com',
    license='MIT',
    packages=['pygraphqlmapper'],
    python_requires='>=3.10.6',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)