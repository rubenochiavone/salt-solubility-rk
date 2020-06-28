import time

class RedlichKisterEquation:

    calculateTag = "RedlichKisterEquation::calculate @"
    
    @staticmethod
    def calculate(params, xi, xj, verbose = False):
        if verbose:
            print RedlichKisterEquation.calculateTag
            print RedlichKisterEquation.calculateTag, "start"
            print RedlichKisterEquation.calculateTag
            start_time = time.time()
        
        fp = 0
        i = 0
        
        if verbose:
            print RedlichKisterEquation.calculateTag, "xi =", xi
            print RedlichKisterEquation.calculateTag, "xj =", xj
            print RedlichKisterEquation.calculateTag, "params =", params
            print RedlichKisterEquation.calculateTag, ""
        
        for param in params:
            if verbose:
                print RedlichKisterEquation.calculateTag, "fp =", fp
                print RedlichKisterEquation.calculateTag, "i =", i
                print RedlichKisterEquation.calculateTag, ""
                
                print RedlichKisterEquation.calculateTag, "param =", param
                print RedlichKisterEquation.calculateTag, "calc =", (pow((xi - xj), i))
            
            tmp = pow((xi - xj), i)
            tmp = param * tmp
            
            if verbose:
                print RedlichKisterEquation.calculateTag, "iteration result =", tmp
                print RedlichKisterEquation.calculateTag, ""
            
            fp += tmp
            i += 1
        
        if verbose:
            print RedlichKisterEquation.calculateTag, "result =",fp
            
            elapsed_time = time.time() - start_time
            
            print RedlichKisterEquation.calculateTag, "it took",elapsed_time,"s"
            print RedlichKisterEquation.calculateTag
            print RedlichKisterEquation.calculateTag, "end"
            print RedlichKisterEquation.calculateTag
        
        return fp
