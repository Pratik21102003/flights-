import mysql.connector

class DB:
    def __init__(self):
        # connect to database
        try:
           self.conn=mysql.connector.connect(
          host='127.0.0.1',
        user='root',
          password=''
           )
           self.mycursor=self.conn.cursor()
        except:
           print('Connection error')
    def fetch_name(self):
        city=[]
        self.mycursor.execute("""SELECT  DISTINCT(Source)FROM flights.flights
                               UNION
                            SELECT DISTINCT(Destination)FROM flights.flights""")
        data=self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
        return city
    
    def fetch_flights(self,Source,Destination):
        self.mycursor.execute("""SELECT Date_of_Journey,Source,
                            Route,Price FROM flights.flights
                           WHERE Source='{}' AND Destination='{}' """.format(Source,Destination))
        data=self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights.flights
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency
        