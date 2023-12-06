extends AnimatableBody2D

var kick

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if $OpenOrCloseTimer.is_stopped():
		set_collision_layer_value(6, true)

func kicked():
	if $Closed.visible:
		$Closed.visible = false
		$Opened.visible = true
		set_collision_layer_value(1, false)
		$DoorOpenSound.play()
		$OpenOrCloseTimer.start()
		set_collision_layer_value(6, false)
	else:
		$Closed.visible = true
		$Opened.visible = false
		set_collision_layer_value(1, true)
		$DoorCloseSound.play()
		$OpenOrCloseTimer.start()
		set_collision_layer_value(6, false)
