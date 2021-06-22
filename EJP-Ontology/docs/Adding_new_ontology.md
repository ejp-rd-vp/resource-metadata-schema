# Adding new ontology to EJP-RD
```
```
### Adding New Ontology to EJP-RD Ontology

Terms are imported to EJP-RD from other ontologies, but not all terms from external ontologies are imported. Occasionally, you will find that a valid identifier exists in an external ontology, but the identifier is not available in Protege because that term is not yet imported. To import a term from an external ontology:

1. Gitclone the repository on your local machine, and navigate to the clone repository of EJP-Ontology i.e from the command line run - git clone https://github.com/EBISPOT/EJP-Ontology.git	

2. Navigate to the ontology folder in the EJP-Ontology folder 

3. Open the ejp-rd-odk.yaml file with any text editor e.g. Atom or Sublime

4. Add the new ontology's prefix after line 28 of the import_group section i.e. at end of line 28 hit enter to go line 29 e.g. if you want to add a new ontology called uberon : add the following and hit enter  : 
	-id: uberon 
5. In line 30 enter the url for the ontology download e.g. for the uberon ontology - 
	mirror_from: https://www.ebi.ac.uk/ols/ontologies/uberon/download

6. In the components section go to the end of the line which in this case will be line 47 and hit enter to go to line 48, and type the following : 
	-filename: uberon.owl  (put the name of your desired ontology there instead)
	
7. Save the file and exist. 

8. Go to the terminal and navigate to the ontology-development-kit folder (note: always update your odk first to be sure its up-to-date by running the command  docker pull obolibrary/odkfull) 

9. Run the command  sh upgrade_ejp-rd.sh 

10. Change Directory to the EJP-Ontology/src/ontology folder and open the makefile to confirm the addition of the new ontology to the makefile import statement and mirror trigger section 

11. The terms from the new ontology must be added to the third column of ejp-rd_seed_tab.tsv in the curation folder (for easy operation , open the file with a spreadsheet application like MS-Excel and add the new terms from the ontology to the terms in the third column at the end of the column safe file and exist). 

12. Go back to the terminal while still in the EJP-Ontology/src/ontology and run the command sh run.sh make MIR=true all_components -B  , this will create all the components

13. Then run the command  
