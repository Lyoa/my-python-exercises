#month in lowercase #Your Astrological sign is : {zodiac sign}
day = int(input("Your birthdate: "))
month = input("Your month of birth: ")

if month == 'december':
    sign = 'Sagittarius' if (day < 22) else 'Capricorn'
elif month == 'january':
    sign = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == 'february':
    sign = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'march':
    sign = 'Pisces' if (day < 21) else 'Aries'
elif month == 'april':
    sign = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may':
    sign = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june':
    sign = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july':
    sign = 'Cancer' if (day < 23) else 'Leo'
elif month == 'august':
    sign = 'Leo' if (day < 23) else 'Virgo'
elif month == 'september':
    sign = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october':
    sign = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november':
    sign = 'Scorpio' if (day < 22) else 'Sagittarius'
print("Your Astrological sign is :", sign)

