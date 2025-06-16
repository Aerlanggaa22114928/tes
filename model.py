import joblib

# Contoh pelatihan model
X = obesitas_df.drop(columns=["NObeyesdad"])
y = obesitas_df["NObeyesdad"]

# Encoding
X = pd.get_dummies(X)
le = LabelEncoder()
y = le.fit_transform(y)

# Split dan training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Simpan model
joblib.dump(clf, "decision_tree_obesitas.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")
