from setuptools import setup

with open('README.md', 'r') as f:
    read = f.read()


setup(
    name='tgraphics',
    version='1.0.1',
    description='An omni-platform terminal graphics module',
    long_description=read,
    long_description_content_type='text/markdown',
    author='Wizard',
    author_email='nlarsen23.student@gmail.com',
    url='https://repl.it/@GrandMoff100/tgraphics',
    packages=['tgraphics', 'tgraphics.readchar'],  
    install_requires=['colorama']
)