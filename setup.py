from click.decorators import option
from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as README:
        long_description = README.read()
    return long_description


def require():
    with open('requirements.txt', 'r') as rq:
        rq_files = rq.read().split('\n')
    return rq_files


setup(
    name="WLM",
    version="0.0.1",
    description="WLM - A all in one tool that will help you in your work productivity, which works both windows and linux. (open source).",
    long_description_content_type="text/markdown",
    long_description=readme(),
    url="https://github.com/almas-ali/WLM",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="wlm, windows, linux, cli",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Topic :: Security :: Cryptography',
        'Natural Language :: English',
        'Environment :: Console',
    ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=require(),
    entry_pointers='''
        [console_scripts]
        wlm=wlm.src.wlm_cli:main
    '''
)
