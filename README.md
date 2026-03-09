# Monkey Mind

An interactive electronic literature piece featuring two voices generating stochastic poetry in real-time, with optional text-to-speech narration.

## Overview

Monkey Mind presents two concurrent streams of generative text—"him" and "her"—each producing phrases composed from randomized subjects, predicates, and conjunctions. The result is an evolving, meditative dialogue that explores themes of relationship, identity, and meaning through algorithmic composition.

Based on Theo Lutz's groundbreaking 1959 program *Stochastische Texte* (Stochastic Texts), reimplemented by [Nick Montfort](http://nickm.com).

## Features

- **Dual Generative Voices**: Two independent text generators with distinct word pools and timing
- **Text-to-Speech**: Listen to the generated poetry read aloud
  - Browser voices (built-in, no setup required)
  - OpenAI AI voices (natural-sounding, requires API key)
- **Stereo Panning**: AI voices are spatially positioned—"him" on the left, "her" on the right
- **Individual Muting**: Silence either voice independently
- **Visual Themes**: Distinct styling for each character with background imagery

## Getting Started

1. Open `index.html` in a modern web browser
2. Click anywhere on the overlay to begin
3. (Optional) Enter an OpenAI API key for enhanced AI voices

### Voice Options

| Mode | Setup | Quality |
|------|-------|---------|
| Browser Voices | None required | Basic, robotic |
| OpenAI TTS | API key required | Natural, expressive |

To use AI voices, enter your OpenAI API key in the input field before starting. The key is saved locally for future sessions.

## Project Structure

```
├── index.html              # Main application (combines both voices)
├── stochastic_thing2.html  # "Him" voice generator
├── stochastic_thing3.html  # "Her" voice generator
├── js/
│   └── monkey-mind.js      # Core stochastic text engine
├── css/
│   ├── base.css            # Shared styles
│   ├── him.css             # "Him" character styling
│   ├── her.css             # "Her" character styling
│   ├── presentation.css    # Presentation mode styles
│   └── text-only.css       # Minimal text-only theme
├── images/                 # Character background images
└── mockups/                # Alternative visual layouts
    ├── dark-gallery.html
    ├── split-screen.html
    └── terminal.html
```

## How It Works

The `MonkeyMind` module generates sentences by randomly combining:

- **Subjects**: Relationship phrases ("you are my", "I am not your", "we were our")
- **Predicates**: Abstract nouns ("silence", "dream", "darkness", "freedom")
- **Conjunctions**: Connectors with parenthetical asides ("and", "but", "(please listen)")

Each voice has its own word pool and interval timing, creating an organic, overlapping conversation effect.

## Roadmap

- **Flexible gender pairings**: Allow any combination of voices — him/him, her/her, him/they, they/her, they/they, etc. — moving beyond the current fixed him/her duet to support a wider range of identity and relationship dynamics

## Credits

- **Original Program**: Theo Lutz (1959) — *Stochastische Texte*
- **Reimplementation**: Nick Montfort
- **Text Translation**: Helen MacCormack

## License

```
Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

## Browser Compatibility

Requires a modern browser with:
- ES6 JavaScript support
- Web Speech API (for browser voices)
- Web Audio API (for AI voice stereo panning)
- Fetch API (for OpenAI TTS)

Tested in Chrome, Firefox, Safari, and Edge.
