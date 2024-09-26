from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='processamento-imagens-matheus',
    version='0.1',
    author='Matheus Pizani',
    description='Image processing package using Skimage',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mpizanii/package_imagens_python',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
