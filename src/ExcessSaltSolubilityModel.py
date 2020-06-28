import math
from RedlichKisterEquation import RedlichKisterEquation

class ExcessSaltSolubilityModel:

    modelTag = "ExcessSaltSolubilityModel::model @"
    residualTag = "ExcessSaltSolubilityModel::residual @"
    
    @staticmethod
    def model(params, data, verbose = False):
        z1 = data[:, 0] / 100  # compound #1 composition data
        z2 = data[:, 1] / 100  # compound #2 composition data
        T = data[:, 3]   # temperature data
        
        if verbose:
            print ExcessSaltSolubilityModel.modelTag, "z1", z1
            print ExcessSaltSolubilityModel.modelTag, "z2", z2
        
        s1 = params['d1'].value # compound #1 density
        s2 = params['d2'].value # compound #2 density
        
        rkp12 = []
        rkp12.append(params['rkp12_1'].value) # #1 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_2'].value) # #2 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_3'].value) # #3 redlich-kister parameter for 1-2 compound composition
        
        vid1 = z1 * math.log(s1)
        vid2 = z2 * math.log(s2)
        
        vid = vid1 + vid2

        vs12 = []
        vexcess = []
        
        for i in range(len(data)):
            vs12.append(z1[i] * z2[i] * RedlichKisterEquation.calculate(rkp12, z1[i], z2[i]))
            
            vexcess.append(vs12[i])
        
        if verbose:
            print ExcessSaltSolubilityModel.modelTag, "ideal volume", vid
            print ExcessSaltSolubilityModel.modelTag, "12 contribution", vs12
            print ExcessSaltSolubilityModel.modelTag, "excess volume", vexcess
        
        soly = []

        for i in range(len(data)):
            v = math.exp(math.log(vid[i]) + vexcess[i])
            soly.append(v)
        
        if verbose:
            print ExcessSaltSolubilityModel.modelTag, "soly calculated", soly
            
        return soly
    
    @staticmethod
    def residual(params, data, soly, verbose = False):
        soly_calc = ExcessSaltSolubilityModel.model(params, data, verbose)
        
        if verbose:
            print ExcessSaltSolubilityModel.residualTag, "soly_calc", soly_calc
            print ExcessSaltSolubilityModel.residualTag, "soly", soly
            print ExcessSaltSolubilityModel.residualTag, "residual", (soly - soly_calc)
        
        return soly - soly_calc

