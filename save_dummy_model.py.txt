from pathlib import Path
from joblib import dump
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Charger un dataset jouet (Iris)
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer quelques modèles simples
best_rf = RandomForestClassifier(n_estimators=10, random_state=42).fit(X_train, y_train)
best_dt = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
pipe_log = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200)).fit(X_train, y_train)

# Créer le dossier artifacts_models s'il n'existe pas
out_dir = Path("./artifacts_models")
out_dir.mkdir(exist_ok=True)

# Sauvegarder les modèles
dump(best_rf, out_dir / "best_random_forest_pipeline.joblib")
dump(best_dt, out_dir / "best_decision_tree_pipeline.joblib")
dump(pipe_log, out_dir / "logistic_pipeline.joblib")

print("✅ Modèles sauvegardés dans:", out_dir.resolve())
