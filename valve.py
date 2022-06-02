import math
from tkinter import *
from PIL import Image, ImageTk

Mainframe_root=Tk()
Mainframe_root.title("Valve Diamensions Calculator")
Mainframe_root.geometry("1050x550")

Mainlabel=Label(Mainframe_root, text="Please Enter Engine Specifications", font="Ariel 15 bold",fg="Blue")
Mainlabel.grid(row=0,column=0,columnspan=2, padx=20, pady=20)

image = Image.open("ValveDesign.gif")
# Resize the image using resize() method
resize_image = image.resize((210, 400))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=img)
label1.grid(row=1,rowspan=9,column=2,padx=50)


fram_label=Label(Mainframe_root, text="Cylinder Bore")
fram_label.grid(row=1,column=0,sticky=W,padx=20)
fram_labe2=Label(Mainframe_root, text="Cylinder Stroke")
fram_labe2.grid(row=2,column=0,sticky=W,padx=20)
fram_labe3=Label(Mainframe_root, text="Engine RPM")
fram_labe3.grid(row=3,column=0,sticky=W,padx=20)
fram_labe4=Label(Mainframe_root, text="Mean Velovity of Gas")
fram_labe4.grid(row=4,column=0,sticky=W,padx=20)
fram_labe5=Label(Mainframe_root, text="Maximum Gas Pressure")
fram_labe5.grid(row=5,column=0,sticky=W,padx=20)
fram_labe6=Label(Mainframe_root, text="Permissible Bending Stress")
fram_labe6.grid(row=6,column=0,sticky=W,padx=20)
fram_labe7=Label(Mainframe_root, text="Total Length of valve")
fram_labe7.grid(row=7,column=0,sticky=W,padx=20)
fram_labe8=Label(Mainframe_root, text="Material Type (For Steel=0.41, For Cast Iron=0.54 ")
fram_labe8.grid(row=8,column=0,sticky=W,padx=20)
fram_labe9=Label(Mainframe_root, text="Fillet Radious ")
fram_labe9.grid(row=9,column=0,sticky=W,padx=20)

Cb_var=DoubleVar()
Cs_var=DoubleVar()
Ermp_var=DoubleVar()
Mvgas_var=DoubleVar()
Mgp_var=DoubleVar()
Mpbs_var=DoubleVar()
Tlv_var=DoubleVar()
Mty_var=DoubleVar()
Fr_var=DoubleVar()

Cb_Entry=Entry(Mainframe_root,textvariable=Cb_var)
Cb_Entry.grid(row=1,column=1,pady=10)
Cs_Entry=Entry(Mainframe_root,textvariable=Cs_var)
Cs_Entry.grid(row=2,column=1,pady=10)
Ermp_Entry=Entry(Mainframe_root,textvariable=Ermp_var)
Ermp_Entry.grid(row=3,column=1,pady=10)
Mvgas_Entry=Entry(Mainframe_root,textvariable=Mvgas_var)
Mvgas_Entry.grid(row=4,column=1,pady=10)
Mgp_Entry=Entry(Mainframe_root,textvariable=Mgp_var)
Mgp_Entry.grid(row=5,column=1,pady=10)
Mpbs_Entry=Entry(Mainframe_root,textvariable=Mpbs_var)
Mpbs_Entry.grid(row=6,column=1,pady=10)
Tlv_Entry=Entry(Mainframe_root,textvariable=Tlv_var)
Tlv_Entry.grid(row=7,column=1,pady=10)
Mty_Entry=Entry(Mainframe_root,textvariable=Mty_var)
Mty_Entry.grid(row=8,column=1,pady=10)
Fr_Entry=Entry(Mainframe_root,textvariable=Fr_var)
Fr_Entry.grid(row=9,column=1,pady=10)




def funcal():
    Cb=Cb_var.get()
    Cs=Cs_var.get()
    Ermp=Ermp_var.get()
    Mvgas=Mvgas_var.get()
    Mgp=Mgp_var.get()
    Mpbs=Mpbs_var.get()
    Tlv=Tlv_var.get()
    Mty=Mty_var.get()
    Fr=Fr_var.get()

    #Area of cylinder
    Area_of_cyliner = (math.pi/4)*math.pow(Cb,2)
    #print(Area_of_cyliner)
    
    #Mean Velocity of piston
    Mean_velocity_of_piston = (2*Cs*Ermp)/(60*1000)
    #print(Mean_velocity_of_piston)
    
    #For Exhaust port diameter
    Exhaust_port_Diameter=math.sqrt((Area_of_cyliner*Mean_velocity_of_piston)*4/(math.pi*Mvgas))
    #print(Exhaust_port_Diameter)
    
    #Thickness of valve Desk
    Thickness_of_valve_desk= Mty * Exhaust_port_Diameter * math.sqrt(Mgp/Mpbs)
    #print(Thickness_of_valve_desk)

    #Valve Head Diameter
    Valve_Head_Diameter=Exhaust_port_Diameter+(2*Thickness_of_valve_desk*0.7071)
    #print(Valve_Head_Diameter)

    #Diameter of valve head opening area
    Diameter_valve_Head_op_Area=math.sqrt(math.pow(Exhaust_port_Diameter,2)+math.pow(Valve_Head_Diameter,2))
    #print(Diameter_valve_Head_op_Area)

    #Diameter of valve Steam
    Diameter_valve_steam=(Exhaust_port_Diameter/8)+4
    #print(Diameter_valve_steam)

    #Width of seating
    Width_of_seating= 0.5*(Valve_Head_Diameter-Exhaust_port_Diameter)
    #print(Width_of_seating)
    

    Label2=Label(Mainframe_root, text="3D Exhaust Valves Parameters",font="Ariel 15 bold", fg="Green")
    Label2.grid(row=1,column=3,columnspan=4,sticky=W)
    Label3=Label(Mainframe_root, text=f"[1] Valve Head Diameter(HD)={Valve_Head_Diameter}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=2,column=3,sticky=W)
    Label3=Label(Mainframe_root, text=f"[2] Disk Thickness(DT)={Thickness_of_valve_desk}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=3,column=3,sticky=W)
    Label3=Label(Mainframe_root, text=f"[3] Fillet Radious(FR)={Fr}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=4,column=3,sticky=W)
    Label3=Label(Mainframe_root, text=f"[4] Steam Diameter(SD)={Diameter_valve_steam}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=5,column=3,sticky=W)
    Label3=Label(Mainframe_root, text=f"[5] Valve Length(VL)={Tlv}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=6,column=3,sticky=W)
    Label3=Label(Mainframe_root, text=f"[6] Seating width(SW)={Width_of_seating}",font="Ariel 10 bold",fg="blue")
    Label3.grid(row=7,column=3,sticky=W)
    
    
    file=open("ValveParameters.txt","a")
    file.write(f"Diameter of valve Head: "+str(Valve_Head_Diameter))
    file.write(f"\nThickness of valve Disk: "+str(Thickness_of_valve_desk))
    file.write(f"\nFillet Radious: "+str(Fr))
    file.write(f"\nDiameter of valve Steam: "+str(Diameter_valve_steam))
    file.write(f"\nTotal Length of valve: "+str(Tlv))
    file.write(f"\nThickness of seating width: "+str(Width_of_seating))
    file.close()


def funcal2():
    Cb_Entry.delete(0, END)
    Cs_Entry.delete(0,END)
    Ermp_Entry.delete(0,END)
    Mvgas_Entry.delete(0,END)
    Mgp_Entry.delete(0,END)
    Mpbs_Entry.delete(0,END)
    Tlv_Entry.delete(0,END)
    Mty_Entry.delete(0,END)
    Fr_Entry.delete(0,END)


def funcal3():
    Mainframe_root.quit()


Evaluate_button=Button(Mainframe_root,text="Create",command=funcal)
Evaluate_button.grid(row=10,column=1,pady=20)
Evaluate_button=Button(Mainframe_root,text="Clear all",command=funcal2)
Evaluate_button.grid(row=10,column=2,padx=20)
Evaluate_button=Button(Mainframe_root,text="Close",command=funcal3)
Evaluate_button.grid(row=10,column=3,padx=20)


Mainframe_root.mainloop()
