class Editor:

    name:str
    vendor:str

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor


    def __str__(self):

        return self.name

editor_instance1=Editor("phycharm","jetbrains")

editor_instance2=Editor("intallis","jetbrains")

editor_instance3=Editor("vscode","microsoft")


print(editor_instance2)