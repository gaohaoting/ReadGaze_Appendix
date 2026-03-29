# Expected session data layout (for `scripts/sanity_check.py`)

Place one folder per simulation session under:

```
scripts/Datasets/<session_id>/
```

Each session folder should contain (when available):

| Pattern | Role |
|---------|------|
| `*_attention_state_classification.csv` | Attention state segments |
| `*_realtime_aoi_timeseries.csv` | AOI features (optional for some checks) |
| `* - Actions.csv` | Clinical actions |
| `* - StageInfo.csv` | Stage boundaries (optional) |

**Privacy:** Only place **de-identified** exports approved for your IRB / institution. This appendix repository does not ship raw session data.
