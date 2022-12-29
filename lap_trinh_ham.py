
import numpy as np

a = float(input("nhập số đầu a=  "))
b = float(input("nhập số cuối b=   "))
n = int(input("nhập số phần tử: "))
def sinh_vecto_so_thuc(a, b, n):
    x = np.linspace(start=a, stop=b, num=n, dtype=float)
    return x


def sap_xep(x):
    x1 = sorted(x, reverse=True)
    print("Danh sách giảm dần", x1)
    x2 = sorted(x, reverse=False)
    print("Danh sách tăng dần", x2)

def sap_xep_giam_dan(x):
    x1 = sorted(x, reverse=True)
    print("Danh sách giảm dần", x1)
def sap_xep_tang_dan(x):
    x2 = sorted(x, reverse=False)
    print("Danh sách tăng dần", x2)

def tim_kiem(x):
    n = float(input("Nhập phần tử muốn tìm kiếm: "))
    vitri=0
    for i in range(len(x)):
        if x[i] == n:
           vitri= i+1
    if vitri == 0:
        print("Không tìm thấy giá trị", n, "trong list")
    else:
        print("Các vị trí xuất hiện là", vitri)



def luu_list(z):
    a= input("Nhập đuôi định dạng: ")
    if a =="wb":
        f=open("E:\\k3.txt", "wb")
        f.writelines(str(z))
        f.close()
        f = open("E:\\k3.txt", "r")
        f.readlines()
        print("đã lưu dạng nhị phân")
    else:
        f=open("E:\\k3.txt", "w")
        f.writelines(str(z))
        f.close()
        f=open("E:\\k3.txt", "r")
        f.readlines()
        print("đã lưu")

def main():
    x = sinh_vecto_so_thuc(a, b, n)
    luu_list(x)
    sap_xep_giam_dan(x)
    luu_list(x)
    tim_kiem(x)

if __name__=="__main__":
    main()

