import setuptools
import versioneer

setuptools.setup(
    name='mkcert',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='build self signed certificates for development',
    url='https://lse.epita.fr',
    author='Gabriel Laskar',
    author_email='gabriel@lse.epita.fr',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=setuptools.find_packages(exclude=[
        'venv'
    ]),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'mkcert=mkcert.__init__:main',
        ],
    },
    zip_safe=False
)
