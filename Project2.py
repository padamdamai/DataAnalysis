import pandas as pd    
  
  
def calculate_demographic_data(print_data=True):
          # Read data from file
          df = pd.read_csv("datas.csv")
  
      #1 How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts() 
  
      # 2 What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean().round(2)
  
      # 3 What is the percentage of people who have a Bachelor's degree?
total_bach = len(df[df['education'] == "Bachelors"])
edu_bach = df['education'].count()
percentage_bachelors =  round(total_bach / edu_bach *100 ,2)
  
  
      #4  What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
      # What percentage of people without advanced education make more than 50K?
  
      # with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]
      
      # percentage with salary >50K
more_than_fiftyk = len(advanced_education[advanced_education['salary']== ">50K"])
higher_education_rich = round(more_than_fiftyk/len(advanced_education)* 100,2)
      
loweredu_more_than_fiftyk =  len(lower_education[lower_education['salary']== ">50K"])
lower_education_rich = round(loweredu_more_than_fiftyk/len(lower_education)*100,2)
      
      # 6 What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours =  df['hours-per-week'].min()
      
      
      # 7 What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  
minimun_hours = df[df['hours-per-week'] ==  minimun_number_hour]
num_min_workers = minimun_hours[minimun_hours['salary']== ">50K"]
      
rich_percentage = round( len(salary_50k)/ len(minimun_hours) * 100,2)
      
      # 8 What country has the highest percentage of people that earn >50K?
total_no_country = df['native-country'].value_counts()  
rich_country = df[df['salary']== ">50K"]['native-country'].value_counts()
highest_earning_country = (rich_country / total_no_country * 100)
      
highest_earning_country_percentage = round((rich_country / total_no_country * 100).max(),2)  
  
      # 9 Identify the most popular occupation for those who earn >50K in India.
people_of_india = df[(df['native-country']== "India") & (df['salary']== ">50K")]
occupation_count = people_of_india['occupation'].value_counts()    
top_IN_occupation =  occupation_count.idxmax()
  
      # DO NOT MODIFY BELOW THIS LINE
if print_data:
          print("Number of each race:\n", race_count) 
          print("Average age of men:", average_age_men)
          print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
          print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
          print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
          print(f"Min work time: {min_work_hours} hours/week")
          print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
          print("Country with highest percentage of rich:", highest_earning_country)
          print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
          print("Top occupations in India:", top_IN_occupation)
        return{
                  'race_count': race_count,
                  'average_age_men': average_age_men,
                  'percentage_bachelors': percentage_bachelors,
                  'higher_education_rich': higher_education_rich,
                  'lower_education_rich': lower_education_rich,
                  'min_work_hours': min_work_hours,
                  'rich_percentage': rich_percentage,
                  'highest_earning_country': highest_earning_country,
                  'highest_earning_country_percentage':
                  highest_earning_country_percentage,
                  'top_IN_occupation': top_IN_occupation
                }
    