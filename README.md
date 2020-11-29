# Petro

**1) Inside the project run: docker-compose up -d --build**

**2) run: docker-compose run web petro/manage.py createsuperuser. And fill the fields**

**3) Open the browser and go to "http://127.0.0.1:8000/admin/users/user/", then click on Import CSV button. or you can go to the "http://127.0.0.1:8000/admin/users/user/import-csv/". Import CSV file like TestData.csv in the project.**

**4) To view list of users, go to the "http://127.0.0.1:8000/api/users/", if u want to filter by registration_date add "?registration_date=year-month-day" to the end of url**
