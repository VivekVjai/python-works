class Grandparent:

    def m(self):

        print("grand parent class m method")

class Parent:

    def m(self):

        print("parent class m method")

#error name ambiguity error [java]  ===> interface

class Child(Grandparent,Parent):  #multipile level inheritance

    def m3(self):

        print("child class m3 method")

child_instance1=Child()

child_instance1.m3()

child_instance1.m()
