from hub import port
import runloop
import motor
import motor_pair
import force_sensor
import math


# ==========================================================
# LEGO 3D PRINTER
# SMALL FIRST LOGO
#
# 3 PASSES WIDE
# 3 LEVELS TALL
#
# A + B = Z axis
# C     = X axis
# E + F = Y axis
# D     = force sensor
#
# CALIBRATION
#
# X = 40 degrees per pin
# Y = 36 degrees per pin
#
# Z:
# +36 degrees = DOWN 1 pin
# -36 degrees = UP 1 pin
# ==========================================================


# ==========================================================
# MOTOR PAIRS
# ==========================================================

motor_pair.pair(
    motor_pair.PAIR_1,
    port.A,
    port.B
)

motor_pair.pair(
    motor_pair.PAIR_2,
    port.E,
    port.F
)


# ==========================================================
# SPEEDS
# ==========================================================

SETUP_SPEED = 200
PRINT_SPEED = 100

DRAW_SPEED = 45
TRAVEL_SPEED = 70
Z_SPEED = 50


# ==========================================================
# CALIBRATION
# ==========================================================

X_DEGREES_PER_PIN = 40
Y_DEGREES_PER_PIN = 36
Z_DEGREES_PER_PIN = 36


# ==========================================================
# STANDARD MOVEMENT
# ==========================================================

async def left_right(rotations):

    degrees = rotations * -360

    await motor.run_for_degrees(
        port.C,
        int(degrees),
        PRINT_SPEED
    )

    await runloop.sleep_ms(300)


async def forward_back(value):

    degrees = value * -36

    await motor_pair.move_for_degrees(
        motor_pair.PAIR_2,
        int(degrees),
        0,
        velocity=PRINT_SPEED
    )

    await runloop.sleep_ms(300)


async def up_down(value):

    degrees = value * -36

    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1,
        int(degrees),
        0,
        velocity=PRINT_SPEED
    )

    await runloop.sleep_ms(300)


# ==========================================================
# PRECISE X MOVEMENT
# ==========================================================

async def move_x_pins(pins, speed=DRAW_SPEED):

    degrees = round(
        pins * X_DEGREES_PER_PIN
    )

    if degrees != 0:

        await motor.run_for_degrees(
            port.C,
            degrees,
            speed
        )


# ==========================================================
# PRECISE Y MOVEMENT
# ==========================================================

async def move_y_pins(pins, speed=DRAW_SPEED):

    degrees = round(
        pins * -Y_DEGREES_PER_PIN
    )

    if degrees != 0:

        await motor_pair.move_for_degrees(
            motor_pair.PAIR_2,
            degrees,
            0,
            velocity=speed
        )


# ==========================================================
# DRAW PRECISE LINE
# ==========================================================

async def line(dx, dy):

    distance = math.sqrt(
        dx * dx +
        dy * dy
    )

    # Tiny steps for smooth diagonals
    steps = max(
        1,
        int(math.ceil(distance / 0.10))
    )

    total_x = dx * X_DEGREES_PER_PIN
    total_y = dy * -Y_DEGREES_PER_PIN

    last_x = 0
    last_y = 0


    for step in range(1, steps + 1):

        fraction = step / steps

        target_x = round(
            total_x * fraction
        )

        target_y = round(
            total_y * fraction
        )

        x_move = target_x - last_x
        y_move = target_y - last_y


        if x_move != 0:

            await motor.run_for_degrees(
                port.C,
                x_move,
                DRAW_SPEED
            )


        if y_move != 0:

            await motor_pair.move_for_degrees(
                motor_pair.PAIR_2,
                y_move,
                0,
                velocity=DRAW_SPEED
            )


        last_x = target_x
        last_y = target_y


# ==========================================================
# TRAVEL
# ==========================================================

async def travel(dx, dy):

    await move_x_pins(
        dx,
        TRAVEL_SPEED
    )

    await move_y_pins(
        dy,
        TRAVEL_SPEED
    )


# ==========================================================
# PIN UP / DOWN FOR TRAVEL
#
# 1/4 pin lift
# ==========================================================

async def pin_up():

    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1,
        -9,
        0,
        velocity=Z_SPEED
    )


async def pin_down():

    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1,
        9,
        0,
        velocity=Z_SPEED
    )


# ==========================================================
# TRIANGLE
# ==========================================================

async def draw_triangle():

    await line(
        0.75,
        1.25
    )

    await line(
        0.75,
        -1.25
    )

    await line(
        -1.50,
        0
    )


# ==========================================================
# SQUARE / DIAMOND
# ==========================================================

async def draw_square():

    await line(
        0.65,
        0.40
    )

    await line(
        0.40,
        -0.65
    )

    await line(
        -0.65,
        -0.40
    )

    await line(
        -0.40,
        0.65
    )


# ==========================================================
# CIRCLE
# ==========================================================

async def draw_circle(radius):

    steps = 36

    previous_x = radius
    previous_y = 0


    for step in range(1, steps + 1):

        angle = (
            2 *
            math.pi *
            step /
            steps
        )

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        dx = x - previous_x
        dy = y - previous_y


        await line(
            dx,
            dy
        )


        previous_x = x
        previous_y = y


# ==========================================================
# ONE THIN LOGO PASS
#
# This is ONE pass of the logo.
# ==========================================================

async def draw_logo_pass():

    # ------------------------------------------------------
    # TRIANGLE
    # ------------------------------------------------------

    await pin_up()

    await travel(
        -1.15,
        -0.35
    )

    await pin_down()

    await draw_triangle()


    # ------------------------------------------------------
    # SQUARE
    # ------------------------------------------------------

    await pin_up()

    await travel(
        1.40,
        1.25
    )

    await pin_down()

    await draw_square()


    # ------------------------------------------------------
    # CIRCLE
    # ------------------------------------------------------

    await pin_up()

    await travel(
        0.75,
        -1.15
    )

    await pin_down()

    await draw_circle(
        0.50
    )


    # ------------------------------------------------------
    # RETURN TO START AREA
    # ------------------------------------------------------

    await pin_up()

    await travel(
        -1.00,
        0.25
    )

    await pin_down()


# ==========================================================
# THREE PASSES WIDE
#
# Each pass is offset only slightly.
#
# Pass 1 = left
# Pass 2 = center
# Pass 3 = right
#
# Total added width = only 0.20 pin
# ==========================================================

async def draw_three_wide():

    print("WIDTH PASS 1")

    # Start slightly left
    await move_x_pins(
        -0.10,
        TRAVEL_SPEED
    )

    await draw_logo_pass()


    print("WIDTH PASS 2")

    # Move to center
    await move_x_pins(
        0.10,
        TRAVEL_SPEED
    )

    await draw_logo_pass()


    print("WIDTH PASS 3")

    # Move slightly right
    await move_x_pins(
        0.10,
        TRAVEL_SPEED
    )

    await draw_logo_pass()


    # Return to original center
    await move_x_pins(
        -0.10,
        TRAVEL_SPEED
    )


# ==========================================================
# THREE LEVELS TALL
#
# Same idea as original printer:
#
# draw layer
# move Z
# draw next layer
#
# Original layer change = up_down(0.2)
# ==========================================================

async def print_first_logo():

    print("")
    print("==============================")
    print(" FIRST LOGO")
    print(" 3 WIDE x 3 LEVELS")
    print("==============================")
    print("")


    for level in range(3):

        print("")
        print("LEVEL", level + 1)
        print("")


        # ==================================================
        # THREE PASSES WIDE
        # ==================================================

        await draw_three_wide()


        # ==================================================
        # MOVE UP TO NEXT LEVEL
        #
        # Same layer movement as original printer.
        #
        # Do not move after level 3.
        # ==================================================

        if level < 2:

            await up_down(
                0.2
            )


    # Lift when completely finished
    await pin_up()


    print("")
    print("==============================")
    print(" LOGO COMPLETE")
    print("==============================")
    print("")


# ==========================================================
# CURRENT CALIBRATED SETUP
#
# KEEP THESE VALUES
# ==========================================================

async def setup():

    global PRINT_SPEED


    print("==============================")
    print(" SETUP")
    print("==============================")


    PRINT_SPEED = SETUP_SPEED


    # Initial plate movement
    await forward_back(
        8
    )


    # Second plate movement
    await forward_back(
        -1
    )


    # X movement
    await left_right(
        -1
    )


    # Z movement
    await up_down(
        10
    )


    # Return X
    await left_right(
        1
    )


    # Final plate position
    await forward_back(
        -4
    )


    # Final pin height
    await up_down(
        -3.85
    )


    PRINT_SPEED = 100


    print("")
    print("WAITING FOR SENSOR D")
    print("")


    await runloop.until(
        lambda: force_sensor.pressed(port.D)
    )


    print("")
    print("SETUP COMPLETE")
    print("")


# ==========================================================
# MAIN
# ==========================================================

async def main():

    print("==============================")
    print(" LEGO 3D PRINTER")
    print(" FIRST LOGO")
    print("==============================")


    # Calibrated setup
    await setup()


    # Print:
    #
    # 3 passes wide
    # 3 levels tall
    await print_first_logo()


runloop.run(main())
