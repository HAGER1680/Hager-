# Hager-def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    """Counts:
        Number of Images
        Number of Dog Images
        Number of "Not-a" Dog Images
       Percentages:
        % Correctly Classified Dog Images
        % Correctly Classified "Not-a" Dog Images
        % Correctly Classified Breeds of Dog Images
        
        The results dictionary will have the following format:
        key = pet image filename (ex: Beagle_01141.jpg)
        value = List with:
        index 0 = Pet Image Label (ex: beagle)
        index 1 = Classifier Label (ex: english foxhound)
        index 2 = 0/1 where 1 = labels match , 0 = labels don't match (ex: 0)
        index 3 = 0/1 where 1= Pet Image Label is a dog, 0 = Pet Image Label isn't a dog (ex: 1)
        index 4 = 0/1 where 1= Classifier Label is a dog, 0 = Classifier Label isn't a dog (ex: 1)
        example_dictionary = {'Beagle_01141.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1]}"""
    results_stats_dic = {}
    number_of_images = len(results_dic)
    number_of_dogs = 0
    corr_dog = 0
    corr_not_dog = 0
    corr_bree = 0
    
    for key in results_dic:
        if results_dic[key][3]:
            number_of_dogs += 1
            if results_dic[key][2]:
                corr_bree += 1
        
        if results_dic[key][3] and results_dic[key][4]:
            corr_dog += 1
        elif not (results_dic[key][3]) and not (results_dic[key][4]):
            corr_not_dog += 1
    
    number_of_not_dogs = number_of_images - number_of_dogs
    """n_correct_dogs, pct_correct_dogs, n_correct_breed, pct_correct_breed"""
    results_stats_dic['n_images'] = number_of_images
    results_stats_dic['n_dogs_img'] = number_of_dogs
    results_stats_dic['pct_correct_dogs'] = corr_dog/number_of_dogs*100.0
    results_stats_dic['pct_correct_notdogs'] = corr_not_dog/number_of_not_dogs*100.0
    results_stats_dic['n_notdogs_img'] = number_of_not_dogs
    results_stats_dic['pct_correct_breed'] = corr_bree/number_of_dogs*100.0
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    return results_stats_dic
