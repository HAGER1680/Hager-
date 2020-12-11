# Hager-Command Line Arguments:
     dir = uploaded_images/ 
    arch = resnet 
 dogfile = dognames.txt

Pet Image Label Dictionary has 4 key-value pairs.
Below are 4 of them:
 1 key:                  kelpie_01.jpg  label:                     kelpie
 2 key:          english_setter_01.jpg  label:             english setter
 3 key:                     fox_01.jpg  label:                        fox
 4 key:                     cat_01.jpg  label:                        cat

     MATCH:

                 kelpie_01.jpg: 
Real:                     kelpie   Classifier:                         kelpie

         english_setter_01.jpg: 
Real:             english setter   Classifier:                 english setter

                    fox_01.jpg: 
Real:                        fox   Classifier:       kit fox, vulpes macrotis

 NOT A MATCH:

                    cat_01.jpg: 
Real:                        cat   Classifier:                           lynx

# Total Images 4 # Matches: 3 # NOT Matches: 1

     MATCH:

                 kelpie_01.jpg: 
Real:                     kelpie   Classifier:                         kelpie  
PetLabelDog: 1  ClassLabelDog: 1

         english_setter_01.jpg: 
Real:             english setter   Classifier:                 english setter  
PetLabelDog: 1  ClassLabelDog: 1

                    fox_01.jpg: 
Real:                        fox   Classifier:       kit fox, vulpes macrotis  
PetLabelDog: 0  ClassLabelDog: 0

 NOT A MATCH:

                    cat_01.jpg: 
Real:                        cat   Classifier:                           lynx  
PetLabelDog: 0  ClassLabelDog: 0

# Total Images 4 # Matches: 3 # NOT Matches: 1

 ** Statistics from calculates_results_stats() function:
N Images:  4  N Dog Images:  2  N NotDog Images:  2 
Pct Corr dog: 100.0 Pct Corr NOTdog: 100.0  Pct Corr Breed: 100.0

 ** Check Statistics - calculated from this function as a check:
N Images:  4  N Dog Images:  2  N NotDog Images:  2 
Pct Corr dog: 100.0 Pct Corr NOTdog: 100.0  Pct Corr Breed: 100.0

Here is the full result using resnet CNN model

Number of Images = 4
Number of Dog Images = 2
Number of Not a Dog Images = 2

The Corrct Classification of Dogs Percentage is 100.0%
The Corrct Classification of Not Dogs Percentage is 100.0%
The Corrct Classification of Breed Percentage is 100.0%
The Misclassificated Dogs Are:
There are no Dogs Misclassifications !

The Misclassificated breed Are:
There are no Breeds Misclassifications !

** Total Elapsed Runtime: 0:0:0
