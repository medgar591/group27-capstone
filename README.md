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

### 1.2 Solution Overview

#### 1.2.1 Hatsune Miku Singing the Text on The Webiste

#### 1.2.2 Hatsune Miku as a Search Bar

### 1.3 References

## 2 User Description

### 2.1 User/Market Demographics

### 2.2 User Personas

### 2.3 User Environment

### 2.4 Key User Needs
 
### 2.5 Alternatives and Competition

## 3 Stakeholders

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

### 8.2 Online Help

### 8.3 Installation Guides, Configuration, “Read Me” File

### 8.4 Labeling and Packaging

## 9 Glossary

