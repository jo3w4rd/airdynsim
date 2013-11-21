from pint import UnitRegistry
ureg = UnitRegistry()

theta_0 = 0 * ureg.degrees
phi_0 = 60 * ureg.degrees

l_ref = 13.6 * ureg.ft

rho = 0.0023769 * ureg.slug * ureg.ft ** -3
S_w = 185 * ureg.ft ** 2
b_w = 33 * ureg.ft
W = 2800 * ureg.lbf
V_0 = 180 * ureg.ft / ureg.sec
I_xx_b = 1000 * ureg.slug * ureg.ft ** 2
I_yy_b = 3000 * ureg.slug * ureg.ft ** 2
I_zz_b = 3500 * ureg.slug * ureg.ft ** 2
I_xy_b = 0 * ureg.slug * ureg.ft ** 2
I_xz_b = 30 * ureg.slug * ureg.ft ** 2
I_yz_b = 0 * ureg.slug * ureg.ft ** 2
h_x_b = 0 * ureg.slug * ureg.ft ** 2
h_y_b = 0 * ureg.slug * ureg.ft ** 2
h_z_b = 0 * ureg.slug * ureg.ft ** 2

C = {}
C['L0'] = 0.393
C['D0'] = 0.050
C['m0'] = 0.000
C['L,muhat'] = 0.000
C['D,muhat'] = 0.000
C['m,muhat'] = 0.000
C['L,alphahat'] = 1.600
C['D,alphahat'] = 0.000
C['m,alphahat'] = -4.350
C['L,M'] = 0.0
C['D,M'] = 0.0
C['m,M'] = 0.0
C['L,alpha'] = 4.400
C['D,alpha'] = 0.350
C['l,alpha'] = 0.0
C['m,alpha'] = -0.680
C['n,alpha'] = 0.0
C['Y,beta'] = -0.560
C['l,beta'] = -0.075
C['m,beta'] = 0.0
C['n,beta'] = 0.070
C['Y,pbar'] = 0.000
C['l,pbar'] = -0.410
C['n,pbar'] = -0.0575
C['L,qbar'] = 3.800
C['D,qbar'] = 0.000
C['m,qbar'] = -9.950
C['Y,rbar'] = 0.240
C['l,rbar'] = 0.105
C['n,rbar'] = -0.125

# print("rho =",rho)
# print("S_w =",S_w)
# print("b_w =",b_w)
# print("W =",W)
# print("V_0 =",V_0)
# print("I_xx_b =",I_xx_b)
# print("I_yy_b =",I_yy_b)
# print("I_zz_b =",I_zz_b)
# print("I_xy_b =",I_xy_b)
# print("I_xz_b =",I_xz_b)
# print("I_yz_b =",I_yz_b)
# print("h_x_b =",h_x_b)
# print("h_y_b =",h_y_b)
# print("h_z_b =",h_z_b)
# print("Constants:",C)
