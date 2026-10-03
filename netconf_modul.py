#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nama file : netconf_modul.py
Tujuan    : Membuat pesan NETCONF untuk konfigurasi VLAN.
Pembuat   : Alya Mayasha
NIM       : 2409106054
"""

import xml.etree.ElementTree as ET

from identitas import kode_cabang


def buat_pesan_netconf():
    """
    Membuat XML NETCONF untuk membuat VLAN berdasarkan kode cabang.
    """

    # MESSAGE LAYER
    rpc = ET.Element(
        "rpc",
        {
            "message-id": "101",
            "xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0"
        }
    )

    # OPERATION LAYER
    edit_config = ET.SubElement(rpc, "edit-config")

    target = ET.SubElement(edit_config, "target")
    ET.SubElement(target, "running")

    config = ET.SubElement(edit_config, "config")

    # CONTENT LAYER
        # CONTENT LAYER
    vlan = ET.SubElement(
        config,
        "vlan",
        {
            "xmlns": "urn:example:network",
            "operation": "create"
        }
    )

    vlan_id = ET.SubElement(vlan, "id")
    vlan_id.text = kode_cabang

    vlan_name = ET.SubElement(vlan, "name")
    vlan_name.text = f"VLAN-{kode_cabang}"

    # Memberikan indentasi agar XML lebih mudah dibaca
    ET.indent(rpc, space="    ")

    pesan_xml = ET.tostring(
        rpc,
        encoding="unicode"
    )

    print("\n=== PESAN NETCONF ===")
    print(pesan_xml)

    return pesan_xml
    

if __name__ == "__main__":
    buat_pesan_netconf()