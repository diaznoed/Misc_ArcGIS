{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "44961425",
   "metadata": {},
   "outputs": [],
   "source": [
    "## import needed python modules\n",
    "from arcgis.gis import GIS\n",
    "import pandas as pd\n",
    "import csv, random, os, glob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ab6d54ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "## run jupyter notebook within same dir that merge.csv is in\n",
    "filename=open(r\"merge.csv\",'r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e5d68a5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "## change amount of records desired within each file\n",
    "records = 2500\n",
    "fieldnames = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'lat', 'long']\n",
    "\n",
    "## get fieldname columns as lists\n",
    "filename = open('merge.csv','r')\n",
    "file = csv.DictReader(filename)\n",
    "first = []\n",
    "last = []\n",
    "email = []\n",
    "gender = []\n",
    "ip = []\n",
    "lat = []\n",
    "long = []\n",
    "\n",
    "## pull data from merge.csv into dictionary reader\n",
    "for col in file:\n",
    "\tfirst.append(col['first_name'])\n",
    "\tlast.append(col['last_name'])\n",
    "\temail.append(col['email'])\n",
    "\tgender.append(col['gender'])\n",
    "\tip.append(col['ip_address'])\n",
    "\tlat.append(col['lat'])\n",
    "\tlong.append(col['long'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8ccd6bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "## point to directory where you desire files to be created\n",
    "#os.mkdir('data')\n",
    "os.chdir(r'\\content_generation_scripts\\data')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0e6e5127",
   "metadata": {},
   "outputs": [],
   "source": [
    "## change <= variable to number of csv files to be created\n",
    "num = 0\n",
    "while num <=10:\n",
    "    write= csv.DictWriter(open(('mock_{0}.csv').format(num), 'w'), fieldnames=fieldnames)\n",
    "    write.writerow(dict(zip(fieldnames, fieldnames)))\n",
    "    for i in range(0,records):\n",
    "        write.writerow(dict([\n",
    "            ('id',i),\n",
    "            ('first_name', random.choice(first)),\n",
    "            ('last_name', random.choice(last)),\n",
    "            ('email', random.choice(email)),\n",
    "            ('gender', random.choice(gender)),\n",
    "            ('ip_address', random.choice(ip)),\n",
    "            ('lat', random.choice(lat)),\n",
    "            ('long', random.choice(long))\n",
    "        ]))\n",
    "    num=num+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "914b8f40",
   "metadata": {},
   "outputs": [],
   "source": [
    "## run to clean up csv files to prepare for portal ingest\n",
    "newfiles = os.listdir()\n",
    "for file in newfiles:\n",
    "    if 'mock' in file:\n",
    "        df = pd.read_csv(file)\n",
    "        df.dropna(inplace=True)\n",
    "        df.to_csv(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "06e29956",
   "metadata": {},
   "outputs": [],
   "source": [
    "## create portal connection\n",
    "gis = GIS('https://portal-url/portal', 'admin-account-name', 'super-secret-password', verify_cert=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8ccca357",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'title': 'mock_0', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_0 published to test portal..\n",
      "{'title': 'mock_1', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_1 published to test portal..\n",
      "{'title': 'mock_10', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_10 published to test portal..\n",
      "{'title': 'mock_2', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_2 published to test portal..\n",
      "{'title': 'mock_3', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_3 published to test portal..\n",
      "{'title': 'mock_4', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_4 published to test portal..\n",
      "{'title': 'mock_5', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_5 published to test portal..\n",
      "{'title': 'mock_6', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_6 published to test portal..\n",
      "{'title': 'mock_7', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_7 published to test portal..\n",
      "{'title': 'mock_8', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_8 published to test portal..\n",
      "{'title': 'mock_9', 'description': 'testing...123', 'tags': ['test', '20221129']}\n",
      "..mock_9 published to test portal..\n"
     ]
    }
   ],
   "source": [
    "## publish csvs to portal\n",
    "for file in newfiles:\n",
    "    if 'mock' in file:\n",
    "        try:\n",
    "            name = file.split('.')\n",
    "            params={\n",
    "                'title':('{0}').format(name[0]),\n",
    "                'description': 'testing...123',\n",
    "                'tags': ['test','20221129']\n",
    "            }\n",
    "            csv_file = file\n",
    "            \n",
    "            ## add csv to portal\n",
    "            ## change owner to desired user to 'own' portal items\n",
    "            z = gis.content.add(data=csv_file, item_properties=params, owner='admin')\n",
    "            \n",
    "            ## publish added csv as a hosted feature layer\n",
    "            z.publish(publish_parameters=params)\n",
    "            print((\"..{0} published to test portal..\").format(name[0]))\n",
    "        except:\n",
    "            pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23d1553d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
