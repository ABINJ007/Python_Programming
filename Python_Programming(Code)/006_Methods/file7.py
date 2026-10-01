class MovieTicket:
    Theatre_name="Urvashi"
    location="Majestic"
    def __init__(self,seatno,movie_name,price):
        self.seatno=seatno
        self.movie_name=movie_name
        self.price=price
    @classmethod
    def diplay_theatre_details(cls):
        print(cls.Theatre_name)
        print(cls.location)
    def display_ticket_details(self):
        print(self.seatno)
        print(self.movie_name)
        print(self.price)
    def change_seatno(self,newseat):
        self.seatno=newseat
        print("seat number changed")
    @staticmethod
    def offers():
        print(f"Tuesday 15% off for Singles")
        print(f"Friday 10% off for BlackDress")
        print(f"Sundays 5% off for Family")
    @staticmethod
    def check_age(movie_rating):
        if movie_rating == "A":
            print("age proof shud be displayed")
        elif movie_rating=="U/A":
            print("parental guidance required")
        else:
            print("You are a Kid")