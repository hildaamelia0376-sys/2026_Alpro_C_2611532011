umur_2011 = int(input("Input Umur Anda: "))
sim_2011 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_2011 >= 17 and sim_2011 =='y':
    print("Anda Sudah Dewasa dan boleh bawa motor")

if umur_2011 >= 17 and sim_2011 != "y":
    print("Anda sudah dewasa tetapi belum boleh bawa motor")

if umur_2011 < 17 and sim_2011 =="y":
    print("Anda belum cukup umur punya SIM")

if umur_2011 < 17 and sim_2011 != "y":
    print("Anda belum cukup umur bawa motor")