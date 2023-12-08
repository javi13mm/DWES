extends Control

var file_dir = "save/settings.json"
var difficulty = 0
var volume = 10


func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	
	read_initial_settings()
	set_settings()
	set_settings_file_data()
	
	$VBoxContainer/PlayButton.grab_focus()
	$Options.hide()
	$DifficultyContainer.hide()

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
	get_tree().change_scene_to_file("res://Level1.tscn")


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
	$VBoxContainer/PlayButton.grab_focus()


func _on_volume_scroll_bar_value_changed(value):
	volume = value
	set_settings_file_data()
	AudioServer.set_bus_volume_db(0, float((value/10) * 80 - 80))

func set_settings_file_data():
	var file = FileAccess.open(file_dir, 2)
	file.store_line("{\"difficulty\":"+str(difficulty)+",\"volume\":"+str(volume)+"}")
	file.close()
