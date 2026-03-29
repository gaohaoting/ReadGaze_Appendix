#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ReadGaze Attention State Classification - Sanity Check
======================================================
Validates the 4-state attention classification algorithm across all sessions.

Validation 1: Pulse Check events should enrich State 4 (Tunneled Attention)
Validation 2: AOI characteristics should differ across states (aoi_count, dominant_proportion)
Validation 3: State duration distribution should be temporally coherent (not noisy)
Validation 4: Clinical stage transitions should correlate with state changes
"""

import os
import csv
import statistics
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

DATASETS_DIR = Path(__file__).parent / "Datasets"

STATE_NAMES = {
    1: "Exploratory Scanning",
    2: "Diverse Anchoring",
    3: "Structured Scanning",
    4: "Tunneled Attention",
}


# ============================================================
# Data Loading
# ============================================================

def find_sessions():
    """Find all session directories with required data files."""
    sessions = []
    if not DATASETS_DIR.is_dir():
        return sessions
    for d in sorted(DATASETS_DIR.iterdir()):
        if not d.is_dir():
            continue
        session_id = d.name
        # Check for required files
        attn_files = list(d.glob("*_attention_state_classification.csv"))
        aoi_files = list(d.glob("*_realtime_aoi_timeseries.csv"))
        action_files = list(d.glob("* - Actions.csv"))
        stage_files = list(d.glob("* - StageInfo.csv"))
        
        if attn_files and action_files:
            sessions.append({
                'id': session_id,
                'dir': d,
                'attn_file': attn_files[0],
                'aoi_file': aoi_files[0] if aoi_files else None,
                'action_file': action_files[0],
                'stage_file': stage_files[0] if stage_files else None,
            })
    return sessions


def parse_datetime(dt_str):
    """Parse datetime string with multiple format support."""
    for fmt in ["%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"]:
        try:
            return datetime.strptime(dt_str.strip(), fmt)
        except ValueError:
            continue
    return None


def load_attention_states(filepath):
    """Load attention state classification data."""
    states = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                states.append({
                    'state': int(row['state']),
                    'label': row['state_label'],
                    'start': float(row['start_time_seconds']),
                    'end': float(row['end_time_seconds']),
                    'duration': float(row['duration_seconds']),
                    'state_count': int(row['state_count']),
                    'mean_entropy': float(row['mean_entropy']),
                    'mean_selfloop': float(row['mean_selfloop']),
                    'start_abs': parse_datetime(row['start_time_absolute']),
                    'end_abs': parse_datetime(row['end_time_absolute']),
                })
            except (ValueError, KeyError):
                continue
    return states


def load_actions(filepath):
    """Load clinical actions data."""
    actions = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                actions.append({
                    'start': parse_datetime(row['Start']),
                    'role': row.get('Role', row.get('role', '')),
                    'action': row.get('Action', row.get('action', '')),
                    'group': row.get('Group', row.get('group', '')),
                    'stage': row.get('Stage', row.get('stage', '')),
                })
            except (ValueError, KeyError):
                continue
    return actions


def load_aoi_timeseries(filepath):
    """Load AOI timeseries data."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                entry = {
                    'time': float(row['time_seconds']),
                    'dominant_aoi': row.get('dominant_aoi', ''),
                    'dominant_proportion': float(row.get('dominant_aoi_proportion', 0)),
                    'aoi_count': int(row.get('aoi_count', 0)),
                    'total_fixation': float(row.get('total_fixation_duration', 0)),
                }
                data.append(entry)
            except (ValueError, KeyError):
                continue
    return data


def load_stages(filepath):
    """Load clinical stage data."""
    stages = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                stages.append({
                    'stage': row['Stage'],
                    'start': parse_datetime(row['Start']),
                    'end': parse_datetime(row['End']),
                })
            except (ValueError, KeyError):
                continue
    return stages


def get_base_time(attn_states):
    """Infer base time from first attention state."""
    if attn_states and attn_states[0]['start_abs']:
        return attn_states[0]['start_abs'] - timedelta(seconds=attn_states[0]['start'])
    return None


def abs_to_relative(abs_time, base_time):
    """Convert absolute time to relative seconds."""
    if abs_time and base_time:
        return (abs_time - base_time).total_seconds()
    return None


# ============================================================
# Validation 1: Pulse Check → State 4 Enrichment
# ============================================================

def validation_1_pulse_check(sessions):
    """Check if State 4 is enriched around Pulse Check events."""
    print("\n" + "=" * 70)
    print("VALIDATION 1: Pulse Check → State 4 (Tunneled Attention) Enrichment")
    print("=" * 70)
    print("Hypothesis: State 4 should occur more frequently within ±15s of")
    print("Pulse Check events compared to baseline.\n")
    
    WINDOW = 15  # seconds around Pulse Check
    
    all_near_pulse = []  # states near pulse checks
    all_baseline = []    # all states (for baseline)
    session_results = []
    
    for sess in sessions:
        attn = load_attention_states(sess['attn_file'])
        actions = load_actions(sess['action_file'])
        base_time = get_base_time(attn)
        
        if not base_time or not attn or not actions:
            continue
        
        # Get teamlead Pulse Check times (relative seconds)
        pulse_times = []
        for a in actions:
            if 'pulse check' in a['action'].lower() and a['role'].lower() == 'teamlead':
                rel = abs_to_relative(a['start'], base_time)
                if rel is not None:
                    pulse_times.append(rel)
        
        if not pulse_times:
            continue
        
        # For each 5s window, determine if it's "near pulse check"
        # Expand attention states to individual 5s windows
        windows = []
        for s in attn:
            t = s['start']
            while t <= s['end']:
                windows.append({'time': t, 'state': s['state']})
                t += 5
        
        near_pulse_states = []
        far_pulse_states = []
        
        for w in windows:
            near = any(abs(w['time'] - pt) <= WINDOW for pt in pulse_times)
            if near:
                near_pulse_states.append(w['state'])
            else:
                far_pulse_states.append(w['state'])
        
        if near_pulse_states and far_pulse_states:
            near_s4 = near_pulse_states.count(4) / len(near_pulse_states) * 100
            far_s4 = far_pulse_states.count(4) / len(far_pulse_states) * 100
            session_results.append({
                'session': sess['id'],
                'n_pulse': len(pulse_times),
                'near_s4_pct': near_s4,
                'far_s4_pct': far_s4,
                'enrichment': near_s4 - far_s4,
                'n_near': len(near_pulse_states),
                'n_far': len(far_pulse_states),
            })
            all_near_pulse.extend(near_pulse_states)
            all_baseline.extend(far_pulse_states)
    
    # Print per-session results
    print(f"{'Session':<25} {'#Pulse':>7} {'Near±15s S4%':>14} {'Baseline S4%':>14} {'Enrichment':>12}")
    print("-" * 75)
    for r in session_results:
        enrichment_str = f"+{r['enrichment']:.1f}%" if r['enrichment'] > 0 else f"{r['enrichment']:.1f}%"
        print(f"{r['session']:<25} {r['n_pulse']:>7} {r['near_s4_pct']:>13.1f}% {r['far_s4_pct']:>13.1f}% {enrichment_str:>12}")
    
    # Aggregate
    if all_near_pulse and all_baseline:
        agg_near = all_near_pulse.count(4) / len(all_near_pulse) * 100
        agg_far = all_baseline.count(4) / len(all_baseline) * 100
        print("-" * 75)
        print(f"{'AGGREGATE':<25} {'':>7} {agg_near:>13.1f}% {agg_far:>13.1f}% {'+' if agg_near > agg_far else ''}{agg_near - agg_far:.1f}%")
        
        # Also show all 4 states distribution near pulse checks
        print(f"\n  State distribution near Pulse Check (n={len(all_near_pulse)} windows):")
        for s in [1, 2, 3, 4]:
            pct = all_near_pulse.count(s) / len(all_near_pulse) * 100
            print(f"    State {s} ({STATE_NAMES[s]}): {pct:.1f}%")
        
        print(f"\n  State distribution baseline (n={len(all_baseline)} windows):")
        for s in [1, 2, 3, 4]:
            pct = all_baseline.count(s) / len(all_baseline) * 100
            print(f"    State {s} ({STATE_NAMES[s]}): {pct:.1f}%")
    
    enriched = sum(1 for r in session_results if r['enrichment'] > 0)
    total = len(session_results)
    print(f"\n  RESULT: State 4 enriched near Pulse Check in {enriched}/{total} sessions")
    
    return session_results


# ============================================================
# Validation 2: AOI Characteristics by State
# ============================================================

def validation_2_aoi_characteristics(sessions):
    """Check if AOI characteristics differ across states as expected."""
    print("\n" + "=" * 70)
    print("VALIDATION 2: AOI Characteristics by Attention State")
    print("=" * 70)
    print("Hypothesis: State 1 (Exploratory) should have higher aoi_count and")
    print("lower dominant_proportion; State 4 (Tunneled) should be the opposite.\n")
    
    state_aoi_counts = defaultdict(list)
    state_dominant_props = defaultdict(list)
    
    for sess in sessions:
        if not sess['aoi_file']:
            continue
        
        attn = load_attention_states(sess['attn_file'])
        aoi_data = load_aoi_timeseries(sess['aoi_file'])
        
        if not attn or not aoi_data:
            continue
        
        # Build time → aoi mapping
        aoi_by_time = {d['time']: d for d in aoi_data}
        
        # For each attention state window, get corresponding AOI data
        for s in attn:
            t = s['start']
            while t <= s['end']:
                if t in aoi_by_time:
                    aoi = aoi_by_time[t]
                    state_aoi_counts[s['state']].append(aoi['aoi_count'])
                    state_dominant_props[s['state']].append(aoi['dominant_proportion'])
                t += 5
    
    # Print results
    print(f"{'State':<30} {'N':>6} {'AOI Count':>12} {'(SD)':>8} {'Dom. Prop.':>12} {'(SD)':>8}")
    print("-" * 80)
    
    for s in [1, 2, 3, 4]:
        counts = state_aoi_counts.get(s, [])
        props = state_dominant_props.get(s, [])
        if counts and props:
            mean_c = statistics.mean(counts)
            sd_c = statistics.stdev(counts) if len(counts) > 1 else 0
            mean_p = statistics.mean(props)
            sd_p = statistics.stdev(props) if len(props) > 1 else 0
            print(f"State {s} ({STATE_NAMES[s]:<22}) {len(counts):>6} {mean_c:>12.2f} {sd_c:>7.2f} {mean_p:>12.3f} {sd_p:>7.3f}")
    
    # Check expected ordering
    if state_aoi_counts[1] and state_aoi_counts[4]:
        s1_mean = statistics.mean(state_aoi_counts[1])
        s4_mean = statistics.mean(state_aoi_counts[4])
        check1 = "PASS" if s1_mean > s4_mean else "FAIL"
        print(f"\n  Check: State 1 aoi_count ({s1_mean:.2f}) > State 4 aoi_count ({s4_mean:.2f})? → {check1}")
    
    if state_dominant_props[1] and state_dominant_props[4]:
        s1_prop = statistics.mean(state_dominant_props[1])
        s4_prop = statistics.mean(state_dominant_props[4])
        check2 = "PASS" if s4_prop > s1_prop else "FAIL"
        print(f"  Check: State 4 dominant_prop ({s4_prop:.3f}) > State 1 dominant_prop ({s1_prop:.3f})? → {check2}")
    
    # Also check entropy and self-loop values directly
    print(f"\n  --- Entropy & Self-Loop by State (from classification data) ---")
    state_entropy = defaultdict(list)
    state_selfloop = defaultdict(list)
    
    for sess in sessions:
        attn = load_attention_states(sess['attn_file'])
        for s in attn:
            state_entropy[s['state']].append(s['mean_entropy'])
            state_selfloop[s['state']].append(s['mean_selfloop'])
    
    print(f"  {'State':<30} {'Mean H':>10} {'(SD)':>8} {'Mean L':>10} {'(SD)':>8}")
    print(f"  {'-'*70}")
    for s in [1, 2, 3, 4]:
        h_vals = state_entropy.get(s, [])
        l_vals = state_selfloop.get(s, [])
        if h_vals and l_vals:
            print(f"  State {s} ({STATE_NAMES[s]:<22}) {statistics.mean(h_vals):>10.4f} {statistics.stdev(h_vals):>7.4f} {statistics.mean(l_vals):>10.4f} {statistics.stdev(l_vals):>7.4f}")


# ============================================================
# Validation 3: State Duration Distribution
# ============================================================

def validation_3_duration(sessions):
    """Check that state durations are temporally coherent."""
    print("\n" + "=" * 70)
    print("VALIDATION 3: State Duration Distribution")
    print("=" * 70)
    print("Hypothesis: States should persist for meaningful durations (not just 5s),")
    print("indicating temporally coherent classification rather than noise.\n")
    
    all_durations = defaultdict(list)
    total_flips = 0
    total_windows = 0
    session_flip_rates = []
    
    for sess in sessions:
        attn = load_attention_states(sess['attn_file'])
        if not attn:
            continue
        
        for s in attn:
            all_durations[s['state']].append(s['duration'])
        
        # Count state flips
        n_transitions = len(attn) - 1  # number of state changes
        if attn:
            session_duration = attn[-1]['end'] - attn[0]['start']
            if session_duration > 0:
                flips_per_min = n_transitions / (session_duration / 60)
                session_flip_rates.append({
                    'session': sess['id'],
                    'duration_min': session_duration / 60,
                    'n_states': len(attn),
                    'flips_per_min': flips_per_min,
                })
                total_flips += n_transitions
                total_windows += len(attn)
    
    # Duration statistics by state
    print(f"{'State':<30} {'N':>5} {'Mean(s)':>9} {'Median(s)':>10} {'SD(s)':>8} {'Min(s)':>8} {'Max(s)':>8} {'IQR':>12}")
    print("-" * 95)
    
    all_combined = []
    for s in [1, 2, 3, 4]:
        durations = all_durations.get(s, [])
        all_combined.extend(durations)
        if durations:
            q = sorted(durations)
            q1_idx = len(q) // 4
            q3_idx = 3 * len(q) // 4
            iqr = f"{q[q1_idx]:.0f}-{q[q3_idx]:.0f}"
            print(f"State {s} ({STATE_NAMES[s]:<22}) {len(durations):>5} {statistics.mean(durations):>9.1f} {statistics.median(durations):>10.1f} {statistics.stdev(durations) if len(durations) > 1 else 0:>8.1f} {min(durations):>8.1f} {max(durations):>8.1f} {iqr:>12}")
    
    print("-" * 95)
    if all_combined:
        q = sorted(all_combined)
        q1_idx = len(q) // 4
        q3_idx = 3 * len(q) // 4
        iqr = f"{q[q1_idx]:.0f}-{q[q3_idx]:.0f}"
        print(f"{'ALL STATES':<30} {len(all_combined):>5} {statistics.mean(all_combined):>9.1f} {statistics.median(all_combined):>10.1f} {statistics.stdev(all_combined):>8.1f} {min(all_combined):>8.1f} {max(all_combined):>8.1f} {iqr:>12}")
    
    # Duration bucket distribution
    print(f"\n  Duration distribution (all states combined, n={len(all_combined)}):")
    buckets = [(5, 5, "= 5s (single window)"), (10, 15, "10-15s"), (20, 30, "20-30s"), (35, 60, "35-60s"), (65, 999, "> 60s")]
    for lo, hi, label in buckets:
        count = sum(1 for d in all_combined if lo <= d <= hi)
        pct = count / len(all_combined) * 100 if all_combined else 0
        bar = "█" * int(pct / 2)
        print(f"    {label:<25} {count:>5} ({pct:>5.1f}%) {bar}")
    
    # State flip rate
    print(f"\n  State flip rate per session:")
    print(f"  {'Session':<25} {'Duration(min)':>14} {'#States':>8} {'Flips/min':>11}")
    print(f"  {'-'*60}")
    for r in session_flip_rates:
        print(f"  {r['session']:<25} {r['duration_min']:>14.1f} {r['n_states']:>8} {r['flips_per_min']:>11.2f}")
    
    if session_flip_rates:
        avg_flip = statistics.mean([r['flips_per_min'] for r in session_flip_rates])
        print(f"  {'-'*60}")
        print(f"  {'AVERAGE':<25} {'':>14} {'':>8} {avg_flip:>11.2f}")
        
        coherent = "PASS" if statistics.median(all_combined) >= 10 else "WARN"
        print(f"\n  RESULT: Median state duration = {statistics.median(all_combined):.1f}s → {coherent}")
        print(f"  (Durations > 5s indicate states are not single-window noise)")


# ============================================================
# Validation 4: State Changes at Clinical Stage Boundaries
# ============================================================

def validation_4_stage_transitions(sessions):
    """Check if state transitions are more likely at clinical stage boundaries."""
    print("\n" + "=" * 70)
    print("VALIDATION 4: State Changes at Clinical Stage Boundaries")
    print("=" * 70)
    print("Hypothesis: State transitions should occur more frequently near")
    print("clinical stage boundaries than within stable stages.\n")
    
    BOUNDARY_WINDOW = 15  # seconds around stage boundary
    
    all_boundary_flips = 0
    all_boundary_windows = 0
    all_interior_flips = 0
    all_interior_windows = 0
    session_results = []
    
    for sess in sessions:
        if not sess['stage_file']:
            continue
        
        attn = load_attention_states(sess['attn_file'])
        stages = load_stages(sess['stage_file'])
        base_time = get_base_time(attn)
        
        if not base_time or not attn or not stages:
            continue
        
        # Get stage boundary times (relative seconds)
        boundary_times = []
        for st in stages:
            if st['start']:
                rel = abs_to_relative(st['start'], base_time)
                if rel is not None and rel > 0:
                    boundary_times.append(rel)
            if st['end']:
                rel = abs_to_relative(st['end'], base_time)
                if rel is not None and rel > 0:
                    boundary_times.append(rel)
        boundary_times = sorted(set(boundary_times))
        
        if not boundary_times:
            continue
        
        # Check each state transition
        boundary_flip_count = 0
        boundary_total = 0
        interior_flip_count = 0
        interior_total = 0
        
        for i in range(len(attn) - 1):
            transition_time = attn[i]['end']  # time of state change
            near_boundary = any(abs(transition_time - bt) <= BOUNDARY_WINDOW for bt in boundary_times)
            
            if near_boundary:
                boundary_flip_count += 1
                boundary_total += 1
            else:
                interior_flip_count += 1
                interior_total += 1
        
        # Also count non-flip windows (within a state segment)
        for s in attn:
            t = s['start']
            while t <= s['end']:
                near_boundary = any(abs(t - bt) <= BOUNDARY_WINDOW for bt in boundary_times)
                if near_boundary:
                    boundary_total += 1
                else:
                    interior_total += 1
                t += 5
        
        if boundary_total > 0 and interior_total > 0:
            boundary_rate = boundary_flip_count / boundary_total * 100
            interior_rate = interior_flip_count / interior_total * 100
            session_results.append({
                'session': sess['id'],
                'n_boundaries': len(boundary_times),
                'boundary_flip_rate': boundary_rate,
                'interior_flip_rate': interior_rate,
                'enrichment': boundary_rate - interior_rate,
            })
            all_boundary_flips += boundary_flip_count
            all_boundary_windows += boundary_total
            all_interior_flips += interior_flip_count
            all_interior_windows += interior_total
    
    print(f"{'Session':<25} {'#Boundaries':>12} {'Boundary Flip%':>16} {'Interior Flip%':>16} {'Enrichment':>12}")
    print("-" * 85)
    for r in session_results:
        e_str = f"+{r['enrichment']:.1f}%" if r['enrichment'] > 0 else f"{r['enrichment']:.1f}%"
        print(f"{r['session']:<25} {r['n_boundaries']:>12} {r['boundary_flip_rate']:>15.1f}% {r['interior_flip_rate']:>15.1f}% {e_str:>12}")
    
    if all_boundary_windows > 0 and all_interior_windows > 0:
        agg_boundary = all_boundary_flips / all_boundary_windows * 100
        agg_interior = all_interior_flips / all_interior_windows * 100
        e = agg_boundary - agg_interior
        print("-" * 85)
        print(f"{'AGGREGATE':<25} {'':>12} {agg_boundary:>15.1f}% {agg_interior:>15.1f}% {'+' if e > 0 else ''}{e:.1f}%")
    
    enriched = sum(1 for r in session_results if r['enrichment'] > 0)
    total = len(session_results)
    print(f"\n  RESULT: State transitions enriched at stage boundaries in {enriched}/{total} sessions")


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 70)
    print("  ReadGaze Attention State Classification — SANITY CHECK REPORT")
    print("=" * 70)
    
    sessions = find_sessions()
    print(f"\nFound {len(sessions)} sessions with data:")
    for s in sessions:
        extras = []
        if s['aoi_file']:
            extras.append("AOI")
        if s['stage_file']:
            extras.append("Stages")
        print(f"  • {s['id']} [Actions, Attention{', ' + ', '.join(extras) if extras else ''}]")
    
    # Run validations
    validation_1_pulse_check(sessions)
    validation_2_aoi_characteristics(sessions)
    validation_3_duration(sessions)
    validation_4_stage_transitions(sessions)
    
    # Summary
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print("""
  V1 (Pulse Check → State 4): Tests construct validity — clinical events
     should correlate with expected attention states.

  V2 (AOI Characteristics): Tests internal consistency — state definitions
     should produce distinct AOI profiles.

  V3 (Duration Distribution): Tests temporal coherence — states should
     persist beyond single windows (not noisy oscillation).

  V4 (Stage Boundaries): Tests external sensitivity — clinical phase
     changes should trigger attention state transitions.
""")


if __name__ == "__main__":
    main()
