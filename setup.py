"""from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

'''def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements'''
    
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__= "0.0.4"
REPO_NAME = "MLOps_MongoDB_Package"
PKG_Name = "databaseautomation"  # "MongoDB-Connect"
AUTHOR_USER_Name = "Iron-Ck"
AUTHOR_EMAIL = "chakrapaniwaghmode8@gmail.com"

'''
setup(
    name='DimondPricePrediction',
    version='0.0.4',
    author='Iron-Ck26',
    author_email='chakrapaniwaghmode8@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)
'''
setup(
    name=PKG_Name,
    version= __version__,
    author=AUTHOR_USER_Name,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_Name}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_Name}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    #install_requires=get_requirements(".\requirements_dev.txt")
)"""


from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.4"
REPO_NAME = "MLOps_MongoDB_Package"
PKG_NAME = "databaseautomation"
AUTHOR_USER_NAME = "Iron_Ck26"
AUTHOR_EMAIL = "chakrapaniwaghmode8@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
    
""" install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
"""