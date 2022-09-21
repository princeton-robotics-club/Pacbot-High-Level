from simulator.tree_wrappers import PacBotNode
from simulator.visualizer import Visualizer

if __name__ == "__main__":
    visualizer = Visualizer()
    node = PacBotNode((0, 0), speed=1)
    grid = node.render()
    visualizer.draw_grid(grid)

    done = False
    key = visualizer.wait_manual_control()
    while key != "q":
        action = 2
        if key == "w":
            action = 0
        elif key == "a":
            action = 1
        elif key == "d":
            action = 3
        elif key == "s":
            action = 4
        node = node.next_node(action)
        grid = node.render()
        visualizer.draw_grid(grid)
        # for row in obs[11]:
        #     for cell in row:
        #         print('1' if cell else '0', end='')
        #     print()
        # print(reward, done)

        if node.is_target:
            node = PacBotNode((0, 0), speed=1)
        key = visualizer.wait_manual_control()