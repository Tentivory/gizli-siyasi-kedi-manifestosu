#!/usr/bin/env python3
# Gizli Siyasi Kedi Manifestosu
# Bu kod çalışır. python kedi_manifesto.py ile çalıştırın.

import base64

def manifesto_uret():
    mesajlar = [
        "Kediler eşittir.",
        "Miyav herkese özgürlüktür.",
        "Kutu içinde demokrasidir."
    ]
    gizli_siyasi = base64.b64encode("demokrasi kediler için de geçerlidir".encode()).decode()
    print("Açık mesajlar:")
    for m in mesajlar:
        print(f"- {m}")
    print("\nGizli siyasi mesaj (base64):", gizli_siyasi)
    print("\u00c7özmek için: base64.decode")

if __name__ == "__main__":
    manifesto_uret()

# Damga: 🐱 İmza: Kayyum Grok | Tarih: 25 Ekim 2026 | İsim: Tentivory
# Ciddi olmasın ama ciddi olsun. Kayyum damgası.
