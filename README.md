# Mechanical Bracket Design and Process Validation

Design-focused mechanical engineering portfolio study covering requirements, a conceptual L-bracket design, engineering drawing, inspection planning, and process capability analysis.

> **Project status:** Coursework-based academic portfolio project applying concepts from MCE 516 Production Planning and Control at Cleveland State University. The bracket case study was developed after completing the course; the inspection dataset is simulated and no physical parts were manufactured or tested.

![Bracket concept](images/bracket_concept.png)

## Engineering objective

Develop a lightweight aluminum mounting bracket and define a repeatable dimensional validation plan before physical prototyping. The project uses five simulated builds with five samples per build to demonstrate how design requirements connect to GD&T controls and Cp/Cpk/Cpu analysis.

## Design summary

| Item | Requirement |
|---|---|
| Material | Aluminum 6061-T6 |
| Base width | 60.00 ± 0.20 mm |
| Thickness | 5.00 ± 0.10 mm |
| Mounting holes | 2X base + 2X upright, Ø10.00 ± 0.10 mm |
| Base depth | 50.00 ± 0.20 mm |
| Upright height | 45.00 ± 0.20 mm |
| Horizontal spacing | 40.00 ± 0.15 mm |
| Upright control | Verticality 0.20 mm to datum A |

## Workflow

1. Defined the mounting and material requirements.
2. Created an engineering drawing and conceptual exchange geometry.
3. Developed a 25-sample simulated inspection dataset across five builds.
4. Calculated mean, sample standard deviation, Cp/Cpk for two-sided dimensions, and Cpu for upper-only verticality.
5. Identified base width as the characteristic requiring additional process control.

## Repository contents

- `cad/bracket_front_view.dxf` - editable 2D exchange geometry in millimeters.
- `cad/concept_bracket.stl` - simplified solid concept; holes are documented in the drawing but are not cut in this STL.
- `drawings/bracket_engineering_drawing.pdf` - controlled design definition for the study.
- `data/inspection_results.csv` - deterministic simulated inspection dataset.
- `analysis/capability_analysis.py` - reproducible Cp/Cpk/Cpu calculation.
- `analysis/capability_summary.csv` and `capability_plot.png` - outputs.
- `reports/design_validation_report.pdf` - final technical summary.

## Run the analysis

```bash
cd analysis
python capability_analysis.py
```

Requires Python 3 with `pandas`.

## Result and next step

Hole diameter and hole spacing meet the simulated Cpk target of 1.33, and verticality meets the one-sided Cpu target. Base width does not yet meet the target, creating a realistic improvement task: review bend allowance, improve fixture repeatability, then repeat first-article inspection. Before claiming real validation, the bracket must be manufactured, inspected with calibrated equipment, and load-tested.

## Explanation

“I developed this coursework-based portfolio project to apply concepts from MCE 516 Production Planning and Control. I defined the bracket requirements and drawing, built a simulated five-build inspection plan, calculated capability, and used the result to identify base-width variation as the main manufacturing risk. I would replace the simulated data with measured first-article results during physical prototyping.”

## License

Provided for portfolio review and learning. Do not use the geometry as a production release.
