def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features = len(vectors)
    num_values = len(vectors[0])

    means = []
    for thing in vectors:
        means.append(sum(thing) / num_values)

    covariance_matrix = []

    for i in range(num_features):
        row = []
        for j in range(num_features):
            total = 0
            for k in range(num_values):
                total += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            row.append(total / (num_values - 1))
        covariance_matrix.append(row)

    return covariance_matrix