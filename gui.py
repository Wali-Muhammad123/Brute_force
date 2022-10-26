from create_matrix import *
from bruteforce_new import brute_force
import tkinter as tk 
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import ttk
from itertools import permutations
class BruteFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.n=tk.IntVar()
        self.label_file_explorer=tk.Label(self,text="Brute Force",font=("Arial",20),bg="lightgrey",fg="black")
        self.label_file_explorer.pack()
        self.button_explore=tk.Button(self,text="Browse CSV File",command=self.browseFiles,font=("Arial",20),bg="lightgrey",fg="black")
        self.button_explore.pack()
        #create a text entry box
        self.text_entry_box=tk.Entry(self,textvariable=self.n,width=50)
        self.text_entry_box.pack()
        self.button_explore0=tk.Button(self,text="Brute Force",command=self.brute_force,font=("Arial",20),bg="lightgrey",fg="black")
        self.button_explore0.pack()
        self.button_explore1=tk.Button(self,text="Plot Graph",command=self.plot_graph,font=("Arial",20),bg="lightgrey",fg="black")
        self.button_explore1.pack()
        self.button_explore2=tk.Button(self,text="Exit",command=self.exit,font=("Arial",20),bg="lightgrey",fg="black")
        self.button_explore2.pack()
    def browseFiles(self):
        self.filename=tk.filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("csv files","*.csv"),("all files","*.*")))
        self.label_file_explorer.configure(text="File Opened: "+self.filename)
    def brute_force(self):
        self.graph=create_matrix(self.filename)
        self.a,self.b=brute_force(self.n.get(),self.graph)

        self.label=tk.Label(self,text=f"Best Route:{self.a} \n Best Weight: {self.b} ",font=("Arial",20),bg="lightgrey",fg="black")
        self.label.pack()
    def plot_graph(self):
        self.G=nx.Graph()
        ''' self.G.add_nodes_from([i for i in range(len(self.graph))])
        self.G.add_edges_from([(i,j) for i in range(len(self.graph)) for j in range(len(self.graph)) if self.graph[i][j]!=0])
        self.pos=nx.spring_layout(self.G)
        plt.figure(figsize=(9,9))
        nx.draw_networkx_nodes(self.G,self.pos,node_size=500,node_color="lightblue")
        nx.draw_networkx_edges(self.G,self.pos,edge_color="black")
        nx.draw_networkx_labels(self.G,self.pos,font_size=20,font_family="sans-serif")'''
        edges=[(self.b[i],self.b[i+1]) for i in range(len(self.b)-1)]
        perm=list(permutations([i for i in range(len(self.b)-1)],2))
        other_edges=[]
        for x in perm:
            if x not in edges:
                other_edges.append(x)
        for i in other_edges:
            self.G.add_edge(i[0],i[1],color='b')
        for i in edges:
            self.G.add_edge(i[0],i[1],color='r',weight=2)
  
        
        self.G.add_nodes_from(self.b)
        colors=nx.get_edge_attributes(self.G,'color').values()
        weights=nx.get_edge_attributes(self.G,'weight').values()
        pos=nx.circular_layout(self.G)
        nx.draw(self.G,pos,edge_color=colors,width=list(weights),with_labels=True)
        plt.show()
        plt.savefig("graph.png")
    def exit(self):
        self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brute Force")
        self.geometry("500x500")
        self.configure(bg="lightgrey")
        self.brute_frame=BruteFrame(self)
        self.brute_frame.pack()
        self.mainloop()


if __name__=='__main__':
    app=App()
    app.mainloop()