import math, random
import numpy as np

sqrt2 = 1/(math.sqrt(2))

identity = np.matrix([[1,0], [0,1]])

states = {'0': np.matrix([[1], [0]]), '1': np.matrix([[0], [1]]), '-': np.matrix([[sqrt2], [-sqrt2]]), '+': np.matrix([[sqrt2], [sqrt2]])}

def rotate(epsilon, vector):
    sin = math.sin(epsilon)
    cos = math.cos(epsilon)
    rot_epsilon = np.kron(np.matrix([[cos, -sin], [sin, cos]]), identity)
    return rot_epsilon * vector

def cnot(vector):
    cnot = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    return cnot * vector

def cnotx(vector):
    cnotx = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1], [0, 0, -1, 0]])
    return cnotx * vector

def x(vector):
    x = np.kron(np.matrix([[0, 1], [1, 0]]), identity)
    return x * vector

def y(vector):
    i = np.imag(1j)
    y = np.kron(np.matrix([[0, -i], [i, 0]]), identity)
    return y * vector

def z(vector):
    z = np.kron(np.matrix([[1, 0], [0, -1]]), identity)
    return z * vector

def h(vector):
    h = np.kron(np.matrix([[sqrt2, sqrt2], [sqrt2, -sqrt2]]), identity)
    return h * vector

def gen_qubit(length):
    qubit = [random.choice(list(states.keys())) for i in range(length)]
    return qubit

def measure_01(vector):
    bra00 = np.transpose(np.kron(states['0'], states['0']))
    bra01 = np.transpose(np.kron(states['0'], states['1']))
    bra10 = np.transpose(np.kron(states['1'], states['0']))
    bra11 = np.transpose(np.kron(states['1'], states['1']))

    prob00 = math.pow(abs(bra00 * vector), 2)
    prob01 = math.pow(abs(bra01 * vector), 2)
    prob10 = math.pow(abs(bra10 * vector), 2)
    prob11 = math.pow(abs(bra11 * vector), 2)

    # probability of the second qubit being 0 or 1
    prob0 = prob00 + prob10
    prob1 = prob01 + prob11

    prob0_dist = int(prob0 * 100) * ['0']
    prob1_dist = int(prob1 * 100) * ['1']
    distribution = prob0_dist + prob1_dist

    second_qubit = random.choice(distribution)

    if second_qubit == '0':
        state = states['0']
        shift = 0
    else:
        state = states['1']
        shift = 1

    alpha = float(vector[0 + shift])
    beta = float(vector[2 + shift])
    scalar = math.sqrt(math.pow(abs(alpha), 2) + math.pow(abs(beta), 2))
    new_vector = np.kron(np.matrix([[alpha], [beta]]) * 1/scalar, state)

    return second_qubit, new_vector


def measure_pm(vector):
    brapp = np.transpose(np.kron(states['+'], states['+']))
    brapm = np.transpose(np.kron(states['+'], states['-']))
    bramp = np.transpose(np.kron(states['-'], states['+']))
    bramm = np.transpose(np.kron(states['-'], states['-']))

    probpp = math.pow(abs(brapp * vector), 2)
    probpm = math.pow(abs(brapm * vector), 2)
    probmp = math.pow(abs(bramp * vector), 2)
    probmm = math.pow(abs(bramm * vector), 2)

    # probability of the second qubit being 0 or 1
    probp = probpp + probmp
    probm = probpm + probmm

    probp_dist = int(probp * 100) * ['+']
    probm_dist = int(probm * 100) * ['-']
    distribution = probp_dist + probm_dist

    second_qubit = random.choice(distribution)

    if second_qubit == '+':
        state = states['+']
        shift = 0
    else:
        state = states['-']
        shift = 1

    alpha = float(vector[0 + shift])
    beta = float(vector[2 + shift])
    scalar = math.sqrt(math.pow(abs(alpha), 2) + math.pow(abs(beta), 2))
    new_vector = np.kron(np.matrix([[alpha], [beta]]) * 1/scalar, state)

    return second_qubit, new_vector

def measure_01_first(vector):
    bra00 = np.transpose(np.kron(states['0'], states['0']))
    bra01 = np.transpose(np.kron(states['0'], states['1']))
    bra10 = np.transpose(np.kron(states['1'], states['0']))
    bra11 = np.transpose(np.kron(states['1'], states['1']))

    prob00 = math.pow(abs(bra00 * vector), 2)
    prob01 = math.pow(abs(bra01 * vector), 2)
    prob10 = math.pow(abs(bra10 * vector), 2)
    prob11 = math.pow(abs(bra11 * vector), 2)

    # probability of the second qubit being 0 or 1
    prob0 = prob00 + prob01
    prob1 = prob10 + prob11

    prob0_dist = int(prob0 * 100) * ['0']
    prob1_dist = int(prob1 * 100) * ['1']
    distribution = prob0_dist + prob1_dist

    first_qubit = random.choice(distribution)

    if first_qubit == '0':
        state = states['0']
        shift = 0
    else:
        state = states['1']
        shift = 1

    alpha = float(vector[0 + shift])
    beta = float(vector[2 + shift])
    scalar = math.sqrt(math.pow(abs(alpha), 2) + math.pow(abs(beta), 2))
    new_vector = np.kron(state, np.matrix([[alpha], [beta]]) * 1/scalar)

    return first_qubit, new_vector

def main():

    flag = "utflag{quantum_bank_robber}"

    valid_choices = ["a", "b", "c"]
    correct_state = gen_qubit(30)
    edited_state = correct_state.copy()

    print("""<== Welcome to Wiesner's Quantum Bank! ==>

Due to totally legitimate reasons, we only have one Schroedinger Buck (SB) in the whole bank. Good thing nobody can copy it!

Each member of Wiesner's Quantum Bank also gets a free qubit with which they can do whatever they want. Surely this will not come back to bite us!

What would you like to do today?

    a) Work with a qubit from the Schroedinger Buck
    b) Submit a valid Schroedinger Buck in exchange for a flag (why do we sell flags???)
    c) Quit""") # TODO fix choices

    while(1):
        print("\nChoice [a|b|c]: ")
        choice = input().lower()
        if choice in valid_choices:

            while choice == 'a':

                op_choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

                print("\nWhich qubit of the Schroedinger Buck would you like to work with? Enter a number between 0-29 (inclusive): ")

                index = int(input())

                if index < 0 or index > 29:
                    print("\nPlease enter a number >= 0 and < 30") # TODO: add error handling for non num
                else:

                    correct_qubit = correct_state[index]
                    edited_qubit = edited_state[index]
                    probe = np.kron(states['0'], states[edited_qubit])

                    print("""What operation would you like to perform?

    a) Apply X gate to my qubit
    b) Apply Y gate to my qubit
    c) Apply Z gate to my qubit
    d) Apply H (Hadamard) gate to my qubit
    e) Apply Rotation gate to my qubit
    f) Apply CNOT gate to my qubit and the SB qubit
    g) Apply CNOT-X gate to my qubit and the SB qubit
    h) Have the SB qubit verified (bank measures)
    i) Measure the SB qubit in the [0,1] basis
    j) Measure the SB qubit in the [+,-] basis
    k) Measure the control qubit (takes you to main menu after)
    l) Go back to the main menu (resets your qubit)""")

                    while(1):
                        print("\nChoice [a|b|c|d|e|f|g|h|i|j|k|l]: ")
                        op_choice = input().lower()

                        if op_choice in op_choices:

                            if op_choice == 'a':
                                probe = x(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'b':
                                probe = y(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'c':
                                probe = z(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'd':
                                probe = h(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'e':
                                print("\nInput degrees of rotation in radians: ")
                                rot = float(input())
                                # while(rot < 0 or rot > 360):
                                #     print("\nPlease input a value >= 0 and < 360")
                                #     print("\nInput degrees of rotation (0 <= x < 360): ")
                                #     rot = int(input())
                                probe = rotate(rot, probe)
                                print("\nGate successfully applied")
                            if op_choice == 'f':
                                probe = cnot(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'g':
                                probe = cnotx(probe)
                                print("\nGate successfully applied")
                            if op_choice == 'h':
                                if correct_qubit in ['0', '1']:
                                    measurement, probe = measure_01(probe)
                                else:
                                    measurement, probe = measure_pm(probe)

                                if measurement != correct_qubit:
                                    print("\nThis is not a valid bill! We have called the Quantum Police and you are now banned from Wiesner's Quantum Bank.")
                                    exit()
                                else:
                                    print("\nNothing wrong with this Schroedinger Buck! Carry on with your day.")
                            if op_choice == 'i': # measure 0,1 basis
                                measurement, probe = measure_01(probe)
                                print("\nThe SB qubit measured as a " + measurement + ". You will now be taken back to the main menu.")
                                edited_state[index] = measurement
                                break
                            if op_choice == 'j': # measue +,- basis
                                measurement, probe = measure_pm(probe)
                                print("\nThe SB qubit measured as a " + measurement + ". You will now be taken back to the main menu.")
                                edited_state[index] = measurement
                                break
                            if op_choice == 'k':
                                measurement, probe = measure_01_first(probe)
                                print("\nYour qubit measured as a " + measurement + ". You will now be taken back to the main menu.")
                                break
                            if op_choice == 'l':
                                break
                        else:
                            print("\nPlease input a valid choice")

                break

            while choice == 'b':

                valid_states = {'0', '1', '+', '-'}

                print("\nPlease input the state of the Schroedinger Buck using {0,1,+,-}. All Schroedinger Bucks are 30 qubits long: ")
                state = input()

                if len(state) != 30: # TODO : change back
                    print("\nPlease ensure the Schroedinger Buck is 30 qubits long")
                elif not valid_states.issuperset(state):
                    print("\nPlease ensure the Schroedinger Buck state only contains the following characters with no spaces: 1 0 + -")
                else:
                    if state == ''.join(correct_state):
                        print("\nCongratulations! This Schroedinger Buck is valid. Here is the flag: " + flag)
                    else:
                        print("\nThat was not a valid Schroedinger Buck! We have called the Quantum Police and you are now banned from Wiesner's Quantum Bank.")
                        exit()

            if choice == 'c': exit()
        else:
            print("\nPlease input a valid choice")

main()
