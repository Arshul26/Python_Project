#homepage is designed from here 
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        self.root=root
        #setting title
        root.title("first.py")
        #setting window size
        width=1000
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_512=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_512["font"] = ft
        GLabel_512["fg"] = "#333333"
        GLabel_512["justify"] = "center"
        GLabel_512["text"] = "WELCOME TO "
        GLabel_512.place(x=410,y=30,width=170,height=30)

        GLabel_939=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_939["font"] = ft
        GLabel_939["fg"] = "#333333"
        GLabel_939["justify"] = "center"
        GLabel_939["text"] = "HEALTHĀSTRA will always be with you in this journey! and trust me it is going to be a exciting journey ahead!"
        GLabel_939.place(x=140,y=220,width=730,height=30)

        GLabel_614=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_614["font"] = ft
        GLabel_614["fg"] = "#333333"
        GLabel_614["justify"] = "center"
        GLabel_614["text"] = "By the way have you ever seen a rabbit wearing glasses!? No!Right??Because he eats carrot!"
        GLabel_614.place(x=180,y=270,width=638,height=30)

        GLabel_292=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_292["font"] = ft
        GLabel_292["fg"] = "#333333"
        GLabel_292["justify"] = "center"
        GLabel_292["text"] = "Yes!You can laugh at my lame joke:-)But According to experts diet is far more important than Exercise!"
        GLabel_292.place(x=150,y=310,width=706,height=45)

        GLabel_707=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_707["font"] = ft
        GLabel_707["fg"] = "#333333"
        GLabel_707["justify"] = "center"
        GLabel_707["text"] = "You can only harness the true power of HEALTHĀSTRA if diet is your first priority!"
        GLabel_707.place(x=140,y=370,width=720,height=34)

        GButton_874=tk.Button(root)
        GButton_874["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_874["font"] = ft
        GButton_874["fg"] = "#000000"
        GButton_874["justify"] = "center"
        GButton_874["text"] = "CONTINUE"
        GButton_874.place(x=440,y=450,width=110,height=30)
        GButton_874["command"] = self.GButton_874_command

        GLabel_8=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#333333"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "Hello! This is your first step towards your fitness journey"
        GLabel_8.place(x=180,y=0,width=622,height=30)

        GLabel_258=tk.Label(root)
        GLabel_258["activebackground"] = "#e3d5d5"
        GLabel_258["activeforeground"] = "#d5baba"
        GLabel_258["bg"] = "#FFFFFF"
        ft = tkFont.Font(family='Times',size=70)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#393d49"
        GLabel_258["justify"] = "center"
        GLabel_258["text"] = "HEALTHĀSTRA"
        GLabel_258.place(x=140,y=70,width=720,height=127)

    def GButton_874_command(self):
        self.root.destroy()



#weekdiet and nutrition
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
from tkinter import *
def display():
    '''if (x1.get()==1):
        print("ok")
    elif (x2.get()==1):
        print("yes")
    elif (x3.get()==1):
        print("no")'''

window = Tk(className='Week Diet')
window.geometry("1000x600")


Label(window, text="Select Day:",font=("Times",20,'bold'),fg='black',bg='white').grid(row=0, sticky=N)
x1 = IntVar()
check_button = Checkbutton(window, text="Monday",variable=x1,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=1, sticky=W)
x2 = IntVar()
check_button = Checkbutton(window, text="Tuesday",variable=x2,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=2, sticky=W)
x3 = IntVar()
check_button = Checkbutton(window, text="Wednesday",variable=x3,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=3, sticky=W)
x4 = IntVar()
check_button = Checkbutton(window, text="Thursday",variable=x4,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=4, sticky=W)
x5 = IntVar()
check_button = Checkbutton(window, text="Friday",variable=x5,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=5, sticky=W)
x6 = IntVar()
check_button = Checkbutton(window, text="Saturday",variable=x6,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=6, sticky=W)
x7 = IntVar()
check_button = Checkbutton(window, text="Sunday",variable=x7,onvalue=1,offvalue=0,command=display,font=("Times",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=7, sticky=W)

button = Button(window, text="Next", command=window.destroy,font=('calibri',15,'bold','underline'),fg='black',bg='white')
button.grid(row=8,column=4,padx=100)

window.mainloop()





from tkinter import *
def display():
    if (x1.get()==1)  and (x2.get()==1) and (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (2562,100,315) )
    
    elif (x1.get()==1) and (x2.get()==1) and (x3.get()==0) and (x4.get()==0):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1200,65,150) )
    elif (x1.get()==1) and (x3.get()==1) and (x3.get()==1) and (x4.get()==1) :
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (800,42,60) )
    elif (x1.get()==1) and (x4.get()==1) and (x3.get()==0 and (x2.get()==0)):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1600,73,17) )
    elif (x2.get()==1) and (x3.get()==1) and  (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (700,38,150) )
    elif (x2.get()==1) and (x4.get()==1) and (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1500,70,200) )
    elif (x3.get()==1) and (x4.get()==1) and  (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1000,38,170) )
    elif (x1.get()==1)  and (x2.get()==1) and (x3.get()==1) and (x4.get()==0):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1500,73,180) )
    elif (x1.get()==1)  and (x2.get()==1) and (x4.get()==1) and (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (2300,110,200) )
    elif (x1.get()==1)  and (x3.get()==1) and (x4.get()==1) and  (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1700,85,180) )
    elif (x2.get()==1)  and (x3.get()==1) and (x4.get()==1) and (x3.get()==1) and (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (1500,77,220) )
    elif (x1.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (656,35.6,30) )
    elif (x2.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (620,30.6,123.6) )
    elif (x3.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (186,7.1,27.2) )
    elif (x4.get()==1):
        print("Total Calorie= %d ,\nTotal Protein= %d,\nTotal Carbs= %d" % (800,40,152) )



window = Tk(className='Week Diet')
window.geometry("1000x500")


Label(window, text="      Select your Meal",font=("Times",20,'bold'),fg='black',bg='white').grid(row=0, sticky=W)
x1 = IntVar()
check_button = Checkbutton(window, text="Breakfast",variable=x1,onvalue=1,offvalue=0,command=display,font=("Arial",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=1, sticky=W)

Label(window, text="         2 Gobhi Paratha,Curd,2 Boiled Egg,100Ml Milk",font=("Ariel",16),fg='white',bg='black').grid(row=2, sticky=W)                        
x2 = IntVar()
check_button = Checkbutton(window, text="Lunch",variable=x2,onvalue=1,offvalue=0,command=display,font=("Arial",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=3, sticky=W)
Label(window, text="         Aloo Palak,Matar Paneer,dal,Veg pulao,3 Roti",font=("Ariel",16),fg='white',bg='black').grid(row=4, sticky=W)
x3 = IntVar()
check_button = Checkbutton(window, text="Snacks",variable=x3,onvalue=1,offvalue=0,command=display,font=("Arial",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=5, sticky=W)
Label(window, text="         Macroni,Tea",font=("Ariel",16),fg='white',bg='black').grid(row=6, sticky=W)                        
x4 = IntVar() 
check_button = Checkbutton(window, text="Dinner",variable=x4,onvalue=1,offvalue=0,command=display,font=("Arial",20),fg='black',
                        activeforeground="green",activebackground="black",padx=25,pady=10).grid(row=7, sticky=W)
Label(window, text="         Soya Masala,Lauki,Chana Dal,Rice,3 Roti,2 Gulab Jamun",font=("Ariel",16),fg='white',bg='black').grid(row=8, sticky=W)

button = Button(window, text="Next", command=window.destroy, font=('calibri',15,'bold','underline'),fg='black',bg='white')
button.grid(row=10, column=20, padx=100)



window.mainloop()

#calorie counter begins here
import tkinter as tk
from functools import partial  
def call_result(label_result, label_result2, n1, n2, n3):  
    num1 = (n1.get())  
    num2 = (n2.get()) 
    num3 = (n3.get())
    
    result = ((66.5 + (13.8*int(num1)) + (5*int(num3)))/6.8* int(num2))/2
    result2 = '''For an ideal person with this weight, height, and age 
                    this the amount of calories one shoould take'''
    label_result.config(text="Result = %d" % result)
    label_result2.config(text=result2)  
    return
       
root = tk.Tk()  
root.geometry('1000x500')  
  
root.title('Calorie Counter')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()  

  
labelNum1 = tk.Label(root, text="Enter your Weight",font=("Times",20),fg='black',).grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Enter your Age",font=("Times",20),fg='black',).grid(row=2, column=0)  

labelNum3 = tk.Label(root, text="Enter your Height in cm",font=("Times",20),fg='black',).grid(row=3, column=0)

labelResult = tk.Label(root,font= ("Times",15,'bold'))
labelResult2 = tk.Label(root,font= ("Times",15,'bold'))  
  
labelResult.grid(row=9, column=2)
labelResult2.grid(row=8, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)  
  

  
call_result = partial(call_result, labelResult, labelResult2, number1, number2, number3)  
  
buttonCal = tk.Button(root, text="Total Calories", font=("Times",20,'underline'),fg='black',bg='white',command=call_result)
buttonCal.grid(row=10,column=0)
button =tk.Button(root, text="Next", command=root.destroy, font=("Times",20,'underline'),fg='black',bg='white') 
button.grid(row=10,column=4)
root.mainloop()



#bmi counter begins here
import tkinter as tk  
from functools import partial  

def call_result(label_result,label_result2,label_result3,label_result4,label_result5, n4, n5):  
    num4 = (n4.get())
    num5 = (n5.get())
    result = float(num4)/((float(num5)*float(num5)))
    result2="If your BMI is under 18 ----You are underweight"
    result3="If your BMI is between 18 and 24 ----You are normal"
    result4="If your BMI is over 24 ----You are overweight "
    result5="Now based upon on your BMI we will suggest exercises specially customised for you!!!"
    label_result.config(text="Your BMI is = %d" % result)
    label_result2.config(text=result2)
    label_result3.config(text=result3)
    label_result4.config(text=result4)
    label_result5.config(text=result5)
    return
    
      

       
root = tk.Tk()  
root.geometry('1000x500') 
 
  
root.title('BMI Calculator')  
   
number4 = tk.StringVar()
number5 = tk.StringVar()


labelNum4 = tk.Label(root, text="Enter your Weight(in kg)",font= ("Times",15,'bold')).grid(row=1,column=1)
labelNum5 = tk.Label(root, text="Enter your Height(in metre)",font=("Times",15,'bold')).grid(row=2,column=1)
labelResult = tk.Label(root,font=("Times",15,'bold'))
labelResult2 = tk.Label(root,font=("Times",15,'bold')) 
labelResult3 = tk.Label(root,font=("Times",15,'bold')) 
labelResult4 = tk.Label(root,font=("Times",15,'bold')) 
labelResult5 = tk.Label(root,font=("Times",15,'bold'))   
  
labelResult.grid(row=7, column=1) 
labelResult2.grid(row=8, column=1) 
labelResult3.grid(row=9, column=1) 
labelResult4.grid(row=10, column=1) 
labelResult5.grid(row=11, column=1)  
  
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=1, column=2)  
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=2, column=2) 
  
call_result = partial(call_result, labelResult,labelResult2, labelResult3, labelResult4, labelResult5, number4, number5)  
  
buttonCal = tk.Button(root, text="BMI",font=("Times",20,'underline'),command=call_result).grid(row=5, column=1) 

button = tk.Button(root, text="Next",font=("Times",20,'underline'),command=root.destroy).grid(row=20, column=1)
  
root.mainloop() 

#exercise code and gym status 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ").lower()
height = int(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kgs: "))
status = input("enter your status(less active,active,very active): ").lower()
goal = input('what is your goal:- fat lose or muscle gain: ')
class workout_plan:

  def func():
    if gender == 'male':
      if status == 'less active' or age >= 40:
        print(" ")
        print("You should follow bro split with 2 days rest")
        print(" ")
        k = input("Do you want to know your workout plan: ").lower()
        if k == 'yes':
          print(" ")
          print("monday - chest")
          print("tuesday - back")
          print("wednesday - shoulder")
          print("thrusday - triceps,tricep")
          print("friday - legs")
          print("saturday,sunday - rest")
        else:
          print("OK")
      elif status == 'active' and age < 40:
        print(" ")
        print("you should follow bro split and hit legs twice a week")
        print(" ")
        l = input("Do you want to know your workout plan: ")
        if l == 'yes':
          print(" ")
          print("monday - legs")
          print("tuesday - chest")
          print('wednesday - back')
          print('thrusday - legs')
          print('friday - shoulder')
          print('saturday - bicep and tricep')
          print('sunday - rest')
        elif l == 'no':
          print('OK')
      elif status == 'very active' and age < 40:
        print(" ")
        print("You should follow PPL split")
        print(" ")
        m = input("Do you want to know your workout: ").lower()
        if m == 'yes':
          print(" ")
          print("monday - chest,tricep")
          print("tuesday - back,bicep")
          print("wednesday - shoulder,legs")
          print("thrusday - chest,tricep")
          print('friday - back,bicep')
          print("saturday - legs,shoulder")
          print('sunday - rest')
        elif m == 'no':
          print("OK")
      else:
        print("status not valid")
    elif gender == 'female':
      if status == 'less active' or age >= 40:
        print(' ')
        print("you should workout 4 days a week")
        print(" ")
        a = input("Do you wish to know your workout plan: ")
        if a == 'yes':
          print(' ')
          print("monday - chest,tricep")
          print('tuesday - back bicep')
          print('wednesday - legs')
          print('thruday - shoulder')
          print('friday,saturday,sunday-rest')
        elif a == 'no':
          print("OK")
      elif status == 'active' and age < 40:
        print(" ")
        print("you should workout 6 days a week following bro split")
        print(' ')
        b = input("Do you want to know your workout plan")
        if b == 'yes':
          print(' ')
          print("monday - chest ")
          print("tuesday - back")
          print('wednesday - legs')
          print('thrusday - shoulder')
          print('friday - bicep,tricep')
          print('saturday - legs')
          print("sunday - rest")
      elif status == 'very active' and age <40:
        print("you should do PPL split")
        print(" ")
      c = input("do you want to know your workout: ").lower
      if c == 'yes':
        print(' ')
        print('monday - chest tricep')
        print('tuesday - back bicep')
        print('wednesday - legs shoulder')
        print('thursday - chest tricep')
        print('friday - back bicep')
        print('saturday - legs shoulder')
      elif c == 'no':
        print('OK')
    if goal == 'fat lose':
      print('you should also do cardio after workout')
exercise = workout_plan
exercise.func()
class exc:
  def workout():
    print(' ')
    a1 = input("Do you want to know any body part exercise if yes then specify\n")
    if a1 == 'chest':
      print(' ')
      print('flat bench press')
      print('incline dumbell press')
      print('cable fly')
      print('butterfly')
      print('pullover')
      print('dips')
    if a1 == 'back':
      print(' ')
      print('lat pull down')
      print('close grip')
      print('seated row')
      print('one arm row')
      print('pull ups ')

    if a1 == 'bicep':
      print(' ')
      print('bicep curl')
      print('hammer curl')
      print('pitcher curl')
      print('close grip barbell curl')

    if a1 == 'tricep':
      print('pull push down')
      print('skull crusher')
      print('kickback')
      print('diamond pushups')

    if a1 == 'shoulder':
      print('dumbell press')
      print('side raises')
      print('front raises')
      print('upright')
      print('shrugs')

    if a1 == 'legs':
      print(' ')
      print('free squats')
      print('weighted squats')
      print('leg press')
      print('lunges')
      print('bulgarian squats')
      print('leg extension')
      print('calve raises')
body_part = exc
body_part.workout()


class gym_status:
  def stats():
    print(" ")
    print("Lets check your gym status")
    x = float(input("Enter your bench press(in kgs): "))
    y = float(input("Enter your deadlift(in kgs): "))
    z = float(input("Enter your squats(in kgs): "))

    if x + y + z <=200:
      print("GYM BRO")
    elif x + y + z > 200 and x + y + z <= 300:
      print('GYM FREAK')
    elif x + y + z > 300 and x + y + z <=400:
      print("GYM RAT")
    elif x + y + z > 400:
      print("GYM GOD")
    else:
      print("WE WILL BE THERE SOON")
legacy = gym_status
legacy.stats()