#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, sql

# for the sys.exit() method call
import sys
# for regex expression
import re
# for plotting the data
import matplotlib.pyplot as plt

# import the Pygame libraries
import pygame
from pygame.locals import *

# set the DB name, table, and table data to 'None'
db_name = "DST2final_project" #need to modify based on the name of your database

# initialize the variables
# below variable are for query 1
country = '' # store the input country
year_month = '' # store the input year/month
province = '' # store the input province
query1_check = [] # store the output of check_country_province function
query1_return = [] # store the sql query return
# below variables are for query 2
n_th_place = 0 # store the input n_th_place
which_month = '' # store the input month
highest_rate_country = [] # store the country with the highest diagnosis rate
current_rate = 0 # use to find the highest rate
query2_return = [] # store the return of query 2
#setting for postgreSQL
#change these globals (user name and user password) to match your settings
user_name = "postgres" #the username for accessing your postgreSQL
user_pass = "136958" #the password for accessing your postgreSQL

# create a class for the buttons and labels
class Button():

    # empty list for button registry
    registry = []

    # selected button (will have outline rect)
    selected = None

    # pygame RGBA colors
    white = (255, 255, 255, 255)
    black = (0, 0, 0, 255)
    red = (255, 0, 0, 255)
    green = (50, 205, 50, 255)
    light_blue = (240, 248, 255, 255)

    # default font color for buttons/labels is white
    def __init__(self, name, loc, color=black):

        # add button to registry
        self.registry.append(self)
        # paramater attributes
        self.name = name
        self.loc = loc
        self.color = color
        # text attr for button
        self.text = ""

        # size of button changes depending on length of text
        self.size = (int(len(self.text)*200), 200)

        # font.render(text, antialias, color, background=None) -> Surface
        self.font = font.render (
            self.name + " " + self.text, # display text
            True, # antialias on
            self.color, # font color
            self.light_blue # background color
        )

        # rect for button
        self.rect = self.font.get_rect()
        self.rect.x = loc[0]
        self.rect.y = loc[1]

# function that connects to Postgres
def connect_postgres(db):

    # connect to PostgreSQL
    print ("\nconnecting to PostgreSQL")
    try:
        conn = connect (
            dbname = db,
            user = user_name,
            host = "localhost",
            password = user_pass
        )
    except Exception as err:
        print ("PostgreSQL Connect() ERROR:", err)
        conn = None

    # return the connection object
    return conn

# function that returns movie with queried rating_button
def return_rate(conn):
    if which_month == None or which_month == '':
        return []
    SQLquery='SELECT return_rate(\''+str(which_month)+"'"+')'+';'

    print(SQLquery)
    # instantiate a new cursor object
    cursor = conn.cursor()

    # (use sql.SQL() to prevent SQL injection attack)
    sql_object = sql.SQL(
        # pass SQL statement to sql.SQL() method
        SQLquery
    )

    try:
        # use the execute() method to put table data into cursor obj
        cursor.execute( sql_object )

        # use the fetchall() method to return a list of all the data
        rate_return = cursor.fetchall()

        # close cursor objects to avoid memory leaks
        cursor.close()
    except Exception as err:

        # print psycopg2 error and set table data to None
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        rate_return = None

    return rate_return

# function that returns movie with queried rating_button
def return_country(conn):
    if country == None or country== '' or year_month == None or year_month == '':
        return []

    SQLquery='SELECT return_country(\''+str(country)+"'"+','+"'"+str(year_month)+"'"+')'+';'
    print(SQLquery)
    # instantiate a new cursor object
    cursor = conn.cursor()

    # (use sql.SQL() to prevent SQL injection attack)
    sql_object = sql.SQL(
        # pass SQL statement to sql.SQL() method
        SQLquery
    )

    try:
        # use the execute() method to put table data into cursor obj
        cursor.execute( sql_object )

        # use the fetchall() method to return a list of all the data
        country_return = cursor.fetchall()
        # close cursor objects to avoid memory leaks
        cursor.close()
    except Exception as err:

        # print psycopg2 error and set table data to None
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        country_return = None
    return country_return

def check_country_province (conn):
    if country == None or country== '' or province == None or province == '':
        return []
    SQLquery='SELECT country_name from country_province where country_name='+"'"+str(country)+"'"+'and province_name='+"'"+str(province)+"'"+';'
    print(SQLquery)
    # instantiate a new cursor object
    cursor = conn.cursor()

    # (use sql.SQL() to prevent SQL injection attack)
    sql_object = sql.SQL(
        # pass SQL statement to sql.SQL() method
        SQLquery
    )

    try:
        # use the execute() method to put table data into cursor obj
        cursor.execute( sql_object )

        # use the fetchall() method to return a list of all the data
        check_return = cursor.fetchall()
        # close cursor objects to avoid memory leaks
        cursor.close()
    except Exception as err:

        # print psycopg2 error and set table data to None
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        check_return = None
    return check_return

def return_province(conn):
    if country == None or country== '' or year_month == None or year_month == '':
        return []

    SQLquery='SELECT return_province(\''+str(province)+"'"+','+"'"+str(year_month)+"'"+')'+';'
    print(SQLquery)
    # instantiate a new cursor object
    cursor = conn.cursor()

    # (use sql.SQL() to prevent SQL injection attack)
    sql_object = sql.SQL(
        # pass SQL statement to sql.SQL() method
        SQLquery
    )

    try:
        # use the execute() method to put table data into cursor obj
        cursor.execute( sql_object )

        # use the fetchall() method to return a list of all the data
        province_return = cursor.fetchall()
        # close cursor objects to avoid memory leaks
        cursor.close()
    except Exception as err:

        # print psycopg2 error and set table data to None
        print ("PostgreSQL psycopg2 cursor.execute() ERROR:", err)
        province_return = None
    return province_return

def plot(results):
    temp = []
    date = []
    number = []
    # store date and confirmed cases in two lists seperately
    for i in range(0,len(results)):
        temp = re.findall(r'[0-9-]+',query1_return[i][0])
        date.append(temp[0])
        number.append(int(temp[1]))
    # set the plot
    fig, ax = plt.subplots()
    ax.ticklabel_format(useOffset=False, style='plain')
    # avoid scientific counting in the plot
    # references: https://www.imooc.com/wenda/detail/604644
    ax.plot(date,number)
"""
PYGAME STARTS HERE
"""

# initialize the pygame window
pygame.init()
pygame.display.set_mode((2000, 1000))#size of the UI，can add picture
mode = 0

# change the caption/title for the Pygame app
pygame.display.set_caption("9057_DST2 Final Project", "9057_DST2 Final Project")

# get the OS screen/monitor resolution
max_width = pygame.display.Info().current_w
max_height = pygame.display.Info().current_h

# create a pygame resizable screen
screen = pygame.display.set_mode(
    (int(max_width*0.55), int(max_height*0.6)),
    HWSURFACE | DOUBLEBUF| RESIZABLE
)

# calculate an int for the font size
font_size = int(max_width / 100)

try:
    font = pygame.font.SysFont('Calibri', font_size)
except Exception as err:
    print ("pygame.font ERROR:", err)
    font = pygame.font.SysFont('Arial', font_size)

# create buttons for PostgreSQL database and table
query1_button_country = Button("country", (10, 10))
query1_button_year_month = Button("year/month", (10, 70))
query1_button_province = Button("province",(10,40))
query2_button_month = Button("month", (510, 10))
query2_button_no = Button ("n th place",(510,40))
#pygame.draw.line( screen, Button.white, (500,1), (500,600), 10 ) #error

# default Postgres connection is 'None'
connection = None

# begin the pygame loop
app_running = True
while app_running == True:

    # reset the screen (set the color of the screen)
    screen.fill( Button.light_blue )

    # set the clock FPS for app
    clock = pygame.time.Clock()

    # iterate over the pygame events
    for event in pygame.event.get():

        # user clicks the quit button on app window
        if event.type == QUIT:
            app_running = False
            pygame.display.quit()
            pygame.quit() # close UI, quit the programme
            sys.exit()
            quit()

        # user presses a key on keyboard
        if event.type == KEYDOWN:

            if Button.selected != None: #if there is a selected botton

                # get the selected button
                b = Button.selected

                # user presses the return key
                if event.key == K_RETURN:
                    # clear all input and output of the previous query
                    query1_return = []
                    query2_return = []
                    query1_check = []
                    country = ''
                    year_month = ''
                    province = ''
                    n_th_place = 0
                    # if the selected button is the query 1's and no province information
                    if ("country" in b.name or "year/month" in b.name or "province" in b.name) and (query1_button_province.text == '' or query1_button_province.text == None):
                        country = query1_button_country.text
                        year_month = query1_button_year_month.text
                        connection = connect_postgres( db_name )
                        query1_return = return_country( connection )
                        # combine 3 records into one line, avoid words overflow the screen
                        query1_return_adj = []
                        leng = len(query1_return)
                        temp = ''
                        for i in range(1,leng+1):
                            if i%3 == 0:
                                temp = temp +' '+ query1_return[i-1][0]
                                query1_return_adj.append(temp)
                                temp = ''
                            else:
                                temp = temp +' '+ query1_return[i-1][0]
                        query1_return_adj.append(temp)
                        plot(query1_return) 
                    # if the selected button is the query 1's and has province information
                    elif ("country" in b.name or "year/month" in b.name or "province" in b.name) and (query1_button_province.text != '' or query1_button_province.text != None):
                        country = query1_button_country.text
                        year_month = query1_button_year_month.text
                        province = query1_button_province.text
                        connection = connect_postgres( db_name )
                        query1_check = check_country_province (connection)
                        query1_return = return_province( connection )
                        # combine 3 records into one line, avoid words overflow the screen
                        query1_return_adj = []
                        leng = len(query1_return)
                        temp = ''
                        for i in range(1,leng+1):
                            if i%3 == 0:
                                temp = temp +' '+ query1_return[i-1][0]
                                query1_return_adj.append(temp)
                                temp = ''
                            else:
                                temp = temp +' '+ query1_return[i-1][0]
                        query1_return_adj.append(temp)
                        plot(query1_return)
                    # if the selected button is the query 2's
                    elif "month" in b.name or "n th place" in b.name:
                        which_month = query2_button_month.text
                        if (len(query2_button_no.text) == 1 and query2_button_no.text >= '1' and query2_button_no.text <= '9') or (query2_button_no.text == '10'):
                             n_th_place = int(query2_button_no.text)
                        connection = connect_postgres( db_name )
                        query2_return = return_rate( connection )
                    print(country)
                    print(year_month)
                    print(province)
                    print(which_month)

                else:
                    # get the key pressed
                    key_press = pygame.key.get_pressed()

                    # iterate over the keypresses
                    for keys in range(255):
                        if key_press[keys]:
                            if keys == 8: # backspace
                                b.text = b.text[:-1]
                            else:
                                # convert key to unicode string
                                b.text += event.unicode
                                print ("KEYPRESS:", event.unicode)

                # append the button text to button font object
                b.font = font.render(b.name + " " + b.text, True, Button.black, Button.light_blue)

        # check for mouse button down events
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print ("\nMOUSE CLICK:", event)

            # iterate over the button registry list
            for b in Button.registry:

                # check if the mouse click collided with button
                if b.rect.collidepoint(event.pos) == 1:
                    # store button object under selected attr
                    Button.selected = b

    # iterate over the button registry list
    for b in Button.registry:
        # blit the button's font to screen
        screen.blit(b.font, b.rect)
        # check if the button has been clicked by user
        if Button.selected == b:
            # blit an outline around button if selected
            rect_pos = (b.rect.x-5, b.rect.y-5, b.rect.width+4, b.rect.height+10) # change "+10" to "+4" to avoid the outline blot out the input
            pygame.draw.rect(screen, Button.black, rect_pos, 3) # width 3 pixels
    # if does not enter any query
    if Button.selected == None: 
        blit_text = "Please select a query. "
        conn_msg = font.render(blit_text, True, Button.green, Button.light_blue)
        screen.blit(conn_msg, (10, 200))
    # if enter query 1
    if Button.selected == query1_button_country or Button.selected == query1_button_year_month or Button.selected == query1_button_province :
        if country == '' and year_month == '':
           # blit instruction messages
            blit_text = "Type at least country and year_month into the fields and press 'Return'."
            conn_msg = font.render(blit_text, True, Button.green, Button.light_blue)
            screen.blit(conn_msg, (10, 200))

        else:
            # connection is valid, but actor doesn't exist
            if connection != None:  
                if query1_return == [] and ((int(year_month) < 1) or (int(year_month) > 12 and int(year_month) != 2020)):
                        blit_text = "Please type the correct month (1-12) or year(2020). "
                        color = Button.red
                        # blit the message to the pygame screen
                        conn_msg = font.render(blit_text, True, color, Button.light_blue)
                        screen.blit(conn_msg, (10, 140))

                   # connection is valid, but rating doesn't exist
                if query1_return == [] and (not((int(year_month) < 1) or (int(year_month) > 12 and int(year_month) != 2020))):
                        blit_text = "The PostgreSQL table does not have the record with this country/province. Please check the country_province.csv"
                        color = Button.red
                        # blit the message to the pygame screen
                        conn_msg = font.render(blit_text, True, color, Button.light_blue)
                        screen.blit(conn_msg, (10, 120))
                 # enumerate() the actor first name data if PostgreSQL API call successful
                if  country != '' and year_month != '' and province == '' and query1_return != []:
                    # enumerate the list of tuple rows
                    for num, row in enumerate(query1_return_adj):
        
                        # blit the table data to Pygame window
                        blit_text = str(row).encode("utf-8", "ignore")
                        table_font = font.render(blit_text, True, Button.black, Button.light_blue)
                        screen.blit(table_font, (10, 190 + int(num*50)))
                    # plot the data
                    plt.ylabel('Confirmed Cases')
                    plt.xticks(rotation=-50)
                    plt.title('Comfirmed COVID-19 cases in '+country+' in '+year_month)
                    # figure saved in the same directory where the python script is
                    plt.savefig('Comfirmed COVID-19 cases in '+country+' in '+year_month,type='png')
                    img = pygame.image.load('Comfirmed COVID-19 cases in '+country+' in '+year_month+".png").convert()
                    screen.blit(img,(750, 250))
                if country != '' and year_month != '' and province != '' and query1_check == []:
                    blit_text = 'The country and province do not match. '
                    color = Button.red
                    conn_msg = font.render(blit_text, True, color, Button.light_blue)
                    screen.blit(conn_msg, (10, 100))
                elif country != '' and year_month != '' and province != '' and query1_check != []:
                    # enumerate the list of tuple rows
                    for num, row in enumerate(query1_return_adj):        
                        # blit the table data to Pygame window
                        blit_text = str(row).encode("utf-8", "ignore")
                        table_font = font.render(blit_text, True, Button.black, Button.light_blue)
                        screen.blit(table_font, (10, 190 + int(num*50)))
                    # plot the data
                    plt.ylabel('Confirmed Cases')
                    plt.xticks(rotation=-50)
                    plt.title('Comfirmed COVID-19 cases in '+province+' in '+year_month)
                    # figure saved in the same directory where the python script is
                    plt.savefig('Comfirmed COVID-19 cases in '+province+' in '+year_month,type='png')
                    img = pygame.image.load('Comfirmed COVID-19 cases in '+province+' in '+year_month+".png").convert()
                    screen.blit(img,(750, 250))
            # connection is invalid
            elif connection == None:
                blit_text = "PostgreSQL connection is invalid."
                color = Button.red
                # blit the message to the pygame screen
                conn_msg = font.render(blit_text, True, color, Button.light_blue)
                screen.blit(conn_msg, (10, 140))
    # enter query 2        
    if Button.selected == query2_button_month or Button.selected == query2_button_no:
            if query2_return != [] and n_th_place != 0: 
                all_number = []
                for i in range (0,len(query2_return)):
                    temp1 = re.findall(r'\d+',query2_return[i][0])
                    all_number.append(int(temp1[0]))
                current_rate = 0
                j=0
                previous_rate = 100000000
                # find the n th highest rate, more explanation in the documentation
                while j < n_th_place:
                    current_rate = 0
                    highest_rate_country = []
                    i = 0
                    while i < len(all_number)-1:
                        if all_number[i] == 0: 
                            i = i + 2
                        elif all_number[i] != 0:
                            temp_rate = (all_number[i+1]-all_number[i])/all_number[i]
                            if temp_rate > current_rate and temp_rate < previous_rate:
                                highest_rate_country = []
                                current_rate = temp_rate
                                temp2 = re.findall(r'[a-zA-Z\s]+',query2_return[i][0])
                                highest_rate_country.append(temp2[0])
                            if temp_rate == current_rate:
                                temp2 = re.findall(r'[a-zA-Z\s]+',query2_return[i][0])
                                highest_rate_country.append(temp2[0])
                            i = i + 2
                    previous_rate = current_rate
                    j = j + 1
                blit_text = str(highest_rate_country[0]).encode("utf-8", "ignore")
                table_font = font.render(blit_text, True, Button.black, Button.light_blue)
                screen.blit(table_font, (10, 250 + int(1*50)))
                blit_text = str(current_rate).encode("utf-8", "ignore")
                table_font = font.render(blit_text, True, Button.black, Button.light_blue)
                screen.blit(table_font, (10, 250 + int(2*50)))
            else: 
                blit_text = 'Please type in valid month (2-12) and n th place (1-10) for diagnosis rate. '
                color = Button.red
                conn_msg = font.render(blit_text, True, color, Button.light_blue)
                screen.blit(conn_msg, (10, 100))
                                
                       
    clock.tick(200)

    # use the flip() method to display text on surface
    pygame.display.flip()
    pygame.display.update()
