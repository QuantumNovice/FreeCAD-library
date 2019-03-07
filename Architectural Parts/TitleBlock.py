'''
Author: n0vice.hasi
7/3/2019
This script draws A3 title block at origin.
The script is in its early stages.
Tested on freecad-0.71
In future versions it will be upgraded to a plugin with different title block styles.
'''
import Draft, FreeCAD


def line(x1, y1, x2, y2, z1=0, z2=0):
    p1 = FreeCAD.Vector(x1, y1, z1)
    p2 = FreeCAD.Vector(x2, y2, z2)
    Draft.makeWire([p1, p2])
    Draft.autogroup(line)

def write(text, x1, y1, fontsize=10, z1=0):
    text = Draft.makeText([text],point=FreeCAD.Vector(x1,y1,z1))
    text.ViewObject.FontSize = fontsize
    Draft.autogroup(text)

class TitleBlock():
    '''
    This class draws Title Bar for A3 Size in FreeCAD which can then be rescaled
    to paper of anysize.
    '''
    def __init__(self):
        self.scale = 'Scale 1:1'
        self.company = 'Novice Inc.'
        self.title = 'Quick Titlebar'
        self.designer = ('', '')
        self.drawer = ('', '')
        self.checker = ('', '')
        self.standard = ('', '')
        self.approver = ('', '')
        self.sheet = (1,1)
        
        
    def draw(self):
        global line,write
        x = 420
        y = 297

        # Sheet Outline
        Draft.makeRectangle(x,y,face=False)
        # Title Block Outline
        Draft.makeRectangle(x/2.21,y/4.57,face=False)
        # Scale Box
        Draft.makeRectangle(x/14.85,y/14.85,face=False)
        Draft.makeRectangle(x/14.85,y/29.7,face=False)

        Draft.makeRectangle(x/3.23,y/14.85,face=False)
        Draft.makeRectangle(x/3.23,y/4.57,face=False)

        # Right side
        ZAxis = FreeCAD.Vector(0, 0, 0)
        p3 = FreeCAD.Vector(130, 0, 0)
        place3 = FreeCAD.Placement(p3, FreeCAD.Rotation(ZAxis, 0))
        Draft.makeRectangle(x/7,y/14.85, placement=place3,face=False)

        # Right line block top
        line(130,55,190,55)

        # Right Side Lines
        for i in range(5):
            line(130,20+(7*i),190,20+(7*i))

        line(150, 20, 150, 65)
        line(175, 20, 175, 65)


        # The Texts
        write(self.company, 800/x, y/5.4)
        write(self.scale,1500/x, y/19, fontsize=5)
        write(self.title,x/13, y/20, fontsize=7)
        entries = ['Designed', 'Drawn', 'Checked','Standard', 'Approved']
        for t in entries:
            text = Draft.makeText([t],point=FreeCAD.Vector(131.685897827,49.2298698425-(7*entries.index(t)),0.0))
            text.ViewObject.FontSize = 4
            Draft.autogroup(text)

        entries = [self.designer[0], self.drawer[0], self.checker[0],self.standard[0], self.approver[0]]
        for t in entries:
            text = Draft.makeText([t],point=FreeCAD.Vector(131.685897827+20,49.2298698425-(7*entries.index(t)),0.0))
            text.ViewObject.FontSize = 4
            Draft.autogroup(text)

        entries = [self.designer[1], self.drawer[1], self.checker[1],self.standard[1], self.approver[1]]
        for t in entries:
            text = Draft.makeText([t],point=FreeCAD.Vector(131.685897827+20+25,49.2298698425-(7*entries.index(t)),0.0))
            text.ViewObject.FontSize = 4
            Draft.autogroup(text)

        text = Draft.makeText(["NAME"],point=FreeCAD.Vector(150.892425537,59.7346763611,0.0))
        text.ViewObject.FontSize = 4
        Draft.autogroup(text)

        text = Draft.makeText(["DATE"],point=FreeCAD.Vector(150.892425537+25,59.7346763611,0.0))
        text.ViewObject.FontSize = 4
        Draft.autogroup(text)

        text = Draft.makeText([" DRAWING NO."],point=FreeCAD.Vector(130.669570923,14.5836391449,0.0))
        text.ViewObject.FontSize = 5
        Draft.autogroup(text)

        text = Draft.makeText(["SHEET {} OF {}".format(self.sheet[0],self.sheet[1])],point=FreeCAD.Vector(142.359405518,2.78295469284,0.0))
        text.ViewObject.FontSize = 4
        Draft.autogroup(text)

    def symbol(self):

        '''
        Draw symbol for first angle projection
        This part is free cad prompt  code works only in empty workspace.
        '''
        pl=FreeCAD.Placement()
        pl.Rotation.Q=(0.0,-0.0,-0.0,1.0)
        pl.Base=FreeCAD.Vector(4.39883899689,5.07238292694,0.0)
        circle = Draft.makeCircle(radius=2.7077144493,placement=pl,face=False,support=None)
        Draft.autogroup(circle)
        points=[FreeCAD.Vector(4.39883899689,7.75253677368,0.0),FreeCAD.Vector(22.4085273743,7.75253677368,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(4.39883899689,2.36466836929,0.0),FreeCAD.Vector(22.7037696838,2.36466836929,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(22.4085273743,7.75253677368,0.0),FreeCAD.Vector(22.4085273743,2.36466836929,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(22.7037696838,2.36466836929,0.0),FreeCAD.Vector(22.7037696838,7.75253677368,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(15.8148155212,3.69459223747,0.0),FreeCAD.Vector(15.8148155212,6.45017337799,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(22.4085273743,7.75253677368,0.0),FreeCAD.Vector(15.8148155212,6.35175991058,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(15.8148155212,3.69459223747,0.0),FreeCAD.Vector(22.6053524017,2.36466836929,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        App.getDocument("Unnamed").recompute()
        App.getDocument("Unnamed1").removeObject("Line009")
        App.getDocument("Unnamed1").recompute()
        App.getDocument("Unnamed").recompute()
        App.getDocument("Unnamed1").removeObject("Line008")
        App.getDocument("Unnamed1").recompute()
        points=[FreeCAD.Vector(22.4085273743,7.75253677368,0.0),FreeCAD.Vector(22.7074614843,7.8160427312,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(22.7037696838,7.75253677368,0.0),FreeCAD.Vector(22.7074623108,7.81604290009,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        App.getDocument("Unnamed1").removeObject("Line010")
        App.getDocument("Unnamed1").recompute()
        points=[FreeCAD.Vector(1.69112443924,5.07238292694,0.0),FreeCAD.Vector(25.6687164307,5.07238292694,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(1.69112443924,5.07238292694,0.0),FreeCAD.Vector(0.816995620728,5.07238292694,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)
        points=[FreeCAD.Vector(4.31038618088,0.640553891659,0.0),FreeCAD.Vector(4.31038618088,9.66146183014,0.0)]
        line = Draft.makeWire(points,closed=False,face=False,support=None)
        Draft.autogroup(line)


def usage():
    '''
    This function shows typica usage of the code
    '''
    t = TitleBlock()
    t.scale = 'Scale 1:1'
    t.company = 'Novice Inc.'
    t.title = 'Quick Titlebar'
    t.designer = ('Designer','9/1/19')
    t.drawer = ('Drawer', '2/2/19')
    t.checker = ('Checker', '2/2/20')
    t.standard = ('ISO', '2018')
    t.approver = ('Approver', '8/12/21')
    t.sheet = (1,1)
    t.draw()


def my_title_block():
    t = TitleBlock()
    t.scale = 'Scale 1:1'
    t.company = 'Novice Inc.'
    t.title = 'Quick Titlebar'
    t.designer = ('H.S','9/1/19')
    t.drawer = ('Python', '2/2/19')
    t.checker = ('J.H', '2/2/20')
    t.standard = ('ISO', '2018')
    t.approver = ('A.A', '8/12/21')
    t.sheet = (1,10)
    t.draw()
    # this part is stable only when the command is executed in empty file
    #t.symbol()


my_title_block()
