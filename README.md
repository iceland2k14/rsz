# rsz
Retrieve ECDSA signature R,S,Z values from blockchain rawtx or txid.

## Info
The script parse the data of rawtx to fetch all the inputs in the transaction and reconstructs the unsigned message for each of them
 to find the Z value. The result is given as R,S,Z,Pubkey for each of the inputs present in the rawtx data. _**[No Internet required]**_  
 
 If txid is given, instead of rawtx then blockchain API is used to fetch the details of rawtx and then R,S,Z calculation starts. _**[Internet required]**_

## Requirements
The required library (3 files) can be obtained from the location https://github.com/iceland2k14/secp256k1

## Math
![image](https://github.com/iceland2k14/rsz/assets/75991805/b90164c8-a361-428b-b3d5-a6044782c59e)
![image](https://github.com/iceland2k14/rsz/assets/75991805/a3dd36ed-3eb4-4a7b-ae3e-44968e34631f)

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

```
(base) C:\anaconda3\RSZ>python LLL_nonce_leakage.py

 Fixed Nonce bits = 128           Minimum Signature Required = 4
###############################################################################
secret: 0x9d14389997898f331015c1f46bb28ffbb574c6e37402fdd05358e03ad9611965
Pubkey: 04d6780000bdd44454c3a0513d65516bb47731b54d0626afda253bd641c122d6f1409745ada09c15222a152254741ec97680bcf7830d30148fed9895764184583a
###############################################################################
 Original Matrix
[[115792089237316195423570985008687907852837564279074904382605163141518161494337, 0, 0, 0, 0], [0, 115792089237316195423570985008687907852837564279074904382605163141518161494337, 0, 0, 0], [0, 0, 115792089237316195423570985008687907852837564279074904382605163141518161494337, 0, 0], [2704712979180801089897423316502096358961597747425164856645825082599503205602156236430776861701200242349195741606503875277981511606703744158117768566559390, -1857241215722559024423997543389879602650264412685938620878792624512536758647213656842819550751876424006877972706909349619866179451984138124466657004071339, -1973682741832018872074663893840565948710799473755744023963335995397415174886136903996078778601290697209893544143262055883247824705384055255627610913812378, 2.938735877055719e-39, 0], [2710090695930584846741498909839758251750492265204201508278284612292485880435119427198367605498446550504611363773646155972127157530405183612824494188818528, -243719807005826150359943150907034916358627482812220649168731561348763165408020985747298379976195924368435100928076689047582488441166922575519748834319241, 6134559479302934944491346664781433391781160257760662094450457465077896873812049086933143386609308200693897009259387607488078956238609666933956199978264324, 0, 340282366920938463463374607431768211456]]


 Reduced Matrix
[[0, 0, 0, 340282366920938463463374607431768211454, 0], [221548368694275960735406751924867063718, 168248519672241120578049771713566173612, 111437557204557226128492447196717086719, -131488577661790770128258542755403100163, 340282366920938463463374607431768211456], [-110866878338400714741580264952861112380863454493112, -674471435454751395201235921717937039573990358835813, -567136596487316351716411480759299433655820183825899, 36191809542616262600958257102862797849, 591395655759045324209646646083280716633975484841984], [406087834009519652014339382908102333183583164862302, 1421021702348559674961890239734268361331465592977107, -2254996253951439726031072416745956528124037410003885, 19369188238169184807391134978546112400, -228520865396664941072764243965595141517151863570432], [-2813891988999695949792633951969273201834161206047301, 1937442488289894704631519036222641267725029667335512, -627699882982756569565187630223032886596264586706623, 148007411327126909376334920545795499321, 1079664204117872291051731126727009923839199421661184]]
---------------------------------------------------------------------------
 found private key = 0x9d14389997898f331015c1f46bb28ffbb574c6e37402fdd05358e03ad9611965
---------------------------------------------------------------------------
```
```
(base) C:\anaconda3\RSZ>python rsz_rdiff_scan.py -a 1BFhrfTTZP3Nw4BNy4eX4KFLsn9ZeijcMm

Starting Program...
------------------------------------------------------------------------------------------------------------------------
Total: 50 Input/Output Transactions in the Address: 1BFhrfTTZP3Nw4BNy4eX4KFLsn9ZeijcMm
UnSupported Tx Input. Presence of Witness Data
Skipped the Tx [d52c7663adf9702529553e8eeb18f7f2bedad1e4ef23a7f9a187660d7dcb3522]........
UnSupported Tx Input. Presence of Witness Data
Skipped the Tx [d52c7663adf9702529553e8eeb18f7f2bedad1e4ef23a7f9a187660d7dcb3522]........
======================================================================
[Input Index #: 0] [txid: 3b7a0a5f4c55718f6374fd718d65e2b4a8fde8fd1158b4f9f659872899530939]
     R: 384327a0bdd1aeb3c33c4a49d7ab617657e24e979085b672017f25f9761722fd
     S: 6e2685a20bc95af56a8aa6035a7e29f1cedbb8cd56403011e9281687ed32ee58
     Z: 938a0a4d20b7e40bbd587f752f85dd1ed7f84b790965ca0407b5367d33f17f6b
PubKey: 04dbd0c61532279cf72981c3584fc32216e0127699635c2789f549e0730c059b81ae133016a69c21e23f1859a95f06d52b7bf149a8f2fe4e8535c8a829b449c5ff
======================================================================
[Input Index #: 0] [txid: d3d0e560d414c86d88ea645a9dbee583d21a95ae2e57f10679b043ef33a0d23c]
     R: 4e1e91433ad7b1f6e52466f4d233c94b7023937f6345ab1179a2b268a22d52cc
     S: 270941b896645a8ecd98253dae59c580766ec10391d5742f830874dbabc4acbe
     Z: 74419baf355e3e14c1e44b9bcd8e7a7a2cdd1488c72fbfd3ab30523a448dd70d
PubKey: 04dbd0c61532279cf72981c3584fc32216e0127699635c2789f549e0730c059b81ae133016a69c21e23f1859a95f06d52b7bf149a8f2fe4e8535c8a829b449c5ff
======================================================================
[Input Index #: 0] [txid: 3e9cd088d9f5462709b0e407c3e938518b348feaad879bc24fb88ff9b0ade941]
     R: 755f50abc717f8a5c7bf41d4ae2f6c702afcb3dccf127ae02dbcf5c64c55f3ea
     S: 45e92613115448bd6710c313ff2c6af2924dafee49d7a57915003ee218f5b73a
     Z: ee540220c3570af1cf96f9d9660b3e1dc593cae60e68a284363badce26830d64
PubKey: 04dbd0c61532279cf72981c3584fc32216e0127699635c2789f549e0730c059b81ae133016a69c21e23f1859a95f06d52b7bf149a8f2fe4e8535c8a829b449c5ff
======================================================================
.....
.....
.....
.....
========  RSZ to PubKey Validation [SUCCESS]  ========
========  RSZ to PubKey Validation [SUCCESS]  ========
========  RSZ to PubKey Validation [SUCCESS]  ========
========  RSZ to PubKey Validation [SUCCESS]  ========
========  RSZ to PubKey Validation [SUCCESS]  ========
========  RSZ to PubKey Validation [SUCCESS]  ========
.....
.....
Duplicate R Found. Congrats!. (87, 95, '0400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
.....
.....
======================================================================
------------------------------------------------------------------------------------------------------------------------
[i=103] [j=105] [R Diff = fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141]
Privatekey FOUND: 0xc477f9f65c22cce20657faa5b2d1d8122336f851a508a1ed04e479c34985bf96
======================================================================
------------------------------------------------------------------------------------------------------------------------
Program Finished ...
```
