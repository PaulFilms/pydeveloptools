'''
# Methods and functions for developing mathematical solutions

\n
`TASK:`

\n
`WARNINGS:`
'''
__version__ = '2023.11.15'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import pandas as pd
from math import log10
from dataclasses import dataclass
from typing import List, Tuple, Union
from enum import Enum

''' CUSTOM LIBRARIES '''
pass


''' FUNCTIONS
-------------------------------------------------------- '''

def MEAN(ACQUISITIONS: List[float] = []) -> Union[float, int]:
    '''
    Get the mean value of an acquisition list
    '''
    if len(ACQUISITIONS) == 0:
        return 0

    mean = sum(ACQUISITIONS) / len(ACQUISITIONS)
    return mean

def STDEV(ACQUISITIONS: List[float] = []) -> Union[float, int]:
    '''
    Deviation Standard
    
    `EXCEL FORMULAS:`
    - DESVEST.M (Spanish)
    - STDEV.S (English)
    '''
    if len(ACQUISITIONS) <= 1:
        return 0

    stdev: Union[float, int] = 0
    mean = MEAN(ACQUISITIONS)
    for value in ACQUISITIONS:
        stdev += (value - mean) ** 2

    return (stdev / (len(ACQUISITIONS) - 1)) ** 0.5

def UNC_TYP_A(ACQUISITIONS: List[float] = []) -> float:
    '''
    Uncertainty Type A
    '''
    # No puede calcular la incertidumbre si no hay uno o mas valores
    if len(ACQUISITIONS) <= 1:
        return 0

    return STDEV(ACQUISITIONS) / (len(ACQUISITIONS) ** 0.5)

def REGRESION_LINE(yValues: List[float], xValues: List[float]) -> Tuple[Union[float, int], Union[float, int]]:
    '''
    Get the regresion line of selected yValues and selected xValues
    - `RESULT:` tuple = (b1 <slope/gradient>, b0 <intercept/base>)
    - `EQUATION:` y = mx + b | y = b1*x + b0
    '''
    xMedia = MEAN(xValues)
    yMedia = MEAN(yValues)

    ## CHECK
    if len(xValues) != len(yValues):
        print("REGRESSION_LINE ERROR / yValues and xValues are not the same length")
        return 0.0, 0.0

    pos = 0
    div = 0
    for i in range(len(xValues)):
        pos += (xValues[i] - xMedia) * (yValues[i] - yMedia)
        div += (xValues[i] - xMedia) ** 2
    b1 = pos / div if div != 0 else 0
    b0 = yMedia - (b1 * xMedia)
    return b1, b0

def ISO_SCI(VALUE: float = 0, PRECISION: int = 1) -> str:
    '''
    Returns selected VALUE like Scientific notation
    '''
    # data = format(VALUE,'.1E')
    data = f"{VALUE:.{PRECISION}E}"
    return data

class UNC_TYP_B:
    def __init__(self) -> None:
        pass

    def FILTER(DATAFRAME: pd.DataFrame, VALUE1: float, VALUE2: float = None) -> pd.DataFrame:
        ## CHECK
        if type(DATAFRAME) == None:
            return None
        if len(DATAFRAME) < 1:
            return None
        if VALUE1 == None:
            return None

        ## DATAFRAME VALUES
        R1_MIN = DATAFRAME["RANGE1_MIN"].min()
        R1_MAX = DATAFRAME["RANGE1_MAX"].max()
        R2_MIN = DATAFRAME["RANGE2_MIN"].min()
        R2_MAX = DATAFRAME["RANGE2_MAX"].max()

        ## DEBUG
        # print("RANGES:\n", "R1_MIN:", R1_MIN, "R1_MAX:", R1_MAX, "R2_MIN:", R2_MIN, "R2_MAX:", R2_MAX)
        
        ## FILTERS
        df_filter = DATAFRAME

        ## 1 RANGE
        if VALUE1 > R1_MAX:
            return None
        if VALUE2 == None \
            and VALUE1 >= R1_MIN and VALUE1 <= R1_MAX:
            df_filter = DATAFRAME[
                (VALUE1 > DATAFRAME["RANGE1_MIN"]) &
                (VALUE1 <=  DATAFRAME["RANGE1_MAX"])
                ]
        
        ## 2 RANGES
        if VALUE1 and VALUE2 \
            and VALUE1 >= R1_MIN and VALUE1 <= R1_MAX \
            and VALUE2 >= R2_MIN and VALUE2 <= R2_MAX:
            df_filter = DATAFRAME[
                    (VALUE1 > DATAFRAME["RANGE1_MIN"]) & 
                    (VALUE1 <=  DATAFRAME["RANGE1_MAX"]) &
                    (VALUE2 > DATAFRAME["RANGE2_MIN"]) & 
                    (VALUE2 <=  DATAFRAME["RANGE2_MAX"])
                    ]
        
        ## DEBUG
        # print("DF FILTERED:\n", df_filter)
        
        if len(df_filter) != 1:
            return None
        
        return df_filter
    
    def EVALUATION(EVALUATION: str, FIELDS: dict) -> float:
        '''
        '''
        for field in FIELDS:
            locals()[field] = FIELDS[field]
        value: float = eval(EVALUATION)
        return value


''' CONVERTERS
-------------------------------------------------------- 
Hay que plantearse usar las librerias de python
[Pint (pypi.org)](https://pypi.org/project/Pint/)
[quantities](https://python-quantities.readthedocs.io/en/latest/user/tutorial.html)
'''

@dataclass
class UNIT:
    unit: str
    factor: int

class UNITS(Enum):
    mV = UNIT("V", 1e-3)
    V = UNIT("V", 1)
    kV = UNIT("V", 1e3)
    W = UNIT("W", 1)
    mW = UNIT("W", 1e-3)
    kW = UNIT("W", 1e3)
    @classmethod
    def to_base(cls, value: float, unit: UNIT) -> float:
        base = value * cls[unit].value.factor
        return base

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

    def swr_to_rloss(value: float) -> float:
        ''' 
        rloss (dBm) = 20*log((SWR-1)/(SWR+1))
        '''
        rloss: float = 20 * log10((value - 1) / (value + 1))
        return rloss

    def percent_to_db(value: float) -> float:
        '''
        dB = 10 * LOG10( 1 + % / 100 )
        '''
        dB = 10 * log10(1 + value / 100)
        return dB
    
    def db_to_percent(value: float) -> float:
        '''
        '''
        percent = 100 * (10 ** (value / 10) - 1)
        return percent
        
''' TEST
-------------------------------------------------------- '''