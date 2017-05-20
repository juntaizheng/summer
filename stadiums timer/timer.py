from Tkinter import *
import time

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 5.0
        self._running = 0
        self._counter = 0
        self._break = 0
        self.counterstr = StringVar()
        self.timestr = StringVar()               
        self.makeWidgets()      

    def makeWidgets(self):                         
        """ Make the time, counter, and break label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)
        c = Label(self, textvariable=self.counterstr)
        self.counterstr.set("Count: " + str(self._counter))
        c.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def _update(self):
        self._elapsedtime = time.time() - self._start
        if (10 - self._counter - self._elapsedtime < 0 and self._break == 0):
            self._counter += 1
            self.counterstr.set("Count: " + str(self._counter))
            self._elapsedtime = 5.0
            self._start = time.time() - self._elapsedtime
            self._break = 1
            print 'on break'
        if (10 - self._elapsedtime < 0 and self._break == 1):
            self._elapsedtime = 5.0
            self._start = time.time() - self._elapsedtime
            self._break = 0
            print "off break"
        if (self._counter == 5):
            self.Stop()
            return
        if self._break == 0 :
            self._setTime(10 - self._counter - self._elapsedtime)
        else:
            self._setTime(10 - self._elapsedtime)
        self._timer = self.after(5, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(5)
            self._running = 0
            self._counter = 0
            self._break = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 5.0    
        self._setTime(self._elapsedtime)
        self.counter = 0
        self.counterstr.set("Count: " + str(self._counter))
        
        
def main():
    root = Tk()
    sw = StopWatch(root)
    sw.pack(side=TOP)
    
    Button(root, text='Start', command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
    Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
    Button(root, text='Quit', command=root.quit).pack(side=LEFT)
    
    root.mainloop()

if __name__ == '__main__':
    main()