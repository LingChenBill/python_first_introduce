Head First Python 练习代码  
1. 打包py模块  
python3 setup.py sdist  

setup.py:  
from distutils.core import setup  

setup(  
    name='lc_nester',  
    version='1.3.0',  
    py_modules=['lc_nester'],  
    author='lc-ling',  
    author_email='lingchen1316@163.com',  
    url='http://www.headfirstlabs.com',  
    description='A simple printer of nested lists'  
)  

setup中的名称与py_modules名称务必要保持一致  

2. 安装py模块  
sudo python3 setup.py install  

3. 引用自定义模块  
import lc_nester  
lc_nester.print_lol(man, out=man_file)  
