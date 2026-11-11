# zodiac sign generator with list values
zodiac = {
    1: ['Aries', 'Mars', 9, 'Fire', 'Ragebaiting king who will start a chaotic argument just to watch the fireworks, but will immediately fight the entire world to protect you.', 'Give them space to burn off steam when they get fired up, and remember they do not hold grudges.'],
    2: ['Taurus', 'Venus', 6, 'Earth', 'Stubborn roadblock who will violently resist leaving the couch, but will quietly build the safest, most loyal haven for you when your life gets chaotic.', 'Never rush their decision-making process, and prioritize quality, peaceful quality time together.'],
    3: ['Gemini', 'Mercury', 5, 'Air', 'Ghosting instigator who will leave your emotional text on read for three days, but will stay up until 3:00 AM remembering every tiny detail to help you through a crisis.', 'Keep the communication playful and intellectually stimulating to keep them from getting bored.'],
    4: ['Cancer', 'Moon', 2, 'Water', 'Passive-aggressive vault who expects you to magically read their mind when they are upset, but instinctively knows exactly when you need comfort and emotional protection.', 'Create a secure emotional environment where they feel completely safe opening up without fear of judgment.'],
    5: ['Leo', 'Sun', 1, 'Fire', 'Exhausting drama magnet who constantly hijacks the spotlight for themselves, but will loudly celebrate your wins and make you feel like absolute royalty.', 'Reassure them with genuine praise and public appreciation, and they will give you the world in return.'],
    6: ['Virgo', 'Mercury', 5, 'Earth', 'Hyper-critical micromanager who ruthlessly judges your flaws to your face, but will silently clean up your chaos and fix your life before you even ask.', 'Notice and thank them for the small, helpful things they do, as they show their love through acts of service.'],
    7: ['Libra', 'Venus', 6, 'Air', 'Infuriating fence-sitter who takes hours to choose a restaurant to avoid conflict, but will happily sacrifice their own comfort to make sure you feel at peace.', 'Help them make daily decisions without pressure, and ensure the relationship maintains a sense of fair balance.'],
    8: ['Scorpio', 'Pluto', 8, 'Water', 'Suspicious interrogator who treats every casual question like a trap, but becomes your absolute ride-or-die guardian the moment you earn their trust.', 'Be completely transparent and honest from day one, as breaking their trust is nearly impossible to repair.'],
    9: ['Sagittarius', 'Jupiter', 3, 'Fire', 'Flaky philosopher who delivers brutal truths and vanishes on a solo trip when things get heavy, but will fiercely protect your freedom and pull you out of your darkest funks.', 'Respect their deep need for personal independence and join them on their spontaneous adventures.'],
    10: ['Capricorn', 'Saturn', 8, 'Earth', 'Emotionless corporate machine who treats your personal relationship like a scheduled business meeting, but will quietly anchor your entire life and secure your future.', 'Support their professional ambitions and rely on them to be your absolute rock during tough times.'],
    11: ['Aquarius', 'Uranus', 4, 'Air', 'Detached alien who treats human emotions like a weird science experiment, but will passionately fight for your rights and accept your strangest quirks without judgment.', 'Be their best friend first, and give them plenty of emotional breathing room to process things on their own.'],
    12: ['Pisces', 'Neptune', 7, 'Water', 'Escapist space-cadet who completely tunes out while you are speaking to live in a dream world, but will absorb your pain and offer you unconditional, soul-deep empathy.', 'Handle their sensitive heart with care, and gently ground them when they get lost in their daydreams.']
}
print('Welcome to ZODIAC WORLD')
a=input('Want to know your zodiac sign Y/N?')
if a.upper()=='Y':
    m = input('Enter your birth month: ').strip().lower()
    d = int(input('Enter your birth date (1-31): '))

    if (m == 'december' and d >= 22) or (m == 'january' and d <= 19):
        print('Capricorn')
    elif (m == 'january' and d >= 20) or (m == 'february' and d <= 18):
        print('Aquarius')
    elif (m == 'february' and d >= 19) or (m == 'march' and d <= 20):
        print('Pisces')
    elif (m == 'march' and d >= 21) or (m == 'april' and d <= 19):
        print('Aries')
    elif (m == 'april' and d >= 20) or (m == 'may' and d <= 20):
        print('Taurus')
    elif (m == 'may' and d >= 21) or (m == 'june' and d <= 20):
        print('Gemini')
    elif (m == 'june' and d >= 21) or (m == 'july' and d <= 22):
        print('Cancer')
    elif (m == 'july' and d >= 23) or (m == 'august' and d <= 22):
        print('Leo')
    elif (m == 'august' and d >= 23) or (m == 'september' and d <= 22):
        print('Virgo')
    elif (m == 'september' and d >= 23) or (m == 'october' and d <= 22):
        print('Libra')
    elif (m == 'october' and d >= 23) or (m == 'november' and d <= 21):
        print('Scorpio')
    elif (m == 'november' and d >= 22) or (m == 'december' and d <= 21):
        print('Sagittarius')
    else:
        print('Invalid date or month entered.')
end='Y'
u=input('Enter your zodiac sign').title()
while end=='Y':
    k=int(input('Enter 1 for know more details about your zodiac sign , 2 for  get fun fact  , 3 for get relationship advice '))
    
    for i in zodiac.values():
        if i[0] == u:
            if k==1:
                 print(f"Sign: {i[0]} | Planet: {i[1]} | Lucky Number: {i[2]} | Element: {i[3]}")
            elif k==2:
                print(i[4])
            elif k==3:
                print(i[5])
    end=input('Want more? Enter Y to continue or press any key to exit ').upper()

    