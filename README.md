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

    This program should show dashboard displaying histograms of data collected from ventilators in the NICU
    It needs to show data for kids under 36 weeks of age and on O2
    It should show histograms of data for a variable amount of time. (1hr, 2hrs, 4hrs, current shift, 8 hrs, 12hrs, 24 hrs, 48 hrs, 72hrs)
    Dashboard needs to accomodate 50 Histograms, but there could be up to 90 beds to tack
    Dashboard should enable the ability to locate bad histograms and identify which bed they represent.
    The histograms should be displayed in the following order: Low sat bad histograms, the high sat bad histograms, then good histograms
    The dashboard should be made up of pages of 6-8 histograms
    If someone clicks on a histogram image, the image is enlarged
    The user should be able to go back in time and grab data for events from a long time ago (exported to a file type, not creating histograms).

## 6 Exemplary Use Cases

## 7 Nonfunctional Requirements

### 7.1 Usability

### 7.2 Reliability

### 7.3 Performance

### 7.4 Supportability

### 7.5 Other Requirements

#### 7.5.1 Applicable Standards

#### 7.5.2 System Requirements

#### 7.5.3 Licensing, Security, and Installation

## 8 Documentation Requirements

### 8.1 User Manual

### 8.2 Online Help

### 8.3 Installation Guides, Configuration, “Read Me” File

### 8.4 Labeling and Packaging

## 9 Glossary

