---
module:			B-INN-000
title:			Learn to scrap with scrappy in python
subtitle:	    Introduction to web-scraping

author:			Florian Azema
version:		1.0
---
#newpage
# 1. setup the project

- create a folder for your project
- install scrapy : `pip install scrapy`
- create a scrapy project in your folder : `scrapy startproject animals`
- create a spider : 
    - `cd animals`
    - `scrapy genspider paresseux https://www.monde-animal.fr/fiches-animaux/bradypus-variegatus/`
- run your spider and redirect it to see the output clearly: `scrapy crawl paresseux > tmp.txt`

# 2. Now its your turn !

you already created a spider, now code it ! 

- get the name of the animal
- get the description of the animal
- get the size of the animal
- get the weight of the animal
and more if you want

go to [Scrappy doc](https://docs.scrapy.org/en/latest/intro/tutorial.html) and read the tutorial.
Don't hesitate to ask for help if you are stuck.

print the result in the terminal

# 3. Multiple animals

now that you can scrap one animal, scrap all of them and their informations.
in fact you're not going to do page by page like you do for one animal, with scrappy you can acces to all the pages of the website.

create a new spider
reminder: `scrapy genspider allanimals https://www.monde-animal.fr/liste-animaux-a-z/`

Don't hesitate to ask for help if you are stuck.

print the result in the terminal

# 4. Store your data

when you do a scrapper we have to store our data somewhere, you can store it in a json file, in a csv file, in a database, etc...

- collect more informations about the animals
- store your data in a csv file
- try to scrap others websites !
