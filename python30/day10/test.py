

with open(r"E:\python_notebook\python\05.构造程序逻辑.md",'w') as f:
    for line in f:
        if "```Python" in line:
            pass
        f.write(line)