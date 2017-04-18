from readID3 import getID3asJSON

root_path = r"C:\Users\Electron\Music\test_music"
obj = getID3asJSON(root_path)
print(obj.results)
