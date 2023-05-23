#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel):
    """
    State class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State instance
        """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Getter attribute that returns the list of City instances with
        state_id equals to the current State.id
        """
        cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
