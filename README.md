# rsz
Retrieve ECDSA signature R,S,Z values from blockchain rawtx or txid.

## Info
The script parse the data of rawtx to fetch all the inputs in the transaction and reconstructs the unsigned message for each of them
 to find the Z value. The result is given as R,S,Z,Pubkey for each of the inputs present in the rawtx data. _**[No Internet required]**_  
 
 If txid is given, instead of rawtx then blockchain API is used to fetch the details of rawtx and then R,S,Z calculation starts. _**[Internet required]**_

## Requirements
The required library (3 files) can be obtained from the location https://github.com/iceland2k14/secp256k1

## Usage: Python 3
```python getz_input.py```

## Run
```
usage: getz_input.py [-h] [-txid TXID] [-rawtx RAWTX]

This tool helps to get ECDSA Signature r,s,z values from Bitcoin rawtx or txid

optional arguments:
  -h, --help    show this help message and exit
  -txid TXID    txid of the transaction. Use Internet to fetch rawtx from
                given txid
  -rawtx RAWTX  Raw Transaction on the blockchain. No internet required

Enjoy the program! :) Tips BTC: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
```

```
(base) C:\anaconda3\RSZ>python getz_input.py -txid 82e5e1689ee396c8416b94c86aed9f4fe793a0fa2fa729df4a8312a287bc2d5e

Starting Program...
======================================================================
[Input Index #: 0]
     R: 009bf436ce1f12979ff47b4671f16b06a71e74269005c19178384e9d267e50bbe9
     S: 00c7eabd8cf796a78d8a7032f99105cdcb1ae75cd8b518ed4efe14247fb00c9622
     Z: 9f4503ab6cae01b9fc124e40de9f3ec3cb7a794129aa3a5c2dfec3809f04c354
PubKey: 04e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6c
======================================================================
[Input Index #: 1]
     R: 0094b12a2dd0f59b3b4b84e6db0eb4ba4460696a4f3abf5cc6e241bbdb08163b45
     S: 07eaf632f320b5d9d58f1e8d186ccebabea93bad4a6a282a3c472393fe756bfb
     Z: 94bbf25ba5b93ba78ee017eff80c986ee4e87804bee5770fae5b486f05608d95
PubKey: 04e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6c
```

```
(base) C:\anaconda3\RSZ>python getz_input.py -rawtx 01000000028370ef64eb83519fd14f9d74826059b4ce00eae33b5473629486076c5b3bf215000000008c4930460221009bf436ce1f12979ff47b4671f16b06a71e74269005c19178384e9d267e50bbe9022100c7eabd8cf796a78d8a7032f99105cdcb1ae75cd8b518ed4efe14247fb00c9622014104e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6cffffffffb0385cd9a933545628469aa1b7c151b85cc4a087760a300e855af079eacd25c5000000008b48304502210094b12a2dd0f59b3b4b84e6db0eb4ba4460696a4f3abf5cc6e241bbdb08163b45022007eaf632f320b5d9d58f1e8d186ccebabea93bad4a6a282a3c472393fe756bfb014104e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6cffffffff01404b4c00000000001976a91402d8103ac969fe0b92ba04ca8007e729684031b088ac00000000

Starting Program...
======================================================================
[Input Index #: 0]
     R: 009bf436ce1f12979ff47b4671f16b06a71e74269005c19178384e9d267e50bbe9
     S: 00c7eabd8cf796a78d8a7032f99105cdcb1ae75cd8b518ed4efe14247fb00c9622
     Z: 9f4503ab6cae01b9fc124e40de9f3ec3cb7a794129aa3a5c2dfec3809f04c354
PubKey: 04e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6c
======================================================================
[Input Index #: 1]
     R: 0094b12a2dd0f59b3b4b84e6db0eb4ba4460696a4f3abf5cc6e241bbdb08163b45
     S: 07eaf632f320b5d9d58f1e8d186ccebabea93bad4a6a282a3c472393fe756bfb
     Z: 94bbf25ba5b93ba78ee017eff80c986ee4e87804bee5770fae5b486f05608d95
PubKey: 04e3896e6cabfa05a332368443877d826efc7ace23019bd5c2bc7497f3711f009e873b1fcc03222f118a6ff696efa9ec9bb3678447aae159491c75468dcc245a6c

```

```
(base) C:\anaconda3\RSZ>python rsz_solve.py

========================================================================
  True Privatekey =  0x6a0d91cdd5cf761fe02de7b56bbe4ae1ed55b7a4faca12db65f02ee8e5b61602
========================================================================
k1: 0x3c977dbdb3deeefcffef9fda93cdfeacfb83a8a9a6439585bb37f052a16f314
r1: 0x2c0a015c8976d170edc918480ee981e75c513dfea11086ddc89baadfd9038a29
s1: 0xf06ac541347ff93f4269579d9ca71cf7ad32859b83596721798b370ec9100749
z1: 0x37c7de2760ab892174e6680d621e72eb60b4b7cde365164ee00fee7f3a3e83dd
  Tx1 Correct: rsz Validated the Pubkey
========================================================================
k2: 0x85e0356d099499f90c926619fdde95b4f60c0a4644daf6f3b597d89dbb27f31c
r2: 0xc2e6e5acb70205a4f8a2639568e2bfd855111ecf334304193d70e967c1e3d7d8
s2: 0xfe7b7da891dfbb1d33a94b810d45caa7e8768b0e3b1bd750da76f08fcd00d814
z2: 0x2a3a32220a7376ce84cbbd96673a89d534f94b0d887fac8e532ec764aab9e86a
  Tx2 Correct: rsz Validated the Pubkey
========================================================================
  Starting to solve rsz using difference of k between 2 Tx
  Extracted Privatekey = 0x6a0d91cdd5cf761fe02de7b56bbe4ae1ed55b7a4faca12db65f02ee8e5b61602
====   Nonce Found using 2 rsz diff   = 0x3c977dbdb3deeefcffef9fda93cdfeacfb83a8a9a6439585bb37f052a16f314

```