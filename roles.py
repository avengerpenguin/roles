import json

from builtins import input


def flip(letters):
    if len(letters) == 0:
        return letters

    letter = letters[0]

    flipped =  {
        "I": "E",
        "E": "I",
        "N": "S",
        "S": "N",
        "T": "F",
        "F": "T",
        "P": "J",
        "J": "P",
    }[letter]

    if len(letters) > 1:
        return flipped + flip(letters[1:])
    else:
        return flipped


def role(initials):
    return {
        "EN": "Detective",
        "IT": "Logician",
        "EF": "Friend",
        "IS": "Teacher",
        "IN": "Philosopher",
        "ET": "Challenger",
        "IF": "Counsellor",
        "ES": "Adventurer",
        "NT": "Innovator",
        "EP": "Explorer",
        "NP": "Creative",
        "TP": "Analyst",
        "IJ": "Leader",
        "SJ": "Organiser",
        "NF": "Idealist",
        "NJ": "Visionary",
        "FJ": "Messenger",
        "SF": "Communitarian",
        "ST": "Tradionalist",
        "EJ": "Driver",
        "IP": "Advisor",
        "SP": "Adapter",
        "TJ": "Architect",
        "FP": "Understanding",
    }[initials]


def villain(initials):
    return {
        "IJ": "Desperation",
        "IS": "Uninspired",
        "SF": "Abandoning Projects",
        "FJ": "Progress Frustration",
        "SJ": "Uncreative: Analysis-Paralysis",
        "EP": "Distracted Leader",
        "SP": "Frenzy",
        "TP": "Critical",
        "ST": "Reactionary",
        "ES": "Overwhelm",
        "IP": "Perfectionist?",
        "NP": "Tantrum?",
        "IT": "Hyper-Critical",
        "NT": "Low Confidence",
        "FP": "Bossy",
    }[initials]


def main(mbti_type):
    energy, perception, judgement, lifestyle = mbti_type

    if energy == 'E':
        if lifestyle == 'J':
            lead = energy + judgement
            hidden = flip(energy) + perception
        else:
            lead = energy + perception
            hidden = flip(energy) + judgement

        dom, aux = lead, hidden
    else:
        if lifestyle == 'J':
            lead = flip(energy) + judgement
            hidden = energy + perception
        else:
            lead = flip(energy) + perception
            hidden = energy + judgement
        dom, aux = hidden, lead

    ter = flip(aux)
    inf = flip(dom)

    opp = flip(dom[0]) + dom[1]
    crit = flip(aux[0]) + aux[1]
    trick = flip(ter[0]) + ter[1]
    demon = flip(inf[0]) + inf[1]

    worldview = perception + judgement
    temperament = energy + lifestyle

    intelligences = {
        perception + lifestyle,
        judgement + lifestyle,
    }

    # stress -- retain energy, but flip lifestyle
    stress_temperament = flip(temperament)
    stress_intelligences = {flip(intelligence) for intelligence in intelligences}

    # anxiety -- retain lifestyle, but flip energy
    stress_dom = flip(dom)

    # "Other" -- both energy and lifestyle retained, but values shifted
    stress_worldview = flip(worldview)

    growth_stretch = flip(judgement + lifestyle)
    growth_bar = perception + flip(lifestyle)
    growth_mindset = perception  + flip(judgement)
    growth_baz = energy + flip(lifestyle)

    mentor_adult = energy + flip(judgement)
    mentor_int1 = judgement + lifestyle
    mentor_int2 = flip(perception) + lifestyle
    mentor_mindset = flip(perception) + judgement
    mentor_temperament = flip(energy) + lifestyle

    data = {
        "functions": {
            "hero_ego_leading": f"{role(dom)} ({dom})",
            "master_ego_creative": f"{role(aux)} ({aux})",
            "student_super_id_mobilizing_hidden_agenda": f"{role(ter)} ({ter})",
            "rival_super_id_suggestive": f"{role(inf)} ({inf})",
            "muse_id_ignoring": f"{role(opp)} ({opp})",
            "child_id_demonstrative": f"{role(crit)} ({crit})",
            "adult_super_ego_vulnerable": f"{role(trick)} ({trick})",
            "slave_super_ego_role": f"{role(demon)} ({demon})",
        },
        "worldview": f"{role(worldview)} ({worldview})",
        "temperament": f"{role(temperament)} ({temperament})",
        "intelligences": [
            f"{role(intelligence)} ({intelligence})"
            for intelligence in intelligences
        ],
        "flow": {
            "natural": f"{role(dom)} ({dom})",
            "aligned": f"{role(worldview)} ({worldview})",
            "energetic": f"{role(temperament)} ({temperament})",
            "intellectual": [
                f"{role(intelligence)} ({intelligence})"
                for intelligence in intelligences
            ],
            "fun": f"{role(crit)} ({crit})",
        },
        "stuck": {
            "stress": {
                "drained": f"{villain(stress_temperament)} ({stress_temperament})",
                "fog": [
                    f"{villain(intelligence)} ({intelligence})"
                    for intelligence in stress_intelligences
                ],
            },
            "anxious": f"{villain(stress_dom)} ({stress_dom})",
            "giving_up": f"{villain(stress_worldview)} ({stress_worldview})",
        },
        "growth": {
            # Drops from dom to tertiary -- used to support, but downplay letting it dominate
            "playful": f"{role(dom)} ({dom})",
            # Tertiary is promoted to dominate as a key focus for development
            "focus": f"{role(ter)} ({ter})",
            # Alternative Worldview to tap into a little -- play a part
            "mindset": f"{role(growth_mindset)} ({growth_mindset})",
            # ?
            "push": f"{role(growth_stretch)} ({growth_stretch})",
            "stretch": f"{role(growth_bar)} ({growth_bar})",
            "broaden": f"{role(growth_baz)} ({growth_baz})",
        },
        "mentor": {
            # Opposite of dom (hero) and your rival/opposite leads -- needs restraint to be opposite to self
            "restraint": f"{role(inf)} ({inf})",
            # Be your best self tapping into your strong, but supporting master/aux self
            "best_self": f"{role(aux)} ({aux})",
            # Using one of your strengths, but the one most needed
            "strength": f"{role(mentor_int1)} ({mentor_int1})",
            # Flipped perception -- either pay zoom in to the data if P or zoom out if S
            "zoom": f"{role(mentor_int2)} ({mentor_int2})",
            "understand": f"{role(mentor_mindset)} ({mentor_mindset})",
            "temper": f"{role(mentor_temperament)} ({mentor_temperament})",
        }
    }

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    mbti_type = input('What is your MBTI? ').upper()
    main(mbti_type)
