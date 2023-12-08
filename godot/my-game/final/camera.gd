extends Camera2D

# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$HealthBar.global_position = get_screen_center_position() + Vector2(-700, 300)
	$BackgroundBar.global_position = $HealthBar.global_position + Vector2(-3, -3)
	
	if get_parent():
		var health = float(get_parent().find_child("Cowboy").health)
		$HealthBar.modulate = Color((200 - health)/200, health/200, 0, 0.8)
