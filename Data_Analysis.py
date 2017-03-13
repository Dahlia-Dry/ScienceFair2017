#Author Dahlia Dry
#Version 1.2
#Last Modified 11/13/16
#This program uses ARIMA and ARMA time series modeling to create 4 models that attempt to 
#predict future points in the data set.  This program also assesses the accuracy of those 
#models.
import pyflux as pf
import pandas as pd
import numpy as np

target1 = open("november_15.csv", 'r')
target2 = open("november_16.csv", 'r')
target3 = open("write.txt", 'w')
partdata1 = pd.read_csv(target1, sep=',', header=None, names=["time", "ADC_Value"])
partdata2 = pd.read_csv(target2, sep=',', header=None, names=["time", "ADC_Value"])
del partdata1['time']
del partdata2['time']
frames = [partdata1, partdata2]
fulldata = pd.concat(frames)
timeseries = pd.DataFrame()
percent_errors_model1 = []
base_models_declared = False
fit_method = 'MLE'
fit_once = True
writer = pd.ExcelWriter('DATA.xlsx')


def concatenate(db1, db2, a):
    plusdata = db2[a:a + 1]
    frame = [db1, plusdata]
    concat = pd.concat(frame)
    return concat



def percent_error_and_binomial_accuracy(actual_data, model, integ):
    percent_error_set = []
    binom_error = 0
    if integ == 0:
        predicted_data = model.predict_is(50)
        for i in range(0, len(predicted_data)-1) :
            length = predicted_data.index[i]
        for i in predicted_data.index:
            k = 0
            error = predicted_data['Series'][i] - actual_data['ADC_Value'][i]
            if i < length - 1:
                if predicted_data['Series'][i] - predicted_data['Series'][i+1] > 0:
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] < 0:
                        binom_error = binom_error + 1
                elif predicted_data['Series'][i] - predicted_data['Series'][i+1] < 0 :
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] > 0:
                        binom_error = binom_error + 1
            if error < 0:
                error = (-1) * error
            percent_error = error / actual_data['ADC_Value'][i]
            if percent_error < 0:
                percent_error = (-1) * percent_error
            percent_error_set.insert(k, percent_error)
            k = k + 1
        binom_accuracy = binom_error / (k + 1)
        median = len(percent_error_set) / 2
        median = percent_error_set[median]
        median_percent_error = median
        median_percent_error = median_percent_error / 100
        calculations = {'binomial accuracy':binom_accuracy,
        'median percent error':median_percent_error}

    if integ == 1:
        difference_values = []
        for i in actual_data.index:
            difference_value = actual_data['ADC_Value'][i]
            difference_values.insert(i, difference_value)
        convert_to_numpy = np.asarray(difference_values)
        differenced_data = np.diff(convert_to_numpy, integ)
        length = len(differenced_data) - 1
        predicted_data = model.predict_is(50)
        j = length - 48
        for i in range(j, j + 48):
            k = 0
            error = predicted_data['Differenced Series'][i] - differenced_data[i]
            if i < (j+ 48):
                if predicted_data['Differenced Series'][i] - predicted_data['Differenced Series'][i+1] > 0:
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] < 0:
                        binom_error = binom_error + 1
                elif predicted_data['Differenced Series'][i] - predicted_data['Differenced Series'][i+1] < 0 :
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] > 0:
                        binom_error = binom_error + 1
            percent_error = error / differenced_data[i]
            if percent_error < 0:
                percent_error = (-1) * percent_error
            percent_error_set.insert(k, percent_error)
            k = k + 1
        binom_accuracy = binom_error / k+1
        median = len(percent_error_set) / 2
        median = percent_error_set[median]
        median_percent_error = median
        median_percent_error = median_percent_error / 100
        calculations = {'binomial accuracy': binom_accuracy,
        'median percent error':median_percent_error}

    if integ == 2:
        difference_values = []
        for i in actual_data.index:
            difference_value = actual_data['ADC_Value'][i]
            difference_values.insert(i, difference_value)
        convert_to_numpy = np.asarray(difference_values)
        differenced_data = np.diff(convert_to_numpy, integ)
        length = len(differenced_data) - 1
        predicted_data = model.predict_is(50)
        j = length - 47
        for i in range(j, j + 47):
            k = 0
            error=predicted_data['Differenced Differenced Series'][i]-differenced_data[i]
            if i < (j+47):
                if predicted_data['Differenced Differenced Series'][i] -predicted_data['Differenced Differenced Series'][i+1] > 0:
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] < 0:
                        binom_error = binom_error + 1
                elif predicted_data['Differenced Differenced Series'][i] - predicted_data['Differenced Differenced Series'][i+1] < 0 :
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] > 0:
                        binom_error = binom_error + 1
            percent_error = error / differenced_data[i]
            if percent_error < 0:
                percent_error = (-1) * percent_error
            percent_error_set.insert(k, percent_error)
            k = k + 1
        binom_accuracy = binom_error / (k+1)
        median = len(percent_error_set) / 2
        median = percent_error_set[median]
        median_percent_error = median
        median_percent_error = median_percent_error / 100
        calculations = {'binomial accuracy': binom_accuracy, 
        'median percent error':median_percent_error}

    if integ == 3:
        difference_values = []
        for i in actual_data.index:
            difference_value = actual_data['ADC_Value'][i]
            difference_values.insert(i, difference_value)
        convert_to_numpy = np.asarray(difference_values)
        differenced_data = np.diff(convert_to_numpy, integ)
        length = len(differenced_data) - 1
        predicted_data = model.predict_is(50)
        print predicted_data
        print length
        j = length - 46
        for i in range(j, j + 46):
            k = 0
            error=predicted_data['Differenced Differenced Differenced Series'][i]
            error = error - differenced_data[i]
            if i < (j+47):
                if predicted_data['Differenced Differenced Differenced Series'][i] -predicted_data['Differenced Differenced Differenced Series'][i+1] > 0:
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] < 0:
                        binom_error = binom_error + 1
                elif predicted_data['Differenced Differenced Differenced Series'][i] - predicted_data['Differenced Differenced Differenced Series'][i+1] < 0 :
                    if actual_data['ADC_Value'][i] - actual_data['ADC_Value'][i + 1] > 0:
                        binom_error = binom_error + 1
            percent_error = error / differenced_data[i]
            if percent_error < 0:
                percent_error = (-1) * percent_error
            percent_error_set.insert(k, percent_error)
            k = k + 1
        binom_accuracy = binom_error / (k+1)
        median = len(percent_error_set) / 2
        median = percent_error_set[median]
        median_percent_error = median
        median_percent_error = median_percent_error / 100
        calculations = {'binomial accuracy': binom_accuracy, 
        'median percent error': median_percent_error}

    return calculations


def find_best_model(errorset):
    lowest_error_index = 0
    for i in range(0, len(errorset) - 1):
        if i == 0:
            lowest_error = errorset[i]
        else:
            if errorset[i] < lowest_error:
                errorset[i] = lowest_error
                lowest_error_index = i
    return lowest_error_index


def calc_optimal_params(z, modeltype):
    if modeltype == 'arima':
        if z % 4 == 0:
            best_integ = 0
        if z % 4 == 1 or z == 1:
            best_integ = 1
        if z % 4 == 2 or z == 2:
            best_integ = 2
        if z % 4 == 3 or k == 3:
            best_integ = 3
        if z < 20:
            best_ar = 1
        if z < 40:
            best_ar = 2
        if z < 60:
            best_ar = 3
        if z < 80:
            best_ar = 4
        if z < 100:
            best_ar = 5
        z = z % 20
        if z >= 0 and z <= 3:
            best_ma = 1
        if z >= 4 and z <= 7:
            best_ma = 2
        if z >= 8 and z <= 11:
            best_ma = 3
        if z >= 12 and z <= 15:
            best_ma = 4
        if z >= 16 and z <= 19:
            best_ma = 5
        best_params = {'ar': best_ar, 'ma': best_ma, 'integ': best_integ}
    if modeltype == 'dar':
        if z % 4 == 0:
            best_integ = 0
        if z % 4 == 1 or z == 1:
            best_integ = 1
        if z % 4 == 2 or z == 2:
            best_integ = 2
        if z % 4 == 3 or k == 3:
            best_integ = 4
        if z >= 0 and z <= 3:
            best_ar = 1
        if z >= 4 and z <= 7:
            best_ar = 2
        if z >= 8 and z <= 11:
            best_ar = 3
        if z >= 12 and z <= 15:
            best_ar = 4
        if z >= 16 and z <= 19:
            best_ar = 5
        best_params = {'ar':best_ar, 'integ':best_integ}
    return best_params

def graph(model, i):
    a=model.plot_fit(figsize=(18,6))
    b=model.plot_z(figsize=(18,6))
    c=model.plot_predict(h=20, past_values = 20, figsize = (18,6))
    filename_a = model + '_fit_i=' + i + '.png'
    filename_b = model + '_latent_variables_i=' + i + '.png'
    filename_c = model + '_predictions_h=20_i=' + i + '.png'
    a.savefig(fname = filename_a)
    b.savefig(fname = filename_b)
    c.savefig(fname = filename_c)

for i in range(0, 15942):  #15942 data points
    timeseries = concatenate(timeseries, fulldata, i)
errorset_model1 = []
errorset_model3 = []
k = 0
for ar in range(1, 5):
    for ma in range(1, 5):
        for integ in range(0, 3):
            model1 = pf.ARIMA(timeseries, ar, ma, integ)
            model1_testfit = model1.fit()
            percent_error_model1 = percent_error_and_binomial_accuracy(timeseries,
            model1, integ)
            errorset_model1.insert(k, percent_error_model1)
            if k <= 19:
                model3 = pf.ARIMA(timeseries, ma,0,integ)
                model3_testfit = model3.fit()
                percent_error_model3 = percent_error_and_binomial_accuracy(timeseries, 
                model3, integ)
                percent_error_model3 = percent_error_model3['median percent error']
                errorset_model3.insert(k,percent_error_model3)
            k = k + 1
z = find_best_model(errorset_model1)
best_params_mod1 = calc_optimal_params(z, 'arima')
model1_ar = best_params_mod1['ar']
model1_ma = best_params_mod1['ma']
model1_integ = best_params_mod1['integ']
model1 = pf.ARIMA(timeseries, model1_ar, model1_ma, model1_integ)
model1_fit = model1.fit()
model1_predictions = pd.DataFrame(model1.predict(50))

zz = find_best_model(errorset_model3)
best_params_mod3 = calc_optimal_params(zz, 'dar')
model3_ar = best_params_mod3['ar']
model3_integ = best_params_mod3['integ']
model3 = pf.ARIMA(timeseries, model3_ar, 0, model3_integ)
model3_fit = model3.fit()
model3_predictions = pd.DataFrame(model3.predict(50))

model2 = pf.ARIMA(timeseries, best_params_mod1['ar'], best_params_mod1['ma'],
best_params_mod1['integ'])
model2_fit = model2.fit()
model2_predictions = pd.DataFrame(model2.predict(50))

model4 = pf.ARIMA(timeseries, best_params_mod3['ar'], 0, best_params_mod3['integ'])
model4_fit = model4.fit()
model4_predictions = pd.DataFrame(model4.predict(50))


for i in range(100, 3000): #15942
    timeseries = concatenate(timeseries, fulldata, i)
    if i % 100 == 0:
        model1 = pf.ARIMA(timeseries, model1_ar, model1_ma, model1_integ)
        model1_fit = model1.fit()
        new_model1_predictions = model1.predict(50)
        model1_predictions.append(new_model1_predictions)

        model3 = pf.ARIMA(timeseries, model3_ar, 0, model3_integ)
        model3_fit = model3.fit()
        new_model3_predictions = model3.predict(50)
        model3_predictions.append(new_model3_predictions)

        errorset_model2 = []
        errorset_model4 = []
        k = 0
        for ar in range(1, 5):
            for ma in range(1, 5):
                for integ in range(0, 3):
                    model2 = pf.ARIMA(timeseries, ar, ma, integ)
                    model2_testfit = model2.fit()
                    percent_error_model2 = percent_error_and_binomial_accuracy(timeseries,
                    model2, integ)
                    errorset_model2.insert(k, percent_error_model2)
                    if k <= 19:
                        model4 = pf.ARIMA(timeseries, ma, 0, integ)
                        model4_testfit = model4.fit()
                        percent_error_model4 = percent_error_and_binomial_accuracy(
                        timeseries, model4, integ)
                        errorset_model4.insert(k, percent_error_model4)
                    k = k + 1
        zzz = find_best_model(errorset_model2)
        best_params = calc_optimal_params(zzz, 'arima')
        model2 = pf.ARIMA(timeseries, best_params['ar'], best_params['ma'],
        best_params['integ'])
        model2_fit = model2.fit()
        new_model2_predictions = model2.predict(50)
        model2_predictions.append(new_model2_predictions)

        zzzz = find_best_model(errorset_model2)
        best_params = calc_optimal_params(zzzz, 'dar')
        model4 = pf.ARIMA(timeseries, best_params['ar'], 0, best_params['integ'])
        model4_fit = model4.fit()
        new_model4_predictions = model4.predict(50)
        model4_predictions.append(new_model4_predictions)

    if i % 3000 == 0:
        graph(model1, i)
        graph(model2, i)
        graph(model3, i)
        graph(model4, i)

model1_predictions.to_excel(writer, 'model1')
model2_predictions.to_excel(writer,'model2')
model3_predictions.to_excel(writer, 'model3')
model4_predictions.to_excel(writer, 'model4')

