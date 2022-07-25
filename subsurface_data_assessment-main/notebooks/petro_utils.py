import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics


def get_bounds(x, y, buffer=0.1):
    minval = np.nanmin(np.concatenate([x, y]))
    maxval = np.nanmax(np.concatenate([x, y]))
    minval -= buffer * minval
    maxval += buffer * minval
    return [minval, maxval]


def compare_pred_results(
    y_train,
    y_train_pred,
    y_test,
    y_test_pred,
    scale_factor=1,
    title="Predicted vs. Actual CER12",
    xlabel="Actual CER12 [bbl/ft3]",
    ylabel="Predicted CER12 [bbl/ft3]",
):

    y_train = y_train.copy() / scale_factor
    y_train_pred = y_train_pred.copy() / scale_factor
    y_test = y_test.copy() / scale_factor
    y_test_pred = y_test_pred.copy() / scale_factor

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.scatter(y_train, y_train_pred, label="Train", color="#4c72b0")
    ax.scatter(y_test, y_test_pred, label="Test", color="#dd8452")

    bounds = get_bounds(y_test_pred, y_test)
    # trend = np.polyfit(y_train_pred, y_train, 1)
    # y_hat = np.poly1d(trend)
    # y_space = np.linspace(bounds[0], bounds[1], 100)
    plt.plot(bounds, bounds, "k")
    # ax.plot(y_space, y_hat(y_space), "k--", lw=1)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)

    ax.legend(fontsize=12)
    ax.set_xlim(bounds)
    ax.set_ylim(bounds)
    ax.set_aspect("equal")

    # text = f"$NRMSE_{{train}} = {np.sqrt(metrics.mean_squared_error(y_train,y_train_pred))/np.mean(y_train):0.3f}$"
    # plt.gca().text(
    #     0.6,
    #     0.10,
    #     text,
    #     transform=plt.gca().transAxes,
    #     fontsize=14,
    #     verticalalignment="bottom",
    # )
    # text = f"$NRMSE_{{test}} = {np.sqrt(metrics.mean_squared_error(y_test,y_test_pred))/np.mean(y_test):0.3f}$"
    # plt.gca().text(
    #     0.6,
    #     0.05,
    #     text,
    #     transform=plt.gca().transAxes,
    #     fontsize=14,
    #     verticalalignment="bottom",
    # )
