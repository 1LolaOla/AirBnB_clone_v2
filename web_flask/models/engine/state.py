# models/state.py

class State(BaseModel, Base):
    # Existing code...

    if models.storage_t == 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            city_list = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
