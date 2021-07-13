import HomPolys

# Edge List Tests

# complete graphs Kn
def check_Kn_0():
    # no edges
    output_0 = (0, [])
    output_1 = (1, [])
    result_0 = HomPolys.create_graph_edges('K0')
    result_1 = HomPolys.create_graph_edges('K1')
    return output_0 == result_0 and output_1 == result_1

def check_Kn_2():
    output = (2, [(0, 1)])
    return output == HomPolys.create_graph_edges('K2')

def check_Kn_3():
    output = (3, [(0, 1), (0, 2), (1, 2)])
    return output == HomPolys.create_graph_edges('K3')

def check_Kn_4():
    output  = (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    return output == HomPolys.create_graph_edges('K4')

# Path graphs Pn

def check_Pn_0():
    # no edges
    output_0 = (0, [])
    output_1 = (1, [])
    result_0 = HomPolys.create_graph_edges('P0')
    result_1 = HomPolys.create_graph_edges('P1')
    return output_0 == result_0 and output_1 == result_1

def check_Pn_2():
    output = (2, [(0, 1)])
    return output == HomPolys.create_graph_edges('P2')

def check_Pn_3():
    output = (3, [(0, 1), (1, 2)])
    return output == HomPolys.create_graph_edges('P3')

def check_Pn_4():
    output = (4, [(0, 1), (1, 2), (2, 3)])
    return output == HomPolys.create_graph_edges('P4')


# Cycle graphs Cn

def check_Cn_0():
    # no edges
    output_0 = (0, [])
    output_1 = (1, [(0, 0)])
    result_0 = HomPolys.create_graph_edges('C0')
    result_1 = HomPolys.create_graph_edges('C1')
    return output_0 == result_0 and output_1 == result_1

def check_Cn_2():
    output = (2, [(0, 1), (0, 1)])
    return output == HomPolys.create_graph_edges('C2')

def check_Cn_3():
    output = (3, [(0, 1), (1, 2), (0, 2)])
    return output == HomPolys.create_graph_edges('C3')

def check_Cn_4():
    output = (4, [(0, 1), (1, 2), (2, 3), (0, 3)])
    return output == HomPolys.create_graph_edges('C4')

# Star graphs Sn

def check_Sn_0():
    # no edges
    output_0 = (0, [])
    output_1 = (1, [])
    result_0 = HomPolys.create_graph_edges('S0')
    result_1 = HomPolys.create_graph_edges('S1')
    return output_0 == result_0 and output_1 == result_1

def check_Sn_2():
    output = (2, [(0, 1)])
    return output == HomPolys.create_graph_edges('S2')

def check_Sn_3():
    output = (3, [(0, 1), (0, 2)])
    return output == HomPolys.create_graph_edges('S3')

def check_Sn_4():
    output = (4, [(0, 1), (0, 2), (0, 3)])
    return output == HomPolys.create_graph_edges('S4')

# Empty graphs On

def check_On_0():
    output_0 = (0, [])
    output_1 = (1, [])
    result_0 = HomPolys.create_graph_edges('O0')
    result_1 = HomPolys.create_graph_edges('O1')
    return output_0 == result_0 and output_1 == result_1

def check_On_2():
    output = (2, [])
    return output == HomPolys.create_graph_edges('O2')

def check_On_3():
    output = (3, [])
    return output == HomPolys.create_graph_edges('O3')

def check_On_4():
    output = (4, [])
    return output == HomPolys.create_graph_edges('O4')


# Monomial tests
def init_test():
    mono = HomPolys.Monomial(20)
    return mono.num_var == 20

def powers_init_test():
    mono = HomPolys.Monomial(2, [1, 2])
    return mono.get_powers()  == [1,  2]

def powers_set_test():
    mono = HomPolys.Monomial(3)
    mono.set_powers([1, 2, 3])
    return mono.get_powers() == [1, 2, 3]

def tex_test():
    mono  = HomPolys.Monomial(3, [1, 2, 1])
    return mono._tex() == 'x_{0}^{1}x_{1}^{2}x_{2}^{1}'

def eq_test_1():
    mono_1 = HomPolys.Monomial(3, [1, 2, 1])
    mono_2 = HomPolys.Monomial(3, [1, 2, 1])
    return mono_1 == mono_2

def eq_test_2():
    mono_1 = HomPolys.Monomial(3, [1, 2, 1])
    mono_2 = HomPolys.Monomial(3)
    mono_2.set_powers([1, 2, 1])
    return mono_1 == mono_2

# Polynomial creation tests
def init_test_poly():
    poly = HomPolys.Polynomial(20)
    results = [
        poly.num_var == 20,
        poly.get_monomials() == [],
        poly.get_coefs() == [],
        poly.get_powers() == []
    ]
    return all(results)

def powers_init_test_poly():
    poly = HomPolys.Polynomial(3, [1, 2], [[0, 1, 2], [2, 0, 0]])
    results = [
        poly.num_var == 3,
        poly.get_monomials() == [
            HomPolys.Monomial(3, [0, 1, 2]),
            HomPolys.Monomial(3, [2, 0, 0])
        ],
        poly.get_coefs() == [1, 2]
    ]
    return all(results)


def check_edge_lists():
    # Run all edge list tests
    edge_tests = [
        check_Kn_0(), check_Kn_2(), check_Kn_3(), check_Kn_4(),
        check_Pn_0(), check_Pn_2(), check_Pn_3(), check_Pn_4(),
        check_Cn_0(), check_Cn_2(), check_Cn_3(), check_Cn_4(),
        check_Sn_0(), check_Sn_2(), check_Sn_3(), check_Sn_4(),
        check_On_0(), check_On_2(), check_On_3(), check_On_4(),
    ]
    return all(edge_tests)

def check_monomials():
    # Creates a number of edge lists and verifies that they create
    # appropriate monomials
    mono_tests = [
        init_test(), powers_init_test(), powers_set_test(),
        tex_test(), eq_test_1(), eq_test_2(),
    ]
    return all(mono_tests)


def check_polynomials_creation():
    poly_tests = [
        init_test_poly(),
        powers_init_test_poly()
    ]
    return all(poly_tests)


def check_polynomials_operators():
    return True


if __name__ == "__main__":
    EDGE_LIST_CHECK = check_edge_lists()

    MONO_CHECK = check_monomials()

    POLY_CHECK = check_polynomials_creation()

    POLY_OP_CHECK = check_polynomials_operators()


    test_results = {
        'EDGE_LIST_CHECK': EDGE_LIST_CHECK,
        'MONO_CHECK': MONO_CHECK,
        'POLY_CHECK': POLY_CHECK,
        'POLY_OP_CHECK': POLY_OP_CHECK,
    }

    if all(test_results.values()):
        print("Passed all tests!")

    else:
        print("Passed {i} of {j} tests".format(
            i = "%d" % sum(test_results.values()),
            j = "%d" % len(test_results.values())))
        pass_fail = lambda x: 'PASSED' if x else 'FAILED'
        
        for key in test_results.keys():
            print(('Test {i}: {j}').format(
                i = key,
                j  = pass_fail(test_results[key])))    
        # print results of each test - use dictionary