from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='What is your age?', min=17, max=125)

    gender = models.StringField(
        choices=[['Man', 'Man'], ['Woman', 'Woman'], ['Non-binary/gender diverse', 'Non-binary/gender diverse']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    major = models.StringField(
        choices=[['Not a student', 'Not a student'], ['Science, technology, engineering and mathematics', 'Science, technology, engineering and mathematics'],
                 ['Social sciences', 'Social sciences'], ['Business, Finance', 'Business, Finance'], ['Art and humanities', 'Art and humanities']],
        label='What is your major?',
        widget=widgets.RadioSelect,
    )

    political = models.StringField(
        choices=[['Left', 'Left'], ['Center', 'Center'], ['Right', 'Right']],
        label='What is your political orientation?',
        widget=widgets.RadioSelect,
    )

    gpa = models.DecimalField(label='What is your GPA?', min=0.0, max=4.0, decimal_places=1, max_digits=2)
