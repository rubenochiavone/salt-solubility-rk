import math
from RedlichKisterEquation import RedlichKisterEquation
from RedlichKisterTemperatureContribution import RedlichKisterTemperatureContribution

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
            print ExcessSaltSolubilityModel.modelTag, "T", T
        
        s1 = params['s1'].value # compound #1 solubility
        s2 = params['s2'].value # compound #2 solubility
        
        rkp12 = []
        rkp12.append(params['rkp12_1'].value) # #1 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_2'].value) # #2 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_3'].value) # #3 redlich-kister parameter for 1-2 compound composition
        
        solyid1 = z1 * math.log(s1)
        solyid2 = z2 * math.log(s2)
        
        solyid = solyid1 + solyid2

        soly12 = []
        solyexcess = []
        
        for i in range(len(data)):
            soly12.append(z1[i] * z2[i] * RedlichKisterEquation.calculate(\
                RedlichKisterTemperatureContribution.quadratic(rkp12, T[i]), z1[i], z2[i]))
            
            solyexcess.append(soly12[i])
        
        if verbose:
            print ExcessSaltSolubilityModel.modelTag, "ideal solubility", solyid
            print ExcessSaltSolubilityModel.modelTag, "12 contribution", soly12
            print ExcessSaltSolubilityModel.modelTag, "excess solubility", solyexcess
        
        soly = []

        for i in range(len(data)):
            v = math.exp(math.log(solyid[i]) + solyexcess[i])
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

