"""Extract Method & Extract Var
methodB() was extracted from methodA(), including a nested extract var refactoring (ext_obj).
"""

class example:
        def methodA(self):
            self.methodB()
            
        def methodB(self):
            ext_obj = obj1.func1()
            obj = ext_obj.func2().func3()
            print("End")