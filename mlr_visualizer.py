import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset_file_path = "TrainingData/CSVData/8Inputs/8input_5target.csv"
dataset = pd.read_csv(dataset_file_path)
r_sq_values = []
columns = ["0_date", "0_CAR_ersst", "0_NTA_ersst", "0_aao", "0_ammsst", "0_amon_sm", "0_amon_sm_long", "0_amon_us", "0_amon_us_long", "0_ao", "0_atltri", "0_brazilrain", "0_censo", "0_censo_long", "0_ea", "0_eofpac", "0_epo", "0_espi", "0_gmsst", "0_hurr", "0_indiamon", "0_ipotpi_hadisst2", "0_jonesnao", "0_meiv2", "0_nao", "0_nina1_anom", "0_nina34_anom", "0_nina3_anom", "0_nina4_anom", "0_noi", "0_np", "0_oni", "0_pdo", "0_pna", "0_qbo", "0_sahelrain", "0_soi", "0_solar", "0_swmonsoon", "0_tna", "0_tni", "0_trend", "0_tsa", "0_whwp", "0_wp", "0_precipitation", "1_date", "1_CAR_ersst", "1_NTA_ersst", "1_aao", "1_ammsst", "1_amon_sm", "1_amon_sm_long", "1_amon_us", "1_amon_us_long", "1_ao", "1_atltri", "1_brazilrain", "1_censo", "1_censo_long", "1_ea", "1_eofpac", "1_epo", "1_espi", "1_gmsst", "1_hurr", "1_indiamon", "1_ipotpi_hadisst2", "1_jonesnao", "1_meiv2", "1_nao", "1_nina1_anom", "1_nina34_anom", "1_nina3_anom", "1_nina4_anom", "1_noi", "1_np", "1_oni", "1_pdo", "1_pna", "1_qbo", "1_sahelrain", "1_soi", "1_solar", "1_swmonsoon", "1_tna", "1_tni", "1_trend", "1_tsa", "1_whwp", "1_wp", "1_precipitation", "2_date", "2_CAR_ersst", "2_NTA_ersst", "2_aao", "2_ammsst", "2_amon_sm", "2_amon_sm_long", "2_amon_us", "2_amon_us_long", "2_ao", "2_atltri", "2_brazilrain", "2_censo", "2_censo_long", "2_ea", "2_eofpac", "2_epo", "2_espi", "2_gmsst", "2_hurr", "2_indiamon", "2_ipotpi_hadisst2", "2_jonesnao", "2_meiv2", "2_nao", "2_nina1_anom", "2_nina34_anom", "2_nina3_anom", "2_nina4_anom", "2_noi", "2_np", "2_oni", "2_pdo", "2_pna", "2_qbo", "2_sahelrain", "2_soi", "2_solar", "2_swmonsoon", "2_tna", "2_tni", "2_trend", "2_tsa", "2_whwp", "2_wp", "2_precipitation", "3_date", "3_CAR_ersst", "3_NTA_ersst", "3_aao", "3_ammsst", "3_amon_sm", "3_amon_sm_long", "3_amon_us", "3_amon_us_long", "3_ao", "3_atltri", "3_brazilrain", "3_censo", "3_censo_long", "3_ea", "3_eofpac", "3_epo", "3_espi", "3_gmsst", "3_hurr", "3_indiamon", "3_ipotpi_hadisst2", "3_jonesnao", "3_meiv2", "3_nao", "3_nina1_anom", "3_nina34_anom", "3_nina3_anom", "3_nina4_anom", "3_noi", "3_np", "3_oni", "3_pdo", "3_pna", "3_qbo", "3_sahelrain", "3_soi", "3_solar", "3_swmonsoon", "3_tna", "3_tni", "3_trend", "3_tsa", "3_whwp", "3_wp", "3_precipitation",
           "4_date", "4_CAR_ersst", "4_NTA_ersst", "4_aao", "4_ammsst", "4_amon_sm", "4_amon_sm_long", "4_amon_us", "4_amon_us_long", "4_ao", "4_atltri", "4_brazilrain", "4_censo", "4_censo_long", "4_ea", "4_eofpac", "4_epo", "4_espi", "4_gmsst", "4_hurr", "4_indiamon", "4_ipotpi_hadisst2", "4_jonesnao", "4_meiv2", "4_nao", "4_nina1_anom", "4_nina34_anom", "4_nina3_anom", "4_nina4_anom", "4_noi", "4_np", "4_oni", "4_pdo", "4_pna", "4_qbo", "4_sahelrain", "4_soi", "4_solar", "4_swmonsoon", "4_tna", "4_tni", "4_trend", "4_tsa", "4_whwp", "4_wp", "4_precipitation", "5_date", "5_CAR_ersst", "5_NTA_ersst", "5_aao", "5_ammsst", "5_amon_sm", "5_amon_sm_long", "5_amon_us", "5_amon_us_long", "5_ao", "5_atltri", "5_brazilrain", "5_censo", "5_censo_long", "5_ea", "5_eofpac", "5_epo", "5_espi", "5_gmsst", "5_hurr", "5_indiamon", "5_ipotpi_hadisst2", "5_jonesnao", "5_meiv2", "5_nao", "5_nina1_anom", "5_nina34_anom", "5_nina3_anom", "5_nina4_anom", "5_noi", "5_np", "5_oni", "5_pdo", "5_pna", "5_qbo", "5_sahelrain", "5_soi", "5_solar", "5_swmonsoon", "5_tna", "5_tni", "5_trend", "5_tsa", "5_whwp", "5_wp", "5_precipitation", "6_date", "6_CAR_ersst", "6_NTA_ersst", "6_aao", "6_ammsst", "6_amon_sm", "6_amon_sm_long", "6_amon_us", "6_amon_us_long", "6_ao", "6_atltri", "6_brazilrain", "6_censo", "6_censo_long", "6_ea", "6_eofpac", "6_epo", "6_espi", "6_gmsst", "6_hurr", "6_indiamon", "6_ipotpi_hadisst2", "6_jonesnao", "6_meiv2", "6_nao", "6_nina1_anom", "6_nina34_anom", "6_nina3_anom", "6_nina4_anom", "6_noi", "6_np", "6_oni", "6_pdo", "6_pna", "6_qbo", "6_sahelrain", "6_soi", "6_solar", "6_swmonsoon", "6_tna", "6_tni", "6_trend", "6_tsa", "6_whwp", "6_wp", "6_precipitation", "7_date", "7_CAR_ersst", "7_NTA_ersst", "7_aao", "7_ammsst", "7_amon_sm", "7_amon_sm_long", "7_amon_us", "7_amon_us_long", "7_ao", "7_atltri", "7_brazilrain", "7_censo", "7_censo_long", "7_ea", "7_eofpac", "7_epo", "7_espi", "7_gmsst", "7_hurr", "7_indiamon", "7_ipotpi_hadisst2", "7_jonesnao", "7_meiv2", "7_nao", "7_nina1_anom", "7_nina34_anom", "7_nina3_anom", "7_nina4_anom", "7_noi", "7_np", "7_oni", "7_pdo", "7_pna", "7_qbo", "7_sahelrain", "7_soi", "7_solar", "7_swmonsoon", "7_tna", "7_tni", "7_trend", "7_tsa", "7_whwp", "7_wp", "7_precipitation"]
for column in columns:
    x = dataset[[column]]
    y = dataset["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=100)
    mlr = LinearRegression()
    mlr.fit(x_train, y_train)
    y_pred_mlr = mlr.predict(x_test)
    mlr_diff = pd.DataFrame(
        {'Actual value': y_test, 'Predicted value': y_pred_mlr})
    meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
    meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
    rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
    r_sq_values.append([column, mlr.score(x, y)*100])

stuff_to_plot = [item for item in r_sq_values if item[1] > 20]
xticks = [x[0] for x in stuff_to_plot]
xs = [x for x in range(len(stuff_to_plot))]
ys = [x[1] for x in stuff_to_plot]

plt.bar(xs, ys)
plt.xticks(xs, xticks)
plt.show()
