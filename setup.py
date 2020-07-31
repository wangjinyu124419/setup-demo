
from setuptools import setup


setup(
    name = "setuptoolsdemo",
    version = "1.0.0",
    author = "wangjinyur",
    author_email = "wangjinyuxxx@gmail.com",
    description = ("An demonstration of setuptools-demo."),
    url = "http://www.baidu.com",
    packages=['src'],
    entry_points={
        'console_scripts': ['setup-func=src.appdemo:hello_setuptools'],
    }
)