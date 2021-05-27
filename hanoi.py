import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"
    domain_file.write("Propositions:")
    # propositions regarding what spots are available (have nothing above them).
    for peg in pegs:
        domain_file.write(" available-" + peg)
    for disk in disks:
        domain_file.write(" available-" + disk)

    # propositions regarding what's on top of what.
    for disk1 in disks:
        for disk2 in disks:
            if disk1 == disk2:
                continue
            domain_file.write(" on-" + disk1 + "-" + disk2)
        for peg in pegs:
            domain_file.write(" on-" + disk1 + "-" + peg)

    # propositions regarding what's smaller than what.
    for disk1 in disks:
        for disk2 in disks:
            if disk1 == disk2:
                continue
            domain_file.write(" smaller-" + disk1 + "-" + disk2)
        for peg in pegs:
            domain_file.write(" smaller-" + disk1 + "-" + peg)

    for disk in disks:
        for from_item in disks + pegs:
            if disk == from_item:
                continue
            for to_item in disks + pegs:
                if disk == to_item or from_item == to_item:
                    continue
                domain_file.write("\nOperator move-" +
                                  disk + "-" +
                                  from_item + "-" +
                                  to_item)

                domain_file.write("\nPRE: on-" + disk + "-" + from_item + "," +
                                  " available-" + disk + "," +
                                  " available-" + to_item + "," +
                                  " smaller-" + disk + "-" + to_item)

                domain_file.write(" ADD: on-" + disk + "-" + to_item + "," +
                                  " available-" + from_item)

                domain_file.write(" DEL: on-" + disk + "-" + from_item + "," +
                                  " available-" + to_item)

    domain_file.close()



def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file

    # Firstly, we write the initial state.
    problem_file.write("Initial state:")

    # Write what spots are available (have nothing above them).
    problem_file.write(" available-" + disks[0])
    for peg in pegs[1:]:
        problem_file.write(" available-" + peg)

    # Write what's on top of what.
    for i in range(1, len(disks)):
        problem_file.write(" on-" + disks[i - 1] + "-" + disks[i])
    problem_file.write(" on-" + disks[-1] + "-" + pegs[0])

    # Write what's smaller than what.
    for i, disk1 in enumerate(disks):
        for disk2 in disks[i + 1:]:
            problem_file.write(" smaller-" + disk1 + "-" + disk2)

        for peg in pegs:
            problem_file.write(" smaller-" + disk1 + "-" + peg)

    # Finally, we write the goal state.
    problem_file.write("\nGoal state:")

    # Write what spots are available (have nothing above them).
    problem_file.write(" available-" + disks[0])
    for peg in pegs[:-1]:
        problem_file.write(" available-" + peg)

    # Write what's on top of what.
    for i in range(1, len(disks)):
        problem_file.write(" on-" + disks[i - 1] + "-" + disks[i])
    problem_file.write(" on-" + disks[-1] + "-" + pegs[-1])

    problem_file.write("\n")
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
