# Torshammer Research Report

**Author:** Veronica Satsangi
**Date Started:** September 19, 2024
**Objective:** This research project investigates the Torshammer tool, specifically its mechanics in launching HTTP-based denial-of-service (DoS) attacks. The goal is to analyze its structure, test its functionality in a safe environment, and document its real-world behavior in controlled simulations. This work is part of a broader initiative in cybersecurity tooling analysis and threat modeling.

## Test Environment

All testing was conducted in a controlled local lab setup using a custom-built HTML web server hosted on `localhost`.
  
- **Platform:** Kali Linux 2024.4  
- **Python Version:** 3.13.2  
- **Target:** Localhost (127.0.0.1) test server  
- **Purpose:** Controlled network stress testing and source-level behavioral analysis

## Methodology

1. Cloned and reviewed the Torshammer source code.
2. Set up a minimal HTTP server in HTML to simulate a vulnerable environment.
3. Conducted functional testing using Torshammer against the local server.
4. Validated that the tool successfully flooded the server and caused performance degradation.
5. Structured the codebase in a Git repository, initialized `.gitignore`, and began documentation.
6. Prepared groundwork for future refactoring and instrumentation.

## Modifications Log

| Date       | File Modified      | Description                                       |
|------------|--------------------|---------------------------------------------------|
| 2024-09-21 | `torshammer.py`    | Initial review and preparation for testing        |
| 2024-10-03 | `torshammer.py`    | Ran local attacks, confirmed behavior on server   |
| 2025-05-25 | `report.md`        | Drafted professional research documentation       |

## Observations

- Torshammer uses raw socket connections to send repeated HTTP GET requests.
- It attempts to keep connections alive to maintain server load.
- In testing, it successfully degraded performance of a custom web server under load.
- The original implementation lacks modularity and structured error handling.
- Tool remains viable under specific conditions, particularly against improperly configured servers.

## Ethical Considerations

All activities were performed in a controlled environment. No third-party systems were targeted or affected. This work complies with ethical guidelines for cybersecurity research and is intended solely for educational and defensive security purposes.

