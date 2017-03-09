# imports
from PrepareEnv.ConfigureMusicSurf import PreProcessing

def main():
    p=PreProcessing()
    p.downloadES()
    p.unzipES()
    p.startES()

if __name__=="__main__":
    main()
        
