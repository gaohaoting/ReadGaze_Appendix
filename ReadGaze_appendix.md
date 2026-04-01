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

- Additional AOI definitions and mapping examples
- Fixation preprocessing details
- A worked example of the Scope–Intensity computation
- Additional validation statistics
- Window-size sensitivity analyses
- Expert/novice comparison details
- Pseudocode

## Monitor-Threshold Flagging Details

- Threshold derivation for expert-referenced monitor flags
- Additional flagged and unflagged example segments

## Formal User Study Materials

- Task prompt and think-aloud instructions
- Comparative interview prompts
- Coding details for primitive engagement and reasoning change
- Exploratory post-session self-report measures
- Instrument wording and descriptive summaries

