import json
import tkinter as tk
import os
from tkinter import filedialog
from shutil import copyfile


class ConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphics Config Swapper")

        self.games = []
        self.load_configs()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack()

        self.load_games_to_listbox()

        new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        new_game_button.pack()

        swap_button = tk.Button(root, text="Swap Config", command=self.swap_config)
        swap_button.pack()
        swap_all_button = tk.Button(root, text="Swap All Configs", command=self.swap_all_configs)
        swap_all_button.pack()
        delete_button = tk.Button(root, text="Delete Game", command=self.delete_game)
        delete_button.pack()

    def select_directory(self, window, entry):
        directory = filedialog.askdirectory(initialdir="C:\\Program Files (x86)\\Steam\\steamapps\\common")
        entry.delete(0, tk.END)
        entry.insert(0, directory)

    def load_configs(self):
        try:
            with open('game_configs.json', 'r') as file:
                data = json.load(file)
                self.games = data.get('games', [])
        except Exception as e:
            print(f"Error loading configs: {e}")

    def save_configs(self):
        try:
            with open('game_configs.json', 'w') as file:
                json.dump({"games": self.games}, file)
        except Exception as e:
            print(f"Error saving configs: {e}")

    def load_games_to_listbox(self):
        self.listbox.delete(0, tk.END)
        for game in self.games:
            last_config = game.get('last_config', '')
            display_text = f"{game.get('name', 'Unknown Game')} - Currently: {last_config}"
            self.listbox.insert(tk.END, display_text)

    def new_game(self):
        window = tk.Toplevel(self.root)
        window.attributes('-topmost', True)
        tk.Label(window, text="Game Name").pack()
        game_name_entry = tk.Entry(window)
        game_name_entry.pack()

        tk.Label(window, text="Game Directory").pack()
        game_directory_entry = tk.Entry(window)
        game_directory_entry.pack()
        game_directory_entry.insert(0, "C:\\Program Files (x86)\\Steam\\steamapps\\common\\")  # Set default value
        game_directory_button = tk.Button(window, text="Select Directory",
                                          command=lambda: self.select_directory(window, game_directory_entry))
        game_directory_button.pack()

        tk.Label(window, text="Config 1 Name").pack()
        config1_name_entry = tk.Entry(window)
        config1_name_entry.pack()

        tk.Label(window, text="Config 1 Files").pack()
        config1_files_button = tk.Button(window, text="Select Files",
                                         command=lambda: self.select_files(window, 'config1_files'))
        config1_files_button.pack()

        tk.Label(window, text="Config 2 Name").pack()
        config2_name_entry = tk.Entry(window)
        config2_name_entry.pack()

        tk.Label(window, text="Config 2 Files").pack()
        config2_files_button = tk.Button(window, text="Select Files",
                                         command=lambda: self.select_files(window, 'config2_files'))
        config2_files_button.pack()

        save_button = tk.Button(window, text="Save", command=lambda: self.save_game(window, game_name_entry.get(), game_directory_entry.get(), config1_name_entry.get(), window.config1_files, config2_name_entry.get(), window.config2_files))
        save_button.pack()

        window.config1_files = []
        window.config2_files = []

    def select_files(self, window, attr_name):
        filenames = filedialog.askopenfilenames()
        setattr(window, attr_name, filenames)

    def save_game(self, window, game_name, game_directory, config1_name, config1_files, config2_name, config2_files):
        self.games.append({
            "name": game_name,
            "directory": game_directory,
            "configs": [
                {"name": config1_name, "files": config1_files},
                {"name": config2_name, "files": config2_files}
            ]
        })
        self.save_configs()
        self.load_games_to_listbox()
        window.destroy()

    def swap_config(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            return
        game = self.games[selected_index[0]]
        window = tk.Toplevel(self.root)
        tk.Label(window, text=f"Select config for {game['name']}").pack()

        var = tk.StringVar(value=game['configs'][0]['name'])

        for config in game['configs']:
            tk.Radiobutton(window, text=config['name'], variable=var, value=config['name']).pack()

        swap_button = tk.Button(window, text="Swap",
                                command=lambda: self.perform_swap(window, game, var.get()))
        swap_button.pack()

    def perform_swap(self, window, game, selected_config_name):
        for config in game['configs']:
            if config['name'] == selected_config_name:
                for file in config['files']:
                    destination = self.get_destination_file_path(game['name'], file)
                    if destination:
                        copyfile(file, destination)
        game['last_config'] = selected_config_name
        self.save_configs()
        self.load_games_to_listbox()
        window.destroy()

    def get_destination_file_path(self, game_name, file):
        game_directory = None
        for game in self.games:
            if game['name'] == game_name:
                game_directory = game.get('directory', None)
                break
            
        if game_directory:
            filename = file.split('/')[-1]  # Extract the filename from the path
            return os.path.join(game_directory, filename)  # Form the full path using os.path.join
        else:
            print(f"Game directory not found for {game_name}")
            return None
    def swap_all_configs(self):
        window = tk.Toplevel(self.root)
        window.title("Swap All Configs")
        
        tk.Label(window, text="Config Name to Swap To:").pack()
        config_name_entry = tk.Entry(window)
        config_name_entry.pack()
        
        swap_button = tk.Button(window, text="Swap All", command=lambda: self.perform_swap_all(window, config_name_entry.get()))
        swap_button.pack()

    def perform_swap_all(self, window, config_name):
        unsuccessful_swaps = []
            
        for game in self.games:
            found = False
            for config in game['configs']:
                if config['name'] == config_name:
                    found = True
                    for file in config['files']:
                        destination = self.get_destination_file_path(game['name'], file)
                        if destination:
                            try:
                                copyfile(file, destination)
                            except Exception as e:
                                print(f"Error copying file: {e}")
                    break
            if found:
                game['last_config'] = config_name
            else:
                unsuccessful_swaps.append(game['name'])
                
        self.save_configs()
        self.load_games_to_listbox()
        window.destroy()
            
        if unsuccessful_swaps:
            error_window = tk.Toplevel(self.root)
            error_window.title("Unsuccessful Swaps")
            tk.Label(error_window, text="The following games did not have the specified config and were not swapped:").pack()
            for game_name in unsuccessful_swaps:
                tk.Label(error_window, text=game_name).pack()

    def delete_game(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            return  # Return if no game is selected
        # Remove the game from the games list and update the listbox and the JSON file
        del self.games[selected_index[0]]
        self.save_configs()
        self.load_games_to_listbox()


root = tk.Tk()
app = ConfigApp(root)
root.mainloop()
