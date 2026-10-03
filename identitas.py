#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : identitas.py
Tujuan    : Menyimpan identitas cabang dan membuat ID perangkat.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""

# Identitas mahasiswa
nim = "2409106054"
nama = "Alya Mayasha"
kode_cabang = "054"


def buat_id_perangkat(jenis, nomor):
    """
    Membuat ID perangkat berdasarkan jenis perangkat,
    kode cabang, dan nomor perangkat.
    """
    return f"{jenis.upper()}-{kode_cabang}-{nomor:02d}"

