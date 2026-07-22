# RUN PIPELINE — Reel #06 image generation (fresh-session prompt)

Paste the block below into a **fresh** Claude Code session on branch
`claude/second-reel-script-assets-8rulhj` AFTER the Freepik hosts have been allowlisted
(`*.cdnpk.net` + `*.magnific.com`). The reachability gate at the top will halt automatically
if the allowlist is not actually live, so no credits are spent on a blocked session.

---

Run the Reel-06 image pipeline on branch `claude/second-reel-script-assets-8rulhj`, using
`Reel-06 - UK Khatam NZ Zinda/Reel-06_SCENE-PROMPTS.md` as the source of truth for prompts,
per-scene model, and references.

STEP 0 — HARD REACHABILITY GATE (do this first, before anything else):
- Run:
  `for h in pikaso.cdnpk.net ak-data.magnific.com; do curl -sS -o /dev/null -w "$h -> HTTP %{http_code}\n" --max-time 15 "https://$h/"; done`
- ABORT CONDITION: if EITHER host prints `HTTP 000`, or curl prints `CONNECT tunnel failed`, or
  `curl -sS "$HTTPS_PROXY/__agentproxy/status"` still lists either host under `recentRelayFailures`
  → STOP IMMEDIATELY. Do NOT upload, do NOT generate, do NOT spend any credits. Report:
  "❌ Allowlist not active — both/one host still blocked (HTTP 000). Halted before spending credits."
- PROCEED CONDITION: only if BOTH hosts return a real HTTP code (200/400/403/404 — anything but 000)
  AND neither appears in recentRelayFailures. Then continue.

STEP 1 — Balance: call Freepik `account_balance`; report available credits. Note the full batch is
~1,215 credits. If available < 1,500, warn me and wait for my go-ahead before generating.

STEP 2 — Kiwi mascot FIRST: generate the kiwi mascot sheet per the KIWI MASCOT spec in the scene
prompts (plain cream bg, waving + thumbs-up poses), download it to
`Reel-06 - UK Khatam NZ Zinda/Characters/Kiwi.png`.

STEP 3 — Upload references (needed for consistency): upload
`Reel-06 - UK Khatam NZ Zinda/Characters/Student 2.png`,
`Reel-06 - UK Khatam NZ Zinda/Characters/Good Consultant.png`, and the new `Kiwi.png`
to Freepik (creations_request_upload → PUT → creations_finalize_upload) and keep their identifiers.

STEP 4 — Generate ONE test (SC-09, "the one open door") with `imagen-nano-banana-2` + the Kiwi
reference. Download it, show it to me, and WAIT for my approval before generating the rest.

STEP 5 — After I approve, generate the remaining 18 scenes exactly per the scene-prompts file:
- `imagen-nano-banana-2` + reference for CHARACTER/KIWI scenes:
  SC-04 (Student 2), SC-10 (Kiwi), SC-11 (Student 2), SC-12 (Kiwi), SC-13 (Kiwi),
  SC-17 (Student 2 + Kiwi), SC-18 (Kiwi), SC-19 (Good Consultant).
- `recraft-v4-1` (no reference) for the OBJECT scenes: SC-01, 02, 03, 05, 06, 07, 08, 14, 15, 16.
- 16:9 for every scene.

STEP 6 — Download each result into `Reel-06 - UK Khatam NZ Zinda/Scenes/SC-01.png … SC-19.png`.
Verify each file is a valid PNG (non-zero size). Then commit ("Reel-06: add generated scene art +
kiwi mascot") and push to `claude/second-reel-script-assets-8rulhj`.

If ANY download returns 403 / HTTP 000 mid-run, STOP and report which scene failed — do not keep
spending credits on images that can't be saved.
