# PCS supplementary upload

**Deadline:** 2026-04-09 AoE (with videos, alt-text, subtitles per [UIST 2026 CFP](https://uist.acm.org/2026/cfp/)).

## Suggested package

From the parent directory of `ReadGaze_Appendix`, the archive `ReadGaze_UIST2026_supplementary_appendix.zip` can be produced with the command below (already run once during setup; re-run after changes).

1. Create a zip of this appendix (exclude `.git` if present):

```bash
cd /Users/gaohaoting/ght/Course/Popov
zip -r ReadGaze_UIST2026_supplementary_appendix.zip ReadGaze_Appendix \
  -x "ReadGaze_Appendix/.git/*" \
  -x "*__pycache__/*" \
  -x "*.pyc"
```

2. In PCS (UIST 2026 → Papers), upload the zip in the **supplementary materials** area as allowed by the form.

3. In the paper PDF appendix, cite:
   - the **PCS-uploaded** supplementary archive (if required by venue wording), and/or
   - the **anonymous.4open.science** URL (see `ANONYMOUS_MIRROR.md`).

Confirm field labels on PCS for the 2026 submission year; if only one upload slot exists, prefer the zip and treat the anonymous link as optional redundancy.
