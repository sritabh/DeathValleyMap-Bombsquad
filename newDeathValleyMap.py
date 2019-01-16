from bsMap import *
import bsPowerup
import bsUtils
import bs



class DeathValley(Map):
    import deathValleyDefs as defs
    name = "DeathValley2.0"

    playTypes = ['teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'alwaysLandBGColor'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel("footballStadium")
        data['vrFillModel'] = bs.getModel('footballStadiumVRFill')
        data['collideModel'] = bs.getCollideModel("footballStadiumCollide")
        data['tex'] = bs.getTexture("bg")
        return data
    
    def __init__(self):
        Map.__init__(self)
        
        platform = bs.newNode('prop', delegate=self, attrs={'position':(-8.00,0.9515026107,-2.0),'velocity':(0,0,0),'sticky':False,'body':'crate','model':bs.getModel('tnt'),'density':0.00000,'colorTexture':bs.getTexture('menuBG'),'bodyScale':6.0,'reflection': 'powerup','damping':9999999999999,'reflectionScale': [0],'modelScale':6.0,'shadowSize':0.0,'materials':[bs.getSharedObject('footingMaterial')]})
        platform = bs.newNode('prop', delegate=self, attrs={'position':(-8.00,0.9515026107,2.0),'velocity':(0,0,0),'sticky':False,'body':'crate','model':bs.getModel('tnt'),'density':0.00000,'colorTexture':bs.getTexture('menuBG'),'bodyScale':6.0,'reflection': 'powerup','damping':9999999999999,'reflectionScale': [0],'modelScale':6.0,'shadowSize':0.0,'materials':[bs.getSharedObject('footingMaterial')]})
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'model':self.preloadData['model'],
                                      'collideModel':self.preloadData['collideModel'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'background':True,
                          'colorTexture':self.preloadData['tex']})
        def credittext():
                #bySoby
                text = bs.newNode('text',
                       attrs={ 'text':'Mod By SobyDamn',
                              'scale':1.0,
                              'maxWidth':0,
                              'position':(0,0),
                              'shadow':1.0,
                              'flatness':0.50,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(text,'opacity',{0: 0.0,500: 1.0,10500: 1.0,11000: 0.0})
                bs.gameTimer(11500,text.delete)
        bs.gameTimer(2000,bs.Call(credittext))
        def path():
                p = bs.newNode('prop', attrs={'position':(-5.750,4.3515026107,-2.0),'velocity':(2.0,1.0,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':1.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':1.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(3000,p.delete)
                p = bs.newNode('prop', attrs={'position':(-5.750,4.3515026107,2.0),'velocity':(2.0,1.0,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':1.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':1.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(3000,p.delete)
        bs.gameTimer(600,bs.Call(path),repeat = True)
        def platform():
                p = bs.newNode('prop', attrs={'position':(0,2,-2),'velocity':(0,0,1),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':5.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':5.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(7000,p.delete)
                p = bs.newNode('prop', attrs={'position':(0,1,2),'velocity':(2.0,0.1,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('eggTex2'),'bodyScale':4.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [0.0],'modelScale':4.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(4000,p.delete)
                p = bs.newNode('prop', attrs={'position':(0,1,-1.5),'velocity':(2.0,0.1,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('eggTex2'),'bodyScale':4.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [0.0],'modelScale':4.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(4000,p.delete)
        bs.gameTimer(200,bs.Call(platform))
        bs.gameTimer(5000,bs.Call(platform),repeat = True)
        def path():
                p = bs.newNode('prop', attrs={'position':(6,2.0,2),'velocity':(2.0,0.8,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':1.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':1.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(4000,p.delete)
                p = bs.newNode('prop', attrs={'position':(6,2.0,-2),'velocity':(2.0,0.8,0),'sticky':False,'body':'landMine','model':bs.getModel('landMine'),'colorTexture':bs.getTexture('achievementWall'),'bodyScale':1.0,'reflection': 'powerup','density':9999999999999999,'reflectionScale': [1.0],'modelScale':1.0,'gravityScale':0,'shadowSize':0.0,'materials':[bs.getSharedObject('objectMaterial'),bs.getSharedObject('footingMaterial')]})
                bs.gameTimer(4000,p.delete)
        bs.gameTimer(600,bs.Call(path),repeat = True)
        g = bs.getSharedObject('globals')
        g.tint = (1.3,1.2,1.0)
        g.ambientColor = (1.3,1.2,1.0)
        g.vignetteOuter = (0.57,0.57,0.57)
        g.vignetteInner = (0.9,0.9,0.9)
        g.vrCameraOffset = (0,-0.8,-1.1)
        g.vrNearClip = 0.5

registerMap(DeathValley)