import csv, pyperclip
import tksheet
from tksheet import Sheet
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *

root = tk.Tk()
root.geometry('%dx%d' % (1000, 800)) # width, height
root.title('Test')
root.configure(bg='#C0DCC0') # or lavender, antiquewhite

####################################################
# VARIABLES
####################################################
#csvlist = []
liColSize = 15
px = 5 # default padx
py = 5 # default pady
####################################################
# CONSTANTS
####################################################
ENG = 0
FRE = ENG+1 # 1
CIS = FRE+1 # 2
SAR = CIS+1 # 3
TAR = SAR+1 # 4
####################################################

def count_rows(string):
    # Split the string into lines and count the resulting list of lines
    row_count = len(string.split("\n"))
    return row_count

def twocontraryeng_clicked():
    output.delete(1.0, tk.END)        
    output.insert('1.0', dic[ENG]['courage']['2-contrary'])

def twocontraryfre_clicked():
    output.delete(1.0, tk.END)        
    output.insert('1.0', dic[FRE]['optimisme']['2-contrary'])

def generatecorpus_clicked():
    global csvlist
    pass

def generatecode_clicked():
    global csvlist
    s = '# list of concepts based on the matrices of concepts.' + '\n'
    s = s + 'dic = {' + '\n' # beginning bracket
    for sublist in csvlist: # A+ concepts
        row = csvlist.index(sublist)
        s = s + '\t' + '"' + csvlist[row][0] + '"' + ':{' + '\n'
        s = s + '\t\t' + "'value':+1" + ',' + '\n' 
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

    s = s + '# end of list of concepts based on the matrices of concepts: ' + str(count_rows(s)) + ' lines' + '\n'
    pyperclip.copy(s)
    output.delete(1.0, tk.END)        
    output.insert('1.0', s)

def loadcsv_clicked(): # load csv file
    global csvlist
    with open(r'matrix.csv', 'r', encoding="utf-8") as read_obj:
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

notebook.add(frame_page1, text='Taxonomy of concepts based on matrices of concepts - MIT license')

page1frame1 = tk.Frame(frame_page1) # Translate tab
page1frame1.pack(side="left", fill="y", expand=False, padx=px, pady=10)
page1frame1.configure(bg='#C0DCC0')
page1frame2 = tk.Frame(frame_page1)
page1frame2.pack(side = 'right', fill="y", expand=False, padx=px, pady=10)
page1frame2.configure(bg='#C0DCC0')

icon10 = PhotoImage(file = "text-x-python.png")

sheet6 = tksheet.Sheet(page1frame1, width=800, height=300, total_columns=7, total_rows=15, show_x_scrollbar=True, show_y_scrollbar=True)
sheet6.font(newfont=("Times New Roman", 11, "normal"))
sheet6.headers(['A+','A0','A-','Ā+','Ā0','Ā-','*'])
sheet6.pack(fill='x')
sheet6.enable_bindings("all")
output = scrolledtext.ScrolledText(page1frame1, width=40, height=4)
output.pack(pady=py, fill="both", expand=True)

button26 = tk.Button(page1frame2, image=icon10, compound="left", text="Generate dictionary code", command=generatecode_clicked)
button26.pack(pady=py, fill="x")
button27 = tk.Button(page1frame2, text="Test #1", command=twocontraryeng_clicked)
button27.pack(pady=py, fill="x")
button28 = tk.Button(page1frame2, text="Test #2", command=twocontraryfre_clicked)
button28.pack(pady=py, fill="x")
button29 = tk.Button(page1frame2, text="Generate corpus", command=generatecorpus_clicked)
button29.pack(pady=py, fill="x")

####################################################
# ENGLISH NESTED DICTIONARY BASED ON MATRICES OF CONCEPTS
####################################################
dicENG = {
	'courage':{
		'value':+1,
		'2-contrary':'cowardice',
		'1-contrary':'temerity',
		'complementary':'prudence',
		'1-neutral':'propensity to take risks',
		'2-neutral':'propensity to avoid risks'
		},
	'generosity':{
		'value':+1,
		'2-contrary':'avarice',
		'1-contrary':'prodigality',
		'complementary':'sense of economy',
		'1-neutral':'propensity to spend',
		'2-neutral':'propensity to spare'
		},
	'firmness':{
		'value':+1,
		'2-contrary':'laxity',
		'1-contrary':'inclemency',
		'complementary':'clemency',
		'1-neutral':'propensity to sanction',
		'2-neutral':'propensity to forgive'
		},
	'objectivity':{
		'value':+1,
		'2-contrary':'subjectivity',
		'1-contrary':'impersonality',
		'complementary':'commitment',
		'1-neutral':'being neutral',
		'2-neutral':'taking sides'
		},
	'frankness':{
		'value':+1,
		'2-contrary':'tendency to bias',
		'1-contrary':'bluntness',
		'complementary':'tact',
		'1-neutral':'acting directly',
		'2-neutral':'acting indirectly'
		},
	'mobility':{
		'value':+1,
		'2-contrary':'sedentariness',
		'1-contrary':'instability',
		'complementary':'stability',
		'1-neutral':'tendency to move',
		'2-neutral':'tendency to stay put'
		},
	'constructive ambition':{
		'value':+1,
		'2-contrary':'self renunciation',
		'1-contrary':'disproportionate ambition',
		'complementary':'abnegation',
		'1-neutral':'ambition',
		'2-neutral':'self-forgetfulness'
		},
	'eclecticism':{
		'value':+1,
		'2-contrary':'compartmentalization',
		'1-contrary':'superficiality',
		'complementary':'expertise',
		'1-neutral':'multi-disciplinarity',
		'2-neutral':'mono-disciplinarity'
		},
	'capacity for abstraction':{
		'value':+1,
		'2-contrary':'prosaicism',
		'1-contrary':'dogmatism',
		'complementary':'pragmatism',
		'1-neutral':'interest in the abstract',
		'2-neutral':'interest in the concrete'
		},
	'resolution':{
		'value':+1,
		'2-contrary':'irresolution',
		'1-contrary':'stubbornness',
		'complementary':'flexibility of mind',
		'1-neutral':'keeping one’s opinion',
		'2-neutral':'changing one’s mind'
		},
	'optimism':{
		'value':+1,
		'2-contrary':'pessimism',
		'1-contrary':'blissful optimism',
		'complementary':'awareness of problems',
		'1-neutral':'seeing the advantages',
		'2-neutral':'seeing the disadvantages'
		},
	'incredulity':{
		'value':+1,
		'2-contrary':'credulity',
		'1-contrary':'hyper-distrust',
		'complementary':'justified confidence',
		'1-neutral':'propensity to doubt',
		'2-neutral':'propensity to believe'
		},
	'temerity':{
		'value':-1,
		'2-contrary':'prudence',
		'1-contrary':'courage',
		'extreme opposite':'cowardice',
		'1-neutral':'propensity to take risks',
		'2-neutral':'propensity to avoid risks'
		},
	'prodigality':{
		'value':-1,
		'2-contrary':'sense of economy',
		'1-contrary':'generosity',
		'extreme opposite':'avarice',
		'1-neutral':'propensity to spend',
		'2-neutral':'propensity to spare'
		},
	'inclemency':{
		'value':-1,
		'2-contrary':'clemency',
		'1-contrary':'firmness',
		'extreme opposite':'laxity',
		'1-neutral':'propensity to sanction',
		'2-neutral':'propensity to forgive'
		},
	'impersonality':{
		'value':-1,
		'2-contrary':'commitment',
		'1-contrary':'objectivity',
		'extreme opposite':'subjectivity',
		'1-neutral':'being neutral',
		'2-neutral':'taking sides'
		},
	'bluntness':{
		'value':-1,
		'2-contrary':'tact',
		'1-contrary':'frankness',
		'extreme opposite':'tendency to bias',
		'1-neutral':'acting directly',
		'2-neutral':'acting indirectly'
		},
	'instability':{
		'value':-1,
		'2-contrary':'stability',
		'1-contrary':'mobility',
		'extreme opposite':'sedentariness',
		'1-neutral':'tendency to move',
		'2-neutral':'tendency to stay put'
		},
	'disproportionate ambition':{
		'value':-1,
		'2-contrary':'abnegation',
		'1-contrary':'constructive ambition',
		'extreme opposite':'self renunciation',
		'1-neutral':'ambition',
		'2-neutral':'self-forgetfulness'
		},
	'superficiality':{
		'value':-1,
		'2-contrary':'expertise',
		'1-contrary':'eclecticism',
		'extreme opposite':'compartmentalization',
		'1-neutral':'multi-disciplinarity',
		'2-neutral':'mono-disciplinarity'
		},
	'dogmatism':{
		'value':-1,
		'2-contrary':'pragmatism',
		'1-contrary':'capacity for abstraction',
		'extreme opposite':'prosaicism',
		'1-neutral':'interest in the abstract',
		'2-neutral':'interest in the concrete'
		},
	'stubbornness':{
		'value':-1,
		'2-contrary':'flexibility of mind',
		'1-contrary':'resolution',
		'extreme opposite':'irresolution',
		'1-neutral':'keeping one’s opinion',
		'2-neutral':'changing one’s mind'
		},
	'blissful optimism':{
		'value':-1,
		'2-contrary':'awareness of problems',
		'1-contrary':'optimism',
		'extreme opposite':'pessimism',
		'1-neutral':'seeing the advantages',
		'2-neutral':'seeing the disadvantages'
		},
	'hyper-distrust':{
		'value':-1,
		'2-contrary':'justified confidence',
		'1-contrary':'incredulity',
		'extreme opposite':'credulity',
		'1-neutral':'propensity to doubt',
		'2-neutral':'propensity to believe'
		},
	'prudence':{
		'value':+1,
		'2-contrary':'temerity',
		'1-contrary':'cowardice',
		'complementary':'courage',
		'1-neutral':'propensity to avoid risks',
		'2-neutral':'propensity to take risks'
		},
	'sense of economy':{
		'value':+1,
		'2-contrary':'prodigality',
		'1-contrary':'avarice',
		'complementary':'generosity',
		'1-neutral':'propensity to spare',
		'2-neutral':'propensity to spend'
		},
	'clemency':{
		'value':+1,
		'2-contrary':'inclemency',
		'1-contrary':'laxity',
		'complementary':'firmness',
		'1-neutral':'propensity to forgive',
		'2-neutral':'propensity to sanction'
		},
	'commitment':{
		'value':+1,
		'2-contrary':'impersonality',
		'1-contrary':'subjectivity',
		'complementary':'objectivity',
		'1-neutral':'taking sides',
		'2-neutral':'being neutral'
		},
	'tact':{
		'value':+1,
		'2-contrary':'bluntness',
		'1-contrary':'tendency to bias',
		'complementary':'frankness',
		'1-neutral':'acting indirectly',
		'2-neutral':'acting directly'
		},
	'stability':{
		'value':+1,
		'2-contrary':'instability',
		'1-contrary':'sedentariness',
		'complementary':'mobility',
		'1-neutral':'tendency to stay put',
		'2-neutral':'tendency to move'
		},
	'abnegation':{
		'value':+1,
		'2-contrary':'disproportionate ambition',
		'1-contrary':'self renunciation',
		'complementary':'constructive ambition',
		'1-neutral':'self-forgetfulness',
		'2-neutral':'ambition'
		},
	'expertise':{
		'value':+1,
		'2-contrary':'superficiality',
		'1-contrary':'compartmentalization',
		'complementary':'eclecticism',
		'1-neutral':'mono-disciplinarity',
		'2-neutral':'multi-disciplinarity'
		},
	'pragmatism':{
		'value':+1,
		'2-contrary':'dogmatism',
		'1-contrary':'prosaicism',
		'complementary':'capacity for abstraction',
		'1-neutral':'interest in the concrete',
		'2-neutral':'interest in the abstract'
		},
	'flexibility of mind':{
		'value':+1,
		'2-contrary':'stubbornness',
		'1-contrary':'irresolution',
		'complementary':'resolution',
		'1-neutral':'changing one’s mind',
		'2-neutral':'keeping one’s opinion'
		},
	'awareness of problems':{
		'value':+1,
		'2-contrary':'blissful optimism',
		'1-contrary':'pessimism',
		'complementary':'optimism',
		'1-neutral':'seeing the disadvantages',
		'2-neutral':'seeing the advantages'
		},
	'justified confidence':{
		'value':+1,
		'2-contrary':'hyper-distrust',
		'1-contrary':'credulity',
		'complementary':'incredulity',
		'1-neutral':'propensity to believe',
		'2-neutral':'propensity to doubt'
		},
	'cowardice':{
		'value':-1,
		'2-contrary':'courage',
		'1-contrary':'prudence',
		'extreme opposite':'temerity',
		'1-neutral':'propensity to avoid risks',
		'2-neutral':'propensity to take risks'
		},
	'avarice':{
		'value':-1,
		'2-contrary':'generosity',
		'1-contrary':'sense of economy',
		'extreme opposite':'prodigality',
		'1-neutral':'propensity to spare',
		'2-neutral':'propensity to spend'
		},
	'laxity':{
		'value':-1,
		'2-contrary':'firmness',
		'1-contrary':'clemency',
		'extreme opposite':'inclemency',
		'1-neutral':'propensity to forgive',
		'2-neutral':'propensity to sanction'
		},
	'subjectivity':{
		'value':-1,
		'2-contrary':'objectivity',
		'1-contrary':'commitment',
		'extreme opposite':'impersonality',
		'1-neutral':'taking sides',
		'2-neutral':'being neutral'
		},
	'tendency to bias':{
		'value':-1,
		'2-contrary':'frankness',
		'1-contrary':'tact',
		'extreme opposite':'bluntness',
		'1-neutral':'acting indirectly',
		'2-neutral':'acting directly'
		},
	'sedentariness':{
		'value':-1,
		'2-contrary':'mobility',
		'1-contrary':'stability',
		'extreme opposite':'instability',
		'1-neutral':'tendency to stay put',
		'2-neutral':'tendency to move'
		},
	'self renunciation':{
		'value':-1,
		'2-contrary':'constructive ambition',
		'1-contrary':'abnegation',
		'extreme opposite':'disproportionate ambition',
		'1-neutral':'self-forgetfulness',
		'2-neutral':'ambition'
		},
	'compartmentalization':{
		'value':-1,
		'2-contrary':'eclecticism',
		'1-contrary':'expertise',
		'extreme opposite':'superficiality',
		'1-neutral':'mono-disciplinarity',
		'2-neutral':'multi-disciplinarity'
		},
	'prosaicism':{
		'value':-1,
		'2-contrary':'capacity for abstraction',
		'1-contrary':'pragmatism',
		'extreme opposite':'dogmatism',
		'1-neutral':'interest in the concrete',
		'2-neutral':'interest in the abstract'
		},
	'irresolution':{
		'value':-1,
		'2-contrary':'resolution',
		'1-contrary':'flexibility of mind',
		'extreme opposite':'stubbornness',
		'1-neutral':'changing one’s mind',
		'2-neutral':'keeping one’s opinion'
		},
	'pessimism':{
		'value':-1,
		'2-contrary':'optimism',
		'1-contrary':'awareness of problems',
		'extreme opposite':'blissful optimism',
		'1-neutral':'seeing the disadvantages',
		'2-neutral':'seeing the advantages'
		},
	'credulity':{
		'value':-1,
		'2-contrary':'incredulity',
		'1-contrary':'justified confidence',
		'extreme opposite':'hyper-distrust',
		'1-neutral':'propensity to believe',
		'2-neutral':'propensity to doubt'
		}
	}

####################################################
# FRENCH NESTED DICTIONARY BASED ON MATRICES OF CONCEPTS
####################################################
# list of concepts based on the matrices of concepts.
dicFRE = {
	'courage':{
		'value':+1,
		'2-contrary':'lâcheté',
		'1-contrary':'témérité',
		'complementary':'prudence',
		'1-neutral':'propension à prendre des risques',
		'2-neutral':'propension à éviter les risques'
		},
	'générosité':{
		'value':+1,
		'2-contrary':'avarice',
		'1-contrary':'prodigalité',
		'complementary':"sens de l'économie",
		'1-neutral':'propension à dépenser',
		'2-neutral':'propension à épargner'
		},
	'fermeté':{
		'value':+1,
		'2-contrary':'laxisme',
		'1-contrary':'inclémence',
		'complementary':'clémence',
		'1-neutral':'propension à sanctionner',
		'2-neutral':'propension à pardonner'
		},
	'objectivité':{
		'value':+1,
		'2-contrary':'subjectivité',
		'1-contrary':'impersonnalité',
		'complementary':'engagement',
		'1-neutral':'propension à la neutralité',
		'2-neutral':'propension à prendre parti'
		},
	'franchise':{
		'value':+1,
		'2-contrary':'tendance à biaiser',
		'1-contrary':'brusquerie',
		'complementary':'tact',
		'1-neutral':"propension à l’action directe",
		'2-neutral':"propension à l’action indirecte"
		},
	'mobilité':{
		'value':+1,
		'2-contrary':'sédentarité',
		'1-contrary':'instabilité',
		'complementary':'stabilité',
		'1-neutral':'propension à se déplacer',
		'2-neutral':'propension à rester sur place'
		},
	'ambition constructive':{
		'value':+1,
		'2-contrary':'renoncement à soi',
		'1-contrary':'ambition disproportionnée',
		'complementary':'abnégation',
		'1-neutral':'ambition',
		'2-neutral':'oubli de soi'
		},
	'éclectisme':{
		'value':+1,
		'2-contrary':'cloisonnement',
		'1-contrary':'superficialité',
		'complementary':'expertise',
		'1-neutral':'attrait pour la pluridisciplinarité',
		'2-neutral':'attrait pour la mono-disciplinarité'
		},
	"capacité d'abstraction":{
		'value':+1,
		'2-contrary':'prosaïsme',
		'1-contrary':'dogmatisme',
		'complementary':'pragmatisme',
		'1-neutral':"intérêt pour l'abstrait",
		'2-neutral':'intérêt pour le concret'
		},
	'résolution':{
		'value':+1,
		'2-contrary':'irrésolution',
		'1-contrary':'entêtement',
		'complementary':"souplesse d'esprit",
		'1-neutral':'propension à maintenir une opinion',
		'2-neutral':"propension à changer d'avis"
		},
	'optimisme':{
		'value':+1,
		'2-contrary':'pessimisme',
		'1-contrary':'optimisme béat',
		'complementary':'conscience des problèmes',
		'1-neutral':'voir les avantages',
		'2-neutral':'voir les inconvénients'
		},
	'incrédulité':{
		'value':+1,
		'2-contrary':'crédulité',
		'1-contrary':'hyper-méfiance',
		'complementary':'confiance justifiée',
		'1-neutral':'propension à douter',
		'2-neutral':'propension à croire'
		},
	'propension à prendre des risques':{
		'value':0,
		'dual':'propension à éviter les risques',
		'1-positive':'courage',
		'1-negative':'témérité',
		'2-positive':'prudence',
		'2-negative':'lâcheté'
		},
	'propension à dépenser':{
		'value':0,
		'dual':'propension à épargner',
		'1-positive':'générosité',
		'1-negative':'prodigalité',
		'2-positive':"sens de l'économie",
		'2-negative':'avarice'
		},
	'propension à sanctionner':{
		'value':0,
		'dual':'propension à pardonner',
		'1-positive':'fermeté',
		'1-negative':'inclémence',
		'2-positive':'clémence',
		'2-negative':'laxisme'
		},
	'propension à la neutralité':{
		'value':0,
		'dual':'propension à prendre parti',
		'1-positive':'objectivité',
		'1-negative':'impersonnalité',
		'2-positive':'engagement',
		'2-negative':'subjectivité'
		},
	"propension à l’action directe":{
		'value':0,
		'dual':"propension à l’action indirecte",
		'1-positive':'franchise',
		'1-negative':'brusquerie',
		'2-positive':'tact',
		'2-negative':'tendance à biaiser'
		},
	'propension à se déplacer':{
		'value':0,
		'dual':'propension à rester sur place',
		'1-positive':'mobilité',
		'1-negative':'instabilité',
		'2-positive':'stabilité',
		'2-negative':'sédentarité'
		},
	'ambition':{
		'value':0,
		'dual':'oubli de soi',
		'1-positive':'ambition constructive',
		'1-negative':'ambition disproportionnée',
		'2-positive':'abnégation',
		'2-negative':'renoncement à soi'
		},
	'attrait pour la pluridisciplinarité':{
		'value':0,
		'dual':'attrait pour la mono-disciplinarité',
		'1-positive':'éclectisme',
		'1-negative':'superficialité',
		'2-positive':'expertise',
		'2-negative':'cloisonnement'
		},
	"intérêt pour l'abstrait":{
		'value':0,
		'dual':'intérêt pour le concret',
		'1-positive':"capacité d'abstraction",
		'1-negative':'dogmatisme',
		'2-positive':'pragmatisme',
		'2-negative':'prosaïsme'
		},
	'propension à maintenir une opinion':{
		'value':0,
		'dual':"propension à changer d'avis",
		'1-positive':'résolution',
		'1-negative':'entêtement',
		'2-positive':"souplesse d'esprit",
		'2-negative':'irrésolution'
		},
	'voir les avantages':{
		'value':0,
		'dual':'voir les inconvénients',
		'1-positive':'optimisme',
		'1-negative':'optimisme béat',
		'2-positive':'conscience des problèmes',
		'2-negative':'pessimisme'
		},
	'propension à douter':{
		'value':0,
		'dual':'propension à croire',
		'1-positive':'incrédulité',
		'1-negative':'hyper-méfiance',
		'2-positive':'confiance justifiée',
		'2-negative':'crédulité'
		},
	'témérité':{
		'value':-1,
		'2-contrary':'prudence',
		'1-contrary':'courage',
		'extreme opposite':'lâcheté',
		'1-neutral':'propension à prendre des risques',
		'2-neutral':'propension à éviter les risques'
		},
	'prodigalité':{
		'value':-1,
		'2-contrary':"sens de l'économie",
		'1-contrary':'générosité',
		'extreme opposite':'avarice',
		'1-neutral':'propension à dépenser',
		'2-neutral':'propension à épargner'
		},
	'inclémence':{
		'value':-1,
		'2-contrary':'clémence',
		'1-contrary':'fermeté',
		'extreme opposite':'laxisme',
		'1-neutral':'propension à sanctionner',
		'2-neutral':'propension à pardonner'
		},
	'impersonnalité':{
		'value':-1,
		'2-contrary':'engagement',
		'1-contrary':'objectivité',
		'extreme opposite':'subjectivité',
		'1-neutral':'propension à la neutralité',
		'2-neutral':'propension à prendre parti'
		},
	'brusquerie':{
		'value':-1,
		'2-contrary':'tact',
		'1-contrary':'franchise',
		'extreme opposite':'tendance à biaiser',
		'1-neutral':"propension à l’action directe",
		'2-neutral':"propension à l’action indirecte"
		},
	'instabilité':{
		'value':-1,
		'2-contrary':'stabilité',
		'1-contrary':'mobilité',
		'extreme opposite':'sédentarité',
		'1-neutral':'propension à se déplacer',
		'2-neutral':'propension à rester sur place'
		},
	'ambition disproportionnée':{
		'value':-1,
		'2-contrary':'abnégation',
		'1-contrary':'ambition constructive',
		'extreme opposite':'renoncement à soi',
		'1-neutral':'ambition',
		'2-neutral':'oubli de soi'
		},
	'superficialité':{
		'value':-1,
		'2-contrary':'expertise',
		'1-contrary':'éclectisme',
		'extreme opposite':'cloisonnement',
		'1-neutral':'attrait pour la pluridisciplinarité',
		'2-neutral':'attrait pour la mono-disciplinarité'
		},
	'dogmatisme':{
		'value':-1,
		'2-contrary':'pragmatisme',
		'1-contrary':"capacité d'abstraction",
		'extreme opposite':'prosaïsme',
		'1-neutral':"intérêt pour l'abstrait",
		'2-neutral':"intérêt pour le concret"
		},
	'entêtement':{
		'value':-1,
		'2-contrary':"souplesse d'esprit",
		'1-contrary':'résolution',
		'extreme opposite':'irrésolution',
		'1-neutral':'propension à maintenir une opinion',
		'2-neutral':"propension à changer d'avis"
		},
	'optimisme béat':{
		'value':-1,
		'2-contrary':'conscience des problèmes',
		'1-contrary':'optimisme',
		'extreme opposite':'pessimisme',
		'1-neutral':'voir les avantages',
		'2-neutral':'voir les inconvénients'
		},
	'hyper-méfiance':{
		'value':-1,
		'2-contrary':'confiance justifiée',
		'1-contrary':'incrédulité',
		'extreme opposite':'crédulité',
		'1-neutral':'propension à douter',
		'2-neutral':'propension à croire'
		},
	'prudence':{
		'value':+1,
		'2-contrary':'témérité',
		'1-contrary':'lâcheté',
		'complementary':'courage',
		'1-neutral':'propension à éviter les risques',
		'2-neutral':'propension à prendre des risques'
		},
	"sens de l'économie":{
		'value':+1,
		'2-contrary':'prodigalité',
		'1-contrary':'avarice',
		'complementary':'générosité',
		'1-neutral':'propension à épargner',
		'2-neutral':'propension à dépenser'
		},
	'clémence':{
		'value':+1,
		'2-contrary':'inclémence',
		'1-contrary':'laxisme',
		'complementary':'fermeté',
		'1-neutral':'propension à pardonner',
		'2-neutral':'propension à sanctionner'
		},
	'engagement':{
		'value':+1,
		'2-contrary':'impersonnalité',
		'1-contrary':'subjectivité',
		'complementary':'objectivité',
		'1-neutral':'propension à prendre parti',
		'2-neutral':'propension à la neutralité'
		},
	'tact':{
		'value':+1,
		'2-contrary':'brusquerie',
		'1-contrary':'tendance à biaiser',
		'complementary':'franchise',
		'1-neutral':"propension à l’action indirecte",
		'2-neutral':"propension à l’action directe"
		},
	'stabilité':{
		'value':+1,
		'2-contrary':'instabilité',
		'1-contrary':'sédentarité',
		'complementary':'mobilité',
		'1-neutral':'propension à rester sur place',
		'2-neutral':'propension à se déplacer'
		},
	'abnégation':{
		'value':+1,
		'2-contrary':'ambition disproportionnée',
		'1-contrary':'renoncement à soi',
		'complementary':'ambition constructive',
		'1-neutral':'oubli de soi',
		'2-neutral':'ambition'
		},
	'expertise':{
		'value':+1,
		'2-contrary':'superficialité',
		'1-contrary':'cloisonnement',
		'complementary':'éclectisme',
		'1-neutral':'attrait pour la mono-disciplinarité',
		'2-neutral':'attrait pour la pluridisciplinarité'
		},
	'pragmatisme':{
		'value':+1,
		'2-contrary':'dogmatisme',
		'1-contrary':'prosaïsme',
		'complementary':"capacité d'abstraction",
		'1-neutral':'intérêt pour le concret',
		'2-neutral':"intérêt pour l'abstrait"
		},
	"souplesse d'esprit":{
		'value':+1,
		'2-contrary':'entêtement',
		'1-contrary':'irrésolution',
		'complementary':'résolution',
		'1-neutral':"propension à changer d'avis",
		'2-neutral':'propension à maintenir une opinion'
		},
	'conscience des problèmes':{
		'value':+1,
		'2-contrary':'optimisme béat',
		'1-contrary':'pessimisme',
		'complementary':'optimisme',
		'1-neutral':'voir les inconvénients',
		'2-neutral':'voir les avantages'
		},
	'confiance justifiée':{
		'value':+1,
		'2-contrary':'hyper-méfiance',
		'1-contrary':'crédulité',
		'complementary':'incrédulité',
		'1-neutral':'propension à croire',
		'2-neutral':'propension à douter'
		},
	'propension à éviter les risques':{
		'value':0,
		'dual':'propension à prendre des risques',
		'1-positive':'prudence',
		'1-negative':'lâcheté',
		'2-positive':'courage',
		'2-negative':'témérité'
		},
	'propension à épargner':{
		'value':0,
		'dual':'propension à dépenser',
		'1-positive':"sens de l'économie",
		'1-negative':'avarice',
		'2-positive':'générosité',
		'2-negative':'prodigalité'
		},
	'propension à pardonner':{
		'value':0,
		'dual':'propension à sanctionner',
		'1-positive':'clémence',
		'1-negative':'laxisme',
		'2-positive':'fermeté',
		'2-negative':'inclémence'
		},
	'propension à prendre parti':{
		'value':0,
		'dual':'propension à la neutralité',
		'1-positive':'engagement',
		'1-negative':'subjectivité',
		'2-positive':'objectivité',
		'2-negative':'impersonnalité'
		},
	"propension à l’action indirecte":{
		'value':0,
		'dual':"propension à l’action directe",
		'1-positive':'tact',
		'1-negative':'tendance à biaiser',
		'2-positive':'franchise',
		'2-negative':'brusquerie'
		},
	'propension à rester sur place':{
		'value':0,
		'dual':'propension à se déplacer',
		'1-positive':'stabilité',
		'1-negative':'sédentarité',
		'2-positive':'mobilité',
		'2-negative':'instabilité'
		},
	'oubli de soi':{
		'value':0,
		'dual':'ambition',
		'1-positive':'abnégation',
		'1-negative':'renoncement à soi',
		'2-positive':'ambition constructive',
		'2-negative':'ambition disproportionnée'
		},
	'attrait pour la mono-disciplinarité':{
		'value':0,
		'dual':'attrait pour la pluridisciplinarité',
		'1-positive':'expertise',
		'1-negative':'cloisonnement',
		'2-positive':'éclectisme',
		'2-negative':'superficialité'
		},
	'intérêt pour le concret':{
		'value':0,
		'dual':"intérêt pour l'abstrait",
		'1-positive':'pragmatisme',
		'1-negative':'prosaïsme',
		'2-positive':"capacité d'abstraction",
		'2-negative':'dogmatisme'
		},
	"propension à changer d'avis":{
		'value':0,
		'dual':'propension à maintenir une opinion',
		'1-positive':"souplesse d'esprit",
		'1-negative':'irrésolution',
		'2-positive':'résolution',
		'2-negative':'entêtement'
		},
	'voir les inconvénients':{
		'value':0,
		'dual':'voir les avantages',
		'1-positive':'conscience des problèmes',
		'1-negative':'pessimisme',
		'2-positive':'optimisme',
		'2-negative':'optimisme béat'
		},
	'propension à croire':{
		'value':0,
		'dual':'propension à douter',
		'1-positive':'confiance justifiée',
		'1-negative':'crédulité',
		'2-positive':'incrédulité',
		'2-negative':'hyper-méfiance'
		},
	'lâcheté':{
		'value':-1,
		'2-contrary':'courage',
		'1-contrary':'prudence',
		'extreme opposite':'témérité',
		'1-neutral':'propension à éviter les risques',
		'2-neutral':'propension à prendre des risques'
		},
	'avarice':{
		'value':-1,
		'2-contrary':'générosité',
		'1-contrary':"sens de l'économie",
		'extreme opposite':'prodigalité',
		'1-neutral':'propension à épargner',
		'2-neutral':'propension à dépenser'
		},
	'laxisme':{
		'value':-1,
		'2-contrary':'fermeté',
		'1-contrary':'clémence',
		'extreme opposite':'inclémence',
		'1-neutral':'propension à pardonner',
		'2-neutral':'propension à sanctionner'
		},
	'subjectivité':{
		'value':-1,
		'2-contrary':'objectivité',
		'1-contrary':'engagement',
		'extreme opposite':'impersonnalité',
		'1-neutral':'propension à prendre parti',
		'2-neutral':'propension à la neutralité'
		},
	'tendance à biaiser':{
		'value':-1,
		'2-contrary':'franchise',
		'1-contrary':'tact',
		'extreme opposite':'brusquerie',
		'1-neutral':'propension à l’action indirecte',
		'2-neutral':'propension à l’action directe'
		},
	'sédentarité':{
		'value':-1,
		'2-contrary':'mobilité',
		'1-contrary':'stabilité',
		'extreme opposite':'instabilité',
		'1-neutral':'propension à rester sur place',
		'2-neutral':'propension à se déplacer'
		},
	'renoncement à soi':{
		'value':-1,
		'2-contrary':'ambition constructive',
		'1-contrary':'abnégation',
		'extreme opposite':'ambition disproportionnée',
		'1-neutral':'oubli de soi',
		'2-neutral':'ambition'
		},
	'cloisonnement':{
		'value':-1,
		'2-contrary':'éclectisme',
		'1-contrary':'expertise',
		'extreme opposite':'superficialité',
		'1-neutral':'attrait pour la mono-disciplinarité',
		'2-neutral':'attrait pour la pluridisciplinarité'
		},
	'prosaïsme':{
		'value':-1,
		'2-contrary':"capacité d'abstraction",
		'1-contrary':'pragmatisme',
		'extreme opposite':'dogmatisme',
		'1-neutral':'intérêt pour le concret',
		'2-neutral':"intérêt pour l'abstrait"
		},
	'irrésolution':{
		'value':-1,
		'2-contrary':'résolution',
		'1-contrary':"souplesse d'esprit",
		'extreme opposite':'entêtement',
		'1-neutral':"propension à changer d'avis",
		'2-neutral':'propension à maintenir une opinion'
		},
	'pessimisme':{
		'value':-1,
		'2-contrary':'optimisme',
		'1-contrary':'conscience des problèmes',
		'extreme opposite':'optimisme béat',
		'1-neutral':'voir les inconvénients',
		'2-neutral':'voir les avantages'
		},
	'crédulité':{
		'value':-1,
		'2-contrary':'incrédulité',
		'1-contrary':'confiance justifiée',
		'extreme opposite':'hyper-méfiance',
		'1-neutral':'propension à croire',
		'2-neutral':'propension à douter'
		}
	}
# end of list of concepts based on the matrices of concepts: 580 lines

####################################################
# NESTED MULTILINGUAL DICTIONARY BASED ON MATRICES OF CONCEPTS
####################################################
dic = [dicENG, dicFRE] # example: dic[ENG]['courage']['2-contrary'] # get the 2-contrary of 'courage' in English

###########################

loadcsv_clicked()
root.mainloop()



