# This is a modified version of Web of Science Categories script. The sections marked with 'EXPERIMENTAL' tag
# are additions on the original script.

# This file is a demonstration of the RDF behavior that leads to automatic creation of instances in cases
# where an instance-class relationship is asserted (i.e., if "Some_Instance_A ---someProperty_B--> SomeClassC"
# then an instance "Some_Instance_C" is created automatically from SomeClassC).

# This demonstrates the RDF behavior that instances can only be connected to classes with rdf:type property;
# all other instance-class connections have to mediated by an instance of the class that the instance is being related to.
# In other words, this means that instances can only be connected to instances except in the case of rdf:type of property.

# TODO: Add class-suclass structure for WOS categories
from x_common_functions import *

wos_categories_list=["Acoustics","AgriculturalEconomicsandPolicy","AgriculturalEngineering","AgricultureDairyandAnimalScience","AgricultureMultidisciplinary","Agronomy","Allergy","AnatomyandMorphology","Andrology","Anesthesiology","Anthropology","Archaeology","Architecture","AreaStudies","Art","AsianStudies","AstronomyandAstrophysics","AutomationandControlSystems","BehavioralSciences","BiochemicalResearchMethods","BiochemistryandMolecularBiology","BiodiversityConservation","Biology","Biophysics","BiotechnologyandAppliedMicrobiology","Business","BusinessFinance","CardiacandCardiovascularSystems","CellandTissueEngineering","CellBiology","ChemistryAnalytical","ChemistryApplied","ChemistryInorganicandNuclear","ChemistryMedicinal","ChemistryMultidisciplinary","ChemistryOrganic","ChemistryPhysical","Classics","ClinicalNeurology","Communication","ComputerScienceArtificialIntelligence","ComputerScienceCybernetics","ComputerScienceHardwareandArchitecture","ComputerScienceInformationSystems","ComputerScienceInterdisciplinaryApplications","ComputerScienceSoftwareEngineering","ComputerScienceTheoryandMethods","ConstructionandBuildingTechnology","CriminologyandPenology","CriticalCareMedicine","Crystallography","CulturalStudies","Dance","Demography","DentistryOralSurgeryandMedicine","Dermatology","DevelopmentalBiology","Ecology","Economics","EducationandEducationalResearch","EducationScientificDisciplines","EducationSpecial","Electrochemistry","EmergencyMedicine","EndocrinologyandMetabolism","EnergyandFuels","EngineeringAerospace","EngineeringBiomedical","EngineeringChemical","EngineeringCivil","EngineeringElectricalandElectronic","EngineeringEnvironmental","EngineeringGeological","EngineeringIndustrial","EngineeringManufacturing","EngineeringMarine","EngineeringMechanical","EngineeringMultidisciplinary","EngineeringOcean","EngineeringPetroleum","Entomology","EnvironmentalSciences","EnvironmentalStudies","Ergonomics","Ethics","EthnicStudies","EvolutionaryBiology","FamilyStudies","FilmRadioTelevision","Fisheries","Folklore","FoodScienceandTechnology","Forestry","GastroenterologyandHepatology","GeneticsandHeredity","GeochemistryandGeophysics","Geography","GeographyPhysical","Geology","GeosciencesMultidisciplinary","GeriatricsandGerontology","Gerontology","HealthCareSciencesandServices","HealthPolicyandServices","Hematology","History","HistoryandPhilosophyofScience","HistoryofSocialSciences","Horticulture","HospitalityLeisureSportandTourism","HumanitiesMultidisciplinary","ImagingScienceandPhotographicTechnology","Immunology","IndustrialRelationsandLabor","InfectiousDiseases","InformationScienceandLibraryScience","InstrumentsandInstrumentation","IntegrativeandComplementaryMedicine","InternationalRelations","LanguageandLinguistics","Law","Limnology","Linguistics","LiteraryReviews","LiteraryTheoryandCriticism","Literature","LiteratureAfricaAustralianCanadian","LiteratureAmerican","LiteratureBritishIsles","LiteratureGermanDutchScandinavian","LiteratureRomance","LiteratureSlavic","Management","MarineandFreshwaterBiology","MaterialsScienceBiomaterials","MaterialsScienceCeramics","MaterialsScienceCharacterizationandTesting","MaterialsScienceCoatingsandFilms","MaterialsScienceComposites","MaterialsScienceMultidisciplinary","MaterialsSciencePaperandWood","MaterialsScienceTextiles","MathematicalandComputationalBiology","Mathematics","MathematicsApplied","MathematicsInterdisciplinaryApplications","Mechanics","MedicalEthics","MedicalInformatics","MedicalLaboratoryTechnology","MedicineGeneralandInternal","MedicineLegal","MedicineResearchandExperimental","MedievalandRenaissanceStudies","MetallurgyandMetallurgicalEngineering","MeteorologyandAtmosphericSciences","Microbiology","Microscopy","Mineralogy","MiningandMineralProcessing","MultidisciplinarySciences","Music","Mycology","NanoscienceandNanotechnology","Neuroimaging","Neurosciences","NuclearScienceandTechnology","Nursing","NutritionandDietetics","ObstetricsandGynecology","Oceanography","Oncology","OperationsResearchandManagementScience","Ophthalmology","Optics","Ornithology","Orthopedics","Otorhinolaryngology","Paleontology","Parasitology","Pathology","Pediatrics","PeripheralVascularDisease","PharmacologyandPharmacy","Philosophy","PhysicsApplied","PhysicsAtomicMolecularandChemical","PhysicsCondensedMatter","PhysicsFluidsandPlasmas","PhysicsMathematical","PhysicsMultidisciplinary","PhysicsNuclear","PhysicsParticlesandFields","Physiology","PlanningandDevelopment","PlantSciences","Poetry","PoliticalScience","PolymerScience","PrimaryHealthCare","Psychiatry","Psychology","PsychologyApplied","PsychologyBiological","PsychologyClinical","PsychologyDevelopmental","PsychologyEducational","PsychologyExperimental","PsychologyMathematical","PsychologyMultidisciplinary","PsychologyPsychoanalysis","PsychologySocial","PublicAdministration","PublicEnvironmentalandOccupationalHealth","RadiologyNuclearMedicineandMedicalImaging","Rehabilitation","Religion","RemoteSensing","ReproductiveBiology","RespiratorySystem","Rheumatology","Robotics","SocialIssues","SocialSciencesBiomedical","SocialSciencesInterdisciplinary","SocialSciencesMathematicalMethods","SocialWork","Sociology","SoilScience","Spectroscopy","SportSciences","StatisticsandProbability","SubstanceAbuse","Surgery","Telecommunications","Theater","Thermodynamics","Toxicology","Transplantation","Transportation","TransportationScienceandTechnology","TropicalMedicine","UrbanStudies","UrologyandNephrology","VeterinarySciences","Virology","WaterResources","WomensStudies","Zoology"]

# namespace prefixes
sr   = "http://clokman.com/ontologies/scientific-research#"
wsc = "http://clokman.com/ontologies/web-of-science-categories#"
rdf  = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
owl  = "http://www.w3.org/2002/07/owl#"

#add_prefix_triple("",     wsc)
#add_prefix_triple("sr",   sr)
#add_prefix_triple("rdf",  rdf)
#add_prefix_triple("rdfs", rdfs)
#add_prefix_triple("owl",  owl)

#add_triple("<http://clokman.com/ontologies/web-of-science-categories>", "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "http://www.w3.org/2002/07/owl#Ontology")

# classes and properties
c_class        = construct_uri(rdfs, "Class")
p_subclass_of  = construct_uri(rdfs, "subClassOf")

c_scientific_field = construct_uri(sr, "ScientificField")
#trpl(c_scientific_field + " " + p_rdf_type + " " + c_class + " .")

### EXPERIMENTATION #############################################
p_rdf_type         = construct_uri(rdf, "type"               )
c_named_individual = construct_uri(owl,  "NamedIndividual"   )
c_object_property  = construct_uri(owl,  "ObjectProperty"    )
add_triple(p_rdf_type, p_rdf_type, c_object_property)
add_triple(c_named_individual, p_rdf_type, c_class)
add_triple(c_object_property, p_rdf_type, c_class)
add_triple(c_class, p_rdf_type, c_class)
################################################################

i_test_instance = construct_uri(sr, "Test_Instance")
p_some_property = construct_uri(sr, "someProperty")
add_triple(i_test_instance, p_rdf_type, c_named_individual)
add_triple(p_some_property, p_rdf_type, c_object_property)

for each_category in wos_categories_list:
    c_current_wos_category = construct_uri(wsc, each_category)
    add_triple(c_current_wos_category, p_subclass_of, c_scientific_field)

    ### EXPERIMENTATION ################################################
    # This should automatically create instances for c_current_wos_category (i.e., the equivalent of i_current_wos_category):
    add_triple(i_test_instance, p_some_property, c_current_wos_category)
    ####################################################################

from pprint import pprint
pprint(triples_list)

# IMPORTANT: CHANGE FILE NAME WITH EACH NEW VERSION IF THE FILE IS TO BE IMPORTED TO PROTEGE.
# Protege does not always understand that this is a new file if the file name is the same with a previously imported file.
file_obj = open("Output/web_of_science_categories_0.2.4-test2.ttl", "w")
for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')