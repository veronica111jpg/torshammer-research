# Torshammer Research & Analysis

**This project is for educational and ethical cybersecurity research only. Do not use this tool for unauthorized attacks or testing on systems you do not own or have permission to assess.**

## Overview

This repository contains a modified, research-oriented version of [Torshammer](https://github.com/Karlheinzniebuhr/torshammer), a Python-based DoS tool that leverages slow POST attacks over the Tor network.

The goal of this project is to:
- Analyze how Torshammer operates at the code and network level
- Investigate its attack vector (slow POST)
- Explore detection and mitigation strategies
- Log traffic and behavioral patterns
- Propose countermeasures from a blue team perspective

---

## Research Goals

- Understand slow POST and its interaction with Apache servers
- Examine Torshammer’s thread, retry, and Tor (`-T`) functionality
- Run safe, controlled simulations in isolated lab environments
- Suggest enhancements, ethical use cases, and potential improvements

---

## How to Use (for testing in lab environments only)

```bash
python3 torshammer.py -t <TARGET-IP> -r <RETRIES> -T

---

## Example usage 

python3 torshammer.py -t 192.174.1.200 -r 1000 -T
