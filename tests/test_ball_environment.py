from world_models.environments.ball_environment import BallEnvironment

def test_ball_moves_in_straight_line():
    env = BallEnvironment(
        width=100,
        height=100,
        radius=1,
        dt=1,
        max_speed=10,
        max_steps=1000,
    )

    env._x = 50
    env._y = 50
    env._vx = 2
    env._vy = 3

    initial_state = env.get_state()
    env.step()
    next_state = env.get_state()

    expected_x = initial_state[0] + initial_state[2] * env.dt
    expected_y = initial_state[1] + initial_state[3] * env.dt

    assert next_state[0] == expected_x
    assert next_state[1] == expected_y

    assert next_state[2] == initial_state[2]
    assert next_state[3] == initial_state[3]