# RLHF Pairwise Evaluation

Pairwise ranking and QMOS / NMOS-style scoring for LLM outputs — the same workflow used in RLHF annotation and model evaluation.

## What it does

- Compares Response A vs Response B for the same prompt
- Records preference, scores naturalness (NMOS) and overall quality (QMOS) 1-5
- Calculates win-rate per model and inter-rater agreement

## Run it

```bash
pip install -r requirements.txt
python evaluate.py
```

Output: `evaluation_results.csv` with win-rates and agreement.

## Files

- `evaluate.py` — pairwise scorer + agreement calculation
- `sample_pairs.json` — synthetic prompt / response pairs
- `rubric.md` — QMOS / NMOS definitions

## Rubric — QMOS / NMOS (1-5)

5 = Excellent, 4 = Good, 3 = Fair, 2 = Poor, 1 = Bad. Score naturalness, prosody / fluency, semantic accuracy, and overall quality separately, then give a preference: A wins, B wins, or tie.

## Skills demonstrated

RLHF, pairwise comparison, QMOS/NMOS, inter-rater reliability, Python / Pandas.
