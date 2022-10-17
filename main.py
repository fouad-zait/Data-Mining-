from tkinter import ttk
from tkinter import *
import pandas as pd
import warnings
import math
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_excel("C:\\Users\\Vaio\\Desktop\\alldatasetDM\\Dataset1_ HR-EmployeeAttrition.xlsx",header=0)
l=df.values.tolist()
attributs=df.columns
def desc(l,attributs):
    listvalnull=list()
    listvalnonnull=list()
    listtype=list()
    listname=list()
    listclass=list()
    for attribut in range(0,len(attributs)):
        cpt=0
        for i in range(0,len(l)):
            if(type(l[i][attribut])!=str):
                if(math.isnan(l[i][attribut])):
                    cpt=cpt+1
        listvalnull.append(cpt)
        listtype.append(l[0][attribut].__class__.__name__)
        listclass.append(l[0][attribut].__class__)
        listvalnonnull.append(len(l)-cpt)
        listname.append(attributs[attribut])
        tabaffichage=pd.DataFrame({'Attributs':listname,'Valeurs null':listvalnull, 'Valeurs Non nulls':listvalnonnull,'Type':listtype,"Class":listclass})
    return tabaffichage
def descdataset(l,attributs):
    colonnes= list()
    lignes = list()
    colonnes.append(len(attributs))
    lignes.append(len(l))
    return pd.DataFrame({'Nombre de colonnes': colonnes, 'Nombre de lignes': lignes})

def moyenne(l, attributs):
    listmoyenne = list()
    listname = list()
    for attribute in range(0, len(attributs)):
        s = 0
        cpt = 0
        for i in range(0, len(l)):
            if (type(l[i][attribute]) != str):
                if (not math.isnan(l[i][attribute])):
                    s = s + l[i][attribute]
                    cpt = cpt + 1
                # print(s)
        if (cpt == 0):
            continue
        listmoyenne.append(s / cpt)
        listname.append(attributs[attribute])
    tabaffichage = pd.DataFrame({"Attributs":listname,'Moyenne': listmoyenne})
    #tabaffichage.index = listname
    # print(tabaffichage)
    return tabaffichage

def mediane(l,attributs):
    listmedianne=list()
    listname=list()
    for attribute in range(0,len(attributs)):
        cpt=0
        listval=list()
        listvaltriee=list()
        for i in range(0,len(l)):
            if(type(l[i][attribute])!=str):
                if(not math.isnan(l[i][attribute])):
                    cpt=cpt+1
                    listval.append(l[i][attribute])
        listvaltriee=tri(listval)
                #print(s)
        if (cpt==0):
            continue
        if(cpt % 2 !=0):
            listmedianne.append(listvaltriee[int(cpt/2)+1])
        if (cpt % 2 ==0) :
            listmedianne.append((listvaltriee[int((cpt+1)/2)]+listvaltriee[int(((cpt+1)/2)-1)])/2)
        listname.append(attributs[attribute])
    tabaffichage=pd.DataFrame({"Attributs":listname,'Medianne':listmedianne})
    #tabaffichage.index=listname
    #print(tabaffichage)
    return tabaffichage
def tri(tab):
    for i in range(len(tab)):
        min= i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab
def mode(l,attributs):
    listmode=list()
    listname=list()
    values=list()
    countall=list()
    for attribute in range(0,len(attributs)):
        listval=list()
        count=list()
        for i in range(0,len(l)):
            cpt=0
            if(l[i][attribute] not in listval ):
                listval.append(l[i][attribute])
                for j in range(0,len(l)):
                    if l[j][attribute]==l[i][attribute]:
                           cpt=cpt+1
                count.append(cpt)
        values.append(listval)
        countall.append(count)
        listname.append(attributs[attribute])
    for i in range(0,len(values)):
        occur=0
        for j in range(0,len(values[i])):
            if (countall[i][j]>occur):
                occur=countall[i][j]
                mode=values[i][j]
        listmode.append(mode)
    tabaffichage=pd.DataFrame({"Attributs":listname,'Mode':listmode})
    tabaffichage.index=listname
    #print(tabaffichage)
    return tabaffichage

def mesdisp(l,attributs):
    #listquartiles=list()
    q1=list()
    _min=list()
    _max=list()
    q3=list()
    q2=list()
    listname=list()
    iqr=list()
    etendu=list()
    midrange=list()
    for attribute in range(0,len(attributs)):
        cpt=0
        listval=list()
        listvaltriee=list()
        outlier=list()
        for i in range(0,len(l)):
            if(type(l[i][attribute])!=str):
                if(not math.isnan(l[i][attribute])):
                    cpt=cpt+1
                    listval.append(l[i][attribute])
        listvaltriee=tri(listval)
                #print(s)
        listquartile=list()
        if (cpt==0):
            continue
        else:
            #Q1
            listquartile.append(listvaltriee[0])
            #Q2
            n=cpt//2
            if(n % 2 !=0):
                listquartile.append(listvaltriee[int((n-1)/2)])
            else:
                listquartile.append((listvaltriee[int(n/2)]+listvaltriee[int(n/2-1)])/2)
            #Q3
            if(cpt % 2 !=0):
                listquartile.append(listvaltriee[int((n-1)/2)])
            else:
                listquartile.append((listvaltriee[int(cpt/2)]+listvaltriee[int(cpt/2-1)])/2)
            #Q4
            if(n % 2 !=0):
                listquartile.append(listvaltriee[int(n/2*3)])
            else:
                listquartile.append((listvaltriee[int(n/2*3)]+listvaltriee[int(n/2*3+1)])/2)
            #Q5
            listquartile.append(listvaltriee[cpt-1])
        _min.append(listquartile[0])
        q1.append(listquartile[1])
        q2.append(listquartile[2])
        q3.append(listquartile[3])
        _max.append(listquartile[4])
        iqr.append(listquartile[3]-listquartile[1])
        etendu.append(listquartile[4]-listquartile[0])
        midrange.append((listquartile[4]+listquartile[0])/2)
        #listquartiles.append(listquartile)
        listname.append(attributs[attribute])
    tabaffichage=pd.DataFrame({"Attributs":listname,"MIN":_min,"Q1":q1,"Q2":q2,"Q3":q3,"MAX":_max,"IQR":iqr,"ETENDU":etendu,"MIDRANGE":midrange})
    #tabaffichage.index=listname
    return tabaffichage

moy=moyenne(l,attributs)
mod=mode(l,attributs)
med=mediane(l,attributs)
def symetrie(moyenne,mode,med):
    columnsmode=mode.index
    listmode=mode.values.tolist()
    listmoy=moyenne["Moyenne"].values.tolist()
    listmed=med["Medianne"].values.tolist()
    listnamemod=list()
    uplistmode=list()
    listsymetrie=list()
    for i in range(0,len(listmode)):
        for j in range(0,len(listmode[i])):
            if(type(listmode[i][j])!=str):
                uplistmode.append(listmode[i][j])
                listnamemod.append(columnsmode[i])
    #print(listmoy)
    #print(listnamemod)
    #print(listmed)
    #print(uplistmode)
    l=list()
    for i in range(0,len(listmed)):
        if(round(listmed[i])==round(uplistmode[i])==round(listmoy[i])):
            listsymetrie.append("Symétrique")
            #l.append(listnamemod[i])
        elif(listmoy[i]>listmed[i]>uplistmode[i]):
            listsymetrie.append("Asymétrique à droite")
            #l.append(listnamemod[i])
        elif(listmoy[i]<listmed[i]<uplistmode[i]):
            listsymetrie.append("Asymétrique à gauche")
            #l.append(listnamemod[i])
        else:
            listsymetrie.append("Asymétrique")
            #l.append(listnamemod[i])
    return pd.DataFrame({'Attributs':listnamemod,"Moyenne":listmoy,"Medianne":listmed,"Mode":uplistmode,"Symetrie":listsymetrie})

def quartiles(l,attributs, attribut):
    b=False
    cpt=0
    for i in attributs:
        if (attribut==i):
            b=True
            nb=cpt
        else:
            cpt=cpt+1
    if (b==False):
        print("l'attribut n'existe pas!")
        return 0
    else:
        cpt=0
        listval=list()
        listvaltriee=list()
        for i in range(0,len(l)):
            if(type(l[i][nb])!=str):
                if(not math.isnan(l[i][nb])):
                    cpt=cpt+1
                    listval.append(l[i][nb])
        listvaltriee=tri(listval)
                #print(s)
        listquartile=list()
        if (cpt!=0):
            #Q1
            listquartile.append(listvaltriee[0])
            #Q2
            n=cpt//2
            if(n % 2 !=0):
                listquartile.append(listvaltriee[int((n-1)/2)])
            else:
                listquartile.append((listvaltriee[int(n/2)]+listvaltriee[int(n/2-1)])/2)
            #Q3
            if(cpt % 2 !=0):
                listquartile.append(listvaltriee[int((n-1)/2)])
            else:
                listquartile.append((listvaltriee[int(cpt/2)]+listvaltriee[int(cpt/2-1)])/2)
            #Q4
            if(n % 2 !=0):
                listquartile.append(listvaltriee[int(n/2*3)])
            else:
                listquartile.append((listvaltriee[int(n/2*3)]+listvaltriee[int(n/2*3+1)])/2)
            #Q5
            listquartile.append(listvaltriee[cpt-1])

        #print(f"Les quartiles de l'attribut '{attribut}' = {listquartile}")
        return listquartile





warnings.filterwarnings('ignore')
root = Tk()
root.title('DATA MINING PART 1')
root.state('zoomed')


# Create frame
my_frame = Frame(root)
my_frame.pack(padx=5,pady=100)
scrollbar = Scrollbar(my_frame)
h=Scrollbar(my_frame, orient='horizontal')
# Create treeview
my_tree = ttk.Treeview(my_frame,height=30)


#frame = Frame(root, width=1500, height=50)
#frame.place(relx=0.0, rely=0.9)
output = ttk.Label(root, text='',font=("Helvetica",10),relief="sunken")
output.place(relx=0.0, rely=0.96, anchor='sw')

#s=Scrollbar(output, orient='horizontal')
#s.config(command=frame.xview)

    # Pack the treeview finally
def set_cell_value(event):
    for item in my_tree.selection():
        item_text = my_tree.item(item, "values")
        column = my_tree.identify_column(event.x)
        row = my_tree.identify_row(event.y)
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(root, width=20 , height=2)
    entryedit.place(x=620, y=690 )

    def saveedit():
        columns=['Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department',
       'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',
       'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
       'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
       'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
       'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager']
        my_tree.set(item, column=column, value=entryedit.get(0.0, "end"))
        treeview_df = pd.DataFrame(None, columns=columns)
        for row in my_tree.get_children():
            # each row will come as a list under name "values"
            values = pd.DataFrame([my_tree.item(row)["values"]],
                                  columns=columns)
            # print(values)
            treeview_df = treeview_df.append(values)
        treeview_df.to_excel('C:\\Users\\Vaio\\Desktop\\alldatasetDM\\Employe.xlsx')
        entryedit.destroy()
        okb.destroy()

    okb = ttk.Button(root, text='Mise a jour du Data Set', width=30, command=saveedit)
    okb.place(x=800, y=690)

def file_open():
    changeText()
    df = pd.read_excel("C:\\Users\\Vaio\\Desktop\\alldatasetDM\\Dataset1_ HR-EmployeeAttrition.xlsx",header=0)
    # Clear old treeview
    clear_tree()
    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    my_tree.pack()
    my_tree.bind('<Double-1>', set_cell_value)

def descriptiondataset():
    changeText()
    df = descdataset(l,attributs)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    #scrollbar.pack(side=RIGHT, fill=Y)
    #h.pack(side=BOTTOM, fill='x')
    #h.config(command=my_tree.xview)
    #scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def descdata():
    changeText()
    df = desc(l, attributs)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def affichagemoyenne():
    changeText()
    df = moyenne(l,attributs)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def affichagemediane():
    changeText()
    df = mediane(l,attributs)
    # Clear old treeview
    clear_tree()
    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def affichagemode():
    changeText()
    df = mode(l,attributs)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()

def affichagesymetrie():
    changeText()
    df=symetrie(moy, mod, med)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def affichagemesdisp():
    changeText()
    df = mesdisp(l, attributs)
    # Clear old treeview
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    # Pack the treeview finally
    my_tree.pack()
def clear_tree():
    my_tree.delete(*my_tree.get_children())
def affichagehist():
    plt.figure(figsize=(4, 4))
    plt.xlabel("Valeurs")
    plt.ylabel("Nombres")
    plt.title("Histogramme de Age")
    plt.hist(df["Age"], color="green")
    plt.show()
def dfcolumns(attributs):
    return pd.DataFrame({'Attributs':attributs})
def dfcolumnsnostring(l,attributs):
    listatt = list()
    for att in range(0, len(attributs)):
        bool=True
        for i in range(0, len(l)):
            if (type(l[0][att])!=str):
                bool=False
        if(bool==False):
            listatt.append(attributs[att])
    return pd.DataFrame({'Attributs': listatt})
def menuattribut():
    changeText()
    df=dfcolumns(attributs)
    clear_tree()
    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    my_tree.pack()
    my_tree.bind('<Double-1>', histogramme)
def histogramme(event):
    for item in my_tree.selection():
        item_text = my_tree.item(item, "values")
        #column = my_tree.identify_column(event.x)
        #row = my_tree.identify_row(event.y)
        #print(item_text[0])
    #cn = int(str(column).replace('#', ''))
    #rn = int(str(row).replace('I', ''))
    #entryedit = Text(root, width=20 , height=2)
    #entryedit.place(x=620, y=690)
    def affichagehist():
        plt.figure(figsize=(6, 6))
        plt.xlabel("Valeurs")
        plt.ylabel("Nombres")
        plt.title("Histogramme")
        plt.hist(df[item_text[0]], color="green")
        plt.show()
        okb.destroy()
    okb = ttk.Button(root, text='Afficher', width=30, command=affichagehist)
    okb.place(x=800, y=690)
def menuattribut2():
    changeText()
    df=dfcolumnsnostring(l,attributs)
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    #print(df_rows)
    for row in df_rows:
        #print(row[0])
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    my_tree.pack()
    my_tree.bind('<Double-1>', boiteamoustache)
def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi
def boiteamoustache(event):
    for item in my_tree.selection():
        item_text = my_tree.item(item, "values")
    def affichageboite():
        listval = list()
        cpt = 0
        attributs=df.columns
        l=df.values.tolist()
        for attribute in range(0, len(attributs)):
            if (attributs[attribute] == item_text[0]):
                for i in range(0, len(l)):
                    if (type(l[i][attribute]) != str):
                        if (not math.isnan(l[i][attribute])):
                            listval.append(l[i][attribute])
                plt.boxplot(listval)
                plt.ylim(0, maximum(listval) + 2)
                plt.xlabel(item_text[0])
                plt.show()
        #listval = list()
        #for attribute in range(0, len(attributs)):
         #   if (attributs[attribute] == item_text):
          #      for i in range(0, len(l)):
           #         if (type(l[i][attribute]) != str):
            #            if (not math.isnan(l[i][attribute])):
             #               listval.append(l[i][attribute])
                #plt.boxplot(df[item_text[0]])
                #plt.ylim(0, maximum(df[item_text[0]]) + 2)
                #plt.xlabel(item_text[0])
                #plt.show()
                okb.destroy()
    okb = ttk.Button(root, text='Afficher', width=30, command=affichageboite)
    okb.place(x=800, y=690)
def menuattribut3():

    df=dfcolumnsnostring(l,attributs)
    clear_tree()

    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    #print(df_rows)
    for row in df_rows:
        #print(row[0])
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    my_tree.pack()
    my_tree.bind('<Double-1>', outliers)
def outliers(event):
    for item in my_tree.selection():
        item_text = my_tree.item(item, "values")
    def afficheOutliers ():
        attributs=df.columns
        l=df.values.tolist()
        quartl = quartiles(l, attributs, item_text[0])
        q1=quartl[1]
        q3=quartl[3]
        IQR=q3-q1
        outliersBas=list()
        outliersHaut=list()
        for attribute in range(0, len(attributs)):
            if (attributs[attribute] == item_text[0]):
                for i in range(0, len(l)):
                    if (type(l[i][attribute]) != str):
                        if(not math.isnan(l[i][attribute])):
                            if(l[i][attribute]<q1-1.5*IQR):
                                outliersBas.append(l[i][attribute])
                            if(l[i][attribute]>q3+1.5*IQR):
                                outliersHaut.append(l[i][attribute])
        outliersHaut=unique(outliersHaut)
        outliersBas=unique(outliersBas)
        # print(f"Les outliers en haut de l'attribut '{item_text[0]}' : {outliersHaut}")
        # print(f"Les outliers en bas de l'attribut '{item_text[0]}' : {outliersBas}")
        s1=""
        s2=""
        cpt=0
        for i in outliersHaut:
            s1=s1+","+str(i)
            cpt=cpt+1
            if(cpt==24):
                s1 = s1 + "\n"
            if(cpt==54):
                s1 = s1 + "\n"
            if (cpt == 84):
                s1 = s1 + "\n"
        for i in outliersBas:
            s2=s2+","+str(i)
        s1=s1[1:]
        s2=s2[1:]
        res = f"Les outliers en haut de l'attribut '{item_text[0]}' : {s1}\nLes outliers en bas de l'attribut '{item_text[0]}' : {s2}"
        if(not(outliersHaut) and not(outliersBas)):
            a=f"L'attribut '{item_text[0]}' n'a pas d'outliers"
            changeText(a)
            #s.pack(side=BOTTOM, fill='x')
            #frame.pack()
        elif(not(outliersHaut) and (outliersBas)):
            b=f"L'attribut '{item_text[0]}' n'a pas d'outliers en haut\nLes outliers en bas de l'attribut '{item_text[0]}' : {s2}"
            changeText(b)
        elif ((outliersHaut) and not(outliersBas)):
            a = f"Les outliers en haut de l'attribut '{item_text[0]}' : {s1}\nL'attribut '{item_text[0]}' n'a pas d'outliers en bas"
            changeText(a)
        else:
            changeText(res)
        okb.destroy()
    def unique(li):
        listUnique = list()
        for i in li:
            exist = False
            for j in listUnique:
                if (i==j):
                    exist = True
            if (exist == False):
                listUnique.append(i)
        return listUnique
    okb = ttk.Button(root, text='Afficher', width=30, command=afficheOutliers)
    okb.place(x=800, y=690)
def changeText(text=""):
    output['text'] = text
def dispertion():
    changeText()
    df=dfcolumns(attributs)
    clear_tree()
    # Set up new treeview
    my_tree["column"] = list(df.columns)
    for i in df.columns:
        my_tree.column(i, anchor=CENTER, width=150)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    scrollbar.pack(side=RIGHT, fill=Y)
    h.pack(side=BOTTOM, fill='x')
    h.config(command=my_tree.xview)
    scrollbar.config(command=my_tree.yview)
    my_tree.pack()
    my_tree.bind('<Return>', afficheDisp)
def afficheDisp(event):
    items=list()
    for item in my_tree.selection():
        i = (str(my_tree.item(item, "values")))
        i = i[2:-3]
        items.append(i)
    print(items)
    def affichageDisp():
        changeText()
        #sns.scatterplot(data=df, x=items[0], y=items[1])
        x=list()
        y=list()
        for attribute in range(0, len(attributs)):
            if (attributs[attribute] == items[0]):
                for i in range(0, len(l)):
                    x.append(l[i][attribute])
            if (attributs[attribute] == items[1]):
                for i in range(0, len(l)):
                    y.append(l[i][attribute])
        plt.scatter(x, y, c ="blue")
        plt.xlabel(items[0])
        plt.ylabel(items[1])
        plt.show()
        okb.destroy()
    okb = ttk.Button(root, text='Afficher', width=30, command=affichageDisp)
    okb.place(x=800, y=690)
my_menu = Menu(root)
root.config(menu=my_menu)

# Add menu dropdown
file_menu = Menu(my_menu, tearoff=False)
#my_menu.add_cascade(label="Questions", menu=file_menu)
#file_menu.add_command(label="Visualiser le DataFrame et MAJ avec enregistrement", command=file_open)
btn=Button(
    root,
    text='Visualiser le Dataset et MAJ avec enregistrement',
    command=file_open,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn.place(x=100, y=20)
btn1=Button(
    root,
    text='Description du Dataset',
    command=descriptiondataset,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn1.place(x=480, y=20)
btn2=Button(
    root,
    text='Description des attributs du Dataset',
    command=descdata,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn2.place(x=675, y=20)
btn3=Button(
    root,
    text='Moyenne',
    command=affichagemoyenne,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn3.place(x=957, y=20)
btn4=Button(
    root,
    text='Mediane',
    command=affichagemediane,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn4.place(x=1055, y=20)
btn5=Button(
    root,
    text='Mode',
    command=affichagemode,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn5.place(x=1150, y=20)
btn6=Button(
    root,
    text='Symétries',
    command=affichagesymetrie,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn6.place(x=1225, y=20)
btn7=Button(
    root,
    text='Mesures de dispersion',
    command=affichagemesdisp,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn7.place(x=100, y=60)
btn72=Button(
    root,
    text='Outliers',
    command=menuattribut3,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn72.place(x=293, y=60)
btn8=Button(
    root,
    text='Histogrammes',
    command=menuattribut,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn8.place(x=380, y=60)
btn9=Button(
    root,
    text='Boite a moustache',
    command=menuattribut2,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn9.place(x=520, y=60)

btn10=Button(    root,
    text='Diagrammes de dispertion des donnees',
    command=dispertion,
    bg='#081947',
    fg='#fff',
    font=('Times BOLD', 12)
    )
btn10.place(x=680, y=60)
#my_label = Label(root, text='hello')
#my_label.pack(pady=300)

root.mainloop()