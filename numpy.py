import numpy as np

def cau1 (m,n):
    x=np.random.randint(-10,10,n)
    A=np.random.randint(-10,10,(m,n))
    print(x*A)

def cau2(m,n):
    A=np.random.randint(-10,10,(m,n))
    B=np.random.randint(-10,10,(m,n))
    print('Kết quả phép nhân ma trận A và B:\n', A@B)
    print("Kết quả phép nhân ma trận chuyển vị của ma trận A và ma trận B:\n", (A.T)@B)

m = float(input("nhạp n: "))
n = float(input("nhap m: "))
def main():
    cau1(m,n)
    cau2(m,n)
if __name__=="__main__":
    main()