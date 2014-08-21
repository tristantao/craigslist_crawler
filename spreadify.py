import os


def get_scraped_files(base_dir):
    #Given a base directory, gets the files inside, recursively
    ad_files = []
    for curdir, dirs, files in os.walk(base_dir):
        for ad_file in files:
            ad_files.append(os.path.join(curdir,check_file))
    return ad_files


if __name__ == "__main__":



