# 一读一写,同时操作

with open('text.txt','r') as f, open('b.txt','w') as g:
    g.write(f.read())