# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:55:11 2021

@author: dedbo
"""
(a) How you have implemented the scraper, what challenges you faced and how did you solve them?

    I have implemented scraper in following steps:
        1) Install the relevant chrome driver.
        2) Then get the given page.
        3) Find the product review section by class of element and scroll downn to it.
        4) Find the see all button using class of element and click it.
        5) Then find the sort by section using class of element and select newest to oldest option.
        6) whlie True
            i) Extract the review block.
            ii loop through review block:
                a) extract the date from each review and convert the date to datetime object.
                b) check the condition date.year == 20202 and date.month< 12.
                c) if conditin holds true: break from for loop and set  a = False.
                d) else ectract the needed information.
            iii) if a == false, break while loop.
            iii) else find the next section by class and click it to get next review block.
        7) close browser.
        9) bulid dataframe from the extracted data.
        10) change dataframe to csv.
        
    The challenged that I faced are:
        1) The program try to search the element which was not rendered.
         solution:
             I solved this using time.sleep() to stop the execution of program for certain amount of time
             and let the browser to render.
        2) The data was mixed after sorting also.
         soluton:
             Here also i used sleep.
             
             
(b) What else you could do to improve your scraper?

    The following can be done to improve scraper:
    
        1) Better handle the program with exceptional handling.
        2) Directly inserting the extracted data to csv file instead of creating 
        list and converting the lidt to dataframe and then to csv file.
    
(c) How would you design it to make it work on other retailers as well?
    I think the best utilization will be to develop for a single retailer.
    If i would design it to work on other retailer as well, I will take input the id/class/ipath of each requied element 
    and try to extract the required information on the basis of given information.
    
        