from bs4 import BeautifulSoup
import requests
URL1 = 'https://www.salvagemarket.co.uk/'
URL2 = 'https://auctions.synetiq.co.uk/'
URL3 = 'https://www.autotrader.co.uk/'
page1 = 'https://auctions.synetiq.co.uk/auction/items/?make=0&fuel=0&transmission=0&category=5&layout=r50&seller=0&location=0&time=all&distance=&search=hatchback&sort=2&tab=0'
#print(''.join(list(page1)))

r = requests.get(page1)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())


table = soup.findAll('div', attrs = {'class' : 'row vehicle_list'})

#intable = table.find('h2', attrs = {'class' : 'ml-2 mr-2'})

#print(table)

#################     FOR SYNETIQ CAR AUCTIONS WEBSITE      ######################

class Synetiq():
    def __init__(self):
        self.link = 'https://auctions.synetiq.co.uk/auction/items/?x=0&type=1&tab=1&list=1&section_id=&make=&transmission=0&fuel=0&seller=&category=&location=0&sort=2&time=0&distance=0&options=&layout=r50&search=&fp=0&page=1'
        self.r = requests.get(self.link)
        self.soup = BeautifulSoup(self.r.content, 'html5lib')
        self.carTable = self.soup.findAll('div', attrs = {'class' : 'row vehicle_list'})
        self.lstPg = self.lstPgSynetiq()
        self.pgNum = 1
        print(self.lstPg)
        

    def getPg(self):
        None

    def lstPgSynetiq(self):
        lstPgSection = self.soup.find('section', attrs = {'class' : 'section-alt'})
        lstPgls = lstPgSection.findAll('li', attrs = {'class' : 'page-item'})
        lstPgNum = len(lstPgls) - 1
        lstPg = lstPgls[lstPgNum].find('a', attrs = {'class' : 'page-link'}).get_text()
        return(int(lstPg))

    def newLnk(self, newLnk):
        self.link = newLnk
        self.r = requests.get(self.link)
        self.soup = BeautifulSoup(self.r.content, 'html5lib')
        self.carTable = (self.soup.findAll('div', attrs = {'class' : 'row vehicle_list'}))

    def chngePg(self):
        split = list(self.link)
        lsEnd = len(split) - 1
        self.pgNum += 1
        nxtPgSpl = list(str(self.pgNum))

        if int(self.pgNum) > self.lstPg:
            self.link = 'END'
        else:
            for x in range(len(nxtPgSpl)):
                if self.pgNum < 11:
                    split[lsEnd] = str(self.pgNum)
                    
                else:
                    split[lsEnd - x] = str(nxtPgSpl[len(nxtPgSpl) - 1 - x])
        newLnk = ''.join(split)
        self.newLnk(newLnk)



        
        ''' nxtPg = int(split[lsEnd]) + 1
        if (self.pgNum + 1) % 10 == 0:

        print(nxtPg)

        if nxtPg > self.lstPg:
            self.link = 'END'
        else:
            split[lsEnd] = str(nxtPg)
            newLnk = ''.join(split)
            self.newLnk()'''
            
     
    


    def searchSynetiqPage(self):
        cars = []

        for row in self.carTable:

            car = {}
            car['Name'] = row.find('h2').get_text()
            car['Price'] = row.find('span', attrs = {'class' : 'list_price_2'}).get_text()

            category = row.find('i', attrs = {'class' : 'fa fa-tag fa-fw list-fa_2 fa-mr10'})
            catPrnt = category.parent.parent #had to go up 2 steps to find parent of this
            car['Category'] = catPrnt.find('span', attrs = {'class' : 'list-group-text-item'}).get_text()
            
            mileage = row.find('i', attrs = {'class' : 'fa fa-tachometer-alt fa-fw list-fa_2 fa-mr10'})
            milPrnt = mileage.parent.parent 
            car['Mileage'] = milPrnt.find('span', attrs = {'class' : 'list-group-text-item'}).get_text()
            
            cars.append(car)
        return cars
    
    def searchSynetiq(self):
        allCars = []
        counter = 0
        while counter != self.lstPg:
            carPg = self.searchSynetiqPage()
            allCars.append(carPg)
            self.chngePg()
            print(self.link)
            counter += 1
        for element in allCars:
            print(element[0])

def searchSalvageMarket():
    None

def searchCopart():
    None


#print(chngePg(14, 'https://auctions.synetiq.co.uk/auction/items/?x=0&type=1&tab=1&list=1&section_id=&make=&transmission=0&fuel=0&seller=&category=&location=0&sort=&time=0&distance=0&options=&layout=r20&search=&fp=0&page=2'))
    

synetiq = Synetiq()
synetiq.searchSynetiq()