class state:
    president="ABC"
    Currency="Rupee"

    @classmethod
    def display_country(cls):
        print(cls.president)
        print(cls.Currency)
    @classmethod
    def elect_president(cls,elect_president):
        cls.president=elect_president

