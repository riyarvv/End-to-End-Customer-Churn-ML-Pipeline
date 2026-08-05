from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def create_preprocessor(categorical_features, numerical_features):
    """
    Create a preprocessing pipeline for categorical and numerical features.
    """

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "num",
                StandardScaler(),
                numerical_features
            )
        ]
    )

    return preprocessor