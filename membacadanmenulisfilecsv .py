import csv

barang = 'data.csv'
f = open(barang, 'w')


def show_menu():
    print('======== MENU UTAMA ========')
    print('[1] Show Data')
    print('[2] Insert Data')
    print('[3] Edit Data')
    print('[4] Delete Data')
    print('[5] Exit')
    print('======================')

    selected_menu = input('Pilih Menu : ')

    if (selected_menu == '1'):
        show_data()
    elif (selected_menu == '2'):
        insert_data()
    elif (selected_menu == '3'):
        edit_data()
    elif (selected_menu == '4'):
        delete_data()
    elif (selected_menu == '5'):
        exit()
    else:
        print('Menu Tidak Tersedia.!!!')
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_data():
    data = []
    with open(barang, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.append(row)

    if (len(data) > 1):
        header = data.pop(0)
        print(f"{header[0]} \t {header[1]} \t\t {header[2]}")
        # wr = csv.writer(csv_file)
        # wr.writerow(('Nama','Kelas','Nilai'))
        print("-" * 34)
        for daftar in data:
            print(f'{daftar[0]} \t {daftar[1]} \t {daftar[2]}')
    else:
        print("DATA KOSONG")
    back_to_menu()


def insert_data():
    data = []
    with open(barang, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.append(row)
        while True:
            with open(barang, 'a') as csv_file:
                writer = csv.writer(csv_file)
                if (len(data) == 0):
                    writer.writerow(('NO', 'NAMA', 'TELEPON'))
                no = input("No urut: ")
                nama = input("Nama lengkap: ")
                telepon = input("No. Telepon: ")
                writer.writerow((no, nama, telepon))
                print("Berhasil disimpan!")
                break
    back_to_menu()


def edit_data():
    data = []

    with open(barang, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    if (len(data) is not 0):
        print("NO \t NAMA \t\t TELEPON")
        print("-" * 32)

        for daftar in data:
            print(f"{daftar['NO']} \t {daftar['NAMA']} \t {daftar['TELEPON']}")

        print("-----------------------")
        no = input("Pilih nomer Urut > ")
        nama = input("Nama Baru: ")
        harga = input("Harga Baru : ")

        indeks = 0
        for daftar in data:
            if (daftar['NO'] == no):
                data[indeks]['NAMA'] = nama
                data[indeks]['TELEPON'] = harga
            indeks = indeks + 1

        with open(barang, 'w') as csv_file:
            fieldnames = ['NO', 'NAMA', 'TELEPON']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in data:
                writer.writerow(
                    {'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})
    else:
        print('DATA KOSONG.!!\nMOHON DI ISI TERLEBIH DAHULU.!!!')
    back_to_menu()


def delete_data():
    data = []

    with open(barang, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    if (len(data) > 0):
        print("NO \t NAMA \t\t TELEPON")
        print("-" * 32)

        for daftar in data:
            print(f"{daftar['NO']} \t {daftar['NAMA']} \t {daftar['TELEPON']}")

        print("-----------------------")
        no = input("Hapus nomer> ")

        indeks = 0
        for daftar in data:
            if (daftar['NO'] == no):
                data.remove(data[indeks])
            indeks = indeks + 1

        with open(barang, mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA', 'TELEPON']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in data:
                writer.writerow(
                    {'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})

        print("Data sudah terhapus")
    else:
        print('DATA KOSONG.!!\nMOHON DI ISI TERLEBIH DAHULU.!!!')

    back_to_menu()


if __name__ == "__main__":
    while True:
        show_menu()
