# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:05:27 2019

@author: Patrick
"""

def getKickSpinClassBalance():
    return (33756, 12067, 273581, 427)

def getLstmKickSpinRaw():
    result = list()
    error = list()
    
    # Configuration 0
    # F-Measure:  [ 0.83286597  0.85723991  0.8531093   0.90282521]  +/-  [ 0.05384703  0.07324613  0.03484044  0.03981307]
    result.append((0.83286597, 0.85723991, 0.8531093, 0.90282521))
    error.append((0.05384703, 0.07324613, 0.03484044, 0.03981307))
    
    # Configuration 1
    # F-Measure:  [ 0.83045586  0.83611203  0.84248791  0.89286276]  +/-  [ 0.05170501  0.07962568  0.01905156  0.04166383]
    result.append((0.83045586, 0.83611203, 0.84248791, 0.89286276))
    error.append((0.05170501, 0.07962568, 0.01905156, 0.04166383))
    
    # Configuration 8
    # F-Measure:  [ 0.84884834  0.85183826  0.86069984  0.9076974 ]  +/-  [ 0.03895471  0.06690016  0.03171143  0.04371748]
    result.append((0.84884834, 0.85183826, 0.86069984, 0.9076974))
    error.append((0.03895471, 0.06690016, 0.03171143, 0.04371748))
    
    # Configuration 9
    # F-Measure:  [ 0.81524778  0.84098606  0.84491118  0.88736788]  +/-  [ 0.07015954  0.06389435  0.04565123  0.03712772]
    result.append((0.81524778, 0.84098606, 0.84491118, 0.88736788))
    error.append((0.07015954, 0.06389435, 0.04565123, 0.03712772))
    
    # Configuration 16
    # F-Measure:  [ 0.83098647  0.8350629   0.84041042  0.90054893]  +/-  [ 0.06882835  0.0745835   0.04797875  0.04101129]
    result.append((0.83098647, 0.8350629, 0.84041042, 0.90054893))
    error.append((0.06882835, 0.0745835, 0.04797875, 0.04101129))
    
    # Configuration 17
    # F-Measure:  [ 0.83069464  0.82699267  0.82956064  0.89078002]  +/-  [ 0.05800342  0.08282779  0.03937129  0.045395  ]
    result.append((0.83069464, 0.82699267, 0.82956064, 0.89078002))
    error.append((0.05800342, 0.08282779, 0.03937129, 0.045395))
    
    return (result, error)
    
def getBaselineKickSpinRaw():
    result = list()
    error = list()
    
    # Configuration 18
    # F-Measure:  [ 0.45931826  0.50826539  0.55070048  0.58713135]  +/-  [ 0.09584294  0.10167097  0.06560972  0.08042713]
    result.append((0.45931826, 0.50826539, 0.55070048, 0.58713135))
    error.append((0.09584294, 0.10167097, 0.06560972, 0.08042713))
    
    # Configruation 19
    # F-Measure:  [ 0.57935824  0.48485244  0.58650123  0.54739124]  +/-  [ 0.07906763  0.16366361  0.07685484  0.08576922]
    result.append((0.57935824, 0.48485244, 0.58650123, 0.54739124))
    error.append((0.07906763, 0.16366361, 0.07685484, 0.08576922))
    
    # Configuration 20
    # F-Measure:  [ 0.43424766  0.52442323  0.58162601  0.46860223]  +/-  [ 0.17433801  0.0931926   0.08202901  0.16750125]
    result.append((0.43424766, 0.52442323, 0.58162601, 0.46860223))
    error.append(( 0.17433801, 0.0931926, 0.08202901, 0.16750125))
    
    # TB
    # F-Measure:  [0.6347264  0.44365826  0.85828954  0.019806763] +/- [0.0478587       0.07442568      0.045351796     0.042142663]
    result.append((0.6347264, 0.44365826, 0.85828954, 0.019806763))
    error.append((0.0478587, 0.07442568, 0.045351796, 0.042142663))
    
    # K ordered
    # F-Measure:  [0.8692585		0.5216949		0.9616143		0.14372626] +/- [0.020905448     0.1351215       0.005771178     0.21999544]
    result.append((0.8692585, 0.5216949, 0.9616143, 0.14372626))
    error.append((0.020905448, 0.1351215, 0.005771178, 0.21999544))
    
    # K unordered
    # F-Measure:  [ 0.682829		0.328519		0.9132589		0.055109072	] +/- [0.07628402      0.12359815      0.011852683     0.14555155]
    result.append(( 0.682829, 0.328519, 0.9132589, 0.055109072))
    error.append((0.07628402, 0.12359815, 0.011852683, 0.14555155))
    
    # K ordered r
    # F-Measure:  [0.7013639		0.30200663		0.90636766		0] +/- [0.056755662     0.08951596      0.040069852     0]
    result.append((0.7013639, 0.30200663, 0.90636766, 0))
    error.append((0.056755662, 0.08951596, 0.040069852, 0))
    
    return (result, error)
