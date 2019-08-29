# https://www.codewars.com/kata/instant-runoff-voting/train/python


def runoff(voters):
    votes_count = dict((key, 0) for key in voters[0])
    for stage_number in range(len(voters[0])):

        for stage_number, vote_stage in enumerate(voters, 1):
            votes_count[candidate] += 1
        rating = list(sorted(votes_count.keys(), key=votes_count.get))
        leader = rating[-1]
        second = rating[-2]
        if votes_count[leader] >= len(votes_count) * stage_number / 2 and votes_count[leader] != votes_count[second]:
            return leader
        else:
            while True:
                last_but_one = rating[1]
                outsider = rating[0]
                if votes_count[outsider] == votes_count[last_but_one]:
                    vote_stages = list(map(lambda array: array.remove(outsider), voters))
                else:
                    vote_stages = list(map(lambda array: array.remove(outsider), voters))
                    break


votes = [['Drake Luft', 'Brian J. Mason', 'Daisuke Aramaki', 'Frank Underwood', 'Lex Luthor', 'Reinhard von Musel'],
            ['Drake Luft', 'Daisuke Aramaki', 'Reinhard von Musel', 'Lex Luthor', 'Frank Underwood', 'Brian J. Mason'],
            ['Lex Luthor', 'Reinhard von Musel', 'Frank Underwood', 'Drake Luft', 'Brian J. Mason', 'Daisuke Aramaki'],
            ['Lex Luthor', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason', 'Reinhard von Musel', 'Drake Luft'],
            ['Reinhard von Musel', 'Daisuke Aramaki', 'Lex Luthor', 'Brian J. Mason', 'Drake Luft', 'Frank Underwood']]

print(runoff(votes))