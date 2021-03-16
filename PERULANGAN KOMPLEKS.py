'''
Edwin Mahendra/71200541

Princess akan membuat program untuk menghitung total uang yang ia sisihkan untuk ditabung setiap bulannya.
Program akan meminta input berapa minggu ia akan menabung dan berapa bulan ia akan berhenti menabung.
Bantulah ia untuk membuat program tersebut!

Input:
minggu
bulan

Proses dan Output:
total=0
if minggu>=1 and minggu<=4:
    if bulan>0:
        for i in range(1,bulan+1):
            bulan=0
            print('Bulan ke-%d'%i)
            for j in range(1,minggu+1):
                x=int(input(tabungan minggu ke%d %i))
                bulan=bulan+x
            print(total tabungan selama bulan ini,bulan)
            total=total+bulan
            print(total keseluruhan tabungan anda adalah, total)
            print()
    else:
        print(program eror)
else:
    print(program eror)

penjelasan:
bulan ke-1
minggu ke-1 rp4000
minggu ke-2 rp5000
total mingguan rp9000
total keseluruhannya 9000

bulan ke-2
minggu ke-1 rp5000
minggu ke-2 rp5000
total mingguan 10000
total keseluruhan 19000
'''
minggu=int(input('mau berapa minggu akan menabung:'))
bulan=int(input('sampai berapa bulan:'))

total=0
if minggu>=1 and minggu<=4:
    if bulan>0:
        for i in range(1,bulan+1):
            bulan=0
            print('Bulan ke-%d'%i)
            for j in range(1,minggu+1):
                x=int(input('Tabungan minggu ke-%d: Rp'%j))
                bulan=bulan+x
            print('total tabungan anda selama bulan ini adalah Rp',bulan)
            total=total+bulan
            print('total keseluruhan tabungan anda adalah Rp',total)
            print()
    else:
        print('program error')
else:
    print('program error')