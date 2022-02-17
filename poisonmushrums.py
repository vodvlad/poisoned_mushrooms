import csv
from math import fabs
import numpy as np
import PySimpleGUI as sg


yes_count1 = np.array([0, 0, 0, 0, 0, 0])
no_count1 = np.array([0, 0, 0, 0, 0, 0])

yes_count2 = np.array([0, 0, 0, 0])
no_count2 = np.array([0, 0, 0, 0])

yes_count3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
no_count3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

yes_count4 = [0, 0]
no_count4 = [0, 0]

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
#how many mushrooms with a certain sign are poisoned and edible

#how many edible and non-edible for each trait
def add_pl(n):
    for i in range(6):
      a = ["b", "c", "x", "f", "k", "s"]
      if n[1] == a[i] and n[0] == "e":
        yes_count1[i] += 1
      elif n[1] == a[i] and n[0] == "p":
        no_count1[i] += 1
    
    for i in range(4):
      a = ["f", "g", "y", "s"]
      if n[2] == a[i] and n[0] == "e":
        yes_count2[i] += 1
      elif n[2] == a[i] and n[0] == "p":
        no_count2[i] += 1

    for i in range(12):
      a = ["k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"]
      if n[9] == a[i] and n[0] == "e":
        yes_count3[i] += 1
      elif n[9] == a[i] and n[0] == "p":
        no_count3[i] += 1

    for i in range(2):
      a = ["b", "n"]
      if n[8] == a[i] and n[0] == "e":
        yes_count4[i] += 1
      elif n[8] == a[i] and n[0] == "p":
        no_count4[i] += 1

e = 0 # count edible mush
p = 0 # count poison mush
with open('datasetmush.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    c = 0
    for row in csv_reader:

            add_pl(row)
            if row[0] == "e":
              e += 1
            elif row[0] == "p":
              p += 1
            line_count += 1

print("тут узнал сколько грибов при определённом признаке отравленных и съедобных")
print(yes_count1) #edibility probability for x, b, x f
print(no_count1)
print("----")
print(yes_count2)
print(no_count2)
print("----")
print(yes_count3)
print(no_count3)
print("----")
print(yes_count4)
print(no_count4)
print("----")
print("----------------------------")
all_count = np.array([listsum(yes_count1), listsum(no_count1)])


yes_count1 = yes_count1 / all_count[0]
no_count1 = no_count1 / all_count[1]

yes_count2 = yes_count2 / all_count[0]
no_count2 = no_count2 / all_count[1]

yes_count3 = yes_count3 / all_count[0]
no_count3 = no_count3 / all_count[1]

yes_count4 = yes_count4 / all_count[0]
no_count4 = no_count4 / all_count[1]


e_yes = e/line_count #P(poisonous)
e_no = p/line_count #P(not poisonous)


def apl(a, b, c, d):
    y_res = yes_count1[a] * yes_count2[b] * yes_count3[c] * yes_count4[d] * e_yes
    n_res = no_count1[a] * no_count2[b] * no_count3[c] * no_count4[d] * e_no
    res = y_res/(y_res+n_res)
    return res


print(line_count)
print("----")
print(all_count)
print("----")
print(e_yes)
print(e_no)



sg.theme('DarkAmber') 

layout = [  [sg.Text('Pravdepodobnost edible:'), sg.Listbox(values=('1'), size=(15, 2), key='textbx')],
            [sg.Text('Cap shape:'), sg.Checkbox('Bell', default=True, key='1'), sg.Checkbox('Conical', default=False, key='2'),sg.Checkbox('Convex', default=False, key='3'), sg.Checkbox('Flat', default=False, key='4'), sg.Checkbox('Knobbed', default=False, key = '5'), sg.Checkbox('Sunken', default=False, key = '6')],
            [sg.Text('Cap surface:'), sg.Checkbox('Fibrous', default=True, key='7'), sg.Checkbox('Grooves', default=False, key='8'), sg.Checkbox('Scaly', default=False, key='9'), sg.Checkbox('Smooth', default=False, key='10')],
            [sg.Text('Gill color:'), sg.Checkbox('Black', default=True, key='11'), sg.Checkbox('Brown', default=False, key='12'), sg.Checkbox('Buff', default=False, key='13'), sg.Checkbox('Chocolate', default=False, key='14'), sg.Checkbox('Gray', default=False, key='15'), sg.Checkbox('Green', default=False, key='16'), sg.Checkbox('Orange', default=False, key='17'), sg.Checkbox('Pink', default=False, key='18'), sg.Checkbox('Purple', default=False, key='19'), sg.Checkbox('Red', default=False, key='20'), sg.Checkbox('White', default=False, key='21'), sg.Checkbox('Yellow', default=False, key='22')],
            [sg.Text('Gill size:'), sg.Checkbox('Broad', default=True, key='23'), sg.Checkbox('Narrow', default=False, key='24')],
            [sg.Button('Ok', key='kk')]]


window = sg.Window('Bayees Klassificator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    if event == 'kk':
        if values['1'] == True:
          a = 0
        elif values['2'] == True:
          a = 1
        elif values['3'] == True:
          a = 2
        elif values['4'] == True:
          a = 3
        elif values['5'] == True:
          a = 4
        elif values['6'] == True:
          a = 5
        if values['7'] == True:
          b = 0
        elif values['8'] == True:
          b = 1
        elif values['9'] == True:
          b = 2
        elif values['10'] == True:
          b = 3
        if values['11'] == True:
          c = 0
        elif values['12'] == True:
          c = 1
        elif values['13'] == True:
          c = 2
        elif values['14'] == True:
          c = 3
        elif values['15'] == True:
          c = 4
        elif values['16'] == True:
          c = 5
        elif values['17'] == True:
          c = 6
        elif values['18'] == True:
          c = 7
        elif values['19'] == True:
          c = 8
        elif values['20'] == True:
          c = 9
        elif values['21'] == True:
          c = 10
        elif values['22'] == True:
          c = 11
        if values['23'] == True:
          d = 0
        elif values['24'] == True:
          d = 1
        apl(a, b, c, d)
        window.Element('textbx').Update(values=[apl(a, b, c, d)])

window.close()
