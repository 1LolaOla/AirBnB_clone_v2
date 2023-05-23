#!/usr/bin/python3
'''database storage engine'''

from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import scoped_session


class DBStorage:
    """
    DBStorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor for DBStorage class
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        from models import classes

        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls, None)
        else:
            cls = classes.values()
        for class_ in cls:
            objects.update({obj.__class__.__name__ + '.' + obj.id: obj
                            for obj in self.__session.query(class_).all()})
        return objects

    def new(self, obj):
        """
        Add the object to the current database session (self.__session)
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and
        create the current database session (self.__session)
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Calls remove() method on the private session attribute (self.__session).
        """
        if self.__session is not None:
            self.__session.remove()
