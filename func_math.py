'''
# Methods and functions for developing mathematical solutions

\n`TASK:`
\n`WARNINGS:`
'''
__version__ = '2023.11.02'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
from math import log10

''' CUSTOM LIBRARIES '''
pass


''' FUNCTIONS
-------------------------------------------------------- '''

def MEAN(ACQUISITIONS: list = []) -> float:
    '''
    Get the mean value of an acquisition list
    '''
    mean = 0
    if type(ACQUISITIONS) == list:
        if len(ACQUISITIONS) > 1:
            summation = 0
            for value in ACQUISITIONS:
                summation += value
            mean = summation / len(ACQUISITIONS)
        if len(ACQUISITIONS) == 1:
            mean = ACQUISITIONS[0]
    return mean

def STDEV(ACQUISITIONS: list = []) -> float:
    '''
    Deviation Standard
    
    EXCEL:
    - DESVEST.M (Spanish)
    - STDEV.S (English)
    '''
    stdev = 0
    if len(ACQUISITIONS) == 0 or len(ACQUISITIONS) == 1:
        stdev = 0
    else:
        mean = MEAN(ACQUISITIONS)
        for value in ACQUISITIONS:
            stdev += (value-mean)**2
        stdev = (stdev/(len(ACQUISITIONS)-1))**0.5
    return stdev

def UNC_TYP_A(ACQUISITIONS: list = []) -> float:
    '''
    Uncertainty Type A
    '''
    unc_typa = 0
    if type(ACQUISITIONS) == list:
        unc_typa = STDEV(ACQUISITIONS) / (len(ACQUISITIONS)**0.5)
    return unc_typa

def REGRESION_LINE(yValues: list, xValues: list) -> tuple:
    '''
    Get the regresion line of selected yValues and selected xValues
    \n - `RESULT:` tuple = (b1 <slope/gradient>, b0 <intercept/base>)
    \n - `EQUATION:` y = mx + b | y = b1*x + b0
    '''
    xMedia = MEAN(xValues)
    yMedia = MEAN(yValues)
    ## CHECK
    if len(xValues) != len(yValues):
        print("REGRESION_LINE ERROR / yValues and The xValues are not the same")
        return 0, 0
    pos = 0
    div = 0
    for i in range(len(xValues)):
        pos += (xValues[i]-xMedia) * (yValues[i]-yMedia)
        div += (xValues[i]-xMedia) ** 2
    b1 = pos / div
    b0 = yMedia - (b1 * xMedia)
    return b1, b0

def ISO_SCI(VALUE: float, PRECISION: int=1) -> str:
    '''
    Returns selected VALUE like Scientific notation
    '''
    # data = format(VALUE,'.1E')
    data = f"{VALUE:.{PRECISION}E}"
    return data


''' CONVERTERS
--------------------------------------------------------
'''

class CONVERTER():
    '''
    Converter tookit class
    '''
    def dbm_to_watts(value: float) -> float:
        '''
        P(W) = 1W * 10(P(dBm) / 10) / 1000
        '''
        watts = 10**((value-30)/10)
        return watts
    
    def watts_to_dbm(value: float) -> float:
        '''
        P(dBm) = 10 * log10( 1000 ⋅ P(W) / 1W)
        '''
        dbm = 10*log10(value*1000/1)
        return dbm

    def hertz_to_sec(value: float) -> float:
        '''
        s = 1 / Hz
        '''
        sec = 1/value
        return sec

    def sec_to_hertz(value: float) -> float:
        '''
        Hz = 1 / s
        '''
        hz = 1/value
        return hz
    
    def vpp_to_vrms(value: float) -> float:
        '''
        Vrms = Vpp * 1 / 2 * RAIZ(2)
        '''
        vrms = value * 1/(2*2**0.5)
        return vrms

    def vrms_to_vpp(value: float) -> float:
        ''' 
        Vpp = (2√2) * Vrms
        '''
        vpp = value * (2*2**0.5)
        return vpp

    def vrms_to_watts(value: float, impedance_ohm: float = 50) -> float:
        '''
        P (W) = ( V (rms) ^ 2 / Imp. (Ohm) )
        '''
        watts = (value**2/impedance_ohm)
        return watts
    
    def vrms_to_dbm(value: float, impedance_ohm: float = 50) -> float:
        '''
        P (dBm) = 10 * LOG( (P (Vrms) ^ 2 / R (Ohm)) * 1000 / 1mW)
        '''
        dbm = 10 * log10((value**2/impedance_ohm)*1000)
        return dbm

    def rloss_to_rho(value: float) -> float:
        '''
        rho (Γ) = 10 ** (R.Loss (dBm) / 20)
        '''
        rho: float = 10**(value/20)
        return rho

    def swr_to_rho(value: float) -> float:
        '''
        rho (Γ) = (SWR-1)/(SWR+1)
        '''
        if value < 1:
            return None
        else:
            rho: float = (value-1)/(value+1)
            return rho

''' TEST
--------------------------------------------------------
'''