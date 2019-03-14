# RR-Verkefni5
**Í seinni hluta (Vigrar) lenti ég í smá vandræðum með að finna horn á milli vigra. Ég sé að þetta eru þvervigrar þannig hornið á að vera 90° en skv formúlunni til að reikna horn á milli vigra enda ég á því að deila í 0 með tölurnar sem ég hef.. kóðinn:**
```python
undir_sqrt = (1 ** 2 + 3 ** 2) * (-3 ** 2 + 1 ** 2)

hornV = math.degrees(math.acos((1 * -3) + (3 * 1) / math.sqrt(undir)))
```
**fæ alltaf errorinn: ValueError: math domain error vegna þessa.**
