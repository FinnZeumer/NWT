# NuWoTra (Nutritions & Workout - Tracker)

Aim of the sotware will be the gathering and tracking of nutitonal as well as fitniss data of the user and the statistical analysis of the data.

This project will be open source. It will be primaraly coded in python and c++

# Table of Contents

# Project Structure

# Nutitional/Food Tracking

On aprt of the application will focus on the nutritions a user takes in per day. Aim is to collect all nutritions not just the macros. This is where the Food Nutrition Aggregator will be used. 

Later on, the software will give the user feedback on what nutritions they may lack on and which might be overconsumed. This is where the Food Nutrion Analyser will be used. 

For both, the Aggregator and the Analyser, the software will collect information form opensource online databases.

## Food Nutrition Aggregator

The Aggregator is meant to collect information about all nutritions/components in (basic) foods. The data will be collected form different sources. There will be an hirachy for the diffrent foods and their realiability. 

The user can then search for a food, the application will collect the data for the searched food from diffrent sources and create one food from them. The diffrent sources are meant to complement each other. If there are multiple sources for one component, these will be combinded to one entrince, also containing the statistical uncertanty.

### Planned Features 

#### In Progress (Prio 1)
- [] collecting data from public databases using api calls
    - [] USDA FoodData
    - [] FooDB
    - [] Swiss Food
- [] Normalized Food Dataframe (food class)
- [] Normalizing units to g/100g
- [] Statistical Aggregation   

#### Ideas (Prio 2)
- [] Export 


### Sources/Databases 

| Database | URL              | Prio |
| -------- | ---------------- | ---- |
| **USDA** | fdc.nal.usda.gov |   1  |


## Food Nutrition Analyser

Let the user search for a food and add how much (weight) of the food he ate. Collect and safe the data. On the end of each week the software will compare the intake to the recommend intake. The analyser will also look for sex, bodyweight and bodyfat as well as body height. Thus, the user will have an "user". 

## Blood Analyser

Later on, the user will be also able to upload/enter official blood values and the software will compare the tracked intake with the actual absorpted nutritions and will calculated an (estimated) personal absorption rate for an food. This can then be used for future nutrition analysing. 

# Workout Tracking
--> Coming Soon

The user will also be able to track their workouts (meaning what exercises, how many sets and how much weight etc).

# Scientific Data Collection
--> Coming Soon

Later on, users will be able to voluntaraly submit their data anonimously to a public database. The application will collect all user data and does an statistical analasis on them. 
