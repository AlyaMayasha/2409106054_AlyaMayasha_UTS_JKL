#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : ssh_modul.py
Tujuan    : Melakukan pemeriksaan akses SSH ke VM cabang.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""

import paramiko
from getpass import getpass
from identitas import kode_cabang


HOST_VM = "127.0.0.1"
PORT_SSH = 2222
USER_SSH = f"admin_{kode_cabang}"


def cek_ssh():
    """
    Menghubungkan program ke VM melalui SSH dan
    menjalankan perintah diagnostik.
    """
    password = getpass("Masukkan password SSH: ")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=HOST_VM,
            port=PORT_SSH,
            username=USER_SSH,
            password=password,
            timeout=10
        )

        print("\n=== HASIL PEMERIKSAAN SSH ===")

        perintah = ["whoami", "hostname"]

        for cmd in perintah:
            stdin, stdout, stderr = client.exec_command(cmd)

            hasil = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            print(f"\nPerintah : {cmd}")

            if hasil:
                print(f"Hasil    : {hasil}")

            if error:
                print(f"Error    : {error}")

        return "SSH berhasil terhubung"

    except Exception as e:
        print(f"\nKoneksi SSH gagal: {e}")
        return "SSH gagal terhubung"

    finally:
        client.close()

if __name__ == "__main__":
    cek_ssh()