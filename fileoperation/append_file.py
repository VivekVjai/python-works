

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\frameworks.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:

    f.write(fw+"\n")

f.close()