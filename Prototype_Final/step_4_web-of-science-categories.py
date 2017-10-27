# TODO: Add class-suclass structure for WOS categories
from x_common_functions import *

wos_categories_list=["Acoustics","AgriculturalEconomicsandPolicy","AgriculturalEngineering","AgricultureDairyandAnimalScience","AgricultureMultidisciplinary","Agronomy","Allergy","AnatomyandMorphology","Andrology","Anesthesiology","Anthropology","Archaeology","Architecture","AreaStudies","Art","AsianStudies","AstronomyandAstrophysics","AutomationandControlSystems","BehavioralSciences","BiochemicalResearchMethods","BiochemistryandMolecularBiology","BiodiversityConservation","Biology","Biophysics","BiotechnologyandAppliedMicrobiology","Business","BusinessFinance","CardiacandCardiovascularSystems","CellandTissueEngineering","CellBiology","ChemistryAnalytical","ChemistryApplied","ChemistryInorganicandNuclear","ChemistryMedicinal","ChemistryMultidisciplinary","ChemistryOrganic","ChemistryPhysical","Classics","ClinicalNeurology","Communication","ComputerScienceArtificialIntelligence","ComputerScienceCybernetics","ComputerScienceHardwareandArchitecture","ComputerScienceInformationSystems","ComputerScienceInterdisciplinaryApplications","ComputerScienceSoftwareEngineering","ComputerScienceTheoryandMethods","ConstructionandBuildingTechnology","CriminologyandPenology","CriticalCareMedicine","Crystallography","CulturalStudies","Dance","Demography","DentistryOralSurgeryandMedicine","Dermatology","DevelopmentalBiology","Ecology","Economics","EducationandEducationalResearch","EducationScientificDisciplines","EducationSpecial","Electrochemistry","EmergencyMedicine","EndocrinologyandMetabolism","EnergyandFuels","EngineeringAerospace","EngineeringBiomedical","EngineeringChemical","EngineeringCivil","EngineeringElectricalandElectronic","EngineeringEnvironmental","EngineeringGeological","EngineeringIndustrial","EngineeringManufacturing","EngineeringMarine","EngineeringMechanical","EngineeringMultidisciplinary","EngineeringOcean","EngineeringPetroleum","Entomology","EnvironmentalSciences","EnvironmentalStudies","Ergonomics","Ethics","EthnicStudies","EvolutionaryBiology","FamilyStudies","FilmRadioTelevision","Fisheries","Folklore","FoodScienceandTechnology","Forestry","GastroenterologyandHepatology","GeneticsandHeredity","GeochemistryandGeophysics","Geography","GeographyPhysical","Geology","GeosciencesMultidisciplinary","GeriatricsandGerontology","Gerontology","HealthCareSciencesandServices","HealthPolicyandServices","Hematology","History","HistoryandPhilosophyofScience","HistoryofSocialSciences","Horticulture","HospitalityLeisureSportandTourism","HumanitiesMultidisciplinary","ImagingScienceandPhotographicTechnology","Immunology","IndustrialRelationsandLabor","InfectiousDiseases","InformationScienceandLibraryScience","InstrumentsandInstrumentation","IntegrativeandComplementaryMedicine","InternationalRelations","LanguageandLinguistics","Law","Limnology","Linguistics","LiteraryReviews","LiteraryTheoryandCriticism","Literature","LiteratureAfricaAustralianCanadian","LiteratureAmerican","LiteratureBritishIsles","LiteratureGermanDutchScandinavian","LiteratureRomance","LiteratureSlavic","Management","MarineandFreshwaterBiology","MaterialsScienceBiomaterials","MaterialsScienceCeramics","MaterialsScienceCharacterizationandTesting","MaterialsScienceCoatingsandFilms","MaterialsScienceComposites","MaterialsScienceMultidisciplinary","MaterialsSciencePaperandWood","MaterialsScienceTextiles","MathematicalandComputationalBiology","Mathematics","MathematicsApplied","MathematicsInterdisciplinaryApplications","Mechanics","MedicalEthics","MedicalInformatics","MedicalLaboratoryTechnology","MedicineGeneralandInternal","MedicineLegal","MedicineResearchandExperimental","MedievalandRenaissanceStudies","MetallurgyandMetallurgicalEngineering","MeteorologyandAtmosphericSciences","Microbiology","Microscopy","Mineralogy","MiningandMineralProcessing","MultidisciplinarySciences","Music","Mycology","NanoscienceandNanotechnology","Neuroimaging","Neurosciences","NuclearScienceandTechnology","Nursing","NutritionandDietetics","ObstetricsandGynecology","Oceanography","Oncology","OperationsResearchandManagementScience","Ophthalmology","Optics","Ornithology","Orthopedics","Otorhinolaryngology","Paleontology","Parasitology","Pathology","Pediatrics","PeripheralVascularDisease","PharmacologyandPharmacy","Philosophy","PhysicsApplied","PhysicsAtomicMolecularandChemical","PhysicsCondensedMatter","PhysicsFluidsandPlasmas","PhysicsMathematical","PhysicsMultidisciplinary","PhysicsNuclear","PhysicsParticlesandFields","Physiology","PlanningandDevelopment","PlantSciences","Poetry","PoliticalScience","PolymerScience","PrimaryHealthCare","Psychiatry","Psychology","PsychologyApplied","PsychologyBiological","PsychologyClinical","PsychologyDevelopmental","PsychologyEducational","PsychologyExperimental","PsychologyMathematical","PsychologyMultidisciplinary","PsychologyPsychoanalysis","PsychologySocial","PublicAdministration","PublicEnvironmentalandOccupationalHealth","RadiologyNuclearMedicineandMedicalImaging","Rehabilitation","Religion","RemoteSensing","ReproductiveBiology","RespiratorySystem","Rheumatology","Robotics","SocialIssues","SocialSciencesBiomedical","SocialSciencesInterdisciplinary","SocialSciencesMathematicalMethods","SocialWork","Sociology","SoilScience","Spectroscopy","SportSciences","StatisticsandProbability","SubstanceAbuse","Surgery","Telecommunications","Theater","Thermodynamics","Toxicology","Transplantation","Transportation","TransportationScienceandTechnology","TropicalMedicine","UrbanStudies","UrologyandNephrology","VeterinarySciences","Virology","WaterResources","WomensStudies","Zoology"]

# namespace prefixes
sr   = "http://clokman.com/ontologies/scientific-research#"
wsc  = "http://clokman.com/ontologies/web-of-science-categories#"
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


for each_category in wos_categories_list:
    c_current_wos_category = construct_uri(wsc, each_category)
    add_triple(c_current_wos_category, p_subclass_of, c_scientific_field)


from pprint import pprint
pprint(triples_list)

# IMPORTANT: CHANGE FILE NAME WITH EACH NEW VERSION IF THE FILE IS TO BE IMPORTED TO PROTEGE.
# Protege does not always understand that this is a new file if the file name is the same with a previously imported file.
file_obj = open("Output/web_of_science_categories_0.2.5.ttl", "w")
for each_triple in triples_list:
    file_obj.write(each_triple)
    file_obj.write('\n')
