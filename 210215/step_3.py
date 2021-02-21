from types import GeneratorType

player_wins = [
    540, 167, 930, 874, 894, 310,
    229, 2, 298, 349, 331, 768, 160,
    902, 491, 39, 725, 7, 784, 998
]
print(player_wins)
att_example = [(930, 874, 894), (874, 894, 310), (349, 331, 768)]
att = (nums
       for nums in zip(player_wins, player_wins[1:], player_wins[2:])
       if min(nums) >= 300)
assert isinstance(att, GeneratorType), 'not generator type'
assert all(el_1 == el_2 for el_1, el_2 in zip(att, att_example)), 'wrong result'
