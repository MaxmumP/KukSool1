import signal
import sys
import datetime
import time
import random
import string
import Technique, Form, Weapon, Exercise, Meditation
import dataGuy
import pprint

class Knowledge:
    UNDER_BB=0
    WHITE=.1
    YELLOW_S=.15
    YELLOW=.2
    BLUE_S=.25
    BLUE=.3
    RED_S=.35
    RED=.4
    BROWN_S=.45
    BROWN=.5
    BL_S1=.55
    BL_S2=.6
    DBN=.7
    FIRST=1
    SECOND=2
    THIRD=3

    def __init__(self):
        self.weapons = [Weapon.Weapon("Gum", [Form.Form("Jung Gum Hyung", 1, "Straight Sword Form", 70)],meaning="Sword", exercises=[Exercise.Exercise("Kneeling", 5), Exercise.Exercise("Drawing and Sheathing", 3), Exercise.Exercise("Moving", 4), Exercise.Exercise("Cutting", 5)]),
                        Weapon.Weapon("Bong", [Form.Form("Joong Bong Il Hyung", 1, "First Staff Form", 35)], meaning="Staff", meditations=[Meditation.Meditation("Standing", 15)], exercises=[Exercise.Exercise("Moving", 3)]),
                        Weapon.Weapon("Dahn Bong", [Form.Form("Dahn Bong Hyung", 4, "Short Staff Form", 25)], meaning="Short Staff", meditations=[Meditation.Meditation("Kneeling", 4)]),
                        Weapon.Weapon("Juhl Bong", [Form.Form("Juhl Bong Hyung", 1, "Nunchucks Form", 50)], meaning="Nunchucks", exercises=
                              [Exercise.Exercise("Spinning", 4, "Set 1"),
                               Exercise.Exercise("Rebounding", 4, "Set 2"),
                               Exercise.Exercise("Around the Body", 4, "Set 3"),
                               Exercise.Exercise("Plum Flower", 1, "Set 4"),
                               Exercise.Exercise("Passing/Transfer", 4, "Set 5"),
                               Exercise.Exercise("Advanced", 4, "Set 6"),
                               Exercise.Exercise("Really Advanced", 4, "Set 7"),
                               Exercise.Exercise("Flying", 5, "Set 8"),
                               Exercise.Exercise("Opposite", 8, "Set 9") ]
                                    )
                        ]

        self.forms = [Form.Form("Ki Cho Hyung", 6, "", Knowledge.YELLOW, 50),
                      Form.Form("Cho Geup Hyung", 1, "", Knowledge.BLUE, 40),
                      Form.Form("Jeung Geup Hyung", 1, "", Knowledge.RED, 45),
                      Form.Form("Goh Geup Hyung", 1, "", Knowledge.BROWN, 40),
                      Form.Form("Dae Geup Hyung", 1, "", Knowledge.DBN, 30),
                      Form.Form("Gum Mo Hyung", 1, "", Knowledge.FIRST, 75),
                      Form.Form("Baek Pahl Ki Hyung", 1, "", Knowledge.SECOND, 85) ]

        # Technique.Set(name, number, meaning, level=-1, starts_with="", techniques=[])
        # TODO: Populate these with Technique.technique(number, description, similarTo, hints=[], hyuls=[])

        self.techniques = [Technique.Set("Sohn Ppae Ki", 5, "", Knowledge.YELLOW_S),
                           Technique.Set("Ki Bohn Soo", 15, "", Knowledge.YELLOW),
                           Technique.Set("Sohn Mohk Soo", 11, "", Knowledge.BLUE_S),
                           Technique.Set("Eui Bohk Soo", 13, "", Knowledge.BLUE),
                           Technique.Set("Ahn Sohn Mohk Soo", 6, "", Knowledge.RED_S),
                           Technique.Set("Maek Chi Ki", 15, "", Knowledge.RED),
                           Technique.Set("Maek Cha Ki", 15, "", Knowledge.BROWN_S),
                           Technique.Set("Joo Muhk Maga Ki Bohn Soo", 15, "", Knowledge.BROWN),
                           Technique.Set("Joong Geup Sohn Mohk Soo", 7, "", Knowledge.BL_S1),
                           Technique.Set("Ahp Eui Bohk Soo", 20, "", Knowledge.BL_S2),
                           Technique.Set("Dee Eui Bohk Soo", 23, "Clothing Techniques against a grab from behind", Knowledge.DBN),
                           Technique.Set("Kwan Juhl Ki", 13, "", Knowledge.DBN),
                           Technique.Set("Too Ki", 13, "", Knowledge.DBN),
                           Technique.Set("Mohk Joh Leu Ki", 5, "", Knowledge.DBN),
                           Technique.Set("Bohn Too Ki", 10, "", Knowledge.DBN),
                           Technique.Set("Yang Sohn Mohk Soo", 15, "", Knowledge.DBN),
                           Technique.Set("Ssang Soo", 15, "", Knowledge.DBN),
                           Technique.Set("Dahn Do Maek Ki", 15, "", Knowledge.DBN),
                           Technique.Set("Ki Bohn Bohn", 10, "Fundamental (Freshmen) Techniques", Knowledge.FIRST),
                           Technique.Set("Gahk Doh Bup", 10, "", Knowledge.FIRST),
                           Technique.Set("Juhn Hwan Bup", 10, "", Knowledge.FIRST),
                           Technique.Set("Goh Geup Sohn Mohk Soo", 15, "", Knowledge.FIRST),
                           Technique.Set("Goh Geup Eui Bohk Soo", 15, "", Knowledge.FIRST),
                           Technique.Set("Jah Ki", 15, "", Knowledge.FIRST),
                           Technique.Set("Wah Ki", 15, "", Knowledge.FIRST),
                           Technique.Set("Ee In Jeh Ahp Sool", 10, "", Knowledge.FIRST),
                           Technique.Set("Jahp Ki", 20, "", Knowledge.FIRST),
                           Technique.Set("Keun Dae Ryuhn", 8, "Close-Range Sparring Techniques", Knowledge.FIRST),
                           Technique.Set("Johk Bahng Uh Sool", 15, "Defense Against Kicking Techniques", Knowledge.FIRST)
                           ]

        '''
        # Old Implementation
        self.techniques = {"Techniques":
                                    ["Sohn Ppae Ki",
                                    "Ki Bohn Soo",
                                    "Sohn Mohk Soo",
                                    "Eui Bohk Soo",
                                    "Ahn Sohn Mohk Soo",
                                    "Maek Chi Ki",
                                    "Maek Cha Ki",
                                    "Joong Maek Maga Ki Bohn Soo",
                                    "Joong Geup Sohn Mohk Soo",
                                    "Ahp Eui Bohk Soo",
                                    "Dee Eui Bohk Soo",
                                    "Kwan Jeul Liu Ki",
                                    "Too Ki",
                                    "Mohk Joh Leu Ki",
                                    "Bohn Too Ki",
                                    "Yang Sohn Mohk Soo",
                                    "Ssang Soo",
                                    "Dahn Do Maek Ki"]
                                 }

        self.first_degree = {"Techniques":
                                ["Ki Bohn Bohn",
                                 "Gahk Doh Bup",
                                 "Juhn Hwan Bup",
                                 "Goh Geup Sohn Mohk Soo",
                                 "Goh Geup Eui Bohk Soo",
                                 "Jah Ki",
                                 "Wah Ki",
                                 "Ee In Jeh Ahp Sool",
                                 "Jahp Ki",
                                 "Keun Dae Ryuhn",
                                 "Johk Bahng Uh Sool"]
                             }'''

        self.altSpellings={"Mohk":["Mek","Mok","Mock"],
                         "Joh": ["Jeul","Jol","Jo","Jul"],
                         "Leu": ["Liu","Li","Lew"],
                         "Ki":  ["Gi"],
                         "Bahng":["Bohn", "Bong"],
                         "Yahng": ["Yohng", "Yang"],
                         "Eue": ["Ew", "Oo", "U"],
                         "Bohk": ["Bok", "Bahk", "Back", "Bach"],
                         "Soo": ["So", "Su", "Sue", "Sew"]}

        # for spelling errors like e/y (pae->pay), g/k (gi->ki), o/oh (mok->mohk), u/oo (soo->su)
        self.letterChange={"o": "oh",
                           "e": "y",
                           "g": "k",
                           "u": "oo"}

    def loadSavedTechniques(self,techniques):
        self.techniques=techniques
        
    def getExactTechnique(self, searchSetName):
        return self.getTechnique(searchSetName, num_res=1)

    def getTechnique(self, searchSetName, num_res=-1, charMatchThreshold=0):
        #totalMatches=0
        matches={}
        for t_set in self.techniques:
            setName=t_set.name
            matches[setName]={"Technique":t_set, "Total Words": 0, "Matched Words": 0,
                                      "Matches":[], "charMatches":0}
            # TODO: add a tracker like usedWords=[] that will allow me to go back through and match that word better- maybe with self.altSpellings
            # TODO: first, fast check for first letter matches (K.B.S. matching KBS/EBS, etc)
            # TODO: Keep track of percent matched as primary assessment, not absolute matches
            setWords=string.capwords(searchSetName).split()
            for actualWord in setName.split():
                matches[setName]["Total Words"]+=1
                bestMatch="_"*len(actualWord)
                bestCharMatch=0
                curMatch=""
                for word in setWords:
                    curCharMatch=0
                    partial_match=False
                    if word==actualWord:
                        matches[setName]["Matched Words"]+=1
                        matches[setName]["charMatches"]+=len(word)
                        curMatch=word
                        bestMatch=word
                        # prevent the same word from matching again
                        # Make this better, iterate to see which is the best- Kwan Jeul Liu Ki/Kwan Jul Ki (#TODO #1 above)
                        setWords.remove(word)
                        break
                    #TODO: add check for near match in self.letterChange
                    else:
                        curMatch=testWords(actualWord, word)
                        curCharMatch=len(curMatch)-curMatch.count("_")
                        if curCharMatch==len(actualWord):
                            setWords.remove(word)
                        elif curCharMatch>0:
                            partial_match=True
                    if curMatch.count("_") < bestMatch.count("_"):
                        bestMatch=curMatch
                        bestCharMatch=curCharMatch
                        if partial_match:
                            # don't try to match this word again
                            setWords.remove(word)
                matches[setName]["charMatches"]+=bestCharMatch
                matches[setName]["Matches"].append(bestMatch)
        first_sort=sorted(matches.iteritems(), key=lambda (k,v): v["charMatches"], reverse=True)
        data_idx=1

        valid_matches=[]
        if num_res!=-1:
            return first_sort[:num_res]
        elif charMatchThreshold>0:
            for candidate in first_sort:
                if candidate[data_idx]["charMatches"]/(len(searchSetName)-(searchSetName.count(" ") if searchSetName.count(" ")!=-1 else 0))>=charMatchThreshold:
                    valid_matches.append[candidate]
            return valid_matches

        # if all words match in the best character match, return that match
        if (first_sort[0][data_idx]["Matched Words"]==first_sort[0][data_idx]["Total Words"]):
            return [first_sort[0]]
        # otherwise, return the first three matches
        else:
            return first_sort[:3]

        #second_sort=sorted(first_sort, key=lambda key: v["charMatches"], reverse=True)
        #pprint(
        #printf("%s has %i  set["Name"], " has "

    def randomWorkout(self):
        results={"Titles":["Under DBN", "DBN", "First Degree", "Hyung", "Weapon"], "Picks":[]}
        #TODO: Keep a record of previous picks, don't duplicate last 5 choices (and ensure pick within certain number of picks

        # separate under-dbn, dbn, first degree techniques
        third=[]
        second=[]
        first=[]
        for technique in self.techniques:
            if technique.level<Knowledge.DBN:
                first.append(technique)
            elif technique.level <Knowledge.FIRST:
                second.append(technique)
            elif technique.level<Knowledge.SECOND:
                third.append(technique)
        # First 11 techniques
        results["Picks"]=[random.choice(first)]
        # Rest of Under Black Belt
        results["Picks"].append(random.choice(second))
        # Black belt curriculum
        results["Picks"].append(random.choice(third))
        # Hyung
        results["Picks"].append(random.choice(self.forms))
        # Weapon
        results["Picks"].append(random.choice(self.weapons))
        dt=datetime.datetime.now().isoformat()
        printstr = "Practice "+dt+":\n"
        for ex in results["Titles"]:
            printstr+=ex+": "+str(results["Picks"][results["Titles"].index(ex)])
            if ex == "Hyung":
                printstr+=" ("+random.choice(["Regular", "Opposite"])+")\n"
            elif ex == "Weapon":
                printstr+=" \n"+random.choice(["^FORM", "^MEDITATION/EXERCISE"])
            else:
                printstr+="\n"
        printstr+="\n"
        recorder(printstr)

    def randomQuiz(self, min_level=0):
        eligible = []
        for tech in self.techniques:
            if tech.level >= min_level:
                eligible.append(tech)
        res=None
        res_buffer=[]
        while not res:
            res_buffer.append(self.setQuiz(random.choice(eligible).name))
            if raw_input("Try a different technique? (y/n) > ")[0].upper()=="Y":
                continue
            else:
                res=res_buffer
        return res

    # order options are all, granular, random, or an integer i (random i from each set)
    # granularity options are coarse (steps of 5-10), fine (1-3), medium (1-6), or none (1)
    def runQuiz(self,test_sets,order="random",granularity="none"):
        step_min=1
        step_max=1
        if granularity=="fine":
            step_max=3
        elif granularity=="medium":
            step_max=6
        elif granularity=="coarse":
            step_min=5
            step_max=10
        quiz_results={"avg":0,"right":0}
        right=0
        tot=0
        time_tot=0
        right_time_tot=0
        wrongs={}
        rights={}
        check=raw_input("Hit Enter to start quiz > ")
        if check!="":
            if check=="q":
                return quiz_results
            else:
                return None
        print "(-=pass, q=quit, h=hint, enter=you know the answer)\n"
        for target_set in test_sets:
            tech_numbers=range(1,target_set.number+1)
            condition_met=False
            while not condition_met:
                if order=="random":
                    tech_num=random.choice(tech_numbers)
                    tot+=1
                    answer=timed_input("%s number %i\n"
                                       "  (%i/%i %0.2fs avg)" % (target_set.get_description(), tech_num, tot, target_set.number, 0 if right==0 else right_time_tot/right)
                                       )
                    if answer[0]=="h":
                        tech=target_set.get_technique(tech_num)
                        if tech:
                            print tech.hint
                        else:
                            print "\n\nSorry, no hints available for this one.\n"
                        answer=timed_input("%s number %i\n"
                                       "  (%i/%i %0.2fs avg)" % (target_set.get_description(), tech_num, tot, target_set.number, 0 if right==0 else right_time_tot/right)
                                       )
                    print ""
                    quiz_results[tech_num]=answer
                    tech_numbers.remove(tech_num)
                    time_tot+=answer[1]
                    if answer[0]=="":
                        right+=1
                        right_time_tot+=answer[1]
                        rights[tech_num]=answer
                    elif answer[0]=="-":
                        wrongs[tech_num]=answer
                    elif answer[0]=="q":
                        wrongs[tech_num]=answer
                        break
                    if len(tech_numbers)==0:
                        condition_met=True
                elif order=="all":
                    pass
        corrections=True
        while corrections:
            print "\nResults:"
            avg=(0 if right==0 else right_time_tot/right)
            print "%i out of %i right, average time: %0.2fs" % (right, tot, avg)
            quiz_results["right"]=right
            quiz_results["avg"]=avg
            print "quiz took %i sec total" % time_tot
            if len(rights)>0:
                print "Right answers:"
                long_sort=sorted(rights.iteritems(), key=lambda (k,v): v[1], reverse=True)
                for lng in long_sort:
                    print str(lng[0])+" ("+str(rights[lng[0]][1])+"s)"
            wrong_sort=sorted(wrongs, key=lambda key: wrongs[key])
            if len(wrongs)>0:
                print "\nAnswered incorrectly:"
                for idx in wrong_sort:
                    print str(idx)+" ("+str(wrongs[idx][1])+"s)"
            cor=raw_input("\nAny corrections? (y/n) ")
            if cor!="" and cor.upper()[0]=="Y":
                cor=int(raw_input("Which number? > "))
                if cor in rights.keys():
                    cor_item=rights.pop(cor)
                    if raw_input("You said you knew number %i, was that answer wrong? (y/n) " % cor).upper()[0]=="Y":
                        print "Ok, marking it as wrong."
                        wrongs[cor]=cor_item
                        right_time_tot-cor_item[1]
                        right-=1
                    else:
                        print "I don't know what to do then."
                elif cor in wrongs.keys():
                    cor_item=wrongs.pop(cor)
                    if raw_input("You said you didn't know number %i, change that to a right answer? (y/n) " % cor).upper()[0]=="Y":
                        print "Ok, marking it right."
                        rights[cor]=cor_item
                        right_time_tot+cor_item[1]
                        right+=1
                    else:
                        print "I don't know what to do then."
                else:
                    print "I don't recognize that technique."
                    if target_set.number<cor:
                        print target_set.name+" only has "+str(target_set.number)+" techniques."
            else:
                corrections=False
        return quiz_results

    def setQuiz(self, set_name, retake=False, enter_data=False):
        #TODO: check for which set by name, initials, etc...
        # right now, just do initials
        res=self.findByInitials(set_name)
        if len(res) > 1:
            #for tech in res:
            #    print tech.name+" ",
            target_set=self.getTechnique(set_name, 1)[0][1]["Technique"]
        elif len(res)==1:
            target_set=res[0]
        else:
            print "No results matching %s" % (set_name)
            return
        tech_numbers=range(1,target_set.number+1)
        print target_set.name
        quiz_results={"avg":0,"right":0}
        right=0
        tot=0
        time_tot=0
        right_time_tot=0
        wrongs={}
        rights={}
        check=raw_input("Hit Enter to start quiz > ")
        if check!="":
            if check=="q":
                return quiz_results
            else:
                return None
        print "(-=pass, q=quit, h=hint, enter=you know the answer)\n"
        while len(tech_numbers)>0:
            tech_num=random.choice(tech_numbers)
            tot+=1
            answer=timed_input("%s number %i\n"
                               "  (%i/%i %0.2fs avg)" % (target_set.get_description(), tech_num, tot, target_set.number, 0 if right==0 else right_time_tot/right),
                               enter_data,
                               default_desc=target_set.get_technique(tech_num).get_description()
                               )
            if answer[0]=="h":
                tech=target_set.get_technique(tech_num)
                if tech:
                    print tech.hint
                else:
                    print "\n\nSorry, no hints available for this one.\n"
                answer=timed_input("%s number %i\n"
                               "  (%i/%i %0.2fs avg)" % (target_set.get_description(), tech_num, tot, target_set.number, 0 if right==0 else right_time_tot/right)
                               )
            print ""
            quiz_results[tech_num]=answer
            if enter_data:
                target_set.get_technique(tech_num).set_description(answer[2])
                if answer[3]:
                    target_set.get_technique(tech_num).set_hint(answer[3])
            tech_numbers.remove(tech_num)
            time_tot+=answer[1]
            if answer[0]=="":
                right+=1
                right_time_tot+=answer[1]
                rights[tech_num]=answer
            elif answer[0]=="q":
                wrongs[tech_num]=answer
                break
            else:
                wrongs[tech_num]=answer
        corrections=True
        while corrections:
            print "\nResults:"
            avg=(0 if right==0 else right_time_tot/right)
            print "%i out of %i right, average time: %0.2fs" % (right, tot, avg)
            quiz_results["right"]=right
            quiz_results["avg"]=avg
            print "quiz took %i sec total" % time_tot
            if len(rights)>0:
                print "Right answers:"
                long_sort=sorted(rights.iteritems(), key=lambda (k,v): v[1], reverse=True)
                for lng in long_sort:
                    print str(lng[0])+" ("+str(rights[lng[0]][1])+"s)"
            wrong_sort=sorted(wrongs, key=lambda key: wrongs[key])
            if len(wrongs)>0:
                print "\nAnswered incorrectly:"
                for idx in wrong_sort:
                    print str(idx)+" ("+str(wrongs[idx][1])+"s)"
            cor=raw_input("\nAny corrections? (y/n) ")
            if cor!="" and cor.upper()[0]=="Y":
                cor=int(raw_input("Which number? > "))
                if cor in rights.keys():
                    cor_item=rights.pop(cor)
                    if raw_input("You said you knew number %i, was that answer wrong? (y/n) " % cor).upper()[0]=="Y":
                        print "Ok, marking it as wrong."
                        wrongs[cor]=cor_item
                        right_time_tot-cor_item[1]
                        right-=1
                    else:
                        print "I don't know what to do then."
                elif cor in wrongs.keys():
                    cor_item=wrongs.pop(cor)
                    if raw_input("You said you didn't know number %i, change that to a right answer? (y/n) " % cor).upper()[0]=="Y":
                        print "Ok, marking it right."
                        rights[cor]=cor_item
                        right_time_tot+cor_item[1]
                        right+=1
                    else:
                        print "I don't know what to do then."
                else:
                    print "I don't recognize that technique."
                    if target_set.number<cor:
                        print target_set.name+" only has "+str(target_set.number)+" techniques."
            else:
                corrections=False
        if not retake:
            done=False
            while not done:
                resp=raw_input("\nWould you like to quiz yourself on this technique again? (y/n) ").upper()
                if len(resp)>0 and resp[0]=="Y":
                    new_results=self.setQuiz(target_set.name, retake=True)
                    print "\nYou got %i right this time around and averaged %0.2fs per answer." % (new_results["right"],new_results["avg"])
                    if new_results["avg"]<quiz_results["avg"] and new_results["right"]>=quiz_results["right"]:
                        print "Looks like you beat your previous best quiz results (%i right, %0.2f s avg), nice work!" % (quiz_results["right"],quiz_results["avg"])
                        quiz_results=new_results
                else:
                    done=True
        return quiz_results

    # granularity indicates how many techniques will be quizzed per set-
    # input options are coarse (steps of 5-10), fine (1-3), medium (1-6), or none (1)
    def spotCheck(self,granularity="medium",level=UNDER_BB):
        sets=self.getLevelSets(level,randomize=False)
        #for tech_set in sets:
        pass

    def getLevelSets(self,level=UNDER_BB,randomize=False):
        eligible=[]
        for tech_set in self.techniques:
            if tech_set.level>level:
                eligible.append(tech_set)
        if randomize:
            return random.shuffle(eligible)
        else:
            return eligible



    def findByInitials(self, initOrName, level=UNDER_BB):
        initOrName=initOrName.strip().upper()
        initials=initOrName
        if initOrName.strip().find(" ")!=-1:
            initials=""
            for word in initOrName.split(" "):
                initials+=word.upper()[0]
        results=[]
        for technique in self.techniques:
            inits=""
            for word in technique.name.strip().split(" "):
                inits+=word.upper()[0]
            if inits==initials:
                results.append(technique)
        return results

def recorder(rec_string,dest="", target=""):
    if dest != "file":
        print rec_string
    if dest != "screen":
        file_loc="C:\Users\Owner\Desktop\Practice.log"
        if target!="":
            file_loc=target
        record_file=file(file_loc,"a")
        record_file.write(rec_string)

def timed_input(prompt, data_entry=False, default_desc=""):
    start_tm=datetime.datetime.now()
    answer=raw_input(prompt+" > ")
    description=""
    add_hint=""
    hint=""
    if answer=="" and data_entry:
        description = raw_input("Enter keyword(s) or description of this technique:\n > %s" % (default_desc)+chr(8)*len(default_desc))
        if not description:
            description=default_desc
        add_hint = raw_input("Would you like to add a hint word? (y/n) > ")
        if len(add_hint)>0 and add_hint[0].upper()=="Y":
            hint = raw_input("Hint word/phrase: > ")
    delta=datetime.datetime.now()-start_tm
    res_time=delta.seconds+delta.microseconds/1000000.
    return [answer, res_time, description, hint]

def testWords(actual, b):
    a=actual
    if len(a)>len(b):
        longerWord=a
        shorterWord=b
    else:
        longerWord=b
        shorterWord=a
    i=0
    frontMatch=""
    for letter in longerWord:
        if (i+1 > len(shorterWord) or letter.upper()!=shorterWord[i].upper()):
            frontMatch+="_"
        else:
            frontMatch+=letter
        i+=1
    # search backwards
    i=len(longerWord)
    backMatch=""
    # reverse longerWord then loop through it
    for letter in longerWord[::-1]:
        if (i+1 > len(shorterWord) or letter.upper()!=shorterWord[i-1].upper()):
            # if this character matched going forward, use it
            if (frontMatch[i-1]!="_"):
                backMatch=frontMatch[i-1]+backMatch
            else:
                backMatch="_"+backMatch
        else:
            backMatch=letter+backMatch
        i-=1
    curMatch=frontMatch
    if backMatch.count("_") < frontMatch.count("_"):
        curMatch=backMatch
    loops=0

    while len(curMatch)>len(actual):
        # if match is too long, try stripping blanks from end first
        if (curMatch[-1])=="_":
            curMatch=curMatch[:-1]
        # go again if the front is blank and it's still too long
        if len(curMatch)>len(actual) and curMatch[0]=="_":
            curMatch=curMatch[1:]
        loops+=1
        if loops>=len(longerWord) or (curMatch[0]!="_" and curMatch[-1]!="_"):
            break
    return curMatch

def getInputs():
    while not selection:
        setName = raw_input("Which set? ")
        k = Knowledge()
        matches = k.getExactTechnique(setName)
        if len(matches)!=1:
            getByWord(setName)
        else:
            selection

def getByWord(setName):
    # setName="Bohn To Ki"
    # sys.stdout.flush()
    k=Knowledge()
    matches = k.getTechnique(setName)
    match=matches[0]
    if len(matches)!=1:
        print "No exact match for %s, select from list:" % setName
        i=1
        for match in matches:
            print str(i)+". "+match[0]
            i+=1
        print str(i)+". Try again with different spelling"
        sys.stdout.flush()
        re_input = int(raw_input("> "))
        if re_input!=i:
            match = matches[re_input-1]
            selection = match
    else:
        selection = match
    print selection


if __name__ == '__main__':
    config_data = {"load_dir": "Data", "save_dir": "Data", "data_dir": "Data"}
    data=dataGuy.dataGuy(config_data)
    selection=""
    k=Knowledge()
    #k.setQuiz("Jahp ki")
    '''data.load_subset("Techniques", "techniques.txt")
    if data.loaded.has_key("Techniques"):
        for item in data.loaded["Techniques"]:
            print item.get_full_description()
        #k.loadSavedTechniques(data.loaded["Techniques"])
    else:
        print "No data loaded"
    #data.save_data(k.forms,"forms.txt")
    #data.load_all()
    for item in data.loaded["Forms"]:
        print item
    # FIXME: Add a quizzer mode where the quiz asks you for the description of the technique/keywords when quizzing
    for technique_set in k.techniques:
        print technique_set.get_full_description()
    print ""
    print k.findByInitials("SPK")[0].get_full_description()
    print k.setQuiz("SPK")
    
    for technique_set in k.techniques:
        print technique_set.get_full_description()
    data.save_data(k.techniques,"techniques.txt")
    '''
    #k.randomQuiz(min_level=Knowledge.DBN)
    k.randomWorkout()
    #getByWord(None)
