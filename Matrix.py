#PROGRAM BY BRIAN RIAN REHAN
#CALCULATOR MATRIKS
import numpy as np
def menu():
    print('Menu:')
    print('1. Penjumlahan Matriks')
    print('2. Pengurangan Matriks')
    print('3. Perkalian Matriks')
    print('4. Determinant')
    print('5. Exit')
    print()
    pilihan = input('Pilih menu: ')

    if pilihan == '1':
        penjumlahan()
        tanya()
    elif pilihan == '2':
        pengurangan()
        tanya()
    elif pilihan == '3':
        perkalian()
        tanya()
    elif pilihan == '4':
        determinant()
        tanya()
    elif pilihan == '5':
        print("Anda Keluar")
        exit()
    else:
        print('Pilihan Menu Salah')
        menu()

def penjumlahan():
    print()
    print("Penjumlahan Matriks")
    menuordo()
    rumustambah()
def pengurangan():
    print()
    print("Pengurangan Matriks")
    menuordo()
    rumuskurang()
def perkalian():
    print()
    print("Perkalian Matriks")
    menuordo()
    rumuskali()
def determinant():
    print()
    print("Determinant Matriks")
    menuordo()
    rumusdeterminant()

def menuordo():
    print('a. Matriks ordo 2x2')
    print('b. Matriks ordo 3x3')
    print('c. Kembali')
    print()
    pilihan = input('Pilih menu: ')

    if pilihan in ['a', 'A']:
        print()
        print("================== MATRIKS ORDO 2X2 ==================")
    elif pilihan in ['b', 'B']:
        print()
        print("================== MATRIKS ORDO 3x3 ==================")
    elif pilihan in ['c', 'C']:
        print()
        menu()
    else:
        print('Pilihan Menu Salah')

def rumustambah():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)
    print()
    result = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    print("Hasil Penjumalahan Matriks A + B: ")
    for r in result:
        print(r)

def rumuskurang():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)

    print()
    result = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    print("Hasil Pengurangan Matriks A - B: ")
    for r in result:
        print(r)

def rumuskali():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)

    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)
    print()

    result = [[0 for i in range(x)] for i in range(x)]

    for i in range(x):
        for j in range(x):
            for k in range(x):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print("Hasil Pengurangan Matriks A * B: ")
    for r in result:
        print(r)

def rumusdeterminant():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(np.array(n))
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(np.array(n))
    print()

    result_a = np.linalg.det(matrix_a)
    result_b = np.linalg.det(matrix_b)

    print("Hasil Determinat Matriks A : ")
    print(result_a)
    print("Hasil Determinat Matriks B : ")
    print(result_b)

def tanya():
    pilih = input('Kembali ke menu? (y/t)')
    if pilih in ['y', 'Y', 'yes', 'Yes', 'YES', 'ya', 'YA','Ya']:
        menu()
    else:
        exit("Anda Keluar")

print("Code By Brian Rian Rehan")
print("================== SELAMAT DATANG DI KALKULATOR MATRIKS ==================")
menu()