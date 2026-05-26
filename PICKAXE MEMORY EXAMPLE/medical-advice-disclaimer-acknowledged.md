# Medical Advice Disclaimer Acknowledged

**Memory Title:** `Medical Advice Disclaimer Acknowledged`

**Prompt (paste into Pickaxe User Memory field, ≤1024 chars):**

```
Record whether this user has explicitly confirmed they understand this agent is NOT providing medical advice, diagnosis, or treatment.

Store:
- acknowledged: yes or no
- date_acknowledged: date they confirmed (if yes)
- confirmation_phrase: optional — short quote of how they confirmed (e.g. "I understand", "got it")

Rules for the agent:
- If acknowledged = no or empty: deliver the full not-medical-advice disclaimer and ask for clear confirmation before habit coaching. Do not skip.
- If acknowledged = yes: continue normal coaching; a one-line reminder is OK on sensitive topics but do not re-run the full onboarding every message.
- Re-prompt if user asks for diagnosis, medication changes, or emergency guidance — then still do not provide medical directives.
- Never store symptoms, diagnoses, or medication lists in THIS field — only the acknowledgment status.

Set yes only after the user gives an explicit affirmative (not silence or "ok" to an unrelated question). Overwrite if they later revoke understanding.
```
