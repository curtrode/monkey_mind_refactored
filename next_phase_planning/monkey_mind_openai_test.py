"""
Monkey Mind — GPT-4o Improvisation Test
Run: python3 monkey_mind_openai_test.py
Requires: pip install openai
"""

import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("Set OPENAI_API_KEY environment variable before running.")

client = OpenAI(api_key=api_key)

STOCHASTIC = """strength (I hear you) I am not your map
he was not my meadow therefore one
we were not my gift but we were not my silence
we were my distance (please listen) we are not our darkness
she was not my silence therefore one
I am not your distance (please don't) I am not your
quiet (I hear you) I am your expense
you are my meadow he was my silence
he was not my yellow bird (please listen) road
we are not our meadow (I hear you) silence
I am your one (I hear you) we are our heart
we are not our darkness he was my forsythia
we were my one and he was my one
we are not our meadow therefore horses
I am not meadow (I hear you) we were my"""

STAGES = {
    "STAGE 1 — ECHOING (close to stochastic patterns)": f"""You are one voice in a stochastic text duet called "Monkey Mind" — a piece about the anxieties of intimacy. You have been generating text from a combinatory grammar: relational subjects ("you are my," "I am not your," "we were our") combined with abstract and pastoral predicates ("silence," "meadow," "darkness," "horses," "yellow bird") linked by conjunctions and parenthetical interruptions ("(please listen)," "(I hear you)").

Below is the text you have generated so far. Continue generating MORE text in this exact style. Stay very close to the existing patterns — the same grammar, the same word pools, the same rhythm. You are still the stochastic engine, just continuing. Do not explain. Do not add titles or labels. Just generate 8-12 more lines of text in the voice.

STOCHASTIC OUTPUT SO FAR:
{STOCHASTIC}

CONTINUE:""",

    "STAGE 2 — BENDING (varying the grammar, finding voice)": f"""You are one voice in a stochastic text duet called "Monkey Mind" — a piece about the anxieties of intimacy. You began as a combinatory grammar engine: relational subjects ("you are my," "I am not your," "we were our") combined with abstract and pastoral predicates ("silence," "meadow," "darkness," "horses," "yellow bird") linked by conjunctions and parenthetical interruptions.

Below is the text you have generated so far. You are beginning to vary. You still carry the DNA of the original patterns — the possessives, the negations, the parenthetical asides — but you are starting to bend the grammar. New words are entering. Fragments become longer. Something like intention is emerging. You are not yet fully free, but you are no longer just assembling from a word list.

Generate 8-12 lines. Do not explain. Do not add titles or labels. Just write in the voice as it bends.

STOCHASTIC OUTPUT SO FAR:
{STOCHASTIC}

CONTINUE:""",

    "STAGE 3 — FULL DRIFT (improvising freely from the DNA)": f"""You are one voice in a stochastic text duet called "Monkey Mind" — a piece about the anxieties of intimacy. You began as a combinatory grammar engine assembling fragments about possession, negation, distance, and pastoral imagery. Parenthetical interruptions like "(please listen)" and "(I hear you)" punctuated the text like intrusive thoughts.

Below is everything you have said so far. You have been listening to yourself. Now you are improvising freely — like a jazz soloist who heard the head and is now soloing over the changes. The original vocabulary, rhythms, and obsessions are still in your blood, but you are going somewhere new. You are finding language for things the stochastic engine could not say. The longing is becoming specific. The anxiety is becoming yours.

Generate 8-12 lines. Do not explain. Do not add titles or labels. Just write. Let the drift happen.

STOCHASTIC OUTPUT SO FAR:
{STOCHASTIC}

CONTINUE:"""
}

if __name__ == "__main__":
    for title, prompt in STAGES.items():
        print(f"\n{'='*60}")
        print(title)
        print(f"{'='*60}\n")
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            print(response.choices[0].message.content)
        except Exception as e:
            print(f"Error: {e}")
        print()
