extends AnimatedSprite2D

var count = 0
var angle_direction = 1
var rotation_angle = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func angle_rotation():
	if abs(count) < 4:
		rotation_angle += angle_direction * PI/18
		rotate(rotation_angle)
		count = count + angle_direction
	else:
		count = count - angle_direction
		angle_direction *= -1
