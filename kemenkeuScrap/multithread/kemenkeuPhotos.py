#! python3
#   - Downloads Kemenkeu photos
import xlsxwriter

import requests, os, bs4, threading, sys


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("201801.xlsx")
worksheet = workbook.add_worksheet()

baseUrl = "https://account.kemenkeu.go.id/manage/uploads/"  # starting url
numberInExcel = 2
os.makedirs("photos", exist_ok=True)  # store comics in ./xkcd
# 1999 03 11 201801 1 001
# year MM DD generation M/L order
errDatas = []


def downloadPhotosByNIP(
    yearStart, yearEnd, monthStart, monthEnd, generationPNS, gender
):

    os.makedirs(f"photos/{generationPNS}", exist_ok=True)
    nip = ""
    try:

        if genderInput == 1:
            genderArray = [1]
        elif genderInput == 2:
            genderArray = [2]
        elif genderInput == 3:
            genderArray = [1, 2]
        for year in range(yearStart, yearEnd):
            yearFormated = repr(year)
            for month in range(monthStart, monthEnd):
                monthFormatted = repr(month).rjust(2, "0")
                for day in range(1, 32):
                    dayFormatted = repr(day).rjust(2, "0")
                    for generation in [
                        generationPNS
                    ]:  # nanti diubah jadi array biar ga cuma 1
                        generationFormatted = repr(generation)
                        for gender in genderArray:
                            seriesNumber = 1
                            genderFormatted = repr(gender)
                            while seriesNumber > 0:
                                global numberInExcel
                                nip = (
                                    yearFormated
                                    + monthFormatted
                                    + dayFormatted
                                    + generationFormatted
                                    + genderFormatted
                                    + repr(seriesNumber).rjust(3, "0")
                                )
                                nameUrl = f"https://account.kemenkeu.go.id/Account/GetNamaPegawai?id={nip}&key=1300d368c9fa449ab69e2699b5bdfe80"
                                photoUrl = baseUrl + nip + ".jpg"
                                # Save the image to ./xkcd
                                identity = requests.get(nameUrl)
                                photo = requests.get(photoUrl)
                                # status = res.raise_for_status()
                                if photo.status_code == 404:
                                    print(nip, " tidak ada")
                                    seriesNumber = 0
                                    break
                                print("Downloading %s..." % nip)
                                identity = identity.json()
                                print(identity)
                                worksheet.write(f"A{numberInExcel}", identity["Nama"])
                                worksheet.write(f"B{numberInExcel}", identity["NIP18"])
                                imageFile = open(
                                    os.path.join(
                                        f"photos/{generation}",
                                        os.path.basename(nip) + ".jpg",
                                    ),
                                    "wb",
                                )
                                for chunk in photo.iter_content(100000):
                                    imageFile.write(chunk)

                                imageFile.close()
                                worksheet.insert_image(
                                    f"C{numberInExcel}",
                                    os.path.join(
                                        f"photos/{generation}",
                                        os.path.basename(nip) + ".jpg",
                                    ),
                                )
                                numberInExcel += 1
                                seriesNumber += 1
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print(f"Could not convert data {ValueError}.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")


print("Tahun kelahiran?")
print("dari ....")
yearStart = int(input())
print("sampai ....")
yearEnd = int(input()) + 1
print("(Tahun penganngkatan PNS) ....")
print("contohnya 201801")
generationPNS = int(input())
print("gender?")
print("cowok :1 || cewek: 2 || campur:3")
genderInput = int(input())


downloadThreads = []
for yy in range(yearStart, yearEnd):
    for mm in range(1, 13, 4):
        print("tahun " + repr(yy) + " bulan: " + repr(mm))
        downloadThread = threading.Thread(
            target=downloadPhotosByNIP,
            args=(yy, yy + 1, mm + 1, mm + 4, generationPNS, genderInput),
        )
        downloadThreads.append(downloadThread)
        downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")

workbook.close()
