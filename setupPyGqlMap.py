from setuptools import setup

excluded = [
    './test/*'
]

setup(
    name='pygqlmap',
    version='0.2.0',    
    description='Python-GraphQL Mapper',
    url='https://github.com/dapalex/py-graphql-mapper/pygqlmap',
    author='Alex Dap',
    author_email='shlisi2017@gmail.com',
    license='MIT',
    packages=['pygqlmap', 'pygqlmap.src'],
    python_requires='>=3.10.6',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)