# Appendix

## Formative Study Materials

### Additional participant details

**Formative interviews (n = 7).** As in the main text: seven semi-structured sessions (45–60 minutes each) with ACLS instructors (minimum five years of experience training cardiac arrest teams); **five female, two male**; **mean clinical experience = 24 years** (aggregate); specialties **paramedic (1), nursing (4), emergency medicine (1), family medicine (1)**.

**Expert walkthrough (n = 1).** One **emergency medicine physician** instructor reviewed recorded **VR cardiac-arrest team training** footage using a **baseline debriefing tool** with **video replay and timeline navigation**, then contrasted interpretation with an ** early debriefing system prototype with Attention entropy curves** (see protocol below). No individual identifiers are reported.


| Cohort                               | n   | Role / context (high level)                                         |
| ------------------------------------ | --- | ------------------------------------------------------------------- |
| Semi-structured formative interviews | 7   | ACLS clinical instructors (see specialty split above)               |
| Expert walkthrough                   | 1   | Emergency medicine; simulation video review + prototype walkthrough |


### Formative interview and walkthrough prompts

**Semi-structured interview guide (reconstructed from study aims and thematic synthesis).** The sessions were not limited to a fixed script; facilitators probed the following topics in order, with follow-ups:

- **Background and debriefing practice:** how the instructor currently prepares for debriefing after simulation, and how video or logs are used.
- **Locating teachable moments:** how candidate moments are noticed when reviewing recordings (what counts as “salient,” time pressure, team vs.\ individual focus).
- **Gaze and attention evidence:** whether and how gaze or attention-related cues could support (or complicate) interpretation of learner reasoning; expectations of **proxy** vs.\ **ground-truth** evidence.
- **Representations and burden:** reactions to **dense gaze displays** (e.g., heatmaps, scanpaths, curves), preferences for **episodes**, **summaries**, or **semantic abstractions** tied to task context.
- **From observation to debriefing talk:** friction moving from “something happened here” to **clinically grounded** and **dialogue-ready** prompts; need for scaffolds vs.\ improvisation.
- **Closing:** desired dashboard/debriefing features and concerns (privacy, group debrief, cognitive load).

**Expert walkthrough protocol (four steps, from the structured expert review session).**

1. **Baseline review:** Expert-team simulation video with **free pause** for discussion; identify **teachable moments** relevant to debriefing.
2. **Prototype introduction:** Early debriefing system prototype (video panel, timeline, **entropy / self-loop** signals, **event** markers).
3. **Re-review with prototype:** Same expert-team footage with ReadGaze overlays; discuss whether curves support **attention** and **teamwork** interpretation.
4. **Comparative segment:** Short **novice-team** clip to contrast **communication, delegation, and attention** patterns and whether ReadGaze supports **differential** interpretation.

### Additional representative quotations supporting F1–F3

Labels **P1–P10** are **not** the formal user study’s participant IDs; they index **anonymous excerpts** from the formative design discussions (see provenance above).

**F1 — Gaze as useful proxy, not ground truth (interpretive caution).**

- **P1:** “[Gaze] is meant to be a proxy for where your focus is… It’s just important… to have it **with a grain of salt** because maybe you were just staring off into space cuz your brain was so busy but you’re just looking at one thing because it’s easier than… continuing to track around the room.”
- **P2:** “A lot of times… you can see that from their pupil tracking, but they **don’t integrate** that information… there was a clear change, but… I don’t know what that is.”
- **P3:** “The gaze is a **good proxy for decision-making**… it could be represented as a heat map… or… as… areas of interest or the sequence… you can really unfold where I look first, second, third.”

**F2 — Raw or dense gaze displays impose interpretive burden; need for semantics and simpler presentation.**

- **P4:** “Things like gaze, cognitive load, and positions… need **a little bit more interpretation**. I think you need to **do something with that data** before it’s useful.”
- **P5:** “It’s **less so**… tracking… throughout the course… it’s very much so… **episodes**… when you’re looking at the monitor, how does your eyes… go through that monitor?… I think those **episodes**… would be… **more useful**.”
- **P6:** “That data’s **not friendly**, though. It’s **not friendly to interpret**… I **don’t really understand it very well**… I think… **presenting** [it] in a very… **simple way**” would help.
- **P7:** “This top part, that heat map… I don’t think you need to go as detail-oriented as that. It can just be… **here’s the path** that you took… I don’t think you need to go… **three-dimensional**.”

**F3 — From noticing moments to debriefing-ready prompts (scaffolding gap).**

- **P8:** “I find myself… having to **pick a few**… You try to watch the session, **come up with a theme on your own**… So I’m not sure that a big tally sheet would be helpful or not.”
- **P9:** “If you have an option to **review that specific segment**, we can either **with the group or not with the group**.”
- **P10:** “The debriefing dashboard should **identify your metrics with the expected metrics**… compare yourself to what your **ideal scenario** looks like… I wanted to know **at what point** did I miss establishing an airway… when would’ve that **ideal place** in the scenario [be]?”

**Observer summary (expert walkthrough, anonymized).** In the structured walkthrough, the clinical expert treated low-entropy / high–self-loop segments as **cues to prompt debriefing questions** (e.g., what the leader was tracking, whether CPR timing remained salient) rather than as stand-alone judgments of error—consistent with **F3** and **D3** (scaffolding toward inquiry-oriented dialogue).

### Summary table mapping F1–F3 to D1–D3


| Finding                                             | Design implication                                                                               | Manifestation in ReadGaze (concise)                                                                                                                    |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **F1** Gaze as useful proxy, not definitive truth   | **D1** Human-in-the-loop interpretation; outputs as **cues**, not correctness labels             | **Queryable Attention Dynamics** framed as **diagnostic semantics**; replay-linked **verification**; language that avoids “ground truth” judgments.    |
| **F2** High burden of raw gaze displays             | **D2** Abstract traces into **interpretable attention states** aligned with **phase and events** | **Scope–Intensity** states; timeline and **clinical context**; interaction primitives for inspecting states/transitions/AOI without raw path decoding. |
| **F3** Gap from observation to debriefing questions | **D3** **Diagnostic scaffolding** from inspected evidence → replay check → **prompt**            | **Debriefing support layer**: diagnostic notes, **EvidenceBox**, **ShapeDebriefing** / inquiry-oriented prompts tied to anchored moments.              |


### Build / upload note

- **Markdown:** This section can be exported to PDF/HTML for the anonymous supplementary site linked from the main paper (`anonymous.4open.science`).

## Representation and Validation Details
This supplement documents area-of-interest (AOI) definitions, fixation preprocessing, Scope–Intensity (routing entropy *H* and weighted self-loop *L*) computation, validation analyses, window-size sensitivity, novice vs expert comparisons, and compact pseudocode. All session-level identifiers are omitted; cohort sizes are reported only in the aggregate.

### Additional AOI definitions and mapping examples

## Representation and Validation Details

This section supplements the manuscript **Representation** layer, **dataset**, and **Dataset and Validation** analyses in `ReadGaze-main.tex`: the AOI set \(\mathcal{A}\), preprocessing, routing entropy *H* (**Scope**) and weighted self-loop prevalence *L* (**Intensity**), validation checks, window-size sensitivity, exploratory cohort contrasts, and pseudocode. **Numeric summaries match the main paper** unless labeled as repository-only diagnostics.

### AOI set and object-to-AOI mapping

Each mapped fixation is assigned to one of seven AOIs, matching the **Equipment–Airway, …, Patient** list in the main text **Representation** section (same semantics as the attention-state table). Internal codes in tooling map to human-readable labels as follows.

| Internal code | Human-readable label |
|---------------|----------------------|
| `AOI_AirwayEquipment` | Equipment – Airway |
| `AOI_CPRHands` | Equipment – CPR |
| `AOI_DefibEquipment` | Equipment – Defib |
| `AOI_Meds_Procedure` | Equipment – Meds & IV |
| `AOI_Monitor` | Patient Vitals Monitor |
| `AOI_NPC/Other` | Other Team Members (and non-mapped / teleport UI when applicable) |
| `AOI_PatientCore` | Patient |

The authoritative **Object Name → AOI** mapping is maintained in `codebook/Copy of Object Names - Fixation - objectFixationCounts.csv`. The team-lead realtime pipeline applies the same mapping logic via `map_object_to_aoi` in `tools/teamlead_realtime_entropy.py`: exact normalized string match against the codebook, then a containment-based fuzzy fallback if no exact hit. Generic examples (no codebook strings): rhythm or numeric display objects are mapped to **Patient Vitals Monitor**; team-member avatars or generic environmental props typically map to **Other Team Members** when not covered by equipment or patient-specific rules.

**Figure A1.** *Schematic placement of the seven AOIs in the simulation view.*

![AOI layout in the simulation environment.](Figures/AOIInSimulation.png)

### Preprocessing and sliding windows

**Manuscript pipeline (authoritative).** The paper preprocesses gaze into fixations using **dispersion-based** identification, then **merges adjacent fixations on the same AOI when the inter-fixation gap is ≤ 300 ms**, consistent with the **Input** and **Representation** sections of `ReadGaze-main.tex`. Reported **Scope** (*H*, routing entropy) and **Intensity** (*L*, weighted self-loop prevalence) are computed on **team-leader** fixation streams aligned to simulation time.

**Repository tooling (secondary).** Some utilities read role-specific `* - Fixation.csv` exports. The helper `fixation_tool/fixation_tool.py` uses duration **≥ 0.1 s** as a fixation cutoff and shorter events as saccades (`FIXATION_THRESHOLD_S = 0.1`) for certain **off-line transition utilities**. That **0.1 s convention does not replace** dispersion + 300 ms merging for the manuscript’s Scope–Intensity windows; it applies only where those scripts are used.

- **Team lead only.** Attention-state streams and transition tables for the team-lead role use fixations filtered to the team-lead observer.
- **Merged AOI segments for transitions.** For attention-transition tabulation (`generate_attention_transition_table.py`), consecutive fixations that map to the **same AOI** along the temporal sequence are merged into one segment before deriving ordered AOI transitions. Object names (and categories where used) are mapped to AOIs via the codebook, with category-level fallbacks (e.g. monitor-like categories → monitor, patient-related → patient core) consistent with the transition-table script.
- **Sliding windows.** Default window length **W = 30 s**, step **5 s**, as in `compute_realtime_entropy_for_file` in `tools/teamlead_realtime_entropy.py`. Each window’s label time is taken at the **center** of the bin (window start + *W*/2), so the scalars *H* (**Scope**) and *L* (**Intensity**) for that label summarize transitions whose fixation end times fall in \([t_0, t_0 + W)\). Timestamps are aligned to simulation start; centered labeling implies the summary is centered on the plotted time (note for reviewers on smoothing vs causality).

### Worked example: Scope–Intensity (*H* = Scope, *L* = Intensity)

The implementation in `compute_routing_metrics` (`tools/teamlead_realtime_entropy.py`) proceeds as follows.

1. **Transition list.** From fixation-level AOI sequence inside the window, form consecutive pairs \((\text{from}, \text{to})\) (after any AOI merge step used upstream).
2. **Count matrix.** For each source AOI *i*, tally outgoing counts \(n_{ij}\) to destination *j*. Let \(r_i = \sum_j n_{ij}\) be the row total and \(N = \sum_i r_i\) the total number of transitions.
3. **Routing entropy *H* (self-loops excluded from the outgoing distribution).** For each source *i* with **off-diagonal mass** \(o_i = \sum_{j \neq i} n_{ij} > 0\), compute Shannon entropy (base 2) over **only** destinations \(j \neq i\), using conditional probabilities \(p_{ij} = n_{ij} / o_i\):
   \[
   H_i = -\sum_{j \neq i,\; n_{ij}>0} p_{ij} \log_2 p_{ij}.
   \]
   Rows with \(o_i = 0\) contribute **zero** to the entropy numerator; the implementation still increments the weight sum by \(r_i\) for those rows. Because \(\sum_i r_i = N\) over all emitting sources in the window, the reported value is
   \[
   H = \frac{1}{N}\sum_{i:\, o_i > 0} H_i \cdot r_i,
   \]
   equivalent to `weighted_entropy / weight_sum` in code (with `weight_sum` = \(N\) for the nonempty count matrix).
4. **Weighted self-loop *L*.** For each source *i*, self-loop proportion \(s_i = n_{ii} / r_i\) (0 if \(r_i = 0\)). The global weighted self-loop is
   \[
   L = \sum_i \frac{r_i}{N} \cdot s_i = \frac{1}{N}\sum_i n_{ii}.
   \]
   The last equality holds because \(\frac{r_i}{N}\cdot\frac{n_{ii}}{r_i}=\frac{n_{ii}}{N}\); the code implements the weighted form explicitly.

**Synthetic toy (three AOIs).** Suppose the window yields these seven transitions in order:  
X→Y, X→Y, X→X, Y→Z, Y→X, Z→Z, Z→X.

| From \\ To | X | Y | Z | Row total \(r_i\) |
|------------|---|---|---|-------------------|
| X | 1 | 2 | 0 | 3 |
| Y | 1 | 0 | 1 | 2 |
| Z | 1 | 0 | 1 | 2 |

Here \(N = 7\).

- **Row X:** \(o_X = 2\), only Y off-diagonal: \(H_X = -\log_2(1) = 0\).
- **Row Y:** \(o_Y = 2\), \(p_{Y\to Z}=p_{Y\to X}=\tfrac12\): \(H_Y = 1\) bit.
- **Row Z:** \(o_Z = 1\), only X: \(H_Z = 0\).

Weighted entropy numerator: \(0\cdot 3 + 1\cdot 2 + 0\cdot 2 = 2\). Weight sum: \(3+2+2 = 7\). **\(H = 2/7 \approx 0.286\)** bits.

Weighted self-loop: \(\frac{3}{7}\cdot\frac{1}{3} + \frac{2}{7}\cdot 0 + \frac{2}{7}\cdot\frac{1}{2} = \frac{2}{7} \approx 0.286\). **\(L = 2/7\)**.

This matches `compute_routing_metrics` on the same transition multiset.

### Dataset scope (team leader, 14 sessions)

Aligning with the **Dataset and Validation** paragraph in the main text: **14** VR training sessions; **77,041** raw fixations → **40,998** after same-AOI merges with gap ≤ 300 ms; analysis focuses on **team leader** gaze → **2,232** analysis windows (30 s / 5 s step) and **666** contiguous **state segments** after run merging. Cohort labels for exploratory comparisons: **novice** trainee-led sessions **n = 10**, **expert** (ACLS-certified instructor team lead) **n = 4**, as in the manuscript. Repository scripts: `sanitycheck/sanity_check.py` and related reports. No per-session identifiers are listed here.

### Validation (order matches the main text)

The four **primary** checks below follow the same order as **Dataset and Validation** in `ReadGaze-main.tex` (internal consistency → temporal coherence → construct validity → cross-session stability). Repository labels **V1–V4** are noted for cross-walking to `sanitycheck` logs.

#### 1. Internal consistency (distinct AOI signatures by state; repo: V2)

**Method.** For every analysis window, AOI-level measures are pooled **within each classified state** across all sessions. **Mean unique AOI count** and **mean dominant AOI proportion** are computed on that pooled sample (not “mean per session then mean of means”). Mean *H* (**Scope**) and mean *L* (**Intensity**) are descriptive aggregates over windows assigned to each state.

**Results (illustrative).** **S1 (Broad Scanning)** vs **S4 (Sustained Fixation)**: mean unique AOI count **4.52** vs **3.19**; mean dominant proportion **0.617** vs **0.741**. Patterns align with the **Attention-state semantics** table in the manuscript: higher *H* (**Scope**) for broad scanning, higher dominant-AOI concentration for **S4 (Sustained Fixation)**. Full state × metric tables: `sanitycheck/sanity_check_report_en.md`.

#### 2. Temporal coherence (segment duration and flip rate; repo: V3)

**Method.** Contiguous runs of the same state yield segment durations. **Median / mean** duration statistics are computed on **pooled** segments. **Flips per minute** = per session, \((\#\text{segments} - 1) / \text{session duration in minutes}\), then **mean across sessions**.

**Results.** **666** segments total; **median** duration **10.0 s**, **mean** **16.8 s**; **63.4%** of segments ≥ **10 s**; mean flip rate **3.54** flips/min (typical per-session range about **2.7–5.0** flips/min). Longest observed bout **120 s**.

#### 3. Construct validity — event-locked shocks (repo: V1)

**Method.** Shock times come from the action log (defibrillation shocks performed by the defib role). Asymmetric bins: **Pre** (−10–0 s), **Post** (0–15 s), **Late** (15–30 s) relative to each shock; **Baseline** = windows not in any shock-relative bin. **Wilcoxon signed-rank** tests use **one summary per session** (e.g. proportion of windows in Post vs Baseline), avoiding pseudoreplication of windows.

**Results (aggregate).** All **14** sessions contribute shock events (**83** shocks total). Example window counts: Pre **133**, Post **204**, Late **183**, Baseline **1712**. Baseline state mix approximately **S1 23.6%**, **S2 24.1%**, **S3 21.0%**, **S4 31.3%**. Post-window **S1 (Broad Scanning)** proportion **51.5%** vs baseline **23.6%** (**+27.9** percentage points unweighted). Session-level **Post vs Baseline** on **S1**: median Post **50.0%** vs Baseline **23.6%**, **W = 1**, **p = .0002**, **r = .864**, **13/14** sessions in the expected direction. **Pre vs Baseline** on **S4 (Sustained Fixation)**: medians **8.3%** vs **33.3%**, **p = .002**, **r = .780**. Other contrasts: `sanitycheck/sanity_check_report_en.md`.

#### 4. Cross-session stability in *H*–*L* space

**Method.** Each window is plotted in the *H*–*L* plane. Classification into **S1–S4** uses **per-session** medians of *H* and *L* as thresholds \(T_H\), \(T_L\) (see Pseudocode 3)—**canonical** for all reported analyses.

**Global visualization (optional).** For **pooled** *H* and *L* across sessions only, the main text reports example **global** medians **T_E = 0.943** and **T_L = 0.701** (routing entropy and self-loop prevalence) showing the same quadrant structure as the **Scope–Intensity** figure in the manuscript; reference implementation context: `sanitycheck/CONTEXT.md`, `sanitycheck/visualize_v2.py`. **Analysis** always uses **session-relative** medians unless explicitly noted.

#### Supplementary: clinical stage boundaries (repo: V4)

**Method.** Compare state flip rate near clinical stage boundaries vs within-stage intervals.

**Result.** **Weak signal**: **5/14** sessions show higher boundary flip rate; aggregate boundary vs interior difference about **+0.3%**. Exploratory only (`sanitycheck/sanity_check_report_en.md`).

### Window-size sensitivity

**Method.** Recompute *H* and *L* with **W ∈ {20, 30, 45} s**, step **5 s**. Reclassify states using **per-window-size** median thresholds; compute **Cohen’s κ** between label sequences on the same timeline for each session; report mean κ across sessions.

**Results (14 sessions).** Adjacent pairs: **W = 20 vs 30 s**: mean κ **0.533** (SD **0.060**); **W = 30 vs 45 s**: mean κ **0.539** (SD **0.075**). **W = 20 vs 45 s**: mean κ **0.372**. Overall mean κ across the three pairings **~0.48**. State **occupancy** percentages are stable across *W* (e.g. each state roughly **28–31%** depending on *W*). Mean flip rate decreases with larger *W* (e.g. **4.32**, **3.45**, **2.69** flips/min for 20 / 30 / 45 s). Implementation: `sanitycheck/sensitivity_analysis.py`; tables: `sanitycheck/sensitivity_analysis_kappa.csv`, `sensitivity_analysis_summary.csv`.

### Expert / novice comparison (exploratory)

**Cohort assignment.** As in the manuscript (Section **Dataset and Validation**): sessions led by **ACLS-certified instructors** are **expert** (**n = 4**); sessions led by **residents or students** are **novice** (**n = 10**). The repository uses a deterministic prefix rule on internal keys (`classify_group` / `EXPERT_PREFIXES` in `sanitycheck/monitor_analysis.py`); literal prefixes are not listed here.

**Statistics.** **Mann–Whitney *U*** tests on **session-level** summaries compare cohorts (two-sided, nonparametric). **Plan A** (`monitor_analysis.py`): overall monitor dwell and visit patterns. **Plan B**: monitor time **conditioned on** classified state (e.g. share of monitor fixation time falling in each state, and within-state monitor proportion). **State occupancy** (time in S1–S4) showed **no** meaningful cohort differences in the exploratory report (`sanitycheck/group_comparison_report.md`, all *p* > .67). Significant or trend differences reported there include, at session level: **total monitor dwell %** lower in the expert cohort than trainees (approximately **12%** vs **22%**, *p* < .05), and exploratory metrics such as bout transition entropy and NPC/other dwell (*p* < .10). 

**Exploratory bout transition.** Compressed state sequences (bouts) can be compared for transition probabilities; one reported contrast is **S4→S1** more frequent in trainees than in experts (e.g. **~3%** vs **~1%** session-level prevalence in the exploratory analysis, *p* < .05; see also `sanitycheck/state_transition_analysis_report.md` for effect size **r ≈ 0.58** on a related bout metric). These are **hypothesis-generating**, not confirmatory.

### Pseudocode

**Pseudocode 1 — Merge adjacent same-AOI segments**

```
INPUT: fixation rows with AOI and time order
SORT by start time
INITIALIZE empty list segments, cursor = first row’s AOI, start = first start, end = first end
FOR each subsequent row r:
    IF r.AOI == cursor:
        end = r.end
    ELSE:
        APPEND segment(cursor, start, end)
        cursor = r.AOI; start = r.start; end = r.end
APPEND final segment
OUTPUT: segments
```

**Pseudocode 2 — Sliding window routing metrics**

```
INPUT: fixation-derived AOI transitions as (from_AOI, to_AOI, time_to)
W, step = 30, 5  // seconds
FOR window start t0 in 0, step, 2*step, ... while t0 + W <= T_sim:
    label_time = t0 + W/2
    T = all transitions with t0 <= time_to < t0 + W
    (H, L, ...) = ComputeRoutingMetrics(T)  // as in “Worked example” / compute_routing_metrics
    EMIT row (label_time, H, L, ...)
```

**Pseudocode 3 — Four-way state from per-session medians**

```
INPUT: series of (H, L) for one session’s windows
T_H = median(all H); T_L = median(all L)
FOR each window:
    IF H >= T_H AND L <  T_L: state = 1  // S1 Broad Scanning (high Scope, low Intensity)
    IF H >= T_H AND L >= T_L: state = 2  // S2 Targeted Check
    IF H <  T_H AND L <  T_L: state = 3  // S3 Anchored with Shifts
    IF H <  T_H AND L >= T_L: state = 4  // S4 Sustained Fixation
OUTPUT: state per window (exact quadrant order matches production code)
```

**Pseudocode 4 — Event-locked bins and session-level paired test**

```
INPUT: shock times; per-window state labels; session boundaries
DEFINE bins relative to each shock: Pre, Post, Late; Baseline = windows in none of these
FOR each session s:
    p_post(s) = proportion of windows in Post that are state k (or vector for k=1..4)
    p_base(s) = same for Baseline
FOR hypothesis on state k:
    PAIRS = {(p_post(s), p_base(s)) for all sessions with valid data}
    EFFECT = Wilcoxon signed-rank on paired differences (session-level)
OUTPUT: test statistic, p-value, effect size r
```

## Monitor-Threshold Flagging Details

- Threshold derivation for expert-referenced monitor flags
- Additional flagged and unflagged example segments

## Formal User Study Materials

- Task prompt and think-aloud instructions
- Comparative interview prompts
- Coding details for primitive engagement and reasoning change
- Exploratory post-session self-report measures
- Instrument wording and descriptive summaries

