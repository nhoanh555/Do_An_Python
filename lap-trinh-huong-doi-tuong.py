import os
import pickle

class NhanVien():
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong

    def __str__(self):
        nv = f'[Họ và tên: {self.hoten}; Tuổi: {self.tuoi}; Lương: {self.luong}]'
        return nv

    def __gt__(self, other):
        return (self.tuoi > other.tuoi)

    def __ge__(self, other):
        return (self.tuoi >= other.tuoi)

    def __lt__(self, other):
        return (self.tuoi < other.tuoi)

    def __le__(self, other):
        return (self.tuoi <= other.tuoi)

    def __eq__(self, other):
        return (self.tuoi == other.tuoi)

def add_nv():
    num = "Thêm"
    Nhanvien = []
    while num == "Thêm" :
        hoten, tuoi, luong = input("Nhập lần lượt họ tên, tuổi, lương  của nhân viên: ").split(", ")
        nv = NhanVien(hoten, tuoi, luong)
        Nhanvien.append(nv)
        num = input('Gõ "Thêm" nếu muốn thêm nhân viên: ')
    else:
        print("Kết thúc thêm nhân viên: ")
    return Nhanvien

def show_nhan_vien(nv):
    for item in nv:
        print(item)

def sap_xep_nhan_vien(nv):
    sap_xep = sorted(nv, reverse=True)

def save_nhan_vien(a, path: str, filename: str):
    try:
        with open(os.path.join(path, filename), 'ab') as f:
            print('Lưu danh sách nhân viên thành công.')
            return pickle.dump(a, f)
    except Exception as e:
        print(e)


def read(path: str, filename: str):
    try:
        with open(os.path.join(path, filename), 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(e)


def main():
    path = 'E:\\'
    filename = "k3.txt"
    a = add_nv()
    b = show_nhan_vien(a)
    c = sap_xep_nhan_vien(a)
    d = save_nhan_vien(a, path, filename)
    e = read(path, filename)


if __name__ == "__main__":
    main()