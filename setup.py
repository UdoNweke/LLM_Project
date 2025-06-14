from setuptools import setup, find_packages


setup(
    name= 'LLM-Project',
    version='0.0.1',
    author='Udo Nweke',
    author_email='unwek001@gmail.com',
    packages=find_packages(),
    install_requires= ['pandas', 'pytoch', 'numpy']
)