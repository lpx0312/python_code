
# shutil模块

## shutil.copy`复制文件`到具体文件或者目录

```python
import shutil    
# 复制文件到另一个文件，可以替代copyfile文件，但是如果文件夹不存在，会报错和copyfile一样。
shutil.copy('1.txt' ,r'demodir2\\3.txt')
# 复制文件到一个文件夹，
shutil.copy('1.mp4.lnk' ,r'demodir')
# 复制文件到文件夹的时候，如果这个文件夹不存在，则会直接将文件更名为你认为的文件夹名
shutil.copy('1.mp4.lnk' ,r'demodir2')
```


[参考1](https://www.cnblogs.com/xiangsikai/p/7787101.html)
[参考2](https://blog.csdn.net/weixin_39870664/article/details/112337164)

## shutil模块常见报错

## 1.报错 Permission denied
> shutil的copyfile函数复制文件常常容易出错，出现如PermissionError Permission denied 等错误，但导致该问题的原因，有时并非文件权限不足，而是src、dst不是符合要求的路径。

- 解决方案：

```python
import shutil
# 用`shutil.copy`复制文件或目录：
# 用copy复制文件：src是文件路径，dst可以是文件或目录
shutil.copy(r"J:\\src_path\\test.txt",r"J:\\dst_path\\") 

# 用shutil.copyfile`复制文件：
# 用copyfile复制文件: src和dst都必须为文件路径
shutil.copyfile(r"J:\\src_path\\test.txt",r"J:\\dst_path\\test.txt")

# 用`shutil.copytree`复制目录：
# 用copytree复制目录：src和dst都必须是目录
shutil.copytree("J:\\src_path\\","J:\\dst_path\\") 
```