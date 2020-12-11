# Vision Document
### Software Engineering Group 27
### Vision Document for Capstone Project
### (C) 2020 Group 27

## Revision History
| Date | Revision | Description | Author |
| :--: | :--: | :--: | :--: |
| 12/7/20 | 1.0 | Initial Version | Matt Edgar, Brodie Gullic, Newsee Patel, Nathan Preuss |
| | | | |
| | | | |

## 1 Introduction

This section provides an overview of the vision document: its contents and its purpose.

### 1.1 Purpose

This document outlines the process of coming up with a proof-of-concept dashboard for displaying histograms of data collected from ventilators in the NICU in EPIC for nurses to determine if certain infants' (under 36 weeks of age) oxygen saturation is too high.

### 1.2 Solution Overview

This document outlines the implementation of this dashboard.

Currently, there are Phillips Monitors that record oxygen saturation data for each infant. The hospital does not use EPIC but is planning to transfer to the system in the near future, so the proof of concept would be able to integrate with this software. The implementation would take the data from the monitors and track it into an application, where it would display graphs and clearly show which infants have oxygen levels above (and below) the safe levels. This application must be accessible from a desktop computer.


### 1.3 References

The Using Health Information Data Strategies to Support Efforts of Sustainability sent to us by Dr. Jabrzemski, as well as Brandon Kuehne and Kimberly Ernst, who helped determine requirements for the project and determine what success looks like.

## 2 User Description

### 2.1 User/Market Demographics

The user demographics will be nurses and supervisors working in the hospital. Potentially this could be brought to market as software for hospitals to purchase, but that is out-of-scope for this assignment. We don't have any specific target demographics, as this product is being made in-house for this specific hospital, but we want to make sure that the needs are met for the hospital. Specifically making sure that our product could be theoretically implemented into EPIC and that it's well documented, so a future team can implement it successfully without confusion.

### 2.2 User Personas

Nurses must be able to see if any infants have too high of oxygen saturation easily to be able to fix the probelm. Supervisors must be able to view past data to determine what nurses are administering too much oxygen and help notify them to fix this issue. Both of these people work in a high stress environment where visibility is key to make sure that solutions are easy to understand and allow quick action. Nurses particularly need to make sure all of their patients are stable and doing well and can get distracted by call buttons in rooms. Their version of success is nothing requiring their urgent attention. For supervisors, it would be making sure that nurses perform their responsibilities and hearing patient complaints. For our product, these patients can't complain, so it is important we vocalize their needs

### 2.3 User Environment

For nurses, this application would sit on a desktop computer / Monitor and would be visible in the NICU, to have clear visibility. Several nurses should pass by, so it should be visible by a casual glance for a nurse to determine if an infant's oxygen saturation is too high (or low). This application will also in the future have to integrate with EPIC, so it should be considered while designing the project.

### 2.4 Key User Needs

Currently, nurses cannot easily determine if an infant's oxygen saturation is too high. For low saturation, they have a buzzer on their person that will tell them to increase. This is not done for high saturation, as it is only dangerous in the long-term. This is why it needs to be visible for nurses, as it is not severely urgent for nurses to be immediately notified but should be fixed when nurses have time or plan to go into the NICU.
 
### 2.5 Alternatives and Competition

Currently there is no known competition for this project, as the hospital would not have come to us for a solution otherwise for a capstone project. This is why they need a custom built solution for their needs, so they are able to address unique concerns for their patients.

## 3 Stakeholders

| Stakeholder | Involvement | Needs |
| ---- | ---- | ----|
| Nurse | Uses the system constantly to evaluate vitals | Fast, easy access to data |
| Supervisor | Uses it occasionally to determine that NICU patient have good Oxygen Saturation over time | Long-term visualization of data, to see which patients have had bad oxygen saturation |

## 4 Product Overview

This section will provide a high level overview of the solution capabilities of our proof-of-concept dashboard.

### 4.1 Product Perspective

This product, while yet a proof-of-concept, will eventually by integrated into the EPIC Healthcare Data Management Platform.  The interfaces for this move are currently unknown, and those that come after us will have to manage the move to EPIC.  Until then, this project is a stand alone application with an attached SQL database to store test data.

### 4.2 Product Position Statement

|For | Healthcare workers in the NICU at The Children's Hospital |
|----|----|
|Who | Want a dashboard to show O2 levels of babies under 36 weeks on O2 to increase workflow efficiency of the nurses|
| The proof-of-concept dashboard | Is a stand-alone application|
| That | Will increase efficiency of diagnoses of BPD and make the workflows more efficient |
| Unlike | the current inefficient workflow. |
| Our product | will save time and resources for the hospital compared to the current method |

### 4.3 Summary of Capabilities

| Feature | Benefit |
| ----- | ---- |
| Dashboard | Health care workers can look at all the O2 data from one place, instead of their current inefficient workflow |
| Histograms | The program will make histrograms of O2 levels for babies that fit the criteria, so that nurses can look at all of them in one place, versus going around to each bed to look at similar histograms | 
| Time variability | The user can set which time period they want to create histograms for, or even export data from a long time ago to a different file format to use in research | 

### 4.4 Assumptions and Dependencies

We are assuming that the hospital stores their healthcare data in some sort of SQL database.
We are assuming that we do not need to worry about HIPPA requirements right now.

### 4.5 Cost and Pricing

Our budget is some GCP credits.
This product will be free.

## 5 Product Features

### 5.1 Dashboard

This program should show dashboard displaying histograms of data collected from ventilators in the NICU.  It should contain pages of 6-8 histograms sorted by low sat bad histograms, high sat bad histograms, followed by normal histograms.

### 5.2 Histograms

The histograms will show a histogram of O2 data for kids under 36 weeks of age and on O2 from the database.  The user should have the option to customize the timeframe for the data.  The histograms will also display which bed they are from.  When clicked on, the histogram will enlarge in size.

## 6 Exemplary Use Cases

#### 1
Dashboard of histogram can help medical staff track many kids in a very less amount of time. This will help to track any kid who needs more attention than others and make it more efficient.

#### 2 
Another use of this system would be to access data of oxygen level at different point of times, this can help medical team assess the condition of the kids and help them treat better.

#### 3 
The system can aslo be used to find records that are not in the dashboard, for example something from like 2 years ago or so. This can help to access a patient's data if they need for their medical history or some other purpose.

## 7 Nonfunctional Requirements

### 7.1 Usability

Dashboard will contain 50 histograms, with each page accomodating 6-8 histograms.

### 7.2 Reliability

Histograms should display oxygen level data in different periods of time, it should be ready with all data collected when needed by medical staff.

### 7.3 Performance

The program should be fast but accurate with the results of data and histograms, and should have ability to deal with problems displaying as it be a huge factor in an emergency.

### 7.4 Supportability

The access to the program should be available to authorized medical staff whenever needed.

### 7.5 Other Requirements

#### 7.5.1 Applicable Standards

The program should comply with the standards of the hospital, NH, and HIPPA.

#### 7.5.2 System Requirements

To make it secure, the program should only run on authorized hospital networks, and able to connect to other conected software of the hospital.

#### 7.5.3 Licensing, Security, and Installation

In order to avoid any legal or privacy issues, the software will be licensed as needed.

## 8 Documentation Requirements

### 8.1 User Manual

This project will eventually require a complete user manual for non-technical hospital staff who will be using the software. As the dashboard is small, this should only be a few pages long and have complete descriptions of the menus and the features.

It will be distributed as a PDF which can both be accessed in the files near the dashboard and from the dashboard itself, under a HELP section.

### 8.2 Online Help

Both for security and simplicity, this software should not be connected to the internet and because this, will not offer any Online Help other than what is found within the software itself.

### 8.3 Installation Guides, Configuration, “Read Me” File

Installation of this software should be simple, involving simply running a single executable. From there, the process should either be automatic or call up a wizard when users need to make selections.

There needs to be configuration options for acquiring the data that the dashboard will run, however, which may be set up during installation or at a later date.

The "Read Me" file should include installation instructions, guidance on setting up data acquisition, and a list of currently known bugs.

### 8.4 Documentation

As this project is one that will be done over the course of years by multiple teams, it is critical that excellent documentation be upheld. In addition to clear and complete requirements included with this project, we will also need to include a document explaining the high-level structure of the dashboard.

All of the code written for this project must include useful and complete documentation as well.

### 8.5 Labeling and Packaging

As this project is a dashboard, it will require a cohesive and clean UI. For the icon, it should also be used on the dashboard as well.

## 9 Glossary

BPD - Bronchopulmonary Dysplasia; a chronic lung issue that can affect newborns, particularly those on supplemental oxygen

HIPAA - Health Insurance Portability and Accountability Act; law requires certain standards be met when dealing with health data

Histograms - A form of bar graph showing trends over time

NICU - Neonatal Intensive Care Unit

O2 - Oxygen
