import stepper
import board

s = stepper.Stepper(
    board.GP13, limit_pins=(board.GP10, board.GP11),
    dir_pin=board.GP12, count_pin=board.GP3)
s.dir_active = "HIGH"
s._setup_sm()

