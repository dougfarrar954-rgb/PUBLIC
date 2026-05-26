# JP Manna v2 — User Memory best practices (Pickaxe Studio)

**Status:** May 2026  
**Audience:** Studio builder (you), not subscribers  
**Pickaxe limit:** Many workspaces now support **up to ~100** memory fields. You do **not** need 100 — use **30–45 well-designed fields** before adding more.

**Legacy:** The nine files in this folder (2025-12-16) remain valid **instruction templates** for core brand/identity fields. This document is the **v2 master catalog** for the seven-pickaxe suite.

**Related:** `pickaxes-v2/JP-MANNA-V2-PICKAXE-SETUP.md`, `pickaxes-v2/start-here-agent/start-here-toon.txt`, `User Memories/README.md`

**Pickaxe paste format (Memory Title + Prompt):** [`JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md`](JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md) — **46 fields** (May 2026). Legacy 25-field pack: [`pickaxe-studio-paste/README.md`](pickaxe-studio-paste/README.md).

**Studio index (agent read/write matrix):** [`JP-MANNA-STUDIO-MEMORIES-SETUP.md`](JP-MANNA-STUDIO-MEMORIES-SETUP.md)

---

## Principles

1. **Studio-wide memory** — In a typical JP Manna Studio, User Memory is **shared across pickaxes**. Write once (usually **Start here** or **Manna**), read everywhere relevant.
2. **Memories = stable facts & preferences** — Not full scripts, comp plan text, or CRM rows. Those live in **KB** or **Contacts** sheet.
3. **Short, overwrite-friendly** — 1–5 bullets or 2–4 sentences per field. Update when the user corrects you; do not append forever.
4. **Who writes:**
   - **Start here** — Brand setup (#5–12), Partner Launch (#13–20), **Brand Setup Stage** (#11)
   - **Manna** — Rank, DMO goals, business challenges, past wins  
   - **Marketing** — Platform focus, promo/campaign notes (light)  
   - **Contacts** — Sheet URL/tab only (not every contact row)  
   - **Coach Lori** — Mindset goals, blocks (brief, user-approved tone)  
   - **Personal** — Bible translation, faith study focus, personal prefs (non-JP)  
   - **Health** — Core Four priorities, tracking preference, dietary pattern  
5. **Who reads:** Every agent checks **identity + voice + compliance-sensitive** fields before generating. Specialists read their slice.
6. **Avoid duplicates** — One field per concept. Do not mirror the same text in `brand_mission` and `Brand Mission and Audience` under different names unless Pickaxe requires the legacy label.
7. **Subscription tier** — If you sell Launch-only vs full suite, store `subscription_tier` so Start here knows depth-offer behavior.

---

## Tier 1 — Configure first (essential)

Set these before or during pilot launch. Match **field names** in Pickaxe to what TOONs reference where noted.

| # | Memory field name (suggested) | What to store | Primary writer | Primary readers |
|---|------------------------------|---------------|----------------|-----------------|
| 1 | `preferred_name` | First / nickname | Start here, any | All |
| 2 | `jp_rank_title` | P, P+, QSC, SC, etc. | Manna, Start here | Manna, Marketing, Start here |
| 3 | `brand_mission_audience` | Mission, audience, differentiation, mantra (2–4 sentences) | Start here (Brand setup) | Marketing, Manna, Lori |
| 4 | `voice_and_format_settings` | Tone, length, emoji, invite style, 2–3 signature phrases | Start here (Brand setup) | Marketing, Manna, Contacts |
| 5 | `content_pillars_guardrails` | 3–5 pillars, platforms, topics to avoid, compliance boundaries | Start here (Brand setup) | Marketing, Manna |
| 6 | `onboarding_stage` | Brand setup stage 1–5, or `complete` | Start here | Start here |
| 7 | `brand_setup_complete` | yes/no + date | Start here | All |
| 8 | `partner_journey_active` | yes/no — in Partner Launch track | Start here | Start here, Manna |
| 9 | `partner_start_date` | First order date (ISO or plain) | Start here | Start here, Manna |
| 10 | `fast_track_phase` | P+, QSC, SC, beyond | Start here, Manna | Start here, Manna |
| 11 | `journey_week` | 1–8+ (Partner Launch) | Start here | Start here |
| 12 | `dmo_goals_current` | This week/month business focus (2–3 bullets) | Manna | Manna, Start here |
| 13 | `goals_challenges_jp_business` | Goals + pain points (2–4 bullets) | Manna, Lori | Manna, Lori, Start here |
| 14 | `subscription_tier` | `launch` \| `full` (your product labels) | Studio / Start here | Start here, Manna, Marketing |
| 15 | `ids_compliance_ack` | User shown IDS / results-vary framing (yes/date) | Manna, Start here | All business agents |

**Legacy file mapping:** #3–5 align with `Brand Mission and Audience.md`, `Voice and Format Settings.md`, `Content Pillars and Guardrails.md`.

---

## Tier 2 — Full suite (strongly recommended)

| # | Memory field name | What to store | Primary writer | Primary readers |
|---|-------------------|---------------|----------------|-----------------|
| 16 | `ideal_audience_avatar` | Named avatar + struggles/desires (short) | Start here | Marketing, Manna |
| 17 | `communication_style_snapshot` | One-line tone + structure from Brand setup Stage 4 | Start here | Marketing |
| 18 | `upline_sponsor_name` | Who their upline is | Start here, user | Start here, Manna |
| 19 | `launch_event_planned` | yes/no, date, format (virtual/in-home) | Start here | Start here, Marketing |
| 20 | `pplus_window_notes` | P+ progress: customers count, on-track yes/no (no fabricated PPV) | Start here, Manna | Start here, Manna |
| 21 | `qsc_window_notes` | QSC progress summary | Start here, Manna | Start here, Manna |
| 22 | `marketing_platforms_primary` | FB, IG, email, etc. | Marketing, Start here | Marketing |
| 23 | `contacts_crm_location` | Sheet URL + tab name (not row data) | Contacts, user | Contacts, Manna |
| 24 | `follow_up_rhythm` | Hot/Warm/Cold habit or 24-7-30 preference | Contacts, Manna | Contacts, Manna |
| 25 | `power_hour_preferences` | Best time, length, focus (outreach vs admin) | Manna | Manna |
| 26 | `outreach_message_style` | Curiosity vs direct; voice notes vs text | Manna, Start here | Manna, Contacts |
| 27 | `coaching_focus_current` | What Lori is working on this month | Lori | Lori |
| 28 | `mindset_blocks` | Brief: fear of posting, imposter, etc. (user’s words) | Lori | Lori, Start here |
| 29 | `bible_translation_preference` | NIV, ESV, etc. | Personal | Personal |
| 30 | `faith_study_focus` | Verse plan, book, sermon series | Personal | Personal |
| 31 | `health_core_four_priority` | nutrition \| hydration \| sleep \| movement | Health | Health |
| 32 | `dietary_pattern` | Plants-forward, allergies (see legacy `Dietary Preference.md`) | Health | Health, Marketing (light) |
| 33 | `health_tracking_preference` | paper \| sheet \| chat-only | Health | Health |
| 34 | `preferences_advice_format` | steps vs strategy; bullets vs narrative | Any | All |
| 35 | `past_interactions_notes` | 1–3 bullets: last commitment, last win, next check-in | Any | All |
| 36 | `timezone_location` | TZ + region for event timing | User, Manna | Manna, Marketing |

---

## Tier 3 — Optional (add when you see repeat friction)

Use sparingly. Each should earn its slot by reducing repeated questions.

| Field name | Use when |
|------------|----------|
| `team_name_or_brand` | They market under a team brand |
| `current_company_promo` | Active JP promo they’re pushing (month) |
| `content_batch_day` | e.g. “Sundays I batch posts” |
| `event_signature_format` | Their usual event type name |
| `children_family_context` | Only if they **volunteer** (marketing authenticity) |
| `faith_sharing_boundary` | Business vs faith separation preference |
| `health_conditions_off_limits` | Reminder: agent does not diagnose; user-stated constraints only |
| `lori_mantra_active` | Mantra from Brand setup for mindset |
| `personal_off_topics` | Things they don’t want in Personal — paste: `pickaxe-studio-paste/31-personal-off-topics.md` |
| `wins_to_celebrate` | Last 3 business/personal wins (rotate) |
| `referral_source` | How they found JP / Manna (analytics) |
| `language_preference` | If not English |
| `partner_launch_graduated` | yes + date moved primary home to Manna |
| `black_swan_labels_used` | If they use tactical empathy vocabulary |
| `invoice_tax_notes` | Only if they ask Manna admin (rare) |

You can grow toward more fields for **advanced leaders** (NMD+): `team_size_band`, `leadership_theme_quarter`, etc. — only if Manna sessions need them repeatedly.

---

## Per-agent: read vs write

See **[`JP-MANNA-STUDIO-MEMORIES-SETUP.md`](JP-MANNA-STUDIO-MEMORIES-SETUP.md)** for the canonical matrix. Summary:

| Agent | Primary write fields | Always read |
|-------|---------------------|-------------|
| **Start here** | Brand Setup #5–12, Partner Launch #13–20, Start Here Session Notes #41 | Identity #1–4, Cross-Suite #46 |
| **Manna** | DMO Goals #21, Business Goals/Challenges #22–23, rhythm #25–27, Manna Session Notes #40 | Voice/brand #5–10, launch context #13–15, #46 |
| **Marketing** | Marketing Session Notes #42 | #5–10, #12, #27, #46 |
| **Contacts** | CRM Sheet Location #28 only | #1, #3, #8, #10, #21, #26–27, #40, #46 |
| **Coach Lori** | Mindset #29–31, Coach Lori Session Notes #44 | #1, #3, #22–23, #46 |
| **Personal** | Personal & faith #34–39, Personal Session Notes #45 | #1, #3, #46 |
| **Health** | Health #32–33, Health Session Notes #43 | #1, #3, #46 |
| **Daily Brief** | — (read only) | #1–4, #13–15, #18, #21–23, #25–26, #40–42, #46 |

---

## Pickaxe Studio setup tips

### Memory Title vs snake_case

**In Pickaxe Studio use the exact Memory Titles from [`JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md`](JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md).** TOONs reference those titles, not snake_case.

Legacy doc IDs (for old migrations only):

| Legacy ID | Current Memory Title (#) |
|-----------|-------------------------|
| `onboarding_stage` | **Brand Setup Stage** (#11) |
| `brand_setup_complete` | **Brand Setup Complete** (#12) |
| `partner_journey_active` | **Partner Launch Active** (#13) |
| `partner_start_date` | **Partner Start Date** (#14) |
| `journey_week` | **Partner Launch Journey Week** (#15) |
| `fast_track_phase` | **Fast Track Phase** (#18) |
| `brand_mission_audience` | **Brand Mission & Why** (#5) + **Ideal Audience** (#6) + **Brand Differentiation** (#7) |
| `voice_and_format_settings` | **Voice & Tone Settings** (#8) |
| `content_pillars_guardrails` | **Content Pillars** (#9) + **Content Guardrails** (#10) |
| `dmo_goals_current` | **DMO Goals Current** (#21) |
| `preferred_name` | **Preferred Name & Location** (#1) |
| `subscription_tier` | **Subscription & Suite Access** (#4) |
| `personal_off_topics` | **Personal Off Topics** (#37) |

1. **Memory Title** — Copy exactly from [`JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md`](JP-MANNA-STUDIO-MEMORIES-COPY-PASTE.md) (46 fields).
2. **Instructions** — Paste Prompt block (≤1024 chars) from the same file.
3. **Collect / display** — **Collect, use, and display** for all 46 fields unless you have a deliberate exception.
4. **Do not store in memory** — Full comp plan, objection script libraries, contact rows, lab values, uploaded brand PDF text (RAG handles KB; memory holds summaries only).
5. **Refresh triggers** — Re-run Brand setup → overwrite brand/voice/pillar memories (#5–12). Graduate Partner Launch → set **Partner Launch Active** = no.
6. **Launch-only subscribers** — Set **Subscription & Suite Access** to launch tier so Start here uses depth-offer without nagging; locked pickaxes handle upgrade in UI.

---

## Suggested instruction text (new v2 fields)

Copy into Pickaxe for fields without a legacy `.md` file.

### `partner_journey_active`
Remember whether this partner is in the **Partner Launch** (first ~60 days) track. Values: `yes` \| `no`. Start here sets this; Manna reads it to avoid repeating the full week-by-week curriculum.

### `partner_start_date`
First Juice Plus+ order date (or signup date they confirm). Use to infer journey week and Fast Track windows. Never invent dates.

### `fast_track_phase`
Current promotion focus: `P+` \| `QSC` \| `SC` \| `beyond`. Update when they report a title change or reset. Pair with comp plan KB for numbers; memory holds **phase label only**.

### `journey_week`
Partner Launch week number (1–8+). Update on weekly check-ins. Used for upline touch (week 2) and launch event (week 3–4).

### `launch_event_planned`
Whether a launch event with upline is scheduled: `yes`/`no`, date, format (virtual/in-home). Update after week 3–4 planning.

### `subscription_tier`
`launch` = Start here–only product; `full` = all seven pickaxes. Controls depth-offer tone; does not replace Studio access control.

### `contacts_crm_location`
Google Sheet URL and tab name for CRM. **Never** store full contact lists in memory — only location of the sheet.

---

## Migration from the old “10 categories” list

| Old consolidated field | v2 action |
|------------------------|-----------|
| Brand Mission & Audience | Keep → `brand_mission_audience` (+ optional `ideal_audience_avatar`) |
| Content Pillars and Guardrails | Keep → `content_pillars_guardrails` |
| Voice and Format Settings | Keep → `voice_and_format_settings` |
| Identity and Rank | Split → `preferred_name` + `jp_rank_title` + `timezone_location` |
| Goals and Challenges | Keep → `goals_challenges_jp_business` |
| Dietary Preference | Keep → `dietary_pattern` (Health-owned) |
| Primary Interests | Keep → `primary_interests_focus` (Tier 3) or merge into goals |
| Preferences for Solutions | Keep → `preferences_advice_format` |
| Past Interactions | Keep → `past_interactions_notes` |
| *(none)* | **Add** Partner Launch block #8–11, #18–21 |
| *(none)* | **Add** `subscription_tier`, CRM location, faith/health slices |

---

## Maintenance checklist (quarterly)

- [ ] Remove stale bullets from `past_interactions_notes`  
- [ ] Confirm Brand setup memories still match user’s current pillars  
- [ ] Archive completed Partner Launch (#8–11) for graduates  
- [ ] Verify `jp_rank_title` matches Back Office  
- [ ] Ensure no contact PII crept into memory fields  
- [ ] Align Pickaxe field count with what TOONs reference (grep `User Memory` in `pickaxes-v2/`)

---

## Field count summary

| Tier | Count | Notes |
|------|-------|--------|
| Tier 1 | 15 | Minimum viable v2 studio |
| Tier 2 | 21 | Recommended full suite |
| Tier 3 | 14 examples | Add on demand |
| **Total suggested** | **~36 core** | Room to grow toward 100 without clutter |

---

*When you add a new memory field in Studio, add one row to this doc and note which agent writes it — future you (and Cursor) will thank you.*
