import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


def list_tasks(task_hierarchy, level=0):
    for task in task_hierarchy:
        print("  " * level + "- " + task["name"])
        if "subtasks" in task:
            list_tasks(task["subtasks"], level + 1)


task_hierarchy_1 = [
    {
        "name": "Craft Legendary Gear",
        "subtasks": [
            {"name": "Gather Rare Materials"},
            {"name": "Level up Crafting Skill"},
            {"name": "Acquire Crafting Recipes", 
             "subtasks": [
                {"name": "Complete Challenging Quests"},
                {"name": "Defeat Legendary Monsters"}
            ]},
            {"name": "Craft Legendary Equipment"}
        ]
    },
    {
        "name": "Complete Legendary Quest",
        "subtasks": [
            {"name": "Discover Quest Giver"},
            {"name": "Gather Information", 
             "subtasks": [
                {"name": "Talk to NPCs"},
                {"name": "Explore Dungeons"}
            ]},
            {"name": "Defeat Powerful Bosses"},
            {"name": "Claim Legendary Rewards"}
        ]
    }
]
task_hierarchy_2 = [
    {
        "name": "Form Powerful Guild",
        "subtasks": [
            {"name": "Recruit Skilled Players", 
             "subtasks": [
                {"name": "Advertise Guild"},
                {"name": "Hold Tryouts"}
            ]},
            {"name": "Establish Guild Headquarters", 
            "subtasks": [
                {"name": "Acquire Guild Hall"},
                {"name": "Decorate Guild Hall"}
            ]}
        ]
    },
    {
        "name": "Conquer Endgame Content",
        "subtasks": [
            {"name": "Organize Raid Team", 
             "subtasks": [
                {"name": "Assign Roles"},
                {"name": "Develop Strategies"}
            ]},
            {"name": "Acquire Powerful Equipment"},
            {"name": "Defeat Challenging Raid Bosses"}
        ]
    }
]

line_break()
print("Task Hierarchy 1:")
list_tasks(task_hierarchy_1)
line_break()

line_break()
print("Task Hierarchy 2:")
list_tasks(task_hierarchy_2)
line_break()
