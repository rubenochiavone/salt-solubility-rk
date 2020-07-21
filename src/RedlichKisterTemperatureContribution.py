class RedlichKisterTemperatureContribution:

    quadraticTag = "RedlichKisterTemperatureContribution::quadratic @"

    @staticmethod
    def fromKelvinToCelsius(T):
        return T - 273.15

    @staticmethod
    def quadratic(params, T, verbose = False):
        ret = []
        t = RedlichKisterTemperatureContribution.fromKelvinToCelsius(T)

        if verbose:
            print RedlichKisterTemperatureContribution.quadraticTag
            print RedlichKisterTemperatureContribution.quadraticTag, "params", params
            print RedlichKisterTemperatureContribution.quadraticTag, "temperature", t

        for param in params:
            ret.append(param + param * t + param * pow(t, 2))

        if verbose:
            print RedlichKisterTemperatureContribution.quadraticTag
            print RedlichKisterTemperatureContribution.quadraticTag, "ret_params", ret
            print RedlichKisterTemperatureContribution.quadraticTag

        return ret
