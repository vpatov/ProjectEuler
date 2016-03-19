"""
This script allows me to automatically pull problem descriptions from projecteuler.net, and then create a .py skeleton for a given problem.
I use urrlib to fetch the HTML data. I slice the HTML (as a string) around where I need it ( around the textual problem description),
and then use clean_html (copied from the NLTK package, and then slightly modified), to clean up the html and get rid of tags,
leaving me with the (almost) pure text I desire. Some of the more complicated mathematical formulations on the site, such as fractions and division,
aren't rendered properly as text, so I leave them looking ugly. Exponents, and some unicode characters are taken care of however.

I haven't made it so that the script can be run with standard arguments, but if I want to create skeletons for problems x to y,
I merely have to invoke extractProblems(x,y). This code is far from unbreakable, its just one of many automation scripts I hope to write :)
"""


import time
startTime = time.clock()

template = """
import time
startTime = time.clock()


#code


endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")
"""


import re
import urllib.request

##copied from stackoverflow
## https://stackoverflow.com/questions/26002076/python-nltk-clean-html-not-implemented
def clean_html(html):
    """
    Copied from NLTK package.
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)


    ###Vasia's line.
    ###Exponents on the website are done with superscripts, here I replace them with a '^'
    cleaned = re.sub(r"<sup>","^",cleaned)

    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()



def getProblemText(url):
    with urllib.request.urlopen(url) as response:
       html = str(response.read())
       probName = html[html.index("<h2>") + len("<h2>"):html.index("</h2>")]
       html = html[html.index('<div class="problem_content" role="problem">'):]
       html = html[:html.index('<div id="footer" class="noprint">')]


    text = clean_html(str(html))
    #turn newlines into actual newlines
    text = text.replace("\\n",'\n')
    #turn the unicode multiplication into a simple ascii star *
    text = text.replace("\\xc3\\x97", "*")
    #get rid of the \\r's
    text = text.replace("\\r",'')


    return((probName,text.rstrip() + "\n"))



#create .py files for all the project euler problems from start to end, inclusive
def extractProblems(start,end=None):
    if (end == None):
        end = start
    masterUrl = "https://projecteuler.net/problem="
    tripleQuotes = '\"\"\"\n'
    for i in range(start,end+1):
        probText = getProblemText(masterUrl + str(i))
        probName = "INCProblem" + str(i) + ".py"
        f = open(probName,'w+')
        f.write(tripleQuotes)
        f.write(" " + masterUrl + str(i) + "\n")
        f.write(" " + probText[0] + "\n")
        f.write(probText[1])
        f.write(tripleQuotes)
        f.write(template)
        f.close()

    print("Successfully created "+ str(end+1 - start) + " .py file(s) for problems numbered " + str(start) + " through " +
          str(end))

extractProblems(34,40)
endTime = time.clock()
print("Time elapsed:", '{:0.6f}'.format(endTime-startTime), "seconds.")