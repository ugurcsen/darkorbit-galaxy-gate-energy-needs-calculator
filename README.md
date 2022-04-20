# Darkorbit Galaxy Gate Energy Calculater
This program calculates needed energy to open a gate. Just adjust lines 12 and 13 in "main.py" for yourself.
```python
gate_size = 111  # Galaxy gate part count
gate_part_count_which_already_have = 0  # Galaxy gate parts you already have
```

## To Run
### Install
```commandline
pip install -r requirements.txt
```
Or
```commandline
pip3 install -r requirements.txt
```

### Run
```commandline
python main.py
```
Or
```commandline
python3 main.py
```
## Sum Statistics About Zeta Gate
```text
When ship nano body is not full
Multiplier: 2 / Avg GG Energy: 1678.75 / Min GG Energy: 1309 / Max GG Energy: 2202
Multiplier: 3 / Avg GG Energy: 1800.61 / Min GG Energy: 1315 / Max GG Energy: 2534
Multiplier: 4 / Avg GG Energy: 1878.79 / Min GG Energy: 1296 / Max GG Energy: 2640
Multiplier: 5 / Avg GG Energy: 1902.16 / Min GG Energy: 1303 / Max GG Energy: 3211
Multiplier: 6 / Avg GG Energy: 1906.75 / Min GG Energy: 1167 / Max GG Energy: 3248
==========================================
When ship nano body is full
Multiplier: 2 / Avg GG Energy: 1508.86 / Min GG Energy: 1026 / Max GG Energy: 2055
Multiplier: 3 / Avg GG Energy: 1659.44 / Min GG Energy: 1259 / Max GG Energy: 2434
Multiplier: 4 / Avg GG Energy: 1695.73 / Min GG Energy: 1051 / Max GG Energy: 2623
Multiplier: 5 / Avg GG Energy: 1696.8 / Min GG Energy: 1087 / Max GG Energy: 2820
Multiplier: 6 / Avg GG Energy: 1786.32 / Min GG Energy: 1084 / Max GG Energy: 2940
```
![Multiplier and GG Energy](Multiplier_and_GG_Energy(Zeta).png)
### Without full nano body
![Part Counts Every GG GEnergy Spends](Part_Counts_Every_GG_Energy_Spends(Zeta).png)
### With full nano body
![Multiplier and GG Energy With Full Nano](Multiplier_and_GG_Energy_With_Full_Nano(Zeta).png)