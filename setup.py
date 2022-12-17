from setuptools import find_packages, setup

setup(
    name='pygqlmap',
    version='0.3.0',    
    description='Python-GraphQL Mapper core',
    url='https://github.com/dapalex/py-graphql-mapper/pygqlmap',
    author='Alex Dap',
    author_email='shlisi2017@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=['pygqlmap', 'pygqlmap.src', 'codegen', 'codegen.src', 'codegen.src.templates'],
    # packages=find_packages(where=['pygqlmap', 'pygqlmap.src', 'codegen', 'codegen.src', 'codegen.src.templates'], exclude=['test.*']),
    python_requires='>=3.10.6',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)