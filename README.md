# Projet 3 - Prédiction du Churn Client

## Structure du dépôt
- `Churn_EDA_Preparation.ipynb` : Notebook détaillé pour l'analyse exploratoire et préparation des données.
- `Churn_Modeling.ipynb` : Notebook de modélisation (Logistic Regression, Decision Tree, Random Forest + tuning).
- `telco_sample.csv` : Exemple de dataset (extrait) pour exécuter les notebooks si le dataset Kaggle complet n'est pas disponible.
- `artifacts/` : répertoire créé lors de l'exécution contenant préprocesseur et modèles sauvegardés.
- `artifacts_models/` : répertoire créé lors de l'exécution du notebook de modélisation contenant les pipelines entrainés sauvegardés.
- `.gitignore`, `requirements.txt` : fichiers de configuration pour le repo.


## Comment exécuter
1. Clonez le dépôt ou téléchargez l'archive.
2. Créez un environnement virtuel Python et installez les dépendances :
3. Exécutez en premier lieu Churn_EDA_preparation.ipynb puis Churn_Modeling.ipynb
4. Exécuter l'API

```bash
python -m venv .venv
source .venv/bin/activate  # ou .\.venv\Scripts\activate sur Windows
pip install -r requirements.txt
```

3. Placez le fichier `Telco-Customer-Churn.csv` (dataset complet) à la racine du dépôt.
4. Ouvrez et exécutez `Churn_EDA_Preparation.ipynb`, puis `Churn_Modeling.ipynb`.


## Remarques
- Les notebooks contiennent des commentaires expliquant les choix de preprocessing et les métriques utilisées.
- Pour la production, exportez les pipelines via `joblib` (déjà implémenté dans les notebooks) et préparez une API si nécessaire.
