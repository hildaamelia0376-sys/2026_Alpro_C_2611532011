# Input dari user
total_belanja_2011 = float(input("Masukkan Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2011 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_2011 = input_member_2011 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2011 = input("Apakah Kode Promo Valid (y/t): ").strip().lower()
kode_promo_valid_2011 = input_promo_2011 in ["y", "ya"]

total_diskon_persen_2011 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus
if total_belanja_2011 > 1000000:
    total_diskon_persen_2011 += 10 # Diskon belanja besar

if is_member_2011:
    total_diskon_persen_2011 += 5 # Diskon belanja member

if kode_promo_valid_2011:
    total_diskon_persen_2011 += 15 # Diskon belanja voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2011 = total_belanja_2011 * (total_diskon_persen_2011 / 100)
total_bayar_2011 = total_belanja_2011 - nominal_diskon_2011

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2011}% (Rp {nominal_diskon_2011:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_2011:,.0f}")

print(f"Total Diskon yang Anda Dapatkan: {total_diskon_persen_2011}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid