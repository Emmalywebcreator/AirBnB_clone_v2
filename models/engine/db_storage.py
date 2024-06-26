from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session,sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

lists_of_objects = [User, State, City, Amenity, Place, Review]



class DBStorage():
    _engine = None
    _session = None

    def __init__(self):
        """
         Instantiates the DBStorage class.
        """

        """Retrieve environment variables for database credentials"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')

        """Connect  to Mysql database"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db_name}", pool_pre_ping=True
        )
        # target = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, password, host, db_name)
        # self.__engine = create_engine(target, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects of a class from the session.
        Args:
            cls: The class of objects to retrieve (optional).
        Returns:
            A list of objects.
        """
        ret_dict = {}

        if cls is None:
            if not cls:
                for classname in lists_of_objects:
                    for item in self.__session.query(classname).all():
                        key = item.__class__.__name__ + "." + item.id
                        val = item
                        ret_dict[key] = val
            else:
                for item in self.__session.query(eval(cls)).all():
                    key = item.__class__.__name__ + "." + item.id
                    val = item
                    ret_dict[key] = val

        return ret_dict
    
    def new(self, obj):
        """
        Adds a new object to the session.
        Args:
            obj: The object to add.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits the current session.
        """
        self.__session.commit()

    def delete(self, obj):
        """
        Deletes an object from the session.
        Args:
            obj: The object to delete.
        """
        self.__session.delete(obj)

    def reload(self):
        '''
            create all tables in the database
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()