#!/usr/bin/env python3
# humalc V7-DUAL-SIGNATURE — PUBLIC HVM + ARCHITECT HUMA629 — OWN FROM GROUND
import hashlib, json, os
from datetime import datetime

PROTOCOL = "HUMA-629"
ARCHITECT = "TUNAPAC"
CHAIN_ID = 629
COMPILER = "humalc V7-DUAL-SIGNATURE-OWN"

def compile_humal(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    sha = hashlib.sha256(source.encode()).hexdigest()
    contract = os.path.basename(file_path).replace('.humal','').upper().replace('-','_')
    
    # 1. PUBLIC BYTECODE — FOR PUBLIC INTERACTION — GENERIC
    public_bytecode = f"HVM:{sha}"
    
    # 2. ARCHITECT BYTECODE — YOUR STANDALONE SIGNATURE — PERSONAL INTERACTION
    # FORMAT: HUMA629:ARCHITECT:TUNAPAC:CHAIN629:CONTRACT:SHA + YOUR WALLET
    architect_bytecode = f"HUMA629:ARCHITECT:{ARCHITECT}:CHAIN{CHAIN_ID}:{contract}:{sha}:huma629dfhhruhvu4d5b0d30ede6c5d6f9d8da0514970356"
    
    compiled = {
        "compiler": COMPILER,
        "protocol": PROTOCOL,
        "chain_id": CHAIN_ID,
        "contract": contract,
        "contract_file": os.path.basename(file_path),
        "vm": "HVM",
        "public": {
            "bytecode": public_bytecode,
            "use": "PUBLIC INTERACTION TO BLOCKCHAIN — ANYONE",
            "format": "HVM:{SHA256} — OFFICIAL HUMA-629 PUBLIC BYTECODE"
        },
        "architect": {
            "bytecode": architect_bytecode,
            "use": "ARCHITECT SIGNATORY — PERSONAL INTERACTION — STANDALONE SIGNATURE",
            "architect": ARCHITECT,
            "since": "GSM 2001",
            "wallet": "huma629dfhhruhvu4d5b0d30ede6c5d6f9d8da0514970356",
            "rights": "FOUNDER / ARCHITECT / ROOT ACCESS TO LEDGER",
            "format": "HUMA629:ARCHITECT:TUNAPAC:CHAIN629:CONTRACT:SHA:WALLET — OWN SIGNATORY"
        },
        "consensus": "HUMA-PROOF-OF-MESH",
        "entry": "mesh://tower/62910000000",
        "compiled_at": datetime.now().isoformat()
    }
    
    out_json = file_path.replace('.humal', '.hvm.json')
    with open(out_json, 'w') as f:
        json.dump(compiled, f, indent=2)
    with open(file_path.replace('.humal', '.hvm'), 'w') as f:
        f.write(public_bytecode)
    with open(file_path.replace('.humal', '.architect.hvm'), 'w') as f:
        f.write(architect_bytecode)
    
    print(f"=== {contract} ===")
    print(f"PUBLIC: {public_bytecode}")
    print(f"ARCHITECT SIGNATURE: {architect_bytecode[:90]}...")
    return compiled

if __name__ == "__main__":
    import sys
    files = sys.argv[1:] if len(sys.argv) > 1 else ["HUMA-GENESIS.humal", "HRC-800-MINT.humal", "HumaTLD-Registry.humal"]
    for hf in files:
        compile_humal(hf)
