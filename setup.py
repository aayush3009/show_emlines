from setuptools import setup, find_packages

setup(
    name='show-emlines',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'your_script = your_script:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Python module for overplotting emission lines on plots',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/show-emlines',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)