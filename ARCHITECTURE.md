# Quantum Trader Architecture

## Philosophy

Quantum Trader is designed around a simple rule:

> Atlas thinks.
> The UI displays.
> The Engine coordinates.

Every system has one responsibility.

---

## Core

The Core contains all business logic.

It never knows anything about buttons, windows, or UI.

Responsibilities:

- Market scanning
- AI analysis
- Indicators
- Trading signals
- Portfolio management

---

## UI

The UI never performs calculations.

It only displays information returned by Atlas.

Responsibilities:

- Market Grid
- Charts
- Portfolio
- Detail Panels
- Alerts

---

## Atlas

Atlas is the intelligence layer.

Future Atlas Brains:

- Momentum
- Trend
- Risk
- Pattern
- Volume
- News
- Whale Activity
- Portfolio

Each brain contributes to one final Analysis.

---

## Analysis

Analysis is the single source of truth.

Every system reads the same Analysis object.

This prevents duplicate calculations.

---

## Long-Term Goal

Create the world's most intelligent AI trading platform with explainable decision making.