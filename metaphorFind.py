import json
import pandas as pd
import regex



# open json file that is in the same directory
with open('reviews.json') as f:
    # load json data into a python object
    data = json.load(f)


# loop through 'tweets' looking for certin keys
#for tweets in data['tweets']:
    #print(tweets['like count'], tweets['url'])
    #del tweets['metaphorFamily']

    # remove all emojis in tweets?

for tweets in data['tweets']:
    content = tweets['review']

    #metaphores stored here
    metaphorsFound = ''

    #metapphor family stored here
    metaphorFamilyFound = ''



# metaphorFind begin -------

    # must split tweet before putting into pandas series
    splitTweet = content.split()
    s1 = pd.Series(splitTweet)



    # metaphor categories start here --------

    # metaphor list 'Natural Disaster'
    naturalDisaster = ['button']
    compareToNaturalDisaster = s1.str.contains('|'.join(naturalDisaster), case = False)

    counter1 = 0

    # for loop through the results to find all the true values.
    for i in compareToNaturalDisaster:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter1] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Button '

        counter1 = counter1 + 1




    # metaphor list 'Battle'
    battle = ['Material']
    compareToBattle = s1.str.contains('|'.join(battle), case = False)

    counter2 = 0

    # for loop through the results to find all the true values.
    for i in compareToBattle:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter2] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Material ' + ', ' + metaphorFamilyFound

        counter2 = counter2 + 1




    # metaphor list 'Disease'
    disease = ['Fit']
    compareToDisease = s1.str.contains('|'.join(disease), case = False)

    counter3 = 0

    # for loop through the results to find all the true values.
    for i in compareToDisease:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter3] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'fit ' + ', ' + metaphorFamilyFound

        counter3 = counter3 + 1




    # metaphor list 'Container'
    container = ['Inseam']
    compareToContainer = s1.str.contains('|'.join(container), case = False)

    counter4 = 0

    # for loop through the results to find all the true values.
    for i in compareToContainer:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter4] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Inseam ' + ', ' + metaphorFamilyFound

        counter4 = counter4 + 1




    # metaphor list 'Positive'
    positive = ['Tight']
    compareToPositive = s1.str.contains('|'.join(positive), case = False)

    counter5 = 0

    # for loop through the results to find all the true values.
    for i in compareToPositive:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter5] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Tight ' + ', ' + metaphorFamilyFound

        counter5 = counter5 + 1




    # metaphor list 'Influx'
    influx = ['Fabric']
    compareToInflux = s1.str.contains('|'.join(influx), case = False)

    counter6 = 0

    # for loop through the results to find all the true values.
    for i in compareToInflux:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter6] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Fabric ' + ', ' + metaphorFamilyFound

        counter6 = counter6 + 1



    # metaphor list 'Email'
    email = ['length', 'inseam', 'long', 'rise', 'hem', 'lbs']
    compareToEmail = s1.str.contains('|'.join(email), case = False)

    counter7 = 0

    # for loop through the results to find all the true values.
    for i in compareToEmail:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter7] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Measurement ' + ', ' + metaphorFamilyFound

        counter7 = counter7 + 1



    # metaphor list 'Return'
    return1 = ['height', 'weight', 'model', 'wearing']
    compareToReturn = s1.str.contains('|'.join(return1), case = False)

    counter8 = 0

    # for loop through the results to find all the true values.
    for i in compareToReturn:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter8] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Model Stats ' + ', ' + metaphorFamilyFound

        counter8 = counter8 + 1





    # metaphor list 'Cart'
    cart = ['Sizing', 'chart']
    compareToCart = s1.str.contains('|'.join(cart), case = False)

    counter9 = 0

    # for loop through the results to find all the true values.
    for i in compareToCart:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter9] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Size ' + ', ' + metaphorFamilyFound

        counter9 = counter9 + 1





    # metaphor list 'Global Site'
    globalsite = ['Inconsistent']
    compareToGlobal = s1.str.contains('|'.join(globalsite), case = False)

    counter10 = 0

    # for loop through the results to find all the true values.
    for i in compareToGlobal:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter10] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Unsure ' + ', ' + metaphorFamilyFound

        counter10 = counter10 + 1




    # metaphor list 'Website'
    website = ['slim', 'straight', 'relax', 'oversize', 'big', 'small', 'short', 'stretch', 'baggy', 'loose', 'tight', 'elastic', 'large', 'rise', 'waist']
    compareToWebsite = s1.str.contains('|'.join(website), case = False)

    counter11 = 0

    # for loop through the results to find all the true values.
    for i in compareToWebsite:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter11] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Fit ' + ', ' + metaphorFamilyFound

        counter11 = counter11 + 1




    # metaphor list 'Customer Service'
    customerservice = ['see through', 'made', 'factory', 'sheer', 'light', 'fabric', 'heavy', 'manufacture', 'soft', 'wrinkle', 'lined', 'nylon', 'polyester', 'resistant', 'sewn']
    compareToCustomer = s1.str.contains('|'.join(customerservice), case = False)

    counter12 = 0

    # for loop through the results to find all the true values.
    for i in compareToCustomer:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter12] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Material ' + ', ' + metaphorFamilyFound

        counter12 = counter12 + 1



    # metaphor list 'Account'
    account = ['zipper']
    compareToAccount = s1.str.contains('|'.join(account), case = False)

    counter13 = 0

    # for loop through the results to find all the true values.
    for i in compareToAccount:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter13] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Zipper ' + ', ' + metaphorFamilyFound

        counter13 = counter13 + 1




    # metaphor list 'Sustainability '
    sustainability  = ['cup', 'band', 'bra', 'underwire' ]
    compareToSustainability = s1.str.contains('|'.join(sustainability), case = False)

    counter14 = 0

    # for loop through the results to find all the true values.
    for i in compareToSustainability:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter14] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Bust  ' + ', ' + metaphorFamilyFound

        counter14 = counter14 + 1



    # metaphor list 'Active '
    active  = ['climb', 'hike', 'yoga', 'tech', 'water', 'breath', 'gusset', 'climate', 'run', 'warm', 'weather', 'upf', 'lined' ]
    compareToActive = s1.str.contains('|'.join(active), case = False)

    counter15 = 0

    # for loop through the results to find all the true values.
    for i in compareToActive:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter15] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Active  ' + ', ' + metaphorFamilyFound

        counter15 = counter15 + 1




    # metaphor list 'Swim '
    swim  = ['bikini', 'onepiece', 'tankini' ]
    compareToSwim = s1.str.contains('|'.join(swim), case = False)

    counter16 = 0

    # for loop through the results to find all the true values.
    for i in compareToSwim:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter16] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Swim  ' + ', ' + metaphorFamilyFound

        counter16 = counter16 + 1




    # metaphor list 'Dress '
    dress  = ['dress' ]
    compareToDress = s1.str.contains('|'.join(dress), case = False)

    counter17 = 0

    # for loop through the results to find all the true values.
    for i in compareToDress:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter17] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Dress ' + ', ' + metaphorFamilyFound

        counter17 = counter17 + 1





    # metaphor list 'Skirt '
    skirt  = ['skort' ]
    compareToSkirt = s1.str.contains('|'.join(skirt), case = False)

    counter18 = 0

    # for loop through the results to find all the true values.
    for i in compareToSkirt:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter18] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Skirt  ' + ', ' + metaphorFamilyFound

        counter18 = counter18 + 1





    # metaphor list 'Pant '
    pant  = ['shorts', 'jeans', 'joggers', 'denim', 'legging']
    compareToPant = s1.str.contains('|'.join(pant), case = False)

    counter19 = 0

    # for loop through the results to find all the true values.
    for i in compareToPant:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter19] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Pant  ' + ', ' + metaphorFamilyFound

        counter19 = counter19 + 1




    # metaphor list 'Shirt '
    shirt  = ['turtleneck', 'henley', 'crew', 'flannel', 'sleeve', 'tee', 'top', 'raglan' ]
    compareToShirt = s1.str.contains('|'.join(shirt), case = False)

    counter20 = 0

    # for loop through the results to find all the true values.
    for i in compareToShirt:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter20] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Shirt  ' + ', ' + metaphorFamilyFound

        counter20 = counter20 + 1





    # metaphor list 'Short '
    short  = ['short' ]
    compareToShort = s1.str.contains('|'.join(short), case = False)

    counter21 = 0

    # for loop through the results to find all the true values.
    for i in compareToShort:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter21] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Short  ' + ', ' + metaphorFamilyFound

        counter21 = counter21 + 1



    # metaphor list 'Sweater '
    sweater  = ['hoodie', 'duster', 'sweatshirt', 'pullover' ]
    compareToSweater = s1.str.contains('|'.join(sweater), case = False)

    counter22 = 0

    # for loop through the results to find all the true values.
    for i in compareToSweater:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter22] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Sweater  ' + ', ' + metaphorFamilyFound

        counter22 = counter22 + 1




    # metaphor list 'Jacket '
    jacket  = ['coat', 'cape' ]
    compareToJacket = s1.str.contains('|'.join(jacket), case = False)

    counter23 = 0

    # for loop through the results to find all the true values.
    for i in compareToJacket:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter23] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Jacket  ' + ', ' + metaphorFamilyFound

        counter23 = counter23 + 1




    # metaphor list 'Style '
    style  = ['fashion' ]
    compareToStyle = s1.str.contains('|'.join(style), case = False)

    counter24 = 0

    # for loop through the results to find all the true values.
    for i in compareToStyle:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter24] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Style  ' + ', ' + metaphorFamilyFound

        counter24 = counter24 + 1




    # metaphor list 'Hat '
    hat  = ['cap', 'beanie', 'trucker' ]
    compareToHat = s1.str.contains('|'.join(hat), case = False)

    counter25 = 0

    # for loop through the results to find all the true values.
    for i in compareToHat:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter25] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Hat  ' + ', ' + metaphorFamilyFound

        counter25 = counter25 + 1



    # metaphor list 'Sustainability '
    sustainability  = ['bluesign', 'chemical', 'fair trade', 'safety', 'organic', 'recycled' ]
    compareToSustainability = s1.str.contains('|'.join(sustainability), case = False)

    counter26 = 0

    # for loop through the results to find all the true values.
    for i in compareToSustainability:
        if i == True:
            #metaphorsFound.append(splitTweet[counter])
            metaphorsFound = splitTweet[counter26] + ' ,' + metaphorsFound
            metaphorFamilyFound = 'Sustainability  ' + ', ' + metaphorFamilyFound

        counter26 = counter26 + 1




    # metaphor categories end here --------





    # add new key:values
    # TO-DO REMOVE DUPLICATETES
    tweets['metaphorsFound'] = metaphorsFound
    tweets['metaphorFamily'] = metaphorFamilyFound


# metaphorFind END -----------





# Save python object to a json file
# First open the file we 'read' into

with open('metaphorsFound.json', 'w') as f:
    json.dump(data, f, indent = 2)
