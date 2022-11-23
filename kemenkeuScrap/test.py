# 1999 03 11 201801 1 001
# year MM DD generation M/L order


from ast import If


for year in range(1995, 2000):
    yearFormated = repr(year)
    for month in range(1, 12):
        monthFormatted = repr(month).rjust(2, "0")
        for day in range(1, 32):
            dayFormatted = repr(day).rjust(2, "0")
            for generation in [201801]:
                generationFormatted = repr(generation)
                for gender in range(1, 3):
                    seriesNumber = 1
                    genderFormatted = repr(gender)
                    while seriesNumber > 0:
                        print(
                            yearFormated
                            + monthFormatted
                            + dayFormatted
                            + generationFormatted
                            + genderFormatted
                            + repr(seriesNumber).rjust(4, "0")
                        )
                        if seriesNumber == 3:
                            break
                        seriesNumber += 1
