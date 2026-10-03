#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : telemetry_modul.py
Tujuan    : Mengolah dan mengklasifikasikan data telemetry CPU.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""


telemetry = {
    "router": {
        "cpuUsage": [90, 75, 40]
    }
}


def klasifikasi_telemetry(data):
    """
    Mengklasifikasikan penggunaan CPU berdasarkan nilai telemetry.
    """

    hasil = []

    for nilai in data["router"]["cpuUsage"]:
        if nilai > 80:
            status = "KRITIS"
        elif nilai >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"

        hasil.append({
            "cpuUsage": nilai,
            "status": status
        })

    return hasil


if __name__ == "__main__":
    print("=== HASIL TELEMETRY ===")

    hasil_telemetry = klasifikasi_telemetry(telemetry)

    for data in hasil_telemetry:
        print(
            f"CPU Usage : {data['cpuUsage']}% "
            f"-> {data['status']}"
        )