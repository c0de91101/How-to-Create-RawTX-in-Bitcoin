from io import BytesIO
from secash import *
from sighash import *

pk = PrivateKey.parse("L1kwoDnvDSMjgqaVV5qU8yoPiQmHoHygucT2Nf19Mx5gqUFMdrTj")
pk.address()
dust_tx = bytes.fromhex("e67a0550848b7932d7796aeea16ab0e48a5cfe81c4e8cca2c5b03e0416850114")
dust_index = 0
send_dust = "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF"
tx_in = TxIn(dust_tx, dust_index, b'', 0xffffffff)
tx_in._script_pubkey = Tx.get_address_data(pk.address())['script_pubkey']
tx_in._value = 30352330
tx_ins = [ tx_in ]
tx_outs = [
    TxOut(600, Tx.get_address_data(send_dust)['script_pubkey'].serialize()),
    TxOut(30351530, Tx.get_address_data(pk.address())['script_pubkey'].serialize())
]
tx = Tx(1, tx_ins, tx_outs, 0, testnet=True)
signature(tx, 0, pk)
tx.serialize().hex()

print("\n--------------------------------------\n")
print("My work Bitcoin Address:  " + pk.address())
print("Address for Getting Rich: " + send_dust)
print("\n--------------------------------------\n")
print(tx_in._script_pubkey)
print(tx_in.script_sig)
print("\n--------------------------------------\n")
print("RawTX for performing isomorphism:")
print(tx.serialize().hex())
print("\n--------------------------------------\n")

