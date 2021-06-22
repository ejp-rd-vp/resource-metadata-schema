# Adding new terms to EJP-RD
```
```
1. Navigate to the EJP-Ontology/src/ontology folder and open the ejp-rd-edit.owl file in protege 

2. To create a new term, the 'Asserted view' must be active (not the 'Inferred view').

2. In the Class hierarchy window, click on the 'Add subclass' button at the upper left of the window.

3. A pop-up window will appear asking you to enter the Name of the new term. When you enter the term name, you will see your ID automatically populate the IRI box. Once you have entered the term, click 'OK' to save the new term. You will see it appear in the class hierarchy.

4. Navigate to the annotation window by clicking on the + icon in front of annotations in the annotation tab section.

5. In the annotation window add:

    1. rdfs:label
       1. Begin typing the label for the term e.g.:
               - ```biological_process```
       2. For Type, select: ```xsd:string```

    2. Definition
       1. Click on the  ```+``` next to the Definition box
       2. Add the textual definition in the pop-up box.
       3. For Type, select: ```Xsd:string```
       4. Click OK.

     3. Add Definition References
        1. Click on the circle with the ‘Ref’ in it next to add Definition References and in the resulting pop-up click on the ```+``` to add a new ref, making sure they are properly formatted with a database abbreviation followed by a colon, followed by the text string or ID. Examples: ```GOC:bhm, PMID:27450630```.
         2. Select Type: ```xsd:string```
         3. Click OK.
         4. Add each definition reference separately by clicking on the ```+``` sign.

      4. Add synonyms and dbxrefs following the same procedure if they are required for the term.
6. If you have created a logical definition for your term, you can delete the asserted ```is_a``` parent in the ‘subclass of’ section. Once you synchronize the reasoner, you will see the automated classification of your new term. If the inferred classification doesn’t make sense, then you will need to modify the logical definition.

	
7. In some cases such as ```part_of``` relations based on external partonomies, it might be necessary to assert the ```part_of``` relationships.

8. Save the file and ___return to your terminal window___. Then, type: ```git status```. This will confirm which file has been modified.

9. To see how the branch was modified, type: ```git diff```. In this case, ejp-rd-edit.owl was modified. 

10. Then from the terminal run the command sh run.sh make IMP=false prepare_release -B 

11. Open the ejp-rd.owl in the EJP-ontology folder (note: not the one in the ontology folder) and confirm the change is effected 

   
