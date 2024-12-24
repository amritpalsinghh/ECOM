# ECOM
ECOM_Website
Actions to user this code
1. Clone the repository
2. Start Server and starts database [eg Xamp]
2. Run the following cmd : 
virtualenv saulgadgets_3_12_5
pip install -r requirements.txt
cd .\saulgadgets_3_12_5\saulgadget
python .\manage.py makemigrations
python .\manage.py migrate
python manage.py createsuperuser
<add admin user  normally i took user "admin" and password= "zxc">
<login to the page "localhost:8000/admin">
<add categories and products under those categories >
python .\manage.py runserver
