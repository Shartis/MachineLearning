import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    dataset = pd.read_csv("train_titanic.csv")
    genders = dataset.Sex
    filterM = genders == 'male'
    filterF = genders == 'female'
    male = dataset.loc[filterM]
    female = dataset.loc[filterF]

    # Распределение  мужчин по классу
    mdf = male[['Survived', 'Pclass']][male['Survived'] == 1].groupby('Pclass').count()
    print(mdf)
    mdf.plot.bar()
    plt.show()

    # Распределение  женщин по классу
    fmdf = female[['Survived', 'Pclass']][female['Survived'] == 1].groupby('Pclass').count()
    fmdf.plot.bar()
    plt.show()

    # Круговая диаграмма
    df = male['Pclass'].value_counts()
    print(df)
    df.plot(kind="pie", label="")
    plt.show()

    # Распределение возрастов всех
    age = dataset['Age'].value_counts()
    print(age)
    age.plot.bar()
    plt.show()