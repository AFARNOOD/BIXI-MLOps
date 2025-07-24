from prefect import flow
from pipeline.tasks import load_data, train_model, evaluate_model, save_model

@flow(name="BIXI ML Training Flow")
def bixi_flow():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)

if __name__ == "__main__":
    bixi_flow()
