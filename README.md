# AI-Enhanced Career Guidance System for Personalized Career Pathways

## 📌 Project Overview

The **AI-Enhanced Career Guidance System** is a terminal-based application that helps students and professionals discover suitable career pathways based on their skills, abilities, interests, and career goals.

The system analyzes the user's skill profile, recommends suitable careers, identifies skill gaps, and generates a personalized learning roadmap.

This project is developed under the **Smart Education** domain and is based on the problem statement provided by the **Ministry of Skill Development and Entrepreneurship (MSDE)** and the **National Council for Vocational Education and Training (NCVET)**.

---

## 🎯 Problem Statement

Choosing the right career can be difficult for students and professionals. Traditional career guidance methods may not fully consider an individual's:

- Aptitude
- Interests
- Aspirations
- Skills
- Abilities
- Work experience
- Long-term career goals

As a result, users may not know which career suits them, what skills they are missing, or how to progress toward their desired career.

This project aims to solve this problem by providing personalized career recommendations and structured learning pathways through an AI-enhanced career guidance system.

---

## 💡 Proposed Solution

The system accepts the user's skill levels and analyzes their profile to recommend suitable career options.

The user can then select a recommended career for detailed analysis. The system identifies the user's strengths, compares their skills with the requirements of the selected career, and generates a personalized learning roadmap.

### The system provides:

1. Skill-based career recommendations
2. Career match percentages
3. Strong skill identification
4. Skill-gap analysis
5. Personalized learning roadmaps
6. Interactive terminal-based input

---

## ✨ Key Features

### 1. Interactive Skill Assessment

The user enters skill levels between **0 and 10**.

The current system evaluates skills such as:

- Python
- SQL
- Mathematics
- Statistics
- Machine Learning
- Data Visualization
- Communication

### 2. Career Recommendations

The system analyzes the user's skill profile and recommends suitable career options.

Each career is displayed with a match percentage.

### 3. Career Selection

The user can select one of the recommended careers for detailed analysis.

### 4. Skill-Gap Analysis

The system compares the user's current skills with the skills required for the selected career.

It displays:

- Strong skills
- Missing skills
- Current skill levels
- Required skill levels

### 5. Personalized Learning Roadmap

The system generates learning steps to help the user improve missing skills and progress toward the selected career.

### 6. Terminal-Based Application

The complete application runs in the terminal using Python. No web browser or frontend is required.

---

## 🔄 System Workflow

```text
Start Application
       |
       v
Enter Skill Levels
       |
       v
Create User Skill Profile
       |
       v
Analyze Skills
       |
       v
Display Career Recommendations
       |
       v
Select a Career
       |
       v
Perform Skill-Gap Analysis
       |
       v
Generate Personalized Roadmap
       |
       v


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cshanmukha777/ai-career-guidance-system.git
```

### 2. Move Into the Project Directory

```bash
cd ai-career-guidance-system
```

### 3. Check Python Installation

```bash
python3 --version
```

### 4. Run the Application

```bash
python3 -m backend.main
```