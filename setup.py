from setuptools import setup, find_packages

setup(
    name="nodevectors",
    version="0.1.17",
    license='MIT',
    description='Fast network node embeddings',
    author='Matt Ranger',
    url='https://github.com/VHRanger/nodevectors/',
    packages=find_packages(),
    keywords=['graph', 'network', 'embedding', 'node2vec'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.txt', '*.rst']
    },
    install_requires=[
    'csrgraph==0.1.17',
    'gensim',
    'networkx',
    'numba',
    'numpy',
    'pandas',
    'scipy',
    'scikit-learn',
    'umap-learn'
    ],
)
