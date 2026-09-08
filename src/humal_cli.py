#!/usr/bin/env python3
# ========================================================
# HUMAL SOVEREIGN SPREADSHEET CLI BRIDGE
# Native Runtime Integration for Huma, Osmo & Alge Engine
# ========================================================

import sys
import subprocess
import os

TARGET_PREFIX = "Huma629"

def eval_humal_cell_formula(formula, address, contract_file):
    print(f"[+] Evaluated Cell Formula: {formula}")
    print(f"[+] Routing to Sovereign Address: {address}")
    
    if not address.startswith(TARGET_PREFIX):
        print(f"[X] Execution Rejected: Address must start with {TARGET_PREFIX}")
        return

    if not os.path.exists(contract_file):
        print(f"[X] Target Contract Binary '{contract_file}' not found in workspace.")
        return

    # Trigger compiled C-bootstrap engine binary directly
    cmd = ["./hc_cpp_driver", address, contract_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print("\n--- HUMAL Grid Cell Output ---")
    print(result.stdout.strip())
    print("------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python humal_cli.py '<FORMULA>' <ADDRESS> <CONTRACT_HVM>")
        print("Example: python humal_cli.py '=HUMAL.STATE()' Huma629rfuykcdsexx HRC-800-MINT.hvm")
        sys.exit(1)

    formula_in = sys.argv[1]
    addr_in = sys.argv[2]
    contract_in = sys.argv[3]

    eval_humal_cell_formula(formula_in, addr_in, contract_in)
