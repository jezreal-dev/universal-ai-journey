import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.tree import DecisionTreeClassifier, export_text

def main():
    print("=== PART 1: EXPLORING AND NORMALIZING DATA ===")
    
    # Robust search paths for Airlines dataset
    paths = [
        "AirlinesCluster.csv",
        "Assignment_3/asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@AirlinesCluster.csv",
        r"C:\Users\USER\Desktop\MIT assignment\Module_4_Assignment\Assignment_3\asset-v1_UAI_SOURCE+UAI.1+2T2025+type@asset+block@AirlinesCluster.csv",
        "/home/jmomoh/universal-ai-journey/resources/AirlinesCluster.csv"
    ]
    
    airlines = None
    for path in paths:
        try:
            airlines = pd.read_csv(path)
            print(f"Loaded airlines data from: {path}")
            break
        except FileNotFoundError:
            continue
            
    if airlines is None:
        raise FileNotFoundError("Could not find AirlinesCluster.csv in any of the search paths.")

    # Q1: Variables with mean less than 20
    desc = airlines.describe()
    mean_less_20 = (desc.loc["mean"] < 20).sum()
    print(f"Q1: Variables with mean < 20: {mean_less_20}")
    print("Variable Means:")
    print(desc.loc["mean"])

    # Q3, Q4, Q5: Normalization
    airlines_norm = (airlines - airlines.mean()) / airlines.std()
    print("\nNormalized variables maximums:")
    print(airlines_norm.max(axis=0))
    print("\nNormalized variables minimums:")
    print(airlines_norm.min(axis=0))
    
    min_below_neg_point_7 = (airlines_norm.min(axis=0) < -0.7).sum()
    print(f"Q5: Number of normalized variables with min < -0.7: {min_below_neg_point_7}")


    print("\n=== PART 2: HIERARCHICAL CLUSTERING ===")
    airline_dist = pdist(airlines_norm, metric="euclidean")
    linkage_matrix = linkage(airline_dist, method="ward")
    
    # Cut into 5 clusters
    cluster_groups = fcluster(linkage_matrix, 5, criterion='maxclust')
    cluster_df = pd.DataFrame(airlines)
    cluster_df["Cluster"] = cluster_groups
    
    print("Cluster sizes:")
    print(cluster_df["Cluster"].value_counts())
    
    print("\nCluster centroids (means):")
    cluster_means = cluster_df.groupby("Cluster").mean()
    print(cluster_means)
    
    print("\nCluster rank rankings (1 = lowest, 5 = highest):")
    print(cluster_means.rank())


    print("\n=== PART 3: K-MEANS CLUSTERING AND DECISION TREE ===")
    np.random.seed(88)
    kmeans = KMeans(n_clusters=5, max_iter=1000, random_state=88)
    kmeans.fit(airlines_norm)
    
    print("K-Means cluster sizes:")
    print(pd.Series(kmeans.labels_).value_counts())
    
    # Train Decision Tree
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(airlines, kmeans.labels_)
    
    print("\nDecision Tree Rules for K-Means labels:")
    print(export_text(tree, feature_names=airlines.columns.tolist()))

if __name__ == "__main__":
    main()
