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
Multiplier: 2 / Avg GG Energy: 2082.85 / Min GG Energy: 1590 / Max GG Energy: 2697
Multiplier: 3 / Avg GG Energy: 2508.7 / Min GG Energy: 1569 / Max GG Energy: 3177
Multiplier: 4 / Avg GG Energy: 2714.37 / Min GG Energy: 1847 / Max GG Energy: 3437
Multiplier: 5 / Avg GG Energy: 2871.39 / Min GG Energy: 2036 / Max GG Energy: 4050
Multiplier: 6 / Avg GG Energy: 3050.22 / Min GG Energy: 2126 / Max GG Energy: 4879
==========================================
When ship nano body is full
Multiplier: 2 / Avg GG Energy: 1872.14 / Min GG Energy: 1205 / Max GG Energy: 2379
Multiplier: 3 / Avg GG Energy: 2254.34 / Min GG Energy: 1601 / Max GG Energy: 2908
Multiplier: 4 / Avg GG Energy: 2464.25 / Min GG Energy: 1675 / Max GG Energy: 3557
Multiplier: 5 / Avg GG Energy: 2599.38 / Min GG Energy: 1755 / Max GG Energy: 3284
Multiplier: 6 / Avg GG Energy: 2873.3 / Min GG Energy: 1969 / Max GG Energy: 4102
```
![Multiplier and GG Energy](Multiplier_and_GG_Energy(Zeta).png)
![Part Counts Every GG GEnergy Spends](Part_Counts_Every_GG_Energy_Spends(Zeta).png)
![Multiplier and GG Energy With Full Nano](Multiplier_and_GG_Energy_With_Full_Nano(Zeta).png)