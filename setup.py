from setuptools import find_packages, setup

setup(
    name='pygqlmap',
    version='0.3.0',    
    description='Python-GraphQL Mapper core',
    url='https://github.com/dapalex/py-graphql-mapper/',
    author='Alex Dap',
    author_email='shlisi2017@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=['pygqlmap', 'pygqlmap.src', 'codegen', 'codegen.src', 'codegen.src.templates'],
    data_files=[('', ['pygqlmap/config.ini'])],
    python_requires='>=3.10.6',
    entry_points ={
            'console_scripts': [
                'pygqlcodegen = codegen.__main__:main'
            ]
        },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)