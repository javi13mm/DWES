extends Node

@export var mob_scene: PackedScene
var score
var username

# Called when the node enters the scene tree for the first time.
func _ready():
	load_username_from_disk()

func load_username_from_disk():
	var file = "save/user_data.json"
	if file:
		var file_string = FileAccess.get_file_as_string(file)
		var json = JSON.parse_string(file_string)
		if json:
			username = json.username
			score = json.score
		else:
			printerr("Error trying to import username data json")
	else:
		printerr("Error trying to import username data file")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func game_over():
	$Music.stop()
	$DeathSound.play()
	$ScoreTimer.stop()
	$MobTimer.stop()
	get_tree().call_group("mobs", "queue_free")
	$HUD.show_game_over()
	send_post_new_score()

func send_post_new_score():
	if username == null:
		printerr("Will NOT send POST data with score due to invalid username")
		printerr("There might have been an error loading user_data file")
		return
	# Username OK. Let's send the request
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed
	http_request.connect("request_completed",_on_server_has_responded)
	var body = {"username":username,"score":score}
	body = JSON.stringify(body)
	http_request.request("http://127.0.0.1:8000/score",
						PackedStringArray(["Content-Type: application/json", "Client-Secret: abc"]),
						HTTPClient.METHOD_POST,
						body)

func _on_server_has_responded(result, response_code, headers, body):
	print(headers)
	var response = JSON.parse_string(body.get_string_from_utf8())
	print("Server response:")
	print(response)

func new_game():
	score = 0
	$Music.play()
	$HUD.update_score(score)
	$HUD.show_message("Get Ready")
	$Player.start($StartPosition.position)
	$StartTimer.start()

func _on_start_timer_timeout():
	$ScoreTimer.start()
	$MobTimer.start()

func _on_score_timer_timeout():
	score += 1
	$HUD.update_score(score)

func _on_mob_timer_timeout():
	# Create a new instance of the Mob scene.
	var mob = mob_scene.instantiate()

	# Choose a random location on Path2D.
	var mob_spawn_location = get_node("MobPath/MobSpawnLocation")
	mob_spawn_location.progress_ratio = randf()

	# Set the mob's direction perpendicular to the path direction.
	var direction = mob_spawn_location.rotation + PI / 2

	# Set the mob's position to a random location.
	mob.position = mob_spawn_location.position

	# Add some randomness to the direction.
	direction += randf_range(-PI / 4, PI / 4)
	mob.rotation = direction

	# Choose the velocity for the mob.
	var velocity = Vector2(randf_range(150.0, 250.0), 0.0)
	mob.linear_velocity = velocity.rotated(direction)

	# Spawn the mob by adding it to the Main scene.
	add_child(mob)
