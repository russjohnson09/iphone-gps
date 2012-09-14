#!/usr/bin/python
import subprocess
from pyparsing import Literal,Word,ZeroOrMore,Forward,nums,oneOf,Group,srange,Suppress



def dec_degrees(lst1):
    """
    returns a tuple containing latitude and longitude written in 
    decimal degrees
    """
    
    
    if lst1[3] == 'S':
        latitude = (lst1[0] + lst1[1] / 60 + lst1[2] / 3600) * -1
    else:
        latitude = lst1[0] + lst1[1] / 60 + lst1[2] / 3600
    if lst1[7] == 'W':
        longitude = (lst1[4] + lst1[5] / 60 + lst1[6] / 3600) * -1
    else:
        longitude = lst1[4] + lst1[5] / 60 + lst1[6] / 3600
    return (latitude, longitude)

def syntax():
    
    number = Word(nums + '.').setParseAction(lambda t: float(t[0]))
    colon = Suppress(":")
    comma = Suppress(",")
    
    deg = number + Suppress('deg')
    min = number + Suppress("'")
    second = number + Suppress('"')
    cardinal = oneOf('N S E W')
    
    latitude = deg + min + second + cardinal
    longitude = latitude
    
    
    gps = (Suppress('GPS') + Suppress("Position") + 
           colon + latitude + comma + longitude)
    
    return gps

def test(s):
    gps = syntax()
    results = gps.parseString(s)
    return results

if __name__ == "__main__":
    name = raw_input("Please enter directory of file you wish to obtain GPS data from: ")
    
    p = subprocess.Popen(["exiftool", name], stdout=subprocess.PIPE)
    out, err = p.communicate()
    
    
    if err:
        print err
        
        
    else:
        lst1 = out.split("\n")
        for element in lst1:
            if element[:5] == "GPS P":
                print element
                print element[52:]
                results = list(test(element))
                print dec_degrees(results)
                
                
                
#/home/russ/photo.JPG
    

#print out

#print str1