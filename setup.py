from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file_path:str) -> List[str]:
  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readlines() # ["pandas\n", "numpy\n"]
    requirements = [req.replace("\n","") for req in requirements]
  
  if HYPEN_E_DOT in requirements:
    requirements.remove(HYPEN_E_DOT)
  print("======================================")
  print("requirements ------------------>", requirements)
  print("============================")
  
  return requirements

setup(
  name = "Fault_Dectection",
  version = "1.0.0",
  author = "quamrul",
  install_requirements=('requirements.txt'),
  packages = find_packages()
)