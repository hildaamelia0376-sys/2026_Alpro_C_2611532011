umur_2011 = int(input("Input umur anda: "))
sim_2011 = input("Apakah Anda Sudah Punya SIM C: ")[0]

if umur_2011 >= 17 and sim_2011 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_2011 >= 17 and sim_2011 != 'y':
     print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2011 < 17 and sim_2011 =='y':
     print("Anda belum cukup umur punya SIM")
else:
     print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")