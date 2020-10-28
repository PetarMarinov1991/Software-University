class Player:
    def __init__(self, name: str, hp: int, mp: int, skills=None, guild='Unaffiliated'):
        if skills is None:
            skills = {}
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = guild
        self.skills = skills

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills.update({skill_name: mana_cost})
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return 'Skill already added'

    def player_info(self):
        player_info = [
            f'Name: {self.name}',
            f'Guild: {self.guild}',
            f'HP: {self.hp}',
            f'MP: {self.mp}'
        ]
        skills_info = [f'==={s} - {m}' for s, m in self.skills.items()]

        return '\n'.join(player_info + skills_info) + '\n'