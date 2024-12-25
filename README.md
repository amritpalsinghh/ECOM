# ECOM
ECOM_Website
Actions to user this code
1. Clone the repository
2. Start Server and starts database [eg Xamp]
2. Run the following cmd : 
virtualenv saulgadgets_3_12_5
.\saulgadgets_3_12_5\Scripts\activate
pip install -r requirement.txt
cd .\saulgadgets_3_12_5\saulgadgets



python .\manage.py makemigrations
python .\manage.py migrate
python manage.py createsuperuser
<add admin user  normally i took user "admin" and password= "zxc">
python .\manage.py runserver
<login to the page "localhost:8000/admin">
<add categories and products under those categories >
python .\manage.py runserver


Whenever resart or rework just do 
.\saulgadgets_3_12_5\Scripts\activate
cd .\saulgadgets_3_12_5\saulgadgets

