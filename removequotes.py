out_file_name = "masterfile_new.csv"
out_file_name_noquotes = "masterfile_noquotes.csv"

with open(out_file_name, "r") as inFile:
        with(open(out_file_name_noquotes, "w")) as outFile:

            for line in inFile:
                line = line.replace('"', '')
                outFile.write(line)
