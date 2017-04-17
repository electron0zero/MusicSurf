from ConfigureMusicSurf import PreProcessing


def main():
    p = PreProcessing()
    p.downloadES()
    p.unzipES()
    # p.deletezipES()
    p.startES()

if __name__ == "__main__":
    main()
