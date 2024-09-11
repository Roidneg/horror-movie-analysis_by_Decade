# horror-movie-analysis_by_Decade
Using data from Evan Gower  via Kaggle, I investigate the horror genre's popularity from 1950 up to 2020
Horror Movie Analysis
Overview

This project analyzes the popularity of horror movies from the 1950s to the 2020s using data from IMDb. The primary goal is to explore trends in the genre's popularity over the decades, identify standout films, and understand shifts in audience preferences.
Dataset

The dataset used in this analysis was sourced from Kaggle. It includes information on horror movies such as titles, genres, release dates, and popularity metrics, covering films from various decades up to the early 2020s.
Objectives

    Analyze Popularity Trends: Investigate how the popularity of horror movies has evolved over the decades.
    Identify Key Contributors: Highlight specific films or periods that contributed significantly to changes in popularity.
    Understand Data Anomalies: Address data inconsistencies, such as outlier years with unusually high popularity scores, and refine the analysis for balanced insights.

Key Findings

    The popularity of horror movies has fluctuated over the decades, with notable peaks in the 2000s.
    Recent data (2020s) initially showed unusually high popularity, likely influenced by the increased accessibility of streaming services and social media impact.
    Adjusting the analysis to exclude incomplete data from 2021 and 2022 provided a more balanced view, highlighting trends up to 2020.

Analysis Workflow

    Data Preparation:
        Data was loaded and filtered to include only horror movies.
        Missing values were handled, and relevant columns were selected.
        Release dates were converted to datetime format, and movies were grouped by decade.
    Visualization:
        Plotted the average popularity of horror movies by decade using Matplotlib, highlighting key trends and anomalies.
    Further Investigation:
        Analyzed specific years and movies contributing to trends, particularly focusing on the high popularity scores in the early 2020s.

How to Run the Analysis

    Clone the repository:

    bash

git clone https://github.com/your-username/horror-movie-analysis.git

Navigate to the project directory:

bash

cd horror-movie-analysis

Install the required dependencies:

bash

pip install -r requirements.txt

Run the analysis script:

bash

    python analysis_script.py

Future Work

    Extend the analysis to include sentiment analysis on horror movie reviews.
    Incorporate additional metrics like box office revenue or critical reception to enrich the analysis.
    Explore the impact of sub-genres within horror to see how specific types have trended over time.

Contributions

Contributions are welcome! Please feel free to fork this repository and submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    Kaggle for providing the dataset.
    Matplotlib and Pandas libraries for data visualization and manipulation.
