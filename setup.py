from setuptools import setup, find_packages

setup(
    name='pantipbot',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = pantipbot.settings']},
    requires=['scrapy']
)
