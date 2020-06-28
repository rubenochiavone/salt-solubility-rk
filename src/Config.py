from lmfit import Parameters
from lmfit import Parameter
import numpy as np

class Config:
    
    def __init__(self, config):
        
        defaultRkpVary = True
        defaultRkpMin = float("-inf")
        defaultRkpMax = float("inf")
        
        params = Parameters()
        
        params['d1'] = Parameter('d1', value=config['compounds'][0]['density'], vary=False)
        params['d2'] = Parameter('d2', value=config['compounds'][1]['density'], vary=False)
        params['d3'] = Parameter('d3', value=config['compounds'][2]['density'], vary=False)

        rkp12Conf = config['binary']['rkp']['x1-x2']
        
        params['rkp12_1'] = \
                Parameter('rkp12_1', \
                        value=rkp12Conf[0]['value'],
                        vary=(rkp12Conf[0]['vary'] if 'vary' in rkp12Conf[0] else defaultRkpVary), \
                        min=(rkp12Conf[0]['min'] if 'min' in rkp12Conf[0] else defaultRkpMin), \
                        max=(rkp12Conf[0]['max'] if 'max' in rkp12Conf[0] else defaultRkpMax))
        params['rkp12_2'] = \
                Parameter('rkp12_2', \
                        value=rkp12Conf[1]['value'],
                        vary=(rkp12Conf[1]['vary'] if 'vary' in rkp12Conf[1] else defaultRkpVary), \
                        min=(rkp12Conf[1]['min'] if 'min' in rkp12Conf[1] else defaultRkpMin), \
                        max=(rkp12Conf[1]['max'] if 'max' in rkp12Conf[1] else defaultRkpMax))
        params['rkp12_3'] = \
                Parameter('rkp12_3', \
                        value=rkp12Conf[2]['value'],
                        vary=(rkp12Conf[2]['vary'] if 'vary' in rkp12Conf[2] else defaultRkpVary), \
                        min=(rkp12Conf[2]['min'] if 'min' in rkp12Conf[2] else defaultRkpMin), \
                        max=(rkp12Conf[2]['max'] if 'max' in rkp12Conf[2] else defaultRkpMax))

        # data
        
        rawdata = np.array(config['data'])
        
        rawdataLength = len(rawdata)
        
        data = np.delete(rawdata, 4, 1)

        soly = np.delete(rawdata, [0, 1, 2, 3], 1).reshape((rawdataLength,))
        
        self.params = params
        self.data = data
        self.soly = soly
        
    def getParams(self):
        return self.params
    
    def getData(self):
        return self.data
    
    def getRho(self):
        return self.soly
