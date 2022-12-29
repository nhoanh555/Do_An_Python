from sympy import *

def giai_he_pt():
    x, y, z = symbols("x,y,z")
    pt1 = Eq(2*x-5*y+z+5,0)
    pt2 = Eq(4*x+2*y-2*z-2,0)
    pt3 = Eq(x+y-z,0)
    ans = solve((pt1,pt2,pt3),(x,y,z))
    print("Nghiệm =  ",ans)

def gioi_han():
    x = symbols("x")
    f = ((x**3-3*x**2)**(1/3)+sqrt(x**2-2*x))
    ans = limit(f, x, oo)
    print("Lim = ",ans)

def dao_ham():
    x = symbols("x")
    f = (2*x-1)/(x+2)
    ans = diff(f,x)
    print('Đạo hàm = ', ans)

def nguyen_ham():
    x = symbols("x")
    f = x/(x**2+1)
    ans = integrate(f,(x))
    print("Nguyên hàm = ", ans)


def tich_phan():
    x = symbols("x")
    f = (1-x*tan(x))/(x*x*cos(x)+x)
    ans = integrate(f,(x,pi,2*pi/3))
    print('Tích phân = ', ans)

def main():
    giai_he_pt()
    gioi_han()
    dao_ham()
    nguyen_ham()
    tich_phan()
if __name__=="__main__":
    main()