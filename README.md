# Introduction

__HireSight__ : AI-powered hiring platform that helps companies hire the best candidates faster. Features resume parsing, video interview analysis, personality prediction, and automated candidate screening.

## Objective

- Application to automate the hiring process
- Personality prediction using ML
- Check confidence and other traits using video and tone analysis
- Send mail to selected/rejected candidates automatically in one-click
- Fast recruitment in larger numbers
- Generate concise insights and provide summary of the candidate's profile
- Handy application for HR/Recruiting Team

## Project Workflow
- Interviewee
     - Enter personal details, upload resume, attempt a questionnaire wherein the candidate has to rate himself/herself
     - Personality prediction (based on [Big Five Personality Traits](https://www.thomas.co/resources/type/hr-guides/what-are-big-5-personality-traits) model) with OCEAN values and CV analysis
     - Video recording in browser. The candidate has to answer few questions put up by the HR team on the portal.
     - Face emotion and Speech Analysis to get insights like confidence level, candidate personality traits
     
- Interviewer/HR team/Admin
     - View all the registered candidates’ details
     - View each candidate's profile summary which includes resume, responses to questions, technical skills, personality traits, video and tone analysis result.
     - Update candidate about selection/rejection, further interview process using one-click mail or phone call

## Presentation Slides



<br>

_Though most of the features has been added, yet the complete process is not yet automated as this application is made for RedCode 3.0 Hackathon.
<br>

# Installation Guide
This project requires the following tools to get started:

- Python - The programming language used by Flask.
- MySQL -  A relational database management system based on SQL.
- Virtualenv - A tool for creating isolated Python environments.
- VSCode - A lightweight source code editor which can be used to view, edit, run, and debug source code for applications. You can optionally use any other code editor of your choice such as Sublime Text or Atom.
- AWS Account - A subsidiary of Amazon providing on-demand cloud computing platforms and APIs. 

To get started, install Python and MySQL on your local computer if you don't have them already.

Also, create an AWS Free Tier account, if you don't have it. Services like Amazon S3 and Amazon Transcribe API will be used in this project.
