import pandas as pd
import string

alpha = list(string.ascii_letters)


def get_points(item):
    return alpha.index(item) + 1


def get_priority(comp1, comp2):
    for item1 in comp1:
        for item2 in comp2:
            if item1 == item2:
                return get_points(item1)


df = pd.read_csv("puzzle_input_day3.txt", names=["supplies"])
df["comp1"] = df["supplies"].apply(lambda row: row[: int(len(row) / 2)])
df["comp2"] = df["supplies"].apply(lambda row: row[int(len(row) / 2) :])
df["priority"] = df.apply(lambda row: get_priority(row["comp1"], row["comp2"]), axis=1)
sum_priority = df["priority"].sum()

print(f"The sum of the priorities is: {sum_priority}")  # 7903


def get_badge(ruck1, ruck2, ruck3):
    for item1 in ruck1:
        if item1 in ruck2 and item1 in ruck3:
            return item1


df["group"] = sorted([i for i in range(1, 101)] * 3)
badges = [
    get_badge(
        list(group[1]["supplies"])[0],
        list(group[1]["supplies"])[1],
        list(group[1]["supplies"])[2],
    )
    for group in df.groupby("group")
]
badge_points = [get_points(badge) for badge in badges]


print(f"The sum of the badge pointes are: {sum(badge_points)}")  # 2548
