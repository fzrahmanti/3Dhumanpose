from helper import *
from pathlib import Path

for folder in Path('C:/Users/Farah/PycharmProjects/coba/DataOri2/').iterdir():
    tmp = Path(folder).stem
    # print(folder, tmp)

    for subfolder in Path(folder).rglob('*.json'):
        meta_file = Path(subfolder).stem
        f = os.path.join(folder, meta_file)
        meta_path = f+".json"
        pcap_path = f+".pcap"
        with open(meta_path, 'r') as f:
            info = client.SensorInfo(f.read())

        source = pcap.Pcap(pcap_path, info)
        meta = source.metadata
        scans = client.Scans(source)
        if not os.path.exists("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/"):
            os.makedirs("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/")

        if not os.path.exists("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/"):
            os.makedirs("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/")

        if not os.path.exists("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/pose"+tmp):
            os.makedirs("C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/pose"+tmp)

        write_path = "C:/Users/Farah/PycharmProjects/coba/DataOri2/PCD/pose"+str(tmp)
        print("Writing PCD to: ",write_path)
        pcap_to_pcd(source=source,metadata=meta, pcd_base=write_path+"/obj")