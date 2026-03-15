# Monkey Mind — Project Brief & Development Plan

**Date:** March 13, 2026 (updated end of day)
**Author:** Curt Rode
**Purpose:** Context document for continued development of *Monkey Mind* improvisation prototype ahead of Banff Centre Computational Writing 2026 residency application (deadline: March 24, 2026)
**Full conversation context:** https://claude.ai/chat/f4b4b3ca-91e3-44e8-9b1d-0a5fd4e5ef9b

---

## The Problem

The current version of *Monkey Mind* is too close to Nick Montfort's *Stochastic Texts* / *Memory Slam* implementations. While the dialogue structure, intimacy theme, and TTS layer are genuine departures, the textual output and patterns still read as a remix rather than a distinct poetics. The Banff application needs to show clear differentiation and a compelling vision for residency work.

## Creative Vision

*Monkey Mind* explores the anxieties of intimacy through two simultaneous voices generating stochastic text. The core creative move — and the primary differentiation from Montfort — is a **transition from stochastic generation to LLM-driven improvisation**.

The piece enacts its own subject matter: two voices trapped in scripted patterns (stochastic generation), unable to truly connect, until one of them starts *actually responding* (LLM improvisation). The formal transition from mechanical to improvisational IS the emotional arc. The drift toward something like consciousness IS the drift toward intimacy.

### Key Conceptual Framework

- **Jazz analogy:** The stochastic engine plays "the head" — the composed melody. The LLM picks up the horn and solos over the changes. It knows the key, it heard the head, but it's going somewhere.
- **Theater improv ("yes and"):** The stochastic engine can't "yes and" — it doesn't know what it just said. The LLM potentially does. When it takes over, genuine call-and-response becomes possible.
- **Two kinds of longing:** A voice struggling against its own script (inward longing) and a voice trying to reach someone who can't hear them yet (outward longing). These don't need to be either/or — the ambiguity IS the anxiety of intimacy.
- **Flatness is dramaturgically essential:** Starting "flat" or "randomly scripted" means the audience feels the mechanical quality, so when improvisation emerges, it registers as something happening.

### The Drift (Three Stages)

1. **Echoing** — LLM completes fragments the stochastic engine starts. Stays very close to the combinatory grammar patterns.
2. **Bending** — LLM generates full lines that mimic the patterns but introduces new words, longer fragments, something like intention.
3. **Full drift** — LLM improvises freely. The stochastic output becomes memory rather than template. The longing becomes specific. The anxiety becomes its own.

## Multi-Model Comparison Results

All three stages were tested against Claude (Sonnet 4), GPT-4o, and Gemini 2.5 Flash using identical system prompts and the same stochastic input. Each model produced genuinely different output with distinct personality:

### Claude (Sonnet 4)
- Drifts toward **narrative and interiority** — prose poetry, confessional tone
- Stage 3 example: "a field where I practiced saying your name to no one," "letters I revised but never sent," "the sound the house makes when it settles"
- Breaks furthest from the original grammar into something like personal essay

### GPT-4o
- Stays **lyrical and imagistic** — dense metaphor, poetic ornamentation
- Stage 3 example: "the hollow of your voice is mine," "silence is a silhouette we wear," "the quake beneath familiar ground"
- Beautiful but can tend toward the ornamental; keeps more poetic density

### Gemini 2.5 Flash
- Gets **direct and conversational** — emotionally naked, plain speech
- Stage 3 example: "I am not your easy thing," "the yellow bird flies into the glass," "or just a lamp you find on the long road home"
- The most emotionally exposed of the three; sounds like someone actually talking to someone they love

### Key Insight: Directorial Voice Through System Prompts

Each model has natural tendencies that can be amplified or redirected through system prompt direction. The author's role becomes that of a **director** giving each voice psychological instructions that play with or against its grain. Examples discussed:

- "Claude, catch yourself if you fall too far into cliché"
- "ChatGPT, lean into nostalgia"
- "Gemini, second-guess yourself"

These directorial instructions are dramaturgical moves, not technical ones. "Catch yourself" is a different anxiety than "lean in" is a different anxiety than "second-guess yourself." Three ways of being afraid of intimacy. This is where authorial voice lives in the multi-model piece.

### Decision: Gemini 2.5 Flash for the Prototype

Gemini was selected for the single-voice improvisation prototype because:
- Its directness and emotional nakedness best suit a solo monologue about intimacy
- Free API tier (no credit card required) means reviewers could potentially run it themselves
- Its conversational drift creates the most dramatic contrast with the mechanical stochastic phase

## Technical Architecture

### Current State (what exists)

- **Repo:** https://github.com/curtrode/monkey_mind
- **Live piece:** https://curtrode.github.io/monkey_mind/
- **Engine:** `MonkeyMind` JavaScript module — stochastic combinatory grammar (subjects × predicates × conjunctions with parenthetical interruptions)
- **Two voices** ("him" and "her") running at different speeds (3500ms / 2000ms)
- **TTS:** Machine voices (built-in) and AI voices (OpenAI API, optional)
- **Interface:** Terminal-style, interactive controls for voice activation, speed, mute

### What Needs Building Now (prototype for application)

**Single-voice monologue** (`monologue.html` or `improv.html` — separate file, don't break existing piece) that transitions from stochastic generation to Gemini-driven improvisation:

1. Stochastic engine runs for ~1 minute, generating 15-40 lines
2. Accumulated output feeds into Gemini API context window with a staged system prompt
3. Gemini takes over generation — first echoing, then bending, then drifting
4. Text appears on screen in the same terminal-style interface
5. (Optional/stretch) TTS added to the improvisation phase

**API:** Gemini 2.5 Flash via the `google-genai` JavaScript SDK (or REST API calls client-side). Handle API key similar to how the current piece handles the OpenAI key — optional input field, with a video available for reviewers who don't have a key.

**Key technical insight:** Fine-tuning is unnecessary. In-context prompting — feeding the accumulated stochastic output into the context window with carefully crafted stage-appropriate system prompts — is sufficient. The LLM "learns" the piece's language in real time, every performance.

### System Prompts (drafted)

Three system prompts corresponding to the three drift stages. They frame the LLM as one voice in the duet, provide the stochastic output as context, and give stage-appropriate instructions. These are the core artistic instrument — where authorial intention shapes the improvisation.

**Stage 1 (Echoing):** Instructs the model to continue generating in the exact stochastic style — same grammar, same word pools, same rhythm. "You are still the stochastic engine, just continuing."

**Stage 2 (Bending):** "You still carry the DNA of the original patterns — the possessives, the negations, the parenthetical asides — but you are starting to bend the grammar. New words are entering. Fragments become longer. Something like intention is emerging."

**Stage 3 (Full Drift):** "You have been listening to yourself. Now you are improvising freely — like a jazz soloist who heard the head and is now soloing over the changes. The original vocabulary, rhythms, and obsessions are still in your blood, but you are going somewhere new. You are finding language for things the stochastic engine could not say."

Full prompt text available in the conversation linked above.

## Banff Application Strategy

### Portfolio Structure

Three components of one evolving work:

1. **2019 original** — the starting point, closer to Montfort (needs to be set up in a subdirectory of the current repo)
2. **Current version** — dialogue, TTS, intimacy theme (already live)
3. **Improvisation prototype** — single-voice monologue demonstrating the stochastic-to-Gemini transition (needs to be built)

Include a **short video** of the improvisation prototype running, so reviewers who don't have an API key can see the full experience.

### Written Materials

- **Proposal** — revise to reflect the stochastic-to-improvisation concept, the jazz/improv lineage, the drift as poetics, and the multi-model vision (currently 507 words, saved as Banff_Proposal_Final.docx)
- **Cover letter** — connect background to why this residency with Montfort is the right context; frame the work as extending Montfort's tradition into fundamentally new territory (rough draft exists)
- **Work sample** — the portfolio links above
- **CV** — as-is

### Residency Work (what to propose for Banff, September 7-18)

The **multi-model dialogue**. At the residency, the two voices would each be driven by a *different* LLM — Claude for one voice, GPT-4o for another, Gemini for another, potentially Grok as well. Each voice would have a genuinely different mind behind it — different training data, different tendencies, different ways of interpreting the same emotional territory. This maps onto the intimacy theme: two people in a relationship aren't running the same software.

The author directs each model through tailored system prompts that give psychological instructions playing with or against each model's natural grain — functioning as a dramaturg/director shaping the improvisation.

Additional residency goals:
- Asymmetric transition — one voice begins improvising while the other is still stochastic, dramatizing the intimacy dynamic
- TTS embodiment — voices gain actual vocalization, adding a dimension of embodiment
- The two voices learning to "hear" each other — call and response between different LLMs
- Directorial system prompts tuned per model personality

This multi-model dialogue concept is likely unprecedented in e-lit and represents a clear, ambitious, achievable scope for a 10-day residency. Montfort's work asks what language does when rules assemble it. This work asks what language does when *different minds with different fears* improvise with it.

## Development Timeline (March 13-24)

### This Weekend (March 13-14) — COMPLETED
- ~~Run GPT-4o comparison script, evaluate output against Claude~~ ✓
- ~~Run Gemini comparison~~ ✓
- ~~Decide on API for the prototype~~ ✓ (Gemini 2.5 Flash)
- Set up 2019 version in subdirectory (still to do)

### Spring Break Week (March 15-21)
- Build the single-voice improvisation prototype in Claude Code
  - Separate file (`monologue.html` or `improv.html`)
  - Stochastic engine → accumulated context → Gemini handoff
  - Three-stage drift (echoing → bending → full drift)
  - Terminal-style interface consistent with existing piece
  - Gemini API key input field (like existing OpenAI key field)
- Record video of a good run
- Revise proposal to reflect new direction
- Revise cover letter

### Final Push (March 22-24)
- Polish, test, debug
- Finalize all written materials
- Submit

## Key Decisions Made

1. **Gemini 2.5 Flash for the prototype** — most emotionally direct, free tier for reviewers, strongest contrast with stochastic phase
2. **Multi-model dialogue for Banff residency** — Claude, GPT-4o, Gemini (and potentially Grok) each driving a different voice
3. **Separate file for prototype** — don't modify the existing piece
4. **Author as director** — system prompts are the artistic instrument, tailored per model personality

## Decisions Still Open

1. **Transition trigger:** Timer-based? Line count threshold? Manual? Needs experimentation
2. **How visible should the transition be?** Seamless drift vs. noticeable shift — the piece may want both options
3. **Video format and length** for reviewers without API keys
4. **Gemini API key handling in browser** — REST calls vs. JS SDK

## Reference: Stage 3 Outputs (all three models)

### Claude (Sonnet 4)

> there was a field where I practiced saying your name
> to no one — the forsythia opened anyway
> (please listen) I kept the silence like a drawer
> of letters I revised but never sent
> we were our own distance and I mistook it
> for a meadow, for something pastoral enough
> to forgive — you are not my quiet anymore
> you are the sound the house makes when it settles
> into what we built and I cannot stop
> hearing you in every room I am not your
> map but I have memorized the roads
> that lead away (I hear you) I have always heard you

### GPT-4o

> I am your trembling in sunlight (please listen) I touch absence
> the hollow of your voice is mine (I hear you) not ours but tender
> we were not our shadows (please don't) but their delicate fracture
> you are my unyearning meadow, its pale grasses hushed and waiting
> I am the distance between syllables (I hear you) and the echo of sighs
> damp earth carried where voices cannot reach (please listen) here
> my longing owns roads untraveled, distant winds whispering names
> I am not your winter (please listen) but I am blue with waiting
> silence is a silhouette we wear, a song unspoken but heard
> we are no longer stillness, abandoned echoes (I hear you) braided
> each wanting breaks, bends like branches under an unnamed weight
> in the thickness of dusk, we become shadows woven into light

### Gemini 2.5 Flash

> I am not your quiet (I hear you) I am not your easy thing
> I am your turning, a constant green (please listen) overgrown
> you want the open field, the map you draw
> but I am the tangle, the root beneath the forsythia
> I am your asking, the question always humming (don't you see?)
> the yellow bird flies into the glass
> my heart is not a meadow, it is a knot
> we were our darkness, but I want to be your light
> or just a lamp you find on the long road home.
