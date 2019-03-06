import sqlite3

# We create a local sqlite database table with a primary key on (almost) all columns.
# We then ignore any data integrity errors (key violation errors) since these would be
# duplicate records so what we end up with are only unique rows from the file in the table.
# Then the table can be simple selected from and the results printed back to a file.

def deleteDuplicates(fileName):
    conn = sqlite3.connect('single.db')
    cur = conn.cursor()

    cur.execute('drop table temp')
    conn.commit()

    cur.execute("""create table temp(
    num text, ID1 text, Year text, ID2 text, Latitude text, Longitude text,
    Elevation text, Tmax01 text, Tmax02 text, Tmax03 text, 
    Tmax04 text, Tmax05 text, Tmax06 text, Tmax07 text, Tmax08 text,
    Tmax09 text, Tmax10 text, Tmax11 text, Tmax12 text, Tmin01 text,
    Tmin02 text, Tmin03 text, Tmin04 text, Tmin05 text, Tmin06 text, 
    Tmin07 text, Tmin08 text, Tmin09 text, Tmin10 text, Tmin11 text,
    Tmin12 text, Tave01 text, Tave02 text, Tave03 text, Tave04 text,
    Tave05 text, Tave06 text, Tave07 text, Tave08 text, Tave09 text,
    Tave10 text, Tave11 text, Tave12 text, PPT01 text, PPT02 text, 
    PPT03 text, PPT04 text, PPT05 text, PPT06 text, PPT07 text, 
    PPT08 text, PPT09 text, PPT10 text, PPT11 text, PPT12 text,
    DD_0_01 text, DD_0_02 text, DD_0_03 text, DD_0_04 text, 
    DD_0_05 text, DD_0_06 text, DD_0_07 text, DD_0_08 text, 
    DD_0_09 text, DD_0_10 text, DD_0_11 text, DD_0_12 text, 
    DD5_01 text, DD5_02 text, DD5_03 text, DD5_04 text, DD5_05 text,
    DD5_06 text, DD5_07 text, DD5_08 text, DD5_09 text, DD5_10 text,
    DD5_11 text, DD5_12 text, DD_18_01 text, DD_18_02 text, 
    DD_18_03 text, DD_18_04 text, DD_18_05 text, DD_18_06 text,
    DD_18_07 text, DD_18_08 text, DD_18_09 text, DD_18_10 text,
    DD_18_11 text, DD_18_12 text, DD18_01 text, DD18_02 text,
    DD18_03 text, DD18_04 text, DD18_05 text, DD18_06 text,
    DD18_07 text, DD18_08 text, DD18_09 text, DD18_10 text,
    DD18_11 text, DD18_12 text, NFFD01 text, NFFD02 text,
    NFFD03 text, NFFD04 text, NFFD05 text, NFFD06 text, NFFD07 text,
    NFFD08 text, NFFD09 text, NFFD10 text, NFFD11 text, NFFD12 text,
    PAS01 text, PAS02 text, PAS03 text, PAS04 text, PAS05 text,
    PAS06 text, PAS07 text, PAS08 text, PAS09 text, PAS10 text,
    PAS11 text, PAS12 text, Eref01 text, Eref02 text, Eref03 text,
    Eref04 text, Eref05 text, Eref06 text, Eref07 text, Eref08 text,
    Eref09 text, Eref10 text, Eref11 text, Eref12 text, CMD01 text,
    CMD02 text, CMD03 text, CMD04 text, CMD05 text, CMD06 text, 
    CMD07 text, CMD08 text, CMD09 text, CMD10 text, CMD11 text, 
    CMD12 text, RH01 text, RH02 text, RH03 text, RH04 text, 
    RH05 text, RH06 text, RH07 text, RH08 text, RH09 text, RH10 text, 
    RH11 text, RH12 text, NA_L1NAME text,

    primary key(ID1,Year,ID2,Latitude,Longitude,Elevation,Tmax01,
    Tmax02, Tmax03, Tmax04, Tmax05, Tmax06, Tmax07, Tmax08, Tmax09,
    Tmax10, Tmax11, Tmax12, Tmin01, Tmin02, Tmin03, Tmin04, Tmin05,
    Tmin06, Tmin07, Tmin08, Tmin09, Tmin10, Tmin11, Tmin12, Tave01,
    Tave02, Tave03, Tave04, Tave05, Tave06, Tave07, Tave08, Tave09,
    Tave10, Tave11, Tave12, PPT01, PPT02, PPT03, PPT04, PPT05,
    PPT06, PPT07, PPT08, PPT09, PPT10, PPT11, PPT12, DD_0_01, 
    DD_0_02, DD_0_03, DD_0_04, DD_0_05, DD_0_06, DD_0_07, DD_0_08,
    DD_0_09, DD_0_10, DD_0_11, DD_0_12, DD5_01, DD5_02, DD5_03, 
    DD5_04, DD5_05, DD5_06, DD5_07, DD5_08, DD5_09, DD5_10, DD5_11,
    DD5_12, DD_18_01, DD_18_02, DD_18_03, DD_18_04, DD_18_05, 
    DD_18_06, DD_18_07, DD_18_08, DD_18_09, DD_18_10, DD_18_11,
    DD_18_12, DD18_01, DD18_02, DD18_03, DD18_04, DD18_05,
    DD18_06, DD18_07, DD18_08, DD18_09, DD18_10, DD18_11, DD18_12,
    NFFD01, NFFD02, NFFD03, NFFD04, NFFD05, NFFD06, NFFD07, NFFD08,
    NFFD09, NFFD10, NFFD11, NFFD12, PAS01, PAS02, PAS03, PAS04, 
    PAS05, PAS06, PAS07, PAS08, PAS09, PAS10, PAS11, PAS12,
    Eref01, Eref02, Eref03, Eref04, Eref05, Eref06, Eref07,Eref08,
    Eref09, Eref10, Eref11, Eref12, CMD01, CMD02, CMD03, CMD04, 
    CMD05, CMD06, CMD07, CMD08, CMD09, CMD10, CMD11, CMD12, RH01,
    RH02, RH03, RH04, RH05, RH06, RH07, RH08, RH09, RH10, RH11, 
    RH12,NA_L1NAME))
    """)

    conn.commit()
    print("Done creating table")
    with open(fileName) as readFile:
        lineNumber = 0
        for line in readFile:
            lineNumber += 1
            currentLine = line.split(",")            
            if (len(currentLine) != 164):
                print("Skipping line number " + str(lineNumber) + ". Number of values does not equal 164.")
                continue

            try:                
                cur.execute("insert into temp values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                , (currentLine[0] , currentLine[1] , currentLine[2]
                , currentLine[3] , currentLine[4]
                , currentLine[5] , currentLine[6]
                , currentLine[7] , currentLine[8]
                , currentLine[9] , currentLine[10]
                , currentLine[11] , currentLine[12]
                , currentLine[13] , currentLine[14]
                , currentLine[15] , currentLine[16]
                , currentLine[17] , currentLine[18]
                , currentLine[19] , currentLine[20]
                , currentLine[21] , currentLine[22]
                , currentLine[23] , currentLine[24]
                , currentLine[25] , currentLine[26]
                , currentLine[27] , currentLine[28]
                , currentLine[29] , currentLine[30]
                , currentLine[31] , currentLine[32]
                , currentLine[33] , currentLine[34]
                , currentLine[35] , currentLine[36]
                , currentLine[37] , currentLine[38]
                , currentLine[39] , currentLine[40]
                , currentLine[41] , currentLine[42]
                , currentLine[43] , currentLine[44]
                , currentLine[45] , currentLine[46]
                , currentLine[47] , currentLine[48]
                , currentLine[49] , currentLine[50]
                , currentLine[51] , currentLine[52]
                , currentLine[53] , currentLine[54]
                , currentLine[55] , currentLine[56]
                , currentLine[57] , currentLine[58]
                , currentLine[59] , currentLine[60]
                , currentLine[61] , currentLine[62]
                , currentLine[63] , currentLine[64]
                , currentLine[65] , currentLine[66]
                , currentLine[67] , currentLine[68]
                , currentLine[69] , currentLine[70]
                , currentLine[71] , currentLine[72]
                , currentLine[73] , currentLine[74]
                , currentLine[75] , currentLine[76]
                , currentLine[77] , currentLine[78]
                , currentLine[79] , currentLine[80]
                , currentLine[81] , currentLine[82]
                , currentLine[83] , currentLine[84]
                , currentLine[85] , currentLine[86]
                , currentLine[87] , currentLine[88]
                , currentLine[89] , currentLine[90]
                , currentLine[91] , currentLine[92]
                , currentLine[93] , currentLine[94]
                , currentLine[95] , currentLine[96]
                , currentLine[97] , currentLine[98]
                , currentLine[99] , currentLine[100]
                , currentLine[101] , currentLine[102]
                , currentLine[103] , currentLine[104]
                , currentLine[105] , currentLine[106]
                , currentLine[107] , currentLine[108]
                , currentLine[109] , currentLine[110]
                , currentLine[111] , currentLine[112]
                , currentLine[113] , currentLine[114]
                , currentLine[115] , currentLine[116]
                , currentLine[117] , currentLine[118]
                , currentLine[119] , currentLine[120]
                , currentLine[121] , currentLine[122]
                , currentLine[123] , currentLine[124]
                , currentLine[125] , currentLine[126]
                , currentLine[127] , currentLine[128]
                , currentLine[129] , currentLine[130]
                , currentLine[131] , currentLine[132]
                , currentLine[133] , currentLine[134]
                , currentLine[135] , currentLine[136]
                , currentLine[137] , currentLine[138]
                , currentLine[139] , currentLine[140]
                , currentLine[141] , currentLine[142]
                , currentLine[143] , currentLine[144]
                , currentLine[145] , currentLine[146]
                , currentLine[147] , currentLine[148]
                , currentLine[149] , currentLine[150]
                , currentLine[151] , currentLine[152]
                , currentLine[153] , currentLine[154]
                , currentLine[155] , currentLine[156]
                , currentLine[157] , currentLine[158]
                , currentLine[159] , currentLine[160]
                , currentLine[161] , currentLine[162]
                , currentLine[163]))

                conn.commit()
            except sqlite3.IntegrityError:
                pass
    conn.commit()
    print("Done inserting into table")

    cur.execute('select * from temp')

    out_file_name = "masterfile_new.csv"
    with open(out_file_name, "w") as writeFile:
        for row in cur:            
            writeFile.write(str(row[0]) + ", " + row[1] + ", " + row[2] + ", " + row[3] + ", " + row[4] + ", " + row[5] + ", " + row[6] + 
                            ", " + row[7] + ", " + row[8] + ", " + row[9] + ", " + row[10] + ", " + row[11] + ", " + row[12] + ", " + row[13] + 
                            ", " + row[14] + ", " + row[15] + ", " + row[16] + ", " + row[17] + ", " + row[18] + ", " + row[19] + ", " + row[20] + 
                            ", " + row[21] + ", " + row[22] + ", " + row[23] + ", " + row[24] + ", " + row[25] + ", " + row[26] + ", " + row[27] + 
                            ", " + row[28] + ", " + row[29] + ", " + row[30] + ", " + row[31] + ", " + row[32] + ", " + row[33] + ", " + row[34] + 
                            ", " + row[35] + ", " + row[36] + ", " + row[37] + ", " + row[38] + ", " + row[39] + ", " + row[40] + ", " + row[41] + 
                            ", " + row[42] + ", " + row[43] + ", " + row[44] + ", " + row[45] + ", " + row[46] + ", " + row[47] + ", " + row[48] + 
                            ", " + row[49] + ", " + row[50] + ", " + row[51] + ", " + row[52] + ", " + row[53] + ", " + row[54] + ", " + row[55] + 
                            ", " + row[56] + ", " + row[57] + ", " + row[58] + ", " + row[59] + ", " + row[60] + ", " + row[61] + ", " + row[62] + 
                            ", " + row[63] + ", " + row[64] + ", " + row[65] + ", " + row[66] + ", " + row[67] + ", " + row[68] + ", " + row[69] + 
                            ", " + row[70] + ", " + row[71] + ", " + row[72] + ", " + row[73] + ", " + row[74] + ", " + row[75] + ", " + row[76] + 
                            ", " + row[77] + ", " + row[78] + ", " + row[79] + ", " + row[80] + ", " + row[81] + ", " + row[82] + ", " + row[82] + 
                            ", " + row[83] + ", " + row[84] + ", " + row[85] + ", " + row[86] + ", " + row[87] + ", " + row[88] + ", " + row[89] + 
                            ", " + row[90] + ", " + row[91] + ", " + row[92] + ", " + row[93] + ", " + row[94] + ", " + row[95] + ", " + row[96] + 
                            ", " + row[97] + ", " + row[98] + ", " + row[99] + ", " + row[100] + ", " + row[101] + ", " + row[102] + ", " + row[103] + 
                            ", " + row[104] + ", " + row[105] + ", " + row[106] + ", " + row[107] + ", " + row[108] + ", " + row[109] + ", " + row[110] + 
                            ", " + row[111] + ", " + row[112] + ", " + row[113] + ", " + row[114] + ", " + row[115] + ", " + row[116] + ", " + row[117] + 
                            ", " + row[118] + ", " + row[119] + ", " + row[120] + ", " + row[121] + ", " + row[122] + ", " + row[123] + ", " + row[124] + 
                            ", " + row[125] + ", " + row[126] + ", " + row[127] + ", " + row[128] + ", " + row[129] + ", " + row[130] + ", " + row[131] + 
                            ", " + row[132] + ", " + row[133] + ", " + row[134] + ", " + row[135] + ", " + row[136] + ", " + row[137] + ", " + row[138] + 
                            ", " + row[139] + ", " + row[140] + ", " + row[141] + ", " + row[142] + ", " + row[143] + ", " + row[144] + ", " + row[145] + 
                            ", " + row[146] + ", " + row[147] + ", " + row[148] + ", " + row[149] + ", " + row[150] + ", " + row[151] + ", " + row[152] + 
                            ", " + row[153] + ", " + row[154] + ", " + row[155] + ", " + row[156] + ", " + row[157] + ", " + row[158] + ", " + row[159] + 
                            ", " + row[160] + ", " + row[161] + ", " + row[162] + ", " + row[163])

    print("Done writing to file")

file = "C:/Users/Austin/Documents/R/8. Treeclim/masterfile.csv"
deleteDuplicates(file)

