"""Rename & Extract Method
With the information of the renaming methodB to methodC, we could deduce that methoD was extracted from methodB.
"""
class example_class:
    def methodC(self):
        print(0)
        if True:
            x = 1 + 2 + 3
        self.methodD()

    def methodD(self):
        print("Extract_Rename")