me = ''
her = ''
gift = str(input('Mau ngasih bunga? y or n: '))
ulang = True
if gift == 'y':
    me = "MISI DIMULAI"
    if me != '':
        print("Kamu mengungkapkan perasaan ke dia dan ajak dia jadian")
        her = str(input("a. Dia Menerima dan mengajak Pacaran\nb. Dia Menolak dengan berbagai alasan\nJawab: "))
        if her == 'a':
            print("Yaudah Selesai Misi Gagal. Kalian Jadian Horeeee....")
        elif her == 'b':
            print('------------------------------------')
            print('Lanjut Misi')
            while ulang == True:
                print("Kamu tetap berkomunikasi dengan dia")
                me = "Kamu sok excited dan seolah olah tergila gila dengan dia dan selalu ngasih Semangat dengan dia"
                print(me)
                her = str(input("a. Dia feedback kamu sesuai dengan harapanmu\nb. Dia Cuek, Dry text dan seolah olah dia nggak mau kamu nggangu dia lagi\nJawab: "))
                if her == 'a':
                    print('------------------------------------')
                    print("Ulang Misi 3 sampai dia cuekkkk!!!!!")
                    ulang = True
                elif her == 'b':
                    ulang = False
                    print('------------------------------------')
                    her = 'Dia cuek dan merasa terganggu dengan kehadiranmu'
                    me = "Kamu akan merasakan sakit hati tapi perlahan perasaanmu ke dia akan hilang"
                    print(her)
                    print(me)
                    print('Tahan Rasa Sakitt dan Rasa Malu')
                    me = str(input("a. Masih Tahann kok aman\nb.Aku nyerah, aku gabisa, aku maluu, aku gengsii\nJawab: "))
                    if me == 'a':
                        me = str(input('Apakah perasaan Anda dengan Dia sudah hilang? y or n \nJawab: '))
                        if me == 'y':
                            print('------------------------------------')
                            print('Finally Kamu Sudah behasil move on')
                        elif me == 'n':
                            print('Ulangi Misi 3')
                            ulang = True
                    elif me == 'b':
                        print('------------------------------------')
                        print("DASAR LEMAHHHH!!!!")
else:
    print("Misi belum dimulai!!!")