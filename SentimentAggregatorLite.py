#!/usr/bin/env python

from lxml import etree
import sys,getopt
from VUKafParserPy import KafParser


########################################################
# This function converts string values in float
# positive" => 1
# negative" => -1
# other   => 0
########################################################
def convertPolarityToFloats(my_data):
    new_data = []
    for lemma,str_polarity,polarity_modifier in my_data:
        value = 0 
        if str_polarity is None:
            value = 0.0
        elif str_polarity == 'positive':
            value = 1.0
        elif str_polarity == 'negative':
            value = -1.0
        new_data.append((lemma,value,polarity_modifier))
    return new_data




########################################################
# This function applies the negation rule
# Shifter + polarity ==> -1 * polarity
########################################################
def applyNegators(my_data):
    ## APPLYING NEGATORS
    idx =0
    new_data = []
    while idx <len(my_data):
        lemma, polarity, polarity_modifier = my_data[idx]
        if polarity_modifier != 'shifter':
            new_data.append((lemma,polarity,polarity_modifier))
        else:
            if idx+1 < len(my_data):
                next_lemma, next_polarity, next_modifier = my_data[idx+1]
                new_data.append((next_lemma,next_polarity*-1,next_modifier))
                idx += 1
            else:
                new_data.append((lemma,polarity,polarity_modifier))
        idx += 1
    return new_data

########################################################
# This function applies the intensification rule
# Intensifier + polarity ==> 2 * polarity
########################################################
def applyIntensifiers(my_data):
    idx =0
    new_data = []
    my_factor = 2
    while idx <len(my_data):
        lemma, polarity, polarity_modifier = my_data[idx]
        if polarity_modifier != 'intensifier':
            new_data.append((lemma,polarity,polarity_modifier))
        else:
            if idx+1 < len(my_data):
                next_lemma, next_polarity, next_modifier = my_data[idx+1]
                new_data.append((next_lemma,next_polarity * my_factor ,next_modifier))
                idx += 1
            else:
                new_data.append((lemma,polarity,polarity_modifier))
        idx += 1
    return new_data
    
##########################################################
# This functions computes the total value by addin the
# polarity values for all the tokens in the text
##########################################################
def computeTotal(my_data):
    return sum(polarity for (_,polarity,_) in my_data)
    
    

def createOpinion(kafObj, value):
    opinion = etree.Element('opinion')
    
    ## Opinion holder --> ??
    ## Nothing ???
    
    ## Opinion target --> all the text
    opinion_target = etree.Element('opinion_target')
    opi_tar_span = etree.Element('span')
    list_ids_with_sentiment = []
    
    for term in kafObj.getTerms():
        ele_id = etree.Element('id')
        ele_id.text = term.getId()
        opi_tar_span.append(ele_id)    
        if term.getSentiment() is not None:
            list_ids_with_sentiment.append(term.getId())
    opinion_target.append(opi_tar_span)
    opinion.append(opinion_target)
    ###################################
    
    
    ## Opinion type
    if value <= 0:
        polarity = 'negative'
    else:
        polarity = 'positive'
    opinion_type = etree.Element('opinion_type', attrib={'polarity':polarity,'strength':str(value)})
    op_type_span = etree.Element('span')
    for id in list_ids_with_sentiment:
        ele_id = etree.Element('id')
        ele_id.text = id
        op_type_span.append(ele_id)
    opinion_type.append(op_type_span)
    opinion.append(opinion_type)
    return opinion
    
    
if __name__ == '__main__':
    
    my_time_stamp = True
    try:
      opts, args = getopt.getopt(sys.argv[1:],"",["no-time"])
      for opt, arg in opts:
        if opt == "--no-time":
          my_time_stamp = False
    except getopt.GetoptError:
      pass
    
    kafObj = KafParser(sys.stdin)
    data_str = kafObj.getSentimentTriples()       
    data= convertPolarityToFloats(data_str)
    my_data_neg = applyNegators(data)   
    my_data_neg_int = applyIntensifiers(my_data_neg)
    total = computeTotal(my_data_neg_int)
    
    opinionObj = createOpinion(kafObj,total)
    kafObj.addLayer('opinions',opinionObj)
    kafObj.addLinguisticProcessor('RuleBasedSentimentAnalyzer','1.0','opinion',time_stamp=my_time_stamp)
    kafObj.saveToFile(sys.stdout)
    
    
    