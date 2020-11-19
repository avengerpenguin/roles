import os

from roles import flip
from jinja2 import Template
from markdown import Markdown


TYPES = ['ENTP', 'INFJ', 'INTP', 'ESFJ', 'ISFP']
with open('roles.md') as f:
    TEMPLATE = Template(f.read())


def get_role(purpose, code: str, variant):
    if not os.path.exists(f'roles/{code}-{variant}.md'):
        with open(f'roles/{code}-{variant}.md', 'w') as f:
            f.write(f'Title: {code} as {purpose}\n\nTODO: {code} as {purpose}\n')

    with open(f'roles/{code}-{variant}.md') as f:
        md = Markdown(extensions=['meta'])
        md.convert(f.read())
        role_info = md.Meta
        return {
            "purpose": purpose,
            "name": role_info['title'][0],
            "code": f"{code}-{variant}",
        }


def main():
    for mbti_type in TYPES:
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
        growth_mindset = perception + flip(judgement)
        growth_baz = energy + flip(lifestyle)

        mentor_adult = energy + flip(judgement)
        mentor_int1 = judgement + lifestyle
        mentor_int2 = flip(perception) + lifestyle
        mentor_mindset = flip(perception) + judgement
        mentor_temperament = flip(energy) + lifestyle

        data = {
            "type": mbti_type,

            "roles": [
                get_role('Muse', opp, 5),

                # Flow
                get_role('Leader', dom, 1),
                get_role('Fool', crit, 6),
                get_role('Priest', worldview, 'f'),
                get_role('Attitude', temperament, 'f'),
                get_role('CoreInt', perception + lifestyle, 'f'),
                get_role('SuppInt', judgement + lifestyle, 'f'),

                # Stress
                get_role('Grip', inf, '4-s'),
                get_role('Vuln', trick, 7),
                get_role('Crisis', flip(worldview), 's'),
                get_role('Desperation', flip(temperament), 's'),
                get_role('Stuck', flip(perception + lifestyle), 's'),
                get_role('Trap', flip(judgement + lifestyle), 's'),

                # Mentor
                get_role('Rival', inf, '4-m'),
                get_role('Adviser', aux, 2),
                get_role('Villain', demon, 8),
                get_role('EgoCheck', flip(energy) + lifestyle, 'm'),  # Stop and validate (is your intuition realistic) or zoom out and consider alternatives (check your senses)
                get_role('Zoom', flip(perception) + lifestyle, 'm'),  # Flip from abstract to concrete or vice versa
                get_role('Understand', flip(perception) + judgement, 'm'),  # Your worldview with the Zoom applied, Innovator <-> Pragmatist, Idealist <-> Communitarian

                # Growth
                get_role('Apprentice', ter, 3),
                get_role('Stretch', perception + flip(lifestyle), 'g'),  # Take your core skill and check for blindspots. Progress from ideas to a how-to plan or a challenge your "clear" vision with new data.
                get_role('Discipline', energy + flip(lifestyle), 'g'),  # Keeping in comfort zone a little (I/E), can you switch focus.
                get_role('Mindset', perception + flip(judgement), 'g'),  # Open worldview a little: loosen constraints of objectivity or be more objective/practical in your decisions
                get_role('Discomfort', flip(judgement + lifestyle), 'g'),  # Might need wrangling with trickster -- Go out of your comfort zone: J people change to P and rely on weaker T/F or P people change to J and do more with alternative T/F
            ],

            # "oldroles": {
            #     "flow": {
            #         "leader": {"name": role(dom), "description": FUNCTIONS["leader"][dom]},
            #         "adviser": {"name": role(aux), "description": FUNCTIONS["adviser"][aux]},
            #     },
            #     "mentor": {
            #         "adviser": {"name": role(aux), "description": FUNCTIONS["adviser"][dom]},
            #     },
            #     "growth": {
            #         "jester": {"name": role(crit), "description": FUNCTIONS["jester"][dom]},
            #     }
            # },
            #
            # "functions": {
            #     "hero_ego_leading": f"{role(dom)} ({dom})",
            #     "master_ego_creative": f"{role(aux)} ({aux})",
            #     "student_super_id_mobilizing_hidden_agenda": f"{role(ter)} ({ter})",
            #     "rival_super_id_suggestive": f"{role(inf)} ({inf})",
            #     "muse_id_ignoring": f"{role(opp)} ({opp})",
            #     "child_id_demonstrative": f"{role(crit)} ({crit})",
            #     "adult_super_ego_vulnerable": f"{role(trick)} ({trick})",
            #     "slave_super_ego_role": f"{role(demon)} ({demon})",
            # },
            # "worldview": f"{role(worldview)} ({worldview})",
            # "temperament": f"{role(temperament)} ({temperament})",
            # "intelligences": [
            #     f"{role(intelligence)} ({intelligence})"
            #     for intelligence in intelligences
            # ],
            # "flow": {
            #     "natural": f"{role(dom)} ({dom})",
            #     "aligned": f"{role(worldview)} ({worldview})",
            #     "energetic": f"{role(temperament)} ({temperament})",
            #     "intellectual": [
            #         f"{role(intelligence)} ({intelligence})"
            #         for intelligence in intelligences
            #     ],
            #     "fun": f"{role(crit)} ({crit})",
            # },
            # "stuck": {
            #     "stress": {
            #         "drained": f"{villain(stress_temperament)} ({stress_temperament})",
            #         "fog": [
            #             f"{villain(intelligence)} ({intelligence})"
            #             for intelligence in stress_intelligences
            #         ],
            #     },
            #     "anxious": f"{villain(stress_dom)} ({stress_dom})",
            #     "giving_up": f"{villain(stress_worldview)} ({stress_worldview})",
            # },
            # "growth": {
            #     # Drops from dom to tertiary -- used to support, but downplay letting it dominate
            #     "playful": f"{role(dom)} ({dom})",
            #     # Tertiary is promoted to dominate as a key focus for development
            #     "focus": f"{role(ter)} ({ter})",
            #     # Alternative Worldview to tap into a little -- play a part
            #     "mindset": f"{role(growth_mindset)} ({growth_mindset})",
            #     # ?
            #     "push": f"{role(growth_stretch)} ({growth_stretch})",
            #     "stretch": f"{role(growth_bar)} ({growth_bar})",
            #     "broaden": f"{role(growth_baz)} ({growth_baz})",
            # },
            # "mentor": {
            #     # Opposite of dom (hero) and your rival/opposite leads -- needs restraint to be opposite to self
            #     "restraint": f"{role(inf)} ({inf})",
            #     # Be your best self tapping into your strong, but supporting master/aux self
            #     "best_self": f"{role(aux)} ({aux})",
            #     # Using one of your strengths, but the one most needed
            #     "strength": f"{role(mentor_int1)} ({mentor_int1})",
            #     # Flipped perception -- either pay zoom in to the data if P or zoom out if S
            #     "zoom": f"{role(mentor_int2)} ({mentor_int2})",
            #     "understand": f"{role(mentor_mindset)} ({mentor_mindset})",
            #     "temper": f"{role(mentor_temperament)} ({mentor_temperament})",
            # }
        }

        with open(f'roles/{mbti_type}.md', 'w') as f:
            f.write(TEMPLATE.render(data))


if __name__ == '__main__':
    main()
