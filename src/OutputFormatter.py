from ExcessSaltSolubilityModel import ExcessSaltSolubilityModel

class OutputFormatter:

    @staticmethod
    def printHeader():
        
        print ""
        print "  @@@@@@@@@@@@@@@@@@@@@@@@@@"
        print "  @@@                    @@@"
        print "  @@@   excess-salt-solubility-rk-fit   @@@"
        print "  @@@                    @@@"
        print "  @@@@@@@@@@@@@@@@@@@@@@@@@@"
        print ""
        print "Performs curve fitting of ternary Redlich-Kister equation"
        print "Authors: Osvaldo Chiavone Filho (osvaldo@nupeg.ufrn.br) and Ruben O. Chiavone"
        print "UFRN - 2016"
        print ""

    @staticmethod
    def printConfig(config):
        
        #TODO: 
        
        print "[[Configurations]]"
        
        print "    x1 =", config['compounds'][0]['name']
        print "    x2 =", config['compounds'][1]['name']
        print "    x3 =", config['compounds'][2]['name']
        print ""
        print "    x1.density =", config['compounds'][0]['density']
        print "    x2.density =", config['compounds'][1]['density']
        print "    x3.density =", config['compounds'][2]['density']
        
    
    @staticmethod
    def printExperimentaldata(data, soly):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        T = data[:, 3]  # temperature data
        
        print "[[Experimental Data]]"
        
        print "      z1", "      ", "z2", "       ", \
                "T", "     ", " soly"
        
        for i in range(len(data)):
            print "    {0:1.5f}   {1:1.5f}   {2:3.2f}   {3:1.5f}" \
                    .format(z1[i], z2[i], T[i], soly[i])
    
    @staticmethod
    def printResults(out, data, soly):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        T = data[:, 3]  # temperature data
        
        soly_calc = ExcessSaltSolubilityModel.model(out.params, data)

        print "[[Results]]"
        print "      z1", "      ", "z2", "       ", \
                "T", "     ", " soly", "  ", "soly_clc", "    ", "err"

        errsum = 0

        mxdev = 0

        for i in range(len(data)):
            err = abs(soly[i] - soly_calc[i])
            
            if err > mxdev:
                mxdev = err
            
            errsum += err
            
            print "    {0:1.5f}   {1:1.5f}   {2:3.2f}   {3:1.5f}   {4:.5f}   {5:.7f}" \
                    .format(z1[i], z2[i], T[i], soly[i], soly_calc[i], err)

        # mean deviation
        mndev = errsum / len(data)


        print "    "

        print "    Mean deviation: {0:5.9f}".format(mndev)
        print "    Max deviation:  {0:5.9f}".format(mxdev)

