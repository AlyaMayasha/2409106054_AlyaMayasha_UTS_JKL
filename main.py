#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : main.py
Tujuan    : Mengintegrasikan seluruh modul pemeriksaan jaringan cabang.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""

from identitas import nim, nama, kode_cabang, buat_id_perangkat
from ssh_modul import cek_ssh
from snmp_modul import cek_snmp
from netconf_modul import buat_pesan_netconf
from telemetry_modul import telemetry, klasifikasi_telemetry


class LaporanCabang:
    """
    Menyimpan dan menampilkan laporan akhir pemeriksaan cabang.
    """

    def __init__(
        self,
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    ):
        self.hasil_ssh = hasil_ssh
        self.hasil_snmp = hasil_snmp
        self.pesan_netconf = pesan_netconf
        self.hasil_telemetry = hasil_telemetry

    def tampilkan_laporan(self):
        """
        Menampilkan satu laporan akhir gabungan.
        """

        print("\n" + "=" * 60)
        print("        LAPORAN AKHIR INTEGRASI JARINGAN")
        print("=" * 60)

        print(f"NIM          : {nim}")
        print(f"Nama         : {nama}")
        print(f"Kode Cabang  : {kode_cabang}")

        print("\n--- IDENTITAS PERANGKAT ---")
        print(f"Router       : {buat_id_perangkat('RTR', 1)}")
        print(f"Switch       : {buat_id_perangkat('SWT', 2)}")
        print(f"Firewall     : {buat_id_perangkat('FW', 3)}")

        print("\n--- HASIL SSH ---")
        print(self.hasil_ssh)

        print("\n--- HASIL SNMP ---")
        print(self.hasil_snmp)

        print("\n--- PESAN NETCONF ---")
        print(self.pesan_netconf)

        print("\n--- HASIL TELEMETRY ---")
        for data in self.hasil_telemetry:
            print(
                f"CPU Usage : {data['cpuUsage']}% "
                f"-> {data['status']}"
            )

        print("\n" + "=" * 60)
        print("          INTEGRASI SELESAI")
        print("=" * 60)


def main():
    """
    Menjalankan seluruh proses integrasi jaringan secara berurutan.
    """

    print("=" * 60)
    print("     INTEGRASI NETWORK CABANG")
    print("=" * 60)

    print("\n[1] Menjalankan pemeriksaan SSH...")
    hasil_ssh = cek_ssh()

    print("\n[2] Menjalankan pemeriksaan SNMP...")
    hasil_snmp = cek_snmp()

    print("\n[3] Membuat pesan NETCONF...")
    pesan_netconf = buat_pesan_netconf()

    print("\n[4] Mengklasifikasikan telemetry...")
    hasil_telemetry = klasifikasi_telemetry(telemetry)

    laporan = LaporanCabang(
        hasil_ssh,
        hasil_snmp,
        pesan_netconf,
        hasil_telemetry
    )

    laporan.tampilkan_laporan()


if __name__ == "__main__":
    main()