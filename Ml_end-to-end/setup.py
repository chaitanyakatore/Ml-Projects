from setuptools import find_packages,setup
#find_package is powerful tool for finding package
#this will find the __init__.py file and run that folder as seprate package
from typing import List
#importing list cause we ae using list

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
name='ML_end_to_end',
version='0.0.1',
author='Chaitanya',
author_email='chaitanyakatore@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)