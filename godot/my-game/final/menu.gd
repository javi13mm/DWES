extends Control

var file_dir = "save/settings.json"
var difficulty = 0
var volume = 10

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	
	read_initial_settings()
	set_settings()
	set_settings_file_data()
	
	$VBoxContainer.show()
	$VBoxContainer/PlayButton.grab_focus()
	$Options.hide()
	$DifficultyContainer.hide()
	$BackButton2.hide()
	$Tips.hide()
	$Leaderboards.hide()

func read_initial_settings():
	var file = FileAccess.open(file_dir, 1)
	var file_content = FileAccess.get_file_as_string(file_dir)
	if file_content != "":
		var json = JSON.parse_string(file_content)
		difficulty = json.difficulty
		volume = json.volume
	else:
		file.store_line("{\"difficulty\":0,\"volume\":10}")
	file.close()

func set_settings():
	if difficulty == 0:
		$Options/OptionsGrid/DifficultyChosen.text = "NORMAL"
	else:
		$Options/OptionsGrid/DifficultyChosen.text = "TRYHARD"
	$Options/OptionsGrid/VolumeScrollBar.value = volume

func _process(delta):
	pass

func _on_exit_button_pressed():
	get_tree().quit()


func _on_play_button_pressed():
	get_tree().change_scene_to_file("res://intro_name.tscn")


func _on_options_button_pressed():
	$VBoxContainer.hide()
	$Options.show()
	$Options/OptionsGrid/DifficultyChosen.grab_focus()
	$Options/OptionsGrid/VolumeScrollBar.focus_mode = 1


func _on_difficulty_chosen_pressed():
	$DifficultyContainer.show()
	$Options/OptionsGrid/DifficultyChosen.focus_mode = 0
	$Options/OptionsGrid/VolumeScrollBar.focus_mode = 0
	$Options/BackButton.focus_mode = 0
	$DifficultyContainer/NormalButton.grab_focus()


func _on_normal_button_pressed():
	difficulty = 0
	set_settings_file_data()
	$DifficultyContainer.hide()
	$Options/OptionsGrid/DifficultyChosen.text = "NORMAL"
	$Options/OptionsGrid/DifficultyChosen.focus_mode = 1
	$Options/OptionsGrid/VolumeScrollBar.focus_mode = 1
	$Options/BackButton.focus_mode = 1
	$Options/OptionsGrid/DifficultyChosen.grab_focus()


func _on_tryhard_button_pressed():
	difficulty = 1
	set_settings_file_data()
	$DifficultyContainer.hide()
	$Options/OptionsGrid/DifficultyChosen.text = "TRYHARD"
	$Options/OptionsGrid/DifficultyChosen.focus_mode = 1
	$Options/OptionsGrid/VolumeScrollBar.focus_mode = 1
	$Options/BackButton.focus_mode = 1
	$Options/OptionsGrid/DifficultyChosen.grab_focus()


func _on_back_button_pressed():
	$DifficultyContainer.hide()
	$Options.hide()
	$VBoxContainer.show()
	$VBoxContainer/OptionsButton.grab_focus()


func _on_volume_scroll_bar_value_changed(value):
	volume = value
	set_settings_file_data()
	AudioServer.set_bus_volume_db(0, float((value/10) * 80 - 80))

func set_settings_file_data():
	var file = FileAccess.open(file_dir, 2)
	file.store_line("{\"difficulty\":"+str(difficulty)+",\"volume\":"+str(volume)+"}")
	file.close()


func _on_tips_button_pressed():
	$VBoxContainer.hide()
	$Tips.show()
	$BackButton2.show()
	$BackButton2.grab_focus()


func _on_back_button_2_pressed():
	$Leaderboards.text = "Cargando..."
	$Leaderboards.hide()
	$BackButton2.hide()
	$Tips.hide()
	$VBoxContainer.show()
	$VBoxContainer/TipsButton.grab_focus()


func _on_leaderboards_button_pressed():
	$VBoxContainer.hide()
	send_get_score()
	$Leaderboards.show()
	$BackButton2.show()
	$BackButton2.grab_focus()

func send_get_score():
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed
	http_request.connect("request_completed",_on_server_has_responded)
	http_request.request("http://127.0.0.1:8000/scorecza",
						PackedStringArray(["Content-Type: application/json", "Client-Secret: abc"]),
						HTTPClient.METHOD_GET)

func _on_server_has_responded(result, response_code, headers, body):
	var response = JSON.parse_string(body.get_string_from_utf8())
	var content = ""
	var pos = 0
	for record in response:
		pos += 1
		content += str(pos)+". Nick: "+str(record.get("username"))+"\n    Score: "+str(record.get("score"))+"\n\n"
	$Leaderboards.text = "TOP 5:\n"+content
