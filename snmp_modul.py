#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : snmp_modul.py
Tujuan    : Melakukan pemeriksaan SNMP untuk mengambil sysName.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""

import asyncio

from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    get_cmd
)

from identitas import kode_cabang


HOST_SNMP = "127.0.0.1"
PORT_SNMP = 1161
COMMUNITY = f"comm_{kode_cabang}"
OID_SYSNAME = "1.3.6.1.2.1.1.5.0"


async def _ambil_sysname():
    """
    Mengambil nilai sysName menggunakan SNMPv2c.
    """
    snmp_engine = SnmpEngine()

    try:
        error_indication, error_status, error_index, var_binds = await get_cmd(
            snmp_engine,
            CommunityData(COMMUNITY, mpModel=1),
            await UdpTransportTarget.create(
                (HOST_SNMP, PORT_SNMP)
            ),
            ContextData(),
            ObjectType(ObjectIdentity(OID_SYSNAME))
        )

        if error_indication:
            print(f"Error SNMP: {error_indication}")
            return "SNMP gagal"

        if error_status:
            print(
                f"Error SNMP: {error_status.prettyPrint()} "
                f"pada index {error_index}"
            )
            return "SNMP gagal"

        for var_bind in var_binds:
            oid, nilai = var_bind
            print(f"OID      : {oid.prettyPrint()}")
            print(f"sysName  : {nilai.prettyPrint()}")

        return "SNMP berhasil"

    except Exception as e:
        print(f"Terjadi kesalahan SNMP: {e}")
        return "SNMP gagal"

    finally:
        snmp_engine.close_dispatcher()


def cek_snmp():
    """
    Menjalankan pemeriksaan SNMP secara sinkron.
    """
    print("\n=== HASIL PEMERIKSAAN SNMP ===")
    print(f"Community : {COMMUNITY}")
    print(f"Target    : {HOST_SNMP}:{PORT_SNMP}")
    print(f"OID       : {OID_SYSNAME}")

    return asyncio.run(_ambil_sysname())


if __name__ == "__main__":
    cek_snmp()