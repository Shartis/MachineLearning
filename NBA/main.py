import pandas as pd
import numpy as np


class NaiveBayesClassifier:
    def __init__(self):
        self.class_probabilities = {}
        self.conditional_probabilities = {}

    def load(self, symptom, disease, disease_total):
        for cls_name, cls_count in disease.iterrows():
            print("load -- cls_name: ", cls_name)
            print("load -- cls_count: ", cls_count)
            print("load -- cls_count[0]: ", cls_count[0])
            self.class_probabilities[cls_name] = cls_count[0] / disease_total
            print("load -- self.class_probabilities[cls_name]: ", self.class_probabilities[cls_name])

        print("load ---------------------------------------------------------------------------")

        for feature_name, feature_probs in symptom.iterrows():
            print("load -- feature_name: ", feature_name)
            print("load -- feature_probs: \n", feature_probs)
            self.conditional_probabilities[feature_name] = {}
            print("self.conditional_probabilities[feature_name]: ", self.conditional_probabilities[feature_name])

            for cls_name, feature_cls_prob in enumerate(feature_probs):
                print("load -- cls_name: ", cls_name)
                print("load -- feature_cls_prob: ", feature_cls_prob)
                self.conditional_probabilities[feature_name][cls_name] = feature_cls_prob
                print("load -- self.conditional_probabilities[feature_name][cls_name]: ",
                      self.conditional_probabilities[feature_name][cls_name])
        print("self.conditional_probabilities: \n", self.conditional_probabilities)
        print("self.class_probabilities: \n", self.class_probabilities)

    def get_prob_for_class(self, vec, cls):
        result = self.class_probabilities[cls]
        print("result: -- result", result)
        for idx, value in enumerate(vec):
            if value:
                result *= self.conditional_probabilities.get(idx, {}).get(cls, 0)
        return result

    def predict(self, X):
        result = []
        for x in X:
            max_y = None
            max_prob = 0
            for cls in self.class_probabilities.keys():
                prob = self.get_prob_for_class(x, cls)
                if prob >= max_prob:
                    max_y = cls
                    max_prob = prob
            result.append(max_y)
        return result

if __name__ == '__main__':
    symptom = pd.read_csv('symptom.csv', sep=';', index_col=0)
    print("Таблица с симптомами: \n", symptom)
    disease_names = symptom.columns
    symptom_names = symptom.index
    symptom.columns = list(range(len(symptom.columns)))
    symptom = symptom.reset_index(drop=True)
    print("Таблица с симптомами matrix: \n", symptom)
    disease = pd.read_csv('disease.csv', sep=';', index_col=0)
    print("Болезни: \n", disease)
    total_disease = disease.iloc[-1][0]
    disease = disease[:9]
    disease = disease.reset_index(drop=True)
    X_test = np.random.randint(0, 2, size=(1, len(symptom)))
    print(X_test)
    print("болезни")
    print(symptom.iterrows())
    for feature_name, feature_probs in disease.iterrows():
        if (X_test[0][feature_name] == 1):
            print(feature_probs)
    NBayesModel = NaiveBayesClassifier()
    NBayesModel.load(symptom, disease, total_disease)
    y_pred = NBayesModel.predict(X_test)
    print(y_pred)
    print("Ответ: ", list(map(lambda x: disease_names[x].strip(), y_pred)))
