def compute_kappa(TP, FP, FN, TN):
    # 计算 p_o (观察一致性)
    p_o = (TP + TN) / (TP + FP + FN + TN)

    # 计算 p_e (预期一致性)
    p_e = ((TP + FN)*(TP + FP) + (FP + TN)*(FN + TN)) / ((TP + FP + FN + TN)**2)

    # 计算 kappa 值
    kappa = (p_o - p_e) / (1 - p_e)

    return kappa

TP = 3 # 真阳性
FP = 97 # 假阳性
FN = 23 # 假阴性
TN= 1363
#frames=1176
#TN = frames-TP-FP-FN # 真阴性
print(TN)
kappa = compute_kappa(TP, FP, FN, TN)
print(f"Cohen's Kappa: {kappa}")

Recall= TP / (TP + FN)
Precision= TP / (TP + FP)
F1score=2 * (Precision * Recall) / (Precision + Recall)

print(f"Recall: {Recall}")
print(f"Precision: {Precision}")
print(f"F1score: {F1score}")


