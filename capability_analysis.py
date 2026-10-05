"""Recalculate capability indices from the simulated inspection dataset."""
import pandas as pd
SPECS={"hole_diameter_mm":(9.90,10.10),"hole_spacing_mm":(39.85,40.15),"base_width_mm":(59.80,60.20),"verticality_mm":(None,0.20)}
df=pd.read_csv("../data/inspection_results.csv")
for col,(lsl,usl) in SPECS.items():
    mean=df[col].mean(); std=df[col].std(ddof=1)
    if lsl is None:
        index=(usl-mean)/(3*std)
        print(f"{col:22s} mean={mean:.3f} std={std:.3f} Cpu={index:.2f}")
    else:
        cp=(usl-lsl)/(6*std); cpk=min((usl-mean)/(3*std),(mean-lsl)/(3*std))
        print(f"{col:22s} mean={mean:.3f} std={std:.3f} Cp={cp:.2f} Cpk={cpk:.2f}")
