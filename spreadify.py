import os
import csv

def get_scraped_files(base_dir):
    #Given a base directory, gets the files inside, recursively
    ad_files = []
    for curdir, dirs, files in os.walk(base_dir):
        for ad_file in files:
            ad_files.append(os.path.join(curdir,ad_file))
    return ad_files


if __name__ == "__main__":
    files = get_scraped_files("data/")
    outfile_path = "ads.csv"
    outfile = csv.writer(open(outfile_path, "wb"))
    outfile.writerow(["ID","BODY","CLASS"])
    ad_contents_set = set()
    for ad_file in files:
        with open(ad_file, 'r') as content_file:
            content = content_file.read()
            if content not in ad_contents_set:
                ad_contents_set.add(content)
                outfile.writerow([ad_file,content,""])
    print len(ad_contents_set)


