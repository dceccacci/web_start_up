import pickle
from pathlib import Path




def load_pickle(path_to_load: Path):
    with open(path_to_load, "rb") as file:
        return pickle.load(file)

def main():
    checkpoint_folder = Path('checkpoints').resolve()

    apps_dict_path = checkpoint_folder.joinpath('apps_dict-ckpt-fin.p')
    excluded_apps_list_path = checkpoint_folder.joinpath('excluded_apps_list-ckpt-fin.p')
    error_apps_list_path = checkpoint_folder.joinpath('error_apps_list-ckpt-fin.p')

    if apps_dict_path.exists():
        apps_dict = load_pickle(apps_dict_path)
        # print("Contents of apps_dict-ckpt-fin.p:")
        print(apps_dict)
        # first_key = next(iter(apps_dict))
        # print({first_key: apps_dict[first_key]})
    else:
        print("apps_dict-ckpt-fin.p does not exist.")

    if excluded_apps_list_path.exists():
        excluded_apps_list = load_pickle(excluded_apps_list_path)
        #print("\nContents of excluded_apps_list-ckpt-fin.p:")
        # print(excluded_apps_list)
    else:
        print("excluded_apps_list-ckpt-fin.p does not exist.")

    if error_apps_list_path.exists():
        error_apps_list = load_pickle(error_apps_list_path)
        # print("\nContents of error_apps_list-ckpt-fin.p:")
        # print(error_apps_list)
    else:
        print("error_apps_list-ckpt-fin.p does not exist.")

if __name__ == '__main__':
    main()