import csv, pyperclip
import tksheet
from tksheet import Sheet
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from PIL import Image, ImageTk
from itertools import permutations

sVersion = 'v1.1.0'
root = tk.Tk()
root.geometry('%dx%d' % (1000, 800)) # width, height
root.title('Taxonomy of common concepts based on matrices of concepts, for AI improvement - MIT license - ' + sVersion)
root.configure(bg='#C0DCC0') # or lavender, antiquewhite

####################################################
# VARIABLES
####################################################
liColSize = 15
px = 5 # default padx
py = 5 # default pady
bCheckbuttonPrepareTrainingdata = tk.BooleanVar()
bAddInitialSpace = tk.BooleanVar()
bAddInitialSpace.set(True)
# image1 = PhotoImage(file = "taxonomy-image.png")
image = Image.open("taxonomy-image.png")
resize_image = image.resize((200, 200))
image1 = ImageTk.PhotoImage(resize_image)
icon9 = PhotoImage(file = "media-floppy.png")
icon10 = PhotoImage(file = "text-x-python.png")
icon11 = PhotoImage(file = "arrow-right.png")
listOptions = [
               'α has a positive/neutral/negative connotation',
               'α1 is contrary/dual/complementary/extreme opposite to α2',
               'α1 and α2 are in the same relationship as α3 and α4'
			   ]
####################################################
# CONSTANTS
####################################################
ENG = 0
FRE = ENG+1 # 1
ITA = FRE+1 # 2
CIS = ITA+1 # 3
SAR = CIS+1 # 4
TAR = SAR+1 # 5

Aplus = 0 # (Aplus+3)%6 = Āplus (the formula gives the concept of the other pole with the same polarity)
A0 = 1 # (Aplus+3)%6 = Ā0
Aminus = 2 # (Aplus+3)%6 = Āminus
Āplus = 3 # (Aplus+3)%6 = Aplus
Ā0 = 4 # (Aplus+3)%6 = A0
Āminus = 5 # (Aplus+3)%6 = Aminus
####################################################
# FUNCTIONS
####################################################

def count_rows(string):
    # Split the string into lines and count the resulting list of lines
    row_count = len(string.split("\n"))
    return row_count

####################################################
# CLICK PROCEDURES
####################################################

def twocontraryeng_clicked():
    output.delete(1.0, tk.END)        
    output.insert('1.0', dic[ENG]['courage']['2-contrary'] + '\n')
    output.insert('1.0', dconcept['ENG']['courage']['2-contrary'] + '\n')

def twocontraryfre_clicked():
    output.delete(1.0, tk.END)        
    output.insert('1.0', dic[FRE]['optimisme']['2-contrary'] + '\n')
    output.insert('1.0', dconcept['FRE']['optimisme']['2-contrary'] + '\n')

def twocontraryita_clicked():
    output.delete(1.0, tk.END)        
    output.insert('1.0', dic[ITA]['ottimismo']['2-contrary'] + '\n')
    output.insert('1.0', dconcept['ITA']['ottimismo']['2-contrary'] + '\n')

def generatecorpus_clicked():
	global csvlist
	s = '# generated list of common concepts based on matrices of concepts.' + '\n'
	if bAddInitialSpace.get() == True: 
		sInitialChar = ' ' # add initial space to completion
	elif bAddInitialSpace.get() == False:
		sInitialChar = '' # no initial space
	match combobox1.current():
		case 0:
			for sublist1 in csvlist: 
				row = csvlist.index(sublist1)
				if bCheckbuttonPrepareTrainingdata.get() == False:
					lstr =  [ # join() instead of string concatenation to speed up
							csvlist[row][Aplus] + ' has a ' + 'positive' + ' connotation' + '\n',
							csvlist[row][A0] + ' has a ' + 'neutral' + ' connotation' + '\n',
							csvlist[row][Aminus] + ' has a ' + 'negative' + ' connotation' + '\n',
							csvlist[row][Āplus] + ' has a ' + 'positive' + ' connotation' + '\n',
							csvlist[row][Ā0] + ' has a ' + 'neutral' + ' connotation' + '\n',
							csvlist[row][Āminus] + ' has a ' + 'negative' + ' connotation' + '\n',
							]
					s = s + ''.join(lstr)
				else: # training data form
					lstr =  [ # join() instead of string concatenation to speed up
							'{"prompt": "What is the connotation of ' + csvlist[row][Aplus] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][Aplus] + ' is ' + 'positive' + '.<|endoftext|>"}\n',
							'{"prompt": "What is the connotation of ' + csvlist[row][A0] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][A0] + ' is ' + 'neutral' + '.<|endoftext|>"}\n',
							'{"prompt": "What is the connotation of ' + csvlist[row][Aminus] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][Aminus] + ' is ' + 'negative' + '.<|endoftext|>"}\n',
							'{"prompt": "What is the connotation of ' + csvlist[row][Aminus] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][Aminus] + ' is ' + 'positive' + '.<|endoftext|>"}\n',
							'{"prompt": "What is the connotation of ' + csvlist[row][Ā0] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][Ā0] + ' is ' + 'neutral' + '.<|endoftext|>"}\n',
							'{"prompt": "What is the connotation of ' + csvlist[row][Āminus] + '?", ' + '"completion": "' + sInitialChar + 'The connotation of ' + csvlist[row][Āminus] + ' is ' + 'negative' + '.<|endoftext|>"}\n'
							]
					s = s + ''.join(lstr)
		case 1:
			for sublist1 in csvlist: 
				row = csvlist.index(sublist1)
				if bCheckbuttonPrepareTrainingdata.get() == False:
					lstr =  [ # join() instead of string concatenation to speed up
							csvlist[row][Aplus] + ' is ' + 'contrary' + ' to ' + csvlist[row][Āminus] + '\n',
							csvlist[row][Āminus] + ' is ' + 'contrary' + ' to ' + csvlist[row][Aplus] + '\n',
							csvlist[row][Aplus] + ' is ' + 'complementary' + ' to ' + csvlist[row][Āplus] + '\n',
							csvlist[row][Āplus] + ' is ' + 'complementary' + ' to ' + csvlist[row][Aplus] + '\n',
							csvlist[row][A0] + ' is ' + 'dual' + ' to ' + csvlist[row][Ā0] + '\n',
							csvlist[row][Ā0] + ' is ' + 'dual' + ' to ' + csvlist[row][A0] + '\n',
							csvlist[row][Aminus] + ' is ' + 'contrary' + ' to ' + csvlist[row][Āplus] + '\n',
							csvlist[row][Āplus] + ' is ' + 'contrary' + ' to ' + csvlist[row][Aminus] + '\n',
							csvlist[row][Aminus] + ' is ' + 'extreme opposite' + ' to ' + csvlist[row][Āminus] + '\n',
							csvlist[row][Āminus] + ' is ' + 'extreme opposite' + ' to ' + csvlist[row][Aminus] + '\n'
							]
					s = s + ''.join(lstr)
				else: # training data form
					lstr =  [ # join() instead of string concatenation to speed up
							'{"prompt": "What is the ' + 'contrary' + ' of ' + csvlist[row][Aplus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Aplus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Aplus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' appropriately. ',
							'The ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Aplus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The contrary of ' + csvlist[row][Aplus] +' is a ' + 'negative' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Aplus]]['2-neutral'] + ' inappropriately. ',
							'The concept of ' + csvlist[row][Āminus] + ' is a ' + dic[ENG][csvlist[row][Āminus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Āminus] + ' is the ' + 'contrary' + ' of ' + csvlist[row][Aplus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'contrary' + ' of ' + csvlist[row][Āminus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Āminus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Āminus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' inappropriately. ',
							'The ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Āminus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The contrary of ' + csvlist[row][Āminus] +' is a ' + 'positive' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Āminus]]['2-neutral'] + ' appropriately. ',
							'The concept of ' + csvlist[row][Aplus] + ' is a ' + dic[ENG][csvlist[row][Aplus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Aplus] + ' is the ' + 'contrary' + ' of ' + csvlist[row][Āminus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'complementary' + ' of ' + csvlist[row][Aplus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Aplus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Aplus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' appropriately. ',
							'The ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Aplus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Aplus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The complementary of ' + csvlist[row][Aplus] +' is a ' + 'positive' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Aplus]]['2-neutral'] + ' appropriately. ',
							'The concept of ' + csvlist[row][Āplus] + ' is a ' + dic[ENG][csvlist[row][Āplus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Āplus] + ' is the ' + 'complementary' + ' of ' + csvlist[row][Aplus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'complementary' + ' of ' + csvlist[row][Āplus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Āplus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Āplus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' appropriately. ',
							'The ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Āplus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The complementary of ' + csvlist[row][Āplus] +' is a ' + 'positive' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Āplus]]['2-neutral'] + ' appropriately. ',
							'The concept of ' + csvlist[row][Aplus] + ' is a ' + dic[ENG][csvlist[row][Aplus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Aplus] + ' is the ' + 'complementary' + ' of ' + csvlist[row][Āplus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'dual' + ' of the ' + csvlist[row][A0] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, the ' + csvlist[row][A0] + ' is a concept which has a ' + dic[ENG][csvlist[row][A0]]['connotation'] + ' connotation. ',
							'The ' + 'dual' + ' concept of the ' + csvlist[row][A0] + ' will also be a ' + 'neutral' + ' concept. '
							'The ' + dic[ENG][csvlist[row][A0]]['dual'] + ' is also a ' + 'neutral' + ' concept. ',
							'Hence, the ' + csvlist[row][Ā0] + ' is the ' + 'dual' + ' of the ' + csvlist[row][A0] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'dual' + ' of the ' + csvlist[row][Ā0] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, the ' + csvlist[row][Ā0] + ' is a concept which has a ' + dic[ENG][csvlist[row][Ā0]]['connotation'] + ' connotation. ',
							'The ' + 'dual' + ' concept of the ' + csvlist[row][Ā0] + ' will also be a ' + 'neutral' + ' concept. '
							'The ' + dic[ENG][csvlist[row][A0]]['dual'] + ' is also a ' + 'neutral' + ' concept. ',
							'Hence, the ' + csvlist[row][A0] + ' is the ' + 'dual' + ' of the ' + csvlist[row][Ā0] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'contrary' + ' of ' + csvlist[row][Aminus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Aminus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Aminus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' inappropriately. ',
							'The ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Aminus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The contrary of ' + csvlist[row][Aminus] +' is a ' + 'positive' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Aminus]]['2-neutral'] + ' appropriately. ',
							'The concept of ' + csvlist[row][Āplus] + ' is a ' + dic[ENG][csvlist[row][Āplus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Āplus] + ' is the ' + 'contrary' + ' of ' + csvlist[row][Aminus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'contrary' + ' of ' + csvlist[row][Āplus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Āplus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Āplus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' appropriately. ',
							'The ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Āplus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Āplus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The contrary of ' + csvlist[row][Āplus] +' is a ' + 'negative' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Āplus]]['2-neutral'] + ' inappropriately. ',
							'The concept of ' + csvlist[row][Aminus] + ' is a ' + dic[ENG][csvlist[row][Aminus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Aminus] + ' is the ' + 'contrary' + ' of ' + csvlist[row][Āplus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'extreme opposite' + ' of ' + csvlist[row][Aminus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Aminus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Aminus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' inappropriately. ',
							'The ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Aminus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Aminus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The extreme opposite of ' + csvlist[row][Aminus] +' is a ' + 'negative' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Aminus]]['2-neutral'] + ' inappropriately. ',
							'The concept of ' + csvlist[row][Āminus] + ' is a ' + dic[ENG][csvlist[row][Āminus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Āminus] + ' is the ' + 'extreme opposite' + ' of ' + csvlist[row][Aminus] + '.<|endoftext|>"}\n',

							'{"prompt": "What is the ' + 'extreme opposite' + ' of ' + csvlist[row][Āminus] + '?", ', 
							'"completion": "' + sInitialChar,
							'On the one hand, ' + csvlist[row][Āminus] + ' is a concept which has a ' + dic[ENG][csvlist[row][Āminus]]['connotation'] + ' connotation. ',
							'It can be defined as the ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' inappropriately. ',
							'The ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' is a ' + 'neutral' + ' concept. ',
							'The dual concept of the ' + dic[ENG][csvlist[row][Āminus]]['1-neutral'] + ' is the ' + dic[ENG][csvlist[row][Āminus]]['2-neutral'] + '. ',
							'It is also a ' + 'neutral' + ' concept. ',
							'The extreme opposite of ' + csvlist[row][Āminus] +' is a ' + 'negative' + ' concept, ',
							'that can be defined as the ' + dic[ENG][csvlist[row][Āminus]]['2-neutral'] + ' inappropriately. ',
							'The concept of ' + csvlist[row][Aminus] + ' is a ' + dic[ENG][csvlist[row][Aminus]]['connotation'] + ' concept that fits this definition. ',
							'Hence, ' + csvlist[row][Aminus] + ' is the ' + 'extreme opposite' + ' of ' + csvlist[row][Āminus] + '.<|endoftext|>"}\n',

							]
					s = s + ''.join(lstr)
		case 2: # all a & b are in the same relationship as c & d
			items = [0,1,2,3,4,5]
			perms = permutations(items, 2) # 30 cases
			lperms = list(perms) # 30 cases: [[0,1],[0,2]...[5,4]]
			for sublist1 in csvlist: 
				row1 = csvlist.index(sublist1)
				for sublist2 in csvlist: 
					row2 = csvlist.index(sublist2)
					if row2 != row1:
						if bCheckbuttonPrepareTrainingdata.get() == False:
							for item in lperms: # select any permutation of two concepts of a given matrix
								# s = s + csvlist[row1][(item[0]+3)%6] + lstr1[1] + csvlist[row1][(item[1]+3)%6] + lstr1[3] + csvlist[row2][item[0]] + lstr1[5] + csvlist[row2][item[1]] + lstr1[7]
								lstr = [
										csvlist[row1][(item[0]+3)%6], # a1
										' and ',
										csvlist[row1][(item[1]+3)%6], # a2
										" are in the same relationship as ",
										csvlist[row2][item[0]], # b1
										' and ',
										csvlist[row2][item[1]], # b2
										'.\n'
										]
								s = s + ''.join(lstr)
						else: # training data form
							for item in lperms: # select any permutation of two concepts of a given matrix
								lstr = [ # join() instead of string concatenation to speed up
										'{"prompt": "With which concept is ',
										csvlist[row1][(item[0]+3)%6], # a1
										' in the same type of relationship as ',
										csvlist[row2][item[0]], # b1
										' and ',
										csvlist[row2][item[1]], # b2
										'?", ',
										'"completion": "' + sInitialChar,
										'On the one hand, ',
										csvlist[row1][(item[0]+3)%6], # a1
										' is a ',
										dic[ENG][csvlist[row1][(item[0]+3)%6]]['connotation'], # positive/neutral/negative
										' concept. ',
										'On the other hand, ',
										csvlist[row2][item[0]], # b1
										' is a ',
										dic[ENG][csvlist[row2][item[0]]]['connotation'], # positive/neutral/negative
										' one and ',
										csvlist[row2][item[1]], # b2
										' is a ',
										dic[ENG][csvlist[row2][item[1]]]['connotation'], # positive/neutral/negative
										' concept. Thus, the missing concept is a ',
										dic[ENG][csvlist[row2][item[1]]]['connotation'], # positive/neutral/negative
										' one. Hence, ',
										csvlist[row1][(item[0]+3)%6], # a1
										' and ',
										csvlist[row1][(item[1]+3)%6], # a2
										" are in the same relationship as ",
										csvlist[row2][item[0]], # b1
										' and ',
										csvlist[row2][item[1]], # b2
										'.<|endoftext|>"}\n'
										]
								s = s + ''.join(lstr)
	s = s + '# end of generated list of common concepts based on matrices of concepts: '  + str(count_rows(s)-2) + ' items' # remove 2 from count for header & trailer
	pyperclip.copy(s)
	output.delete(1.0, tk.END)
	output.insert('1.0', s)

def savemodule_clicked():
	generatecode_clicked() # generate code
	match combobox2.get():
		case 'english': 
			suffix = 'ENG'
		case 'français': 
			suffix = 'FRE'
		case 'italiano': 
			suffix = 'ITA'
	s = output.get("1.0", "end") # get whole text
	with open('dconcept' + suffix + '.py', 'w', encoding='utf8') as data: 
		data.write(s)

def generatecode_clicked():
    global csvlist
    match combobox2.get():
        case 'english': 
            suffix = 'ENG'
        case 'français': 
            suffix = 'FRE'
        case 'italiano': 
            suffix = 'ITA'
    s = '# list of concepts based on the matrices of concepts' + '\n'
    s = s + 'dconcept' + suffix + ' = {' + '\n' # beginning bracket
    for sublist in csvlist: # A+ concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][0] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':+1" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'positive'" + ',' + '\n' 
        s = s + '\t\t' + "'2-contrary':" + '"' + csvlist[row][5] + '"' + ',' + '\n' 
        s = s + '\t\t' + "'1-contrary':" + '"' + csvlist[row][2] + '"' + ',' + '\n' 
        s = s + '\t\t' + "'complementary':" + '"' + csvlist[row][3] + '"' + ',' + '\n' 
        s = s + '\t\t' + "'1-neutral':" + '"' + csvlist[row][1] + '"' + ',' + '\n' 
        s = s + '\t\t' + "'2-neutral':" + '"' + csvlist[row][4] + '"' + '\n' 
        s = s + '\t\t' + '},' + '\n'
    for sublist in csvlist: # A0 concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][1] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':0" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'neutral'" + ',' + '\n' 
        s = s + '\t\t' + "'dual':" + '"' + csvlist[row][4]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-positive':" + '"' + csvlist[row][0]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-negative':" + '"' + csvlist[row][2]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-positive':" + '"' + csvlist[row][3]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-negative':" + '"' + csvlist[row][5]+ '"'  + '\n' 
        s = s + '\t\t' + '},' + '\n'
    for sublist in csvlist: # A- concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][2] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':-1" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'negative'" + ',' + '\n' 
        s = s + '\t\t' + "'2-contrary':" + '"' + csvlist[row][3]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-contrary':" + '"' + csvlist[row][0]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'extreme opposite':" + '"' + csvlist[row][5]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-neutral':" + '"' + csvlist[row][1]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-neutral':" + '"' + csvlist[row][4]+ '"'  + '\n' 
        s = s + '\t\t' + '},' + '\n'
    for sublist in csvlist: # Ā+ concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][3] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':+1" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'positive'" + ',' + '\n' 
        s = s + '\t\t' + "'2-contrary':" + '"' + csvlist[row][2]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-contrary':" + '"' + csvlist[row][5]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'complementary':" + '"' + csvlist[row][0]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-neutral':" + '"' + csvlist[row][4]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-neutral':" + '"' + csvlist[row][1]+ '"'  + '\n' 
        s = s + '\t\t' + '},' + '\n'
    for sublist in csvlist: # Ā0 concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][4] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':0" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'neutral'" + ',' + '\n' 
        s = s + '\t\t' + "'dual':" + '"' + csvlist[row][1]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-positive':" + '"' + csvlist[row][3]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-negative':" + '"' + csvlist[row][5]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-positive':" + '"' + csvlist[row][0]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-negative':" + '"' + csvlist[row][2]+ '"'  + '\n' 
        s = s + '\t\t' + '},' + '\n'
    for sublist in csvlist: # Ā- concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][5] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':-1" + ',' + '\n' 
        s = s + '\t\t' + "'connotation':'negative'" + ',' + '\n' 
        s = s + '\t\t' + "'2-contrary':" + '"' + csvlist[row][0]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-contrary':" + '"' + csvlist[row][3]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'extreme opposite':" + '"' + csvlist[row][2]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'1-neutral':" + '"' + csvlist[row][4]+ '"'  + ',' + '\n' 
        s = s + '\t\t' + "'2-neutral':" + '"' + csvlist[row][1]+ '"'  + '\n' 
        if row == len(csvlist)-1:
            s = s + '\t\t' + '}' + '\n' # last item no , needed
        else:
            s = s + '\t\t' + '},' + '\n' # default case
    s = s + '\t' + '}' + '\n' # closing bracket

    s = s + '# end of generated list of concepts based on the matrices of concepts: ' + str(count_rows(s)) + ' lines' + '\n'
    pyperclip.copy(s)
    output.delete(1.0, tk.END)        
    output.insert('1.0', s)

def loadcsv_clicked(): # load csv file
    global csvlist
    match combobox2.get():
        case 'english': 
            filename = 'matrixENG.csv'
        case 'français': 
            filename = 'matrixFRE.csv'
        case 'italiano': 
            filename = 'matrixITA.csv'
    with open(filename, 'r', encoding="utf-8") as read_obj:
    # with open(r'matrix.csv', 'r', encoding="utf-8") as read_obj:
        csv_reader = csv.reader(read_obj, delimiter=';')
        csvlist = list(csv_reader) # convert string to list
    sheet6.set_sheet_data(data = csvlist,redraw = True)
    sheet6.set_column_widths(liColSize) # does not work at initialization
    sheet6.redraw()

notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill='both', expand=True)
frame_page1 = tk.Frame(notebook)
frame_page1.configure(bg='#C0DCC0')
frame_page1.pack(fill='both', expand=True, side="left")

# notebook.add(frame_page1, text='Taxonomy of concepts based on matrices of concepts, for AI improvement - MIT license - ' + sVersion)
notebook.add(frame_page1)

page1frame1 = tk.Frame(frame_page1) # Translate tab
page1frame1.pack(side="left", fill="y", expand=False, padx=px, pady=10)
page1frame1.configure(bg='#C0DCC0')
page1frame2 = tk.Frame(frame_page1)
page1frame2.pack(side = 'right', fill="y", expand=False, padx=px, pady=10)
page1frame2.configure(bg='#C0DCC0')

# input = scrolledtext.ScrolledText(page1frame1, width = 40, height = 3, font =("Times New Roman", 11),wrap=tk.WORD)
# input.pack(pady=py, side="top", fill="both", expand=True) #needs own line
sheet6 = tksheet.Sheet(page1frame1, width=780, height=300, total_columns=7, total_rows=15, show_x_scrollbar=True, show_y_scrollbar=True)
sheet6.font(newfont=("Times New Roman", 11, "normal"))
sheet6.headers(['A+','A0','A-','Ā+','Ā0','Ā-','*'])
sheet6.pack(fill='x')
sheet6.enable_bindings("all")
output = scrolledtext.ScrolledText(page1frame1, width=40, height=4)
output.pack(pady=py, fill="both", expand=True)
button29 = tk.Button(page1frame1, image=icon11, compound="left", text="Generate corpus", command=generatecorpus_clicked)
button29.pack(pady=py)
combobox1 = ttk.Combobox(page1frame1, values = listOptions, state="readonly")
combobox1.pack(pady=py, fill="x")
combobox1.current(0)
checkbutton21 = Checkbutton(page1frame1, text = "Prepare training data", variable = bCheckbuttonPrepareTrainingdata, onvalue = 1, offvalue = 0)
checkbutton21.pack(pady=0)
checkbutton22 = Checkbutton(page1frame1, text = "Add space character before completion", variable = bAddInitialSpace, onvalue = 1, offvalue = 0)
checkbutton22.pack(pady=0)

button25 = tk.Button(page1frame2, text="Load csv file", command=loadcsv_clicked)
button25.pack(pady=py, fill="x")
combobox2 = ttk.Combobox(page1frame2, values = ['english','français','italiano'], state="readonly")
combobox2.pack(pady=2, fill="x")
combobox2.current(0)
button26 = tk.Button(page1frame2, image=icon10, compound="left", text="Generate dictionary code", command=generatecode_clicked)
button26.pack(pady=py)
button30 = tk.Button(page1frame2, image=icon9, compound="left", text="Save module", command=savemodule_clicked)
button30.pack(pady=py)
button27 = tk.Button(page1frame2, text="dic[ENG]['courage']['2-contrary']", command=twocontraryeng_clicked)
button27.pack(pady=py)
button28 = tk.Button(page1frame2, text="dic[FRE]['optimisme']['2-contrary']", command=twocontraryfre_clicked)
button28.pack(pady=py)
button24 = tk.Button(page1frame2, text="dic[ITA]['ottimismo']['2-contrary']", command=twocontraryita_clicked)
button24.pack(pady=py)
button29 = tk.Button(page1frame2, compound="left", image=image1, height=200, width=200)
button29.pack(pady=py, fill="x")

########################################################
# NESTED DICTIONARIES BASED ON MATRICES OF CONCEPTS
########################################################

from dconceptENG import dconceptENG # English
from dconceptFRE import dconceptFRE # French
from dconceptITA import dconceptITA # Italian

########################################################
# NESTED MULTILINGUAL DICTIONARY BASED ON MATRICES OF CONCEPTS
########################################################

dic = [dconceptENG, dconceptFRE, dconceptITA] # example: dic[ENG]['courage']['2-contrary'] # get the 2-contrary of 'courage' in English
dconcept = {'ENG': dconceptENG, 'FRE': dconceptFRE, 'ITA': dconceptITA} # example: dconcept['ENG']['courage']['2-contrary'] # get the 2-contrary of 'courage' in English
########################################################

loadcsv_clicked()
root.mainloop()
