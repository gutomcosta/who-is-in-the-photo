class PersonRepository(object):
    
    def __init__(self):
        self.person_names = self._load_names()

    def get_person_name(self, id):
        try:
            return self.person_names[id]
        except Exception:
            return "Unknown"

    def _load_names(self):
        return  [
        'Adam Sandler',
        'Alec Baldwin',
        'Angelina Jolie',
        'Anna Kournikova',
        'Ashton Kutcher',
        'Avril Lavigne',
        'Barack Obama',
        'Ben Affleck',
        'Beyonce Knowles',
        'Brad Pitt',
        'Cameron Diaz',
        'Cate Blanchett',
        'Charlize Theron',
        'Christina Ricci',
        'Claudia Schiffer',
        'Clive Owen',
        'Colin Farrell',
        'Colin Powell',
        'Cristiano Ronaldo',
        'Daniel Craig',
        'Daniel Radcliffe',
        'David Beckham',
        'David Duchovny',
        'Denise Richards',
        'Drew Barrymore',
        'Dustin Hoffman',
        'Ehud Olmert',
        'Eva Mendes',
        'Faith Hill',
        'George Clooney',
        'Gordon Brown',
        'Gwyneth Paltrow',
        'Halle Berry',
        'Harrison Ford',
        'Hugh Jackman',
        'Hugh Laurie',
        'Jack Nicholson',
        'Jennifer Aniston',
        'Jennifer Lopez',
        'Jennifer Love Hewitt',
        'Jessica Alba',
        'Jessica Simpson',
        'Joaquin Phoenix',
        'John Travolta',
        'Julia Roberts',
        'Julia Stiles',
        'Kate Moss',
        'Kate Winslet',
        'Katherine Heigl',
        'Keira Knightley',
        'Kiefer Sutherland',
        'Leonardo DiCaprio',
        'Lindsay Lohan',
        'Mariah Carey',
        'Martha Stewart',
        'Matt Damon',
        'Meg Ryan',
        'Meryl Streep',
        'Michael Bloomberg',
        'Mickey Rourke',
        'Miley Cyrus',
        'Morgan Freeman',
        'Nicole Kidman',
        'Nicole Richie',
        'Orlando Bloom',
        'Reese Witherspoon',
        'Renee Zellweger',
        'Ricky Martin',
        'Robert Gates',
        'Sania Mirza',
        'Scarlett Johansson',
        'Shahrukh Khan',
        'Shakira',
        'Sharon Stone',
        'Silvio Berlusconi',
        'Stephen Colbert',
        'Steve Carell',
        'Tom Cruise',
        'Uma Thurman',
        'Victoria Beckham',
        'Viggo Mortensen',
        'Will Smith',
        'Zac Efron']

