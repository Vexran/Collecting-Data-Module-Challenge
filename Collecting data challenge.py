import pandas as pd
import os

#Del 1
root = 'C:\\Users\\natha\\Downloads\\Student_Data_Challenge_Starter_Code (1)\\'
filename = 'new_full_student_data.csv'
#print('\\n')
filename = os.path.join(root, filename)
print(filename)
student_df = pd.read_csv(filename, sep=',')
print(student_df)

#Del 2
student_df_nan_removed = student_df.dropna()
student_df_nan_removed_and_summed = student_df.dropna().sum()
print(student_df_nan_removed_and_summed)
print(student_df_nan_removed)
print(student_df_nan_removed)
data_types = student_df_nan_removed.dtypes
print(data_types)
coloumn_without_th = student_df_nan_removed['grade'].str.replace(r'th', '')
print(coloumn_without_th)

coloumn_without_th_into_int = pd.to_numeric(coloumn_without_th)
data_types = coloumn_without_th_into_int.dtypes
print(data_types)
student_df_dup_removed = student_df_nan_removed.duplicated().sum()
print(student_df_dup_removed)

#Del 3
described = student_df.describe()
print(described)
mean = student_df.mean()
print(mean)
min_reading_score = student_df['reading_score'].min()
print(min_reading_score)

#Del 4

print('----')
grade = student_df.loc[:,['grade']]
print(grade)
iloc_cols = student_df.iloc[:, [3, 4, 5]]
print(iloc_cols)
print('---')
print(student_df_nan_removed)
print('__')
grade_nine_described = student_df.loc[student_df['grade'] == '9th'].describe()
print(grade_nine_described)
print('-=')
print(min_reading_score)
min_reading_row = student_df.loc[student_df['reading_score'] == min_reading_score]
print(min_reading_row)
print(student_df.loc[(student_df['grade'] == '10th') & (student_df['school_name'] == 'Dixon High School')])
upperclassmen_df = student_df.loc[(student_df['grade'] == '11th') | (student_df['grade'] == '12th')]
mean_reading_score = upperclassmen_df['reading_score'].mean()
#upperclassmen_mean = upperclassmen_df.loc[upperclassmen_df['reading_score'] == mean_reading_score]
print(mean_reading_score)
#print(upperclassmen_mean)


#Del 5

print('----')
avg_math_type = student_df.groupby(['school_type', 'grade']).mean()
avg_math_type.loc[:, ['math_score']].round()






