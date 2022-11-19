from setuptools import setup,find_packages
from typing import List


#declaring variable for setup function
PROJECT_NAME ="housing-predictor"
VERSION = "0.0.3"
AUTHOR="ABDUL AHAD"
DESCRIPTION = "This is the First machine Learning project"
REQUIREMENT_FILE_NAME ="requirements.txt"

def get_requirements_list()->List[str] :
    """
    Description : This function is going to return list of requirement mention 
    in requirements.txt 

    return This function is going to return a list which contain name of 
    libraries mention in requirements.txt 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(

    name=PROJECT_NAME,
    version =VERSION,
    author=AUTHOR,
    description= DESCRIPTION,
    packages =  find_packages(),
    install_requires = get_requirements_list()
    )

if __name__=="__main__":
    print(get_requirements_list())