import sys

from Bio import SeqIO


namesWeHaveSeenSoFar = {}

for record in SeqIO.parse(sys.stdin, 'fasta'):
    # print(record)
    name = record.description

    if len(record.seq) > 3000:
        print(name, "is really long:", len(record.seq), "nucleotides!")

    if name in namesWeHaveSeenSoFar:
        if record.seq == namesWeHaveSeenSoFar[name]:
            # print("We've already seen", name,
            # "but the sequences are the same - no big deal.")
            pass
        else:
            print("We've already seen", name, "and the sequences differ.")
    else:
        namesWeHaveSeenSoFar[name] = record.seq
