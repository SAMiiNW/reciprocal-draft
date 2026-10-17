# Steward remediation matrix

| Steward request | Code change | Regression / proof | Status |
| --- | --- | --- | --- |
| State what the product does immediately | Add a plain-language definition above the fold: it matches public NEED profiles with OFFER profiles only when both satisfy one shared rule | Desktop browser QA | Complete |
| Make the next action obvious | Add a three-step path, separate organizer/participant roles, and a clearly labelled start action | Frontend content assertions and browser QA | Complete |
| Explain inputs and output | Explain what a table, profile URL, consensus draw, and final pair mean next to the controls | Frontend content assertions and organizer-dialog QA | Complete |
| Provide a usable first-run path | Add a guided example and progress checklist instead of dropping the visitor into an unexplained board | Browser QA from a fresh session | Complete |
| Prevent a future partial-profile rejection | Align the accepted profile limit with the complete 9,000-byte consensus input; never slice a larger frozen file | Beyond-boundary regression and a new exact-source deployment | Complete |
| Preserve the verified contract lifecycle | Deploy the corrected contract and rerun its public read/write flow after the UI update | `deployment.json` and fresh finalized `evidence/live-run.json` | Complete |

