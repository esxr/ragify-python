from setuptools import setup, find_packages

setup(
    name="ragify",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ragify=ragify.main:main',
        ],
    },
    install_requires=[
        # List your dependencies here
        'argparse'
    ],
    license='MIT',
    author='Pranav Dhoolia',
    author_email='pranav@dhoolia.com',
    description='Make a rag friendly document (or documents) from a folder, that can then be used to provide context to ChatGPT',
    url='https://github.com/esxr/ragify',
)