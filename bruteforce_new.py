import itertools
import tkinter as tk 
from tkinter import Label,Button,filedialog,Entry
from create_matrix import create_matrix
def brute_force(s,matrix):
    k=len(matrix)
    path=[i for i in range(k) if i!=s ]
    all_path=list(itertools.permutations(path))
    route_weight=[]
    for x in all_path:
        x=list(x)
        x.append(s)
        x.insert(0,s)
        weight=0
        for i in range(len(x)-1):
            weight+=matrix[x[i]][x[i+1]]
        route_weight.append(weight)
    min_weight=min(route_weight)
    min_index=route_weight.index(min_weight)
    best_route=list(all_path[min_index][:])
    best_route.append(s)
    best_route.insert(0,s)
    return min_weight,best_route




if __name__=='__main__':
    path=filedialog.askopenfilename()
    graph=create_matrix(path)
    window=tk.Tk()
    window.title("Brute Force")
    window.geometry("500x500")
    window.configure(bg="lightgrey")
    label_file_explorer=tk.Label(window,text="Brute Force",font=("Arial",20),bg="lightgrey",fg="black")
    a,b=brute_force(0,graph)
    label=Label(window,text=f"Best Route:{a} \n Best Weight: {b} ",font=("Arial",20),bg="lightgrey",fg="black")
    label.pack()

    window.mainloop()
