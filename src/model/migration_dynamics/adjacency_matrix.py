import numpy as np

def migration_function(uebergangsmatrix_funktion):

    def migrate(nodes, t):

        hawk_vec = []
        dove_vec = []

        for node_i in nodes:
            hawk_i, dove_i = node_i.get_value()
            hawk_vec.append(hawk_i)
            dove_vec.append(dove_i)

        hawk_vec = np.array(hawk_vec)
        dove_vec = np.array(dove_vec)


        hawk_matrix, dove_matrix = uebergangsmatrix_funktion(nodes, t)

        hawk_vec = hawk_matrix.dot(hawk_vec)
        dove_vec = dove_matrix.dot(dove_vec)

        for i in range(0, len(nodes)):
            nodes[i].set_value((hawk_vec[i], dove_vec[i]))


    return migrate

def berechne_uebergang(nodes, i, j, species, a):
    if(nodes[i].is_connected_to(nodes[j])):
        nodes_i_val = nodes[i].get_value()
        nodes_j_val = nodes[j].get_value()

        return max(a*(nodes_i_val[species]/sum(nodes_i_val) - nodes_j_val[species]/sum(nodes_j_val)), 0)/(nodes[i].distance(nodes[j]))
    return 0


#Idee: Replikatiordynamik auf Diagonalelemente
def uebergangsmatrix_matrix(nodes, t, a_hawk=0.5, a_dove=0.5, diag_hawk=0.5, diag_dove=0.5):

    matrix_hawk = np.zeros((len(nodes), len(nodes)))
    matrix_dove = np.zeros((len(nodes), len(nodes)))

    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if (i != j):
                matrix_hawk[i][j] = berechne_uebergang(nodes, i, j, 0, a_hawk)
                matrix_dove[i][j] = berechne_uebergang(nodes, i, j, 1, a_dove)

    matrix_hawk = np.transpose(matrix_hawk)
    matrix_dove = np.transpose(matrix_dove)
    for i in range(0, len(nodes)):
    
        
        zeilen_summe_hawk_ohne_diag = np.sum(matrix_hawk[i])
        if(zeilen_summe_hawk_ohne_diag != 0):
            norm_factor_hawk = diag_hawk/zeilen_summe_hawk_ohne_diag
            matrix_hawk[i] *= norm_factor_hawk
            matrix_hawk[i][i] = diag_hawk
        else:
            matrix_hawk[i][i] = 1
        

        zeilen_summe_dove_ohne_diag = np.sum(matrix_dove[i])
        if(zeilen_summe_dove_ohne_diag != 0):
            norm_factor_dove = diag_dove/zeilen_summe_dove_ohne_diag
            matrix_dove[i] *= norm_factor_dove
            matrix_dove[i][i] = diag_dove
        else:
            matrix_dove[i][i] = 1

    matrix_hawk = np.transpose(matrix_hawk)
    matrix_dove = np.transpose(matrix_dove)

    return matrix_hawk, matrix_dove






    