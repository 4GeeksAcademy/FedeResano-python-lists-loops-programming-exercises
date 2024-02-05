all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

def generate_li(Color):
    return "<li>{color['label']}</li>"

def filter_colors(color):
    return color["sexy"]

sexy_colors = list(filter(filter_colors, all_colors))

filtered_list = list(map(generate_li, sexy_colors))

print(filtered_list)
