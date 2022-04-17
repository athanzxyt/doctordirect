# Doctor Direct

#### Doctor Direct aims to directly connect potential patients with the CORRECT medical professional for them, regardless of whatever particular need they have, saving valuable time for all parties.

## Inspiration
We drew inspiration for this problem after hearing constant complaints from our parents about finding a doctor. A few common complaints always arose: "It always takes so long to get a doctor" and "It's never the right doctor." With a little bit of research into the healthcare industry, we realized there was a _real_ problem with the medical system. Medical professionals are often understaffed, and time becomes increasingly valuable for both patients and medical professionals. Additionally, we found that a common waste of time in the healthcare industry, we **improper** appointments, a.k.a. people going to the wrong doctor. Thus, we created DoctorDirect to **solve all of these problems**.

## What it does
Our website receives user inputs which include user location and symptoms to find the nearest medical professional to treat the user. Using a Support Vector Classifier(SVC) and a Kaggle dataset with 4000+ data points, the machine learning model is able to classify the medical conditions to the inputted symptoms. DoctorDirect currently recognizes 132 symptoms which classify into 40 diseases/medical conditions. Once the disease is classified using the symptoms received from user input, the model matches it to a medical professional

## How we built it
For the machine learning model, we used Google Colab with downloaded datasets to Google drive as the two have a close affinity to each other. The dataset was arranged into a data frame format and used an SVC with "symptoms" as data and "disease" as labels. The "symptoms" have weights labeled to scale which allows some symptoms to have a greater effect on the result of some medical conditions. The model was trained with an 85:15 split between training and testing points which returned a 93 percent accuracy. Using the data frame .iloc function, we created multiple methods so our inputs could adapt to the model. This model accurately assigned specific diseases and medical specialties to the symptom user inputs. 

Then using webscraping techniques, we sought out medical professionals based on location and specialty. Libraries such as cloudscraper, requests, beautifulsoup4, and more, were used to seek all **qualified** medical professionals for the treatment that the user may need. This was done by scraping medical websites, geographical maps, and basic search queries.

Lastly, all of this was seamlessly merged onto a dynamic web platform. Connecting our python files to the typical web dev files, we used Flask to connect all of our models and files to integrate it into a web app, which is hosted on Heroku.

## Challenges we ran into
A major challenge we ran into with the machine learning model was overfitting. This was largely due to improper cleaning of our dataset. With a little bit of data manipulation and a switch of ML models, we were able to significantly boost the accuracy of our model.

A second major challenge we ran into was running into CAPTCHAs when web scraping. To bypass this, we randomly generated user-agents to access the designated website, this would constantly refresh our way of connection, protecting us from CAPTCHAs.

## Accomplishments that we're proud of
We're proud of all aspects of this project. Firstly, overall product design, research, and idea were ideas of our own that we were very passionate about. Secondly, we're happy to have been able to integrate so many fields of computer science into one project, implementing machine learning, data web scraping, web development, and text processing. Thirdly, we're happy to have completed our project!

## What we learned
That webscraping is hard. To be honest, we learned that everything is hard. Also pushing yourself to pull an all-nighter is hard. But we did it!

## What's next for Doctor Direct
Currently, we recognize 42 medical conditions and 132 symptoms. We plan to expand the symptoms and medical conditions to cover a greater range including physical injuries and mental illnesses. Additionally, we can continue to expand onto our website, linking APIs from hospitals directly to our services. This would allow for a more ubiquitous and thorough service. 
