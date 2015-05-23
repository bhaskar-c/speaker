#Speaking with Markov chain - Tkinter Interface


from tkinter import *
from markov import *
from sys import exit as çık
from time import strftime
from glob import glob

BİLGİ=["Bilgi",("Markov Speaker\n"+
                    "Markov chains using some basic text "+
                    "a software that can talk. The various texts "+
                            "exploitalble")]
ASİ=["Akıllı Sözcük İşleme",("This simple feature, the software right words\n"+
                             "format allows the interpretation.\n"+
                             "Stepless remove, correct pronouns\n"+
                             "There are such functions. Moreover, the software's\n"+
                             "It made almost no difference in the rate can not answer.\n"+
                             "\nThe only reason it's closing is an advanced \n"+
                             "The user can extract the software you want.\n")]
GGS=["Gelişigüzel Seçim","""The answer will be given in a word how this feature
It determines whether selected. If it is closed, which may be first
The answer; answers that could all be turned on
collected is given a randomly selected responses.

This feature, although the software more fun
Also, hell rate is about 25 times lower.
However, words alone software than 1 second
It is waiting less."""]

KO=["Konuya odaklanma","""
When this is turned on, the computer respond to you, if you want to continue without writing anything passing mention of the computer ("Enter" button) You can keep the promise of the computer."""]
class Uyg(Frame):
    def __init__(self,yazı,zS,abi=None):
        Frame.__init__(self,abi)
        self.grid()
        self.hazırla()
        self.arkadaşAdı="Bilgisayar"
        self.son=0
        self.geçmişGirdiler=[]
        self.geçmişGirdiU=10
        self.sonYanıt=""
        self.Markov=markov(zS)
        self.Markov.oku(yazı)
    def hazırla(self):
        self.master.title("Markov Speaker")

        self.seçke=Menu(self)
        ayarlarS=Menu(self.seçke,tearoff=0)
        ayarlarS.add_command(label="Copy the entire speech",
                             command=self.kopyala)
        ayarlarS.add_command(label="Clear conversation history",
                             command=self.temizle)
        ayarlarS.add_separator()
        self.asi=IntVar()
        self.asi.set(1)
        ayarlarS.add_checkbutton(label="Smart word processing",variable=self.asi, \
                                 onvalue=1,offvalue=0)
        self.ggs=IntVar()
        self.ggs.set(1)
        ayarlarS.add_checkbutton(label="random selection",variable=self.ggs, \
                                 onvalue=1,offvalue=0)
        self.ko=IntVar()
        self.ko.set(1)
        ayarlarS.add_checkbutton(label="Focus Subject",variable=self.ko, \
                                 onvalue=1,offvalue=0)
        ayarlarS.add_separator()
        ayarlarS.add_command(label="Document / Chain selection",
                             command=self.ayarla)
        ayarlarS.add_command(label="Exit",command=self.master.destroy)
        self.seçke.add_cascade(label="Settings",menu=ayarlarS)
        yardımS=Menu(self.seçke,tearoff=0)
        yardımS.add_command(label="Intelligent Word Processing",command=lambda: self.bilgi(ASİ))
        yardımS.add_command(label="random selection",command=lambda: self.bilgi(GGS))
        yardımS.add_command(label="Focus Subject",command=lambda: self.bilgi(KO))
        yardımS.add_separator()
        yardımS.add_command(label="Information",command=lambda: self.bilgi(BİLGİ))
        self.seçke.add_cascade(label="Help",menu=yardımS)

        self.master.config(menu=self.seçke)
        
        self.yazı=Text(self.master,width=90,height=30)
        self.yazı.tag_config("kızıl",foreground="red")
        self.yazı.tag_config("yeşil",foreground="green")
        self.yazı.tag_config("mavi",foreground="blue")
        self.yazı.insert(INSERT,strftime("Konuşma başladı. Saat %H:%M, tarih %d.%m.%y \n")+"Kullanılan belge: "+belgeAdı+"\nZincir başına sözcük sayısı: "+str(ZincirS)+"\n\n","kızıl")
        self.yazı.config(state=DISABLED)
        
        self.yazı.grid(row=0,column=0,columnspan=4,sticky="EW")

        self.durumYazı=StringVar()
        Label(self.master,textvariable=self.durumYazı,bg="blue",fg="white",
              anchor="w").grid(column=0,row=1,columnspan=4,sticky="EW")
        self.durumYazı.set("Konuşmaya başlamak için iletinizi aşağıya yazınız. Konuşmaya bilgisayarın başlamasını isterseniz hiçbir şey yazmadan iletebilirsiniz.")
        
        self.girdi=Entry(self.master,width=90)
        self.girdi.grid(row=2,column=0,columnspan=3)
        self.girdi.bind("<Return>",self.gireBas)
        self.girdi.bind("<Up>",self.yukarı)
        self.girdi.bind("<Down>",self.aşağı)

        Button(self.master,text="transmission",command=self.iletim,relief=GROOVE,width=30).grid(row=2,column=3)
        Button(self.master,text="You answered my place computer",command=self.bilgisayarYanıtlasın,bg="green",fg="white",relief=GROOVE).grid(row=3,column=0)
        Button(self.master,text="Exit",command=self.master.destroy,bg="red",fg="white",relief=GROOVE).grid(row=3,column=3)
        self.grid_columnconfigure(0,weight=1)
        self.master.resizable(False,False)

        self.master.focus_force()
        self.girdi.focus_set()
        self.girdi.selection_range(0,END)
    def yukarı(self,e):
        ş=self.girdi.get()
        s=""
        try:
            s=self.geçmişGirdiler[self.geçmişGirdiler.index(ş)-1]
        except ValueError:
            try:
                s=self.geçmişGirdiler[-1]
                self.geçmişGirdiler.append(ş)
                if len(self.geçmişGirdiler)>self.geçmişGirdiU:
                    self.geçmişGirdiler=self.geçmişGirdiler[1:]
            except IndexError:
                return
        except IndexError:
            return #bu boş return komutları işlevden çıkarır
        self.girdi.delete(0,END)
        self.girdi.insert(END,s)
    def aşağı(self,e):
        ş=self.girdi.get()
        s=""
        try:
            s=self.geçmişGirdiler[self.geçmişGirdiler.index(ş)+1]
        except ValueError:
            return
        except IndexError:
            return
        self.girdi.delete(0,END)
        self.girdi.insert(END,s)
    def gireBas(self,e):
        self.iletim()
    def bilgisayarYanıtlasın(self):
        self.girdi.delete(0,END)
        self.girdi.insert(END,self.Markov.yanıtla(self.sonYanıt))
    def iletim(self):
        ileti=self.girdi.get()
        self.geçmişGirdiler.append(ileti)
        if len(self.geçmişGirdiler)>self.geçmişGirdiU:
            self.geçmişGirdiler=self.geçmişGirdiler[1:]
        self.Markov.akıllıSözcükİşleme=self.asi.get()
        self.Markov.gelişigüzelSeçim=self.ggs.get()
        self.Markov.odaklanma=self.ko.get()
        self.durumYazı.set(self.arkadaşAdı+" yazıyor...")
        if ileti:
            self.yazıEkleTakı("Sen: ","yeşil")
            self.yazıEkle(ileti+"\n")
        self.girdi.delete(0,END)
        self.master.update()
        yanıt=self.Markov.yanıtla(ileti)
        self.yazıEkleTakı(self.arkadaşAdı+": ","mavi")
        self.sonYanıt=yanıt
        self.yazıEkle(yanıt+"\n")
        self.durumYazı.set(strftime("Son alınan ileti saat %H:%M 'de, tarih %d.%m.%y"))
        self.girdi.focus_set()
    def yazıEkle(self,girdi):
        self.yazı.config(state=NORMAL)
        self.yazı.insert(END,girdi)
        self.yazı.see(END)
        self.yazı.config(state=DISABLED)
    def yazıEkleTakı(self,girdi,t):
        self.yazı.config(state=NORMAL)
        self.yazı.insert(END,girdi,t)
        self.yazı.see(END)
        self.yazı.config(state=DISABLED)
    def bilgi(self,b):
        messagebox.showinfo(b[0],b[1])
    def kopyala(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.yazı.get(1.0,END)+"\nMarkov Konuşucusu - İlker IŞIK - 2014")
    def temizle(self):
        self.yazı.config(state=NORMAL)
        self.yazı.delete(1.0,END)
        self.yazı.insert(END,strftime("Conversation history is cleared ... Time %H:%M, Date %d.%m.%y \n")+"The document used: "+belgeAdı+"\nThe number of words per chain: "+str(ZincirS)+"\n\n","kızıl")
        self.yazı.config(state=DISABLED)
    def ayarla(self):
        self.master.destroy()
        başlangıç(False,Tk())
        
class başlangıç(Frame):
    def __init__(self,ilk=True,abi=None):
        Frame.__init__(self,abi)
        self.belgeler=[x[2:] for x in glob("./*.txt")]
        ilkBelge=""
        ilkZS=0
        if ".\\konuşucu.ayarlar" in glob("./*.ayarlar"):
            with open("konuşucu.ayarlar") as ayrB:
                ayar=ayrB.read().split("\n")
            ilkBelge=ayar[0]
            ilkZS=int(ayar[1])
            if ilk and ilkBelge in self.belgeler:
                self.master.destroy()
                UygBaşlat(ilkBelge,ilkZS)
                return
                
        
        self.grid()
        self.master.title("Speakers Settings")
        Label(self.master,text="Select the certificate to be used:").grid(row=0,column=0)
        self.çs=Listbox(self.master,selectmode=SINGLE,width=30)
        if not self.belgeler:
            self.bilgi(["Issue","No .txt document at the location where the software is located. \ n an extension .txt document to the operation of the software is required. \ n The software will be closed."])
            self.master.destroy()
        for s,b in enumerate(self.belgeler):
            self.çs.insert(s,b)
            if b==ilkBelge:
                self.çs.selection_set(s)
        if not self.çs.curselection():
            self.çs.selection_set(0)
        self.çs.grid(row=1,column=0,columnspan=2)
        Label(self.master,text="The number of words per chain:").grid(column=0,row=2)
        self.zS=DoubleVar()
        self.zS.set(ilkZS if ilkZS else 2)
        Scale(self.master,variable=self.zS,orient=HORIZONTAL,from_=1,to=5).grid(row=3,column=0)
        Button(self.master,relief=GROOVE,text="What is this?",command=lambda: self.bilgi(["The number of words per chain, "" This value defines how many words you'll find in a chain. \ NA low value while increasing casualness \ n High values reduce promiscuity."])).grid(row=3,column=1)
        Button(self.master,relief=GROOVE,text="Start",command=self.başlat).grid(row=4,column=0,columnspan=2)

        self.master.focus_force()
        self.çs.focus_set()
    def bilgi(self,b):
        messagebox.showinfo(b[0],b[1])
    def başlat(self):
        ad=(self.belgeler[self.çs.curselection()[0]])
        sy=int(self.zS.get())
        self.master.destroy()
        with open("Speaker Settings","w") as belge:
            belge.write(ad+"\n"+str(sy))
            
        UygBaşlat(ad,sy)
        
def UygBaşlat(bA,zS):
    global belgeAdı,ZincirS
    belgeAdı,ZincirS=bA,zS
    with open(bA) as belge:
        yazı=belge.read()
    yazı=yazı.replace("\n"," ")
    uyg=Uyg(yazı,zS,Tk())
    uyg.mainloop()
if __name__=="__main__":
    """with open(belgeAdı) as b:
        yazı=b.read()
    yazı=yazı.replace("\n"," ")
    u=Uyg()
    u.Markov=markov()
    u.Markov.oku(yazı)
    u.mainloop()"""
    başlangıç(True,Tk())

