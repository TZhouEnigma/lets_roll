<b>Me and my team participated in the 2016 Yhack (annual intercollegiate Hackathon held by Yale University) and made a web app called "Let's Roll" using ARCGIS rest api. The app uses Esri's powerful geolocation and mapping services to cater special routing needs for people with disabilities.</b>





#Installation

##Getting the files
```
git clone https://github.com/benlawson/Photoshare-Skeleton.git
cd Photoshare-Skeleton/
```

##Database setup: (for ubuntu)
First install MySQL with the following:
```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install mysql-server mysql-client
sudo apt-get install libmysqlclient-dev
```
Then start mysql:
```
mysql -u root -p
```
password is None so just press enter.
```
source ./schema.sql 
```
Now quit MySQL (enter CTRL-D or \q)

##Application Setup:
```
virtualenv photoenv
source photoenv/bin/activate #use photoenv/Scripts/activate on windows
pip install -r requirements.txt
python app.py
```

You can now point your favorite web brower to [localhost:5000](localhost:5000) to see your web app. 
