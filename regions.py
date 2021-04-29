import mysql.connector

mydb=mysql.connector.connect(

	host="localhost",

	user="root",

	passwd="",

	database="geo_data"
	)

mycursor=mydb.cursor()



regions=["Arusha",
        "Dar es Salaam",
        "Dodoma",
        "Geita",
        "Iringa",
        "Kagera",
        "Katavi",
        "Kigoma",
        "Kilimanjaro",
        "Lindi",
        "Manyara",
        "Mara",
        "Mbeya",
        "Morogoro",
        "Mtwara",
        "Mwanza",
        "Njombe",
        "Pemba Kaskazini",
        "Pemba Kusini",
        "Pwani",
        "Rukwa",
        "Ruvuma",
        "Shinyanga",
        "Simiyu",
        "Singida",
        "Songwe",
        "Tabora",
        "Tanga",
        "Unguja Kaskazini",
        "Unguja Mjini Magharibi",
        "Unguja Kusini"
        ]





for region in regions:
		sql = """INSERT INTO regions(name) VALUES (%s)"""
		val = (region,)	
		mycursor.execute(sql, val)
		print(region)
		mydb.commit()
	