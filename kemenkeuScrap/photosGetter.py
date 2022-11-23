#! python3
# downloadXkcd.py - Downloads Kemenkeu photos

import requests, os, bs4

baseUrl = "https://account.kemenkeu.go.id/manage/uploads/"  # starting url
os.makedirs("photos", exist_ok=True)  # store comics in ./xkcd
# 1999 03 11 201801 1 001
# year MM DD generation M/L order

print(range(1999, 1999))

print("Tahun kelahiran berapa?")
print("dari ....")
yearStart = int(input())
print("sampai ....")
yearEnd = int(input()) + 1
print("angkatan tahun berapa (Tahun penganngkatan PNS) ....")
print("contohnya 201801")
generationPNS = int(input())
print("gendernya?")
print("cowok :1 || cewek: 2 || campur:3")
genderInput = int(input())
if genderInput == 1:
    genderArray = [1]
elif genderInput == 2:
    genderArray = [2]
elif genderInput == 3:
    genderArray = [1, 2]


for year in range(yearStart, yearEnd):
    yearFormated = repr(year)
    for month in range(1, 13):
        monthFormatted = repr(month).rjust(2, "0")
        for day in range(1, 32):
            dayFormatted = repr(day).rjust(2, "0")
            for generation in [generationPNS]:  # nanti diubah jadi array biar ga cuma 1
                generationFormatted = repr(generation)
                for gender in genderArray:
                    seriesNumber = 1
                    genderFormatted = repr(gender)
                    while seriesNumber > 0:
                        nip = (
                            yearFormated
                            + monthFormatted
                            + dayFormatted
                            + generationFormatted
                            + genderFormatted
                            + repr(seriesNumber).rjust(3, "0")
                            + ".jpg"
                        )
                        photoUrl = baseUrl + nip
                        # Save the image to ./xkcd
                        photo = requests.get(photoUrl)
                        # status = res.raise_for_status()
                        if photo.status_code == 404:
                            print(nip, " tidak ada")
                            seriesNumber = 0
                            break
                        print("Downloading %s..." % nip)
                        seriesNumber += 1
                        imageFile = open(
                            os.path.join("photos", os.path.basename(nip)), "wb"
                        )
                        for chunk in photo.iter_content(100000):
                            imageFile.write(chunk)
                        imageFile.close()
